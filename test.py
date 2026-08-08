import re
import csv

python_file = "main.py"
csv_file = "card_analysis.csv"

# --------------------------------------------------
# READ YOUR PYTHON FILE
# --------------------------------------------------

with open(python_file, "r", encoding="utf-8") as f:
    code = f.read()


rows = []


# --------------------------------------------------
# CHECK CARDS 1–70
# --------------------------------------------------

for n in range(1, 71):

    problems = []

    # ----------------------------------------------
    # FIND CARD COLOR
    # ----------------------------------------------

    color_match = re.search(
        rf'main\.card_(\w+)_{n}_frame',
        code
    )

    if color_match:
        color = color_match.group(1)
    else:
        color = "UNKNOWN"
        problems.append("Missing card")


    # ----------------------------------------------
    # FIND CARD MOVEMENT TEXT
    # ----------------------------------------------

    card_movement_match = re.search(
        rf'main\.card_\w+_{n}_label_middle_down'
        rf'.*?text="([^"]+)"',
        code,
        re.DOTALL
    )

    if card_movement_match:

        card_text = card_movement_match.group(1)

        # Check forward/backward
        direction_match = re.search(
            r'\b(forward|backward)\b',
            card_text,
            re.IGNORECASE
        )

        # Check number
        number_match = re.search(
            r'(\d+)\s*spaces?',
            card_text,
            re.IGNORECASE
        )

        if direction_match:
            card_direction = direction_match.group(1).lower()
        else:
            card_direction = ""
            problems.append("No forward/backward in card")

        if number_match:
            card_movement = int(number_match.group(1))
        else:
            card_movement = ""
            problems.append("No movement number in card")

    else:

        card_text = ""
        card_direction = ""
        card_movement = ""

        problems.append("Missing movement label")


    # ----------------------------------------------
    # FIND CONTINUE BUTTON
    # ----------------------------------------------

    button_pattern = (
        rf'main\.card_\w+_{n}_continue'
        rf'\s*=\s*tk\.Button'
    )

    button_exists = bool(
        re.search(button_pattern, code)
    )

    if not button_exists:
        problems.append("Missing Continue button")


    # ----------------------------------------------
    # CHECK BUTTON COMMAND
    # ----------------------------------------------

    button_command_pattern = (
        rf'main\.card_\w+_{n}_continue'
        rf'\.config\(\s*command\s*='
        rf'\s*continue_\w+_{n}\s*\)'
    )

    button_has_command = bool(
        re.search(button_command_pattern, code)
    )

    if not button_has_command:

        # Also check if command was inside the Button itself
        button_inline_pattern = (
            rf'main\.card_\w+_{n}_continue'
            rf'\s*=\s*tk\.Button'
            rf'.*?command\s*=\s*continue_\w+_{n}'
        )

        button_has_command = bool(
            re.search(
                button_inline_pattern,
                code,
                re.DOTALL
            )
        )

    if not button_has_command:
        problems.append("Missing button command")


    # ----------------------------------------------
    # FIND CONTINUE FUNCTION
    # ----------------------------------------------

    function_pattern = (
        rf'def\s+continue_\w+_{n}\s*\(\)\s*:'
        rf'(.*?)(?=\n\s*def\s|\Z)'
    )

    function_match = re.search(
        function_pattern,
        code,
        re.DOTALL
    )

    function_exists = bool(function_match)

    if not function_exists:

        problems.append("Missing Continue function")

        code_movement = ""
        code_direction = ""

    else:

        function_code = function_match.group(1)

        # ------------------------------------------
        # FIND move_f_or_b()
        # ------------------------------------------

        move_match = re.search(
            r'move_f_or_b\(\s*(\d+)\s*,\s*["\']([fb])["\']\s*\)',
            function_code
        )

        if move_match:

            code_movement = int(move_match.group(1))

            code_direction = (
                "forward"
                if move_match.group(2) == "f"
                else "backward"
            )

        else:

            code_movement = ""
            code_direction = ""

            problems.append(
                "No move_f_or_b() in function"
            )


    # ----------------------------------------------
    # CHECK MOVEMENT NUMBER
    # ----------------------------------------------

    if (
        card_movement != ""
        and code_movement != ""
        and card_movement != code_movement
    ):

        problems.append(
            f"Number mismatch: card={card_movement}, "
            f"code={code_movement}"
        )


    # ----------------------------------------------
    # CHECK FORWARD / BACKWARD
    # ----------------------------------------------

    if (
        card_direction
        and code_direction
        and card_direction != code_direction
    ):

        problems.append(
            f"Direction mismatch: card={card_direction}, "
            f"code={code_direction}"
        )


    # ----------------------------------------------
    # FINAL RESULT
    # ----------------------------------------------

    correct = len(problems) == 0


    rows.append([
        n,
        color,
        card_text,
        card_movement,
        card_direction,
        code_movement,
        code_direction,
        button_exists,
        button_has_command,
        function_exists,
        correct,
        "; ".join(problems)
    ])


# --------------------------------------------------
# CREATE CSV
# --------------------------------------------------

with open(
    csv_file,
    "w",
    newline="",
    encoding="utf-8-sig"
) as f:

    writer = csv.writer(f)

    writer.writerow([
        "Card",
        "Color",
        "Card Text",
        "Card Movement",
        "Card Direction",
        "Code Movement",
        "Code Direction",
        "Button Exists",
        "Button Has Command",
        "Function Exists",
        "Correct",
        "Problems"
    ])

    writer.writerows(rows)


# --------------------------------------------------
# ANALYSIS
# --------------------------------------------------

total = len(rows)

correct = sum(
    row[10] is True
    for row in rows
)

wrong = total - correct


print("=" * 60)
print("        SEED ADVENTURE CARD ANALYSIS")
print("=" * 60)

print("Total cards :", total)
print("Correct     :", correct)
print("Problems    :", wrong)

print()


# --------------------------------------------------
# SHOW PROBLEMS
# --------------------------------------------------

print("=" * 60)
print("PROBLEMS")
print("=" * 60)

for row in rows:

    if row[10] is False:

        print(
            f"\nCard {row[0]} ({row[1]})"
        )

        print(
            f"  Card : {row[4]} {row[3]}"
        )

        print(
            f"  Code : {row[6]} {row[5]}"
        )

        print(
            f"  Button exists : {row[7]}"
        )

        print(
            f"  Button command: {row[8]}"
        )

        print(
            f"  Function      : {row[9]}"
        )

        print(
            "  Problems      :",
            row[11]
        )


print()
print("=" * 60)
print("CSV CREATED:", csv_file)
print("=" * 60)