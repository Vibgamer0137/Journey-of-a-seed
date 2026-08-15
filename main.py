import tkinter as tk
import random as r
import winsound as w
import time as t
import os as o
import sys
class SeedAdventure:
    def resource_path(main,relative_path):
        if getattr(sys, "frozen", False):
            base_path = sys._MEIPASS
        else:
            base_path = o.path.dirname(o.path.abspath(__file__))    
        return o.path.join(base_path, relative_path)
    def __init__(main, root):
        main.DICE_SOUND = main.resource_path(o.path.join("Assets", "Sounds", "Wav", "dice_sound.wav"))
        main.CARD_SOUND = main.resource_path(o.path.join("Assets", "Sounds", "Wav", "Card_pop_sound.wav"))
        main.root = root
        main.player_position = 0
        main.is_animating = False
        main.animate_move_steps = 0
        main.animate_move_direction = None
        main.dice_animation_running = False
        main.dice_animation_steps = 0
        main.final_dice_number = 0
        # Responsive layout values are initialized here.
        # They are recalculated after the game canvas is created.
        main.board_x = 0
        main.board_y = 0
        main.board_size = 800
        main.tile_size = 100
        main.player_size = 30
        main._resize_after_id = None
    def resize_game_layout(main, event=None):
        """Resize the 8x8 board and player without changing game positions."""
        if not hasattr(main, "canvas_for_game"):
            return

        canvas_width = max(1, main.canvas_for_game.winfo_width())
        canvas_height = max(1, main.canvas_for_game.winfo_height())

        # Keep space around the board and leave room at the top for
        # the dice controls.
        horizontal_margin = max(25, int(canvas_width * 0.04))
        top_margin = max(80, int(canvas_height * 0.10))
        bottom_margin = max(25, int(canvas_height * 0.04))

        available_width = max(1, canvas_width - (horizontal_margin * 2))
        available_height = max(
            1,
            canvas_height - top_margin - bottom_margin
        )

        board_size = min(available_width, available_height)
        main.board_size = board_size
        main.tile_size = max(1, board_size / 8)

        # Center the board inside the usable area.
        main.board_x = (canvas_width - board_size) / 2
        main.board_y = top_margin + (
            (available_height - board_size) / 2
        )

        # Resize every existing board tile.
        if hasattr(main, "tiles"):
            for index, tile in enumerate(main.tiles):
                row = index // 8
                col = index % 8
                x1 = main.board_x + col * main.tile_size
                y1 = main.board_y + row * main.tile_size
                x2 = x1 + main.tile_size
                y2 = y1 + main.tile_size
                main.canvas_for_game.coords(tile, x1, y1, x2, y2)

        # Keep the seed/player centered inside the correct tile.
        if hasattr(main, "player") and main.canvas_for_game.type(main.player):
            row = main.player_position // 8
            if row % 2 == 0:
                col = main.player_position % 8
            else:
                col = 7 - (main.player_position % 8)

            player_size = max(12, main.tile_size * 0.30)
            padding = (main.tile_size - player_size) / 2
            x1 = main.board_x + col * main.tile_size + padding
            y1 = main.board_y + row * main.tile_size + padding
            x2 = x1 + player_size
            y2 = y1 + player_size
            main.player_size = player_size
            main.canvas_for_game.coords(main.player, x1, y1, x2, y2)

        # Cards remain centered, but their outer frame scales with the window.
        if hasattr(main, "card") and main.card.winfo_ismapped():
            main.place_card_responsive(main.card)

    def place_card_responsive(main, card):
        """Keep every card centered and keep all card contents grouped in the middle."""
        width = max(1, main.root.winfo_width())
        height = max(1, main.root.winfo_height())

        # Responsive card size.
        card_width = max(280, min(700, int(width * 0.72)))
        card_height = max(220, min(400, int(height * 0.38)))

        # Put the whole card exactly in the center of the window.
        card.place(
            relx=0.5,
            rely=0.5,
            anchor="center",
            width=card_width,
            height=card_height
        )

        # Every card in Journey of a Seed is created in this order:
        # title, main message, movement message, Continue button.
        widgets = card.winfo_children()

        if len(widgets) >= 4:
            title = widgets[0]
            middle = widgets[1]
            middle_down = widgets[2]
            continue_button = widgets[3]

            # Remove the old pack positions. The old Continue button used
            # side="bottom", which created the large empty space.
            title.pack_forget()
            middle.pack_forget()
            middle_down.pack_forget()
            continue_button.pack_forget()

            # Group everything around the vertical center of the card.
            title.place(
                relx=0.5,
                rely=0.22,
                anchor="center"
            )

            middle.place(
                relx=0.5,
                rely=0.43,
                anchor="center"
            )

            middle_down.place(
                relx=0.5,
                rely=0.59,
                anchor="center"
            )

            continue_button.place(
                relx=0.5,
                rely=0.78,
                anchor="center"
            )

    def show_card_after_move(main):
        current_colour = main.colours_for_tiles[main.player_position]  
        if current_colour == main.colours[0]:
            main.rolleddicebuttonlabel.place_forget()
            main.game.place_forget()
            blue_cards = [
                main.card_blue_1_frame,
                main.card_blue_2_frame,
                main.card_blue_3_frame,
                main.card_blue_4_frame,
                main.card_blue_5_frame,
                main.card_blue_6_frame,
                main.card_blue_7_frame,
                main.card_blue_8_frame,
                main.card_blue_9_frame,
                main.card_blue_10_frame,
                main.card_blue_71_frame,
                main.card_blue_72_frame,
                main.card_blue_73_frame,
                main.card_blue_74_frame,
                main.card_blue_75_frame
            ]
            main.root.after(
                    1200,
                    lambda: w.PlaySound(
                        main.CARD_SOUND,
                        w.SND_FILENAME | w.SND_ASYNC
                    )
)
            main.card = r.choice(blue_cards)
            main.place_card_responsive(main.card)
            main.rolleddicebuttonlabel.place(x=10,y=65)
        elif current_colour == main.colours[1]:
            main.rolleddicebuttonlabel.place_forget()
            main.game.place_forget()
            red_cards = [
                main.card_red_11_frame,
                main.card_red_12_frame,
                main.card_red_13_frame,
                main.card_red_14_frame,
                main.card_red_15_frame,
                main.card_red_16_frame,
                main.card_red_17_frame,
                main.card_red_18_frame,
                main.card_red_19_frame,
                main.card_red_20_frame,
                main.card_red_76_frame,
                main.card_red_77_frame,
                main.card_red_78_frame,
                main.card_red_79_frame,
                main.card_red_80_frame
            ]
            main.root.after(
                    1200,
                    lambda: w.PlaySound(
                        main.CARD_SOUND,
                        w.SND_FILENAME | w.SND_ASYNC
                    )
)
            main.card = r.choice(red_cards)
            main.place_card_responsive(main.card)
            main.rolleddicebuttonlabel.place(x=10,y=65)
        elif current_colour == main.colours[2]:
            main.rolleddicebuttonlabel.place_forget()
            main.game.place_forget()
            green_cards = [
                main.card_green_21_frame,
                main.card_green_22_frame,
                main.card_green_23_frame,
                main.card_green_24_frame,
                main.card_green_25_frame,
                main.card_green_26_frame,
                main.card_green_27_frame,
                main.card_green_28_frame,
                main.card_green_29_frame,
                main.card_green_30_frame,
                main.card_green_81_frame,
                main.card_green_82_frame,
                main.card_green_83_frame,
                main.card_green_84_frame,
                main.card_green_85_frame
            ]
            main.root.after(
                    1200,
                    lambda: w.PlaySound(
                        main.CARD_SOUND,
                        w.SND_FILENAME | w.SND_ASYNC
                    )
                )
            main.card = r.choice(green_cards)
            main.place_card_responsive(main.card)
            main.rolleddicebuttonlabel.place()
        elif current_colour == main.colours[3]:
            main.rolleddicebuttonlabel.place_forget()
            main.game.place_forget()
            yellow_cards = [
                main.card_yellow_31_frame,
                main.card_yellow_32_frame,
                main.card_yellow_33_frame,
                main.card_yellow_34_frame,
                main.card_yellow_35_frame,
                main.card_yellow_36_frame,
                main.card_yellow_37_frame,
                main.card_yellow_38_frame,
                main.card_yellow_39_frame,
                main.card_yellow_40_frame,
                main.card_yellow_86_frame,
                main.card_yellow_87_frame,
                main.card_yellow_88_frame,
                main.card_yellow_89_frame,
                main.card_yellow_90_frame
            ]
            main.root.after(
                    1200,
                    lambda: w.PlaySound(
                        main.CARD_SOUND,
                        w.SND_FILENAME | w.SND_ASYNC
                    )
)
            main.card = r.choice(yellow_cards)
            main.place_card_responsive(main.card)
            main.rolleddicebuttonlabel.place(x=10,y=65)
        elif current_colour == main.colours[4]:
            main.rolleddicebuttonlabel.place_forget()
            main.game.place_forget()
            brown_cards = [
                main.card_brown_41_frame,
                main.card_brown_42_frame,
                main.card_brown_43_frame,
                main.card_brown_44_frame,
                main.card_brown_45_frame,
                main.card_brown_46_frame,
                main.card_brown_47_frame,
                main.card_brown_48_frame,
                main.card_brown_49_frame,
                main.card_brown_50_frame,
                main.card_brown_91_frame,
                main.card_brown_92_frame,
                main.card_brown_93_frame,
                main.card_brown_94_frame,
                main.card_brown_95_frame
            ]
            main.root.after(
                    1200,
                    lambda: w.PlaySound(
                        main.CARD_SOUND,
                        w.SND_FILENAME | w.SND_ASYNC
                    )
)
            main.card = r.choice(brown_cards)
            main.place_card_responsive(main.card)
            main.rolleddicebuttonlabel.place(x=10,y=65)
        elif current_colour == main.colours[5]:
            main.rolleddicebuttonlabel.place_forget()
            main.game.place_forget()
            purple_cards = [
                main.card_purple_51_frame,
                main.card_purple_52_frame,
                main.card_purple_53_frame,
                main.card_purple_54_frame,
                main.card_purple_55_frame,
                main.card_purple_56_frame,
                main.card_purple_57_frame,
                main.card_purple_58_frame,
                main.card_purple_59_frame,
                main.card_purple_60_frame,
                main.card_purple_96_frame,
                main.card_purple_97_frame,
                main.card_purple_98_frame,
                main.card_purple_99_frame,
                main.card_purple_100_frame,
            ]
            main.root.after(
                    1200,
                    lambda: w.PlaySound(
                        main.CARD_SOUND,
                        w.SND_FILENAME | w.SND_ASYNC
                    )
)
            main.card = r.choice(purple_cards)
            main.place_card_responsive(main.card)
            main.rolleddicebuttonlabel.place(x=10,y=65)
        elif current_colour == main.colours[6]:
            main.rolleddicebuttonlabel.place_forget()
            main.game.place_forget()
            orange_cards = [
                main.card_orange_61_frame,
                main.card_orange_62_frame,
                main.card_orange_63_frame,
                main.card_orange_64_frame,
                main.card_orange_65_frame,
                main.card_orange_66_frame,
                main.card_orange_67_frame,
                main.card_orange_68_frame,
                main.card_orange_69_frame,
                main.card_orange_70_frame,
                main.card_orange_101_frame,
                main.card_orange_102_frame,
                main.card_orange_103_frame,
                main.card_orange_104_frame,
                main.card_orange_105_frame,
            ]
            main.root.after(
                    1200,
                    lambda: w.PlaySound(
                        main.CARD_SOUND,
                        w.SND_FILENAME | w.SND_ASYNC
                    )
                )
            main.card = r.choice(orange_cards)
            main.place_card_responsive(main.card)
            main.rolleddicebuttonlabel.place(x=10,y=65)
        else:
            print("Error code:5500")
    def check_win(main):
        if main.player_position >= 63:
            main.show_win_screen()
            return 
        else:
            main.root.after(100, main.check_win)  # Check again in 100 ms
    def show_win_screen(main):
        #w.PlaySound("", w.SND_FILENAME | w.SND_ASYNC)
        main.tree_image = tk.PhotoImage(
            file=r"C:\Users\Sai Varun\Tkinter\Journey of a seed\Assets\Images\Supported types\tree.png")
        # Stop background sound (optional)
        # winsound.PlaySound(None, 0)

        # Win frame
        main.win_frame = tk.Frame(main.root, bg="#c8f7c5")
        main.win_frame.place(relwidth=1, relheight=1,relx=0,rely=0)

        # Title
        tk.Label(
            main.win_frame,
            text="🏆 YOU WIN! 🏆",
            font=("Segoe UI", 30, "bold"),
            bg="#c8f7c5",
            fg="darkgreen"
        ).pack(pady=20)

        # Tree Image

        tk.Label(
            main.win_frame,
            image=main.tree_image,
            bg="#c8f7c5"
        ).pack()

        # Congratulations
        tk.Label(
            main.win_frame,
            text="Congratulations!\n"
                "You successfully guided the seed\n"
                "through its amazing journey.\n\n"
                "The seed has now grown into\na beautiful tree! 🌳",
            font=("Segoe UI", 18),
            bg="#c8f7c5",
            justify="center"
        ).pack(pady=20)

        # Play Again Button
        tk.Button(
            main.win_frame,
            text="🔄 Play Again",
            font=("Segoe UI", 18, "bold"),
            bg="black",
            fg="white",
            activebackground="gray20",
            activeforeground="white",
            command=main.show_menu
        ).pack(pady=10)

        # Exit Button
        tk.Button(
            main.win_frame,
            text="❌ Exit",
            font=("Segoe UI", 16),
            bg="darkred",
            fg="white",
            command=main.root.destroy
        ).pack(pady=5)
    def animate_player_step(main, after_move = None):
        if main.animate_move_steps <= 0:
            main.is_animating = False
            main.animate_move_direction = None

            print("Animation finished!")
            print("Final position:", main.player_position)
            if after_move:
                after_move()
            return

        if main.animate_move_direction == "f":
            main.player_position += 1
        else:
            main.player_position -= 1

        if main.player_position < 0:
            main.player_position = 0
            main.animate_move_steps = 0

        elif main.player_position > 63:
            main.player_position = 63
            main.animate_move_steps = 0

        row = main.player_position // 8

        if row % 2 == 0:
            col = main.player_position % 8
        else:
            col = 7 - (main.player_position % 8)

        # Calculate the player's position from the current board size.
        player_size = max(12, main.tile_size * 0.30)
        padding = (main.tile_size - player_size) / 2
        x = main.board_x + col * main.tile_size + padding
        y = main.board_y + row * main.tile_size + padding

        main.player_size = player_size
        main.canvas_for_game.coords(
            main.player,
            x, y,
            x + player_size, y + player_size
        )

        print("Player position:", main.player_position)

        main.animate_move_steps -= 1

        main.root.after(
            550,
            lambda: main.animate_player_step(after_move)
        )
        main.check_win()
    def animate_dice(main):
        if main.dice_animation_steps <= 0:
            main.dice_animation_running = False

            # Show final dice number
            main.rolleddicebuttonlabel.config(text=str(main.final_dice_number))

            # Start player movement
            main.animate_move_steps = main.final_dice_number
            main.animate_move_direction = "f"
            main.is_animating = True

            # Move smoothly, then show the card
            main.animate_player_step(main.show_card_after_move)
            return

        # Show a random number while rolling
        random_number = r.randint(1, 3)
        main.rolleddicebuttonlabel.config(text=str(random_number))

        main.dice_animation_steps -= 1

        main.root.after(150, main.animate_dice)
    def move_f_or_b(main, how_much_to_move, f_or_b):
        if main.is_animating:
            print("Already moving — ignoring movement request.")
            return
        print("=== CARD MOVE ===")
        print("Move amount:", how_much_to_move)
        print("Direction:", f_or_b)
        print("Before:", main.player_position)

        if f_or_b not in ("f", "b"):
            print("ERROR: Invalid direction!")
            return

        # Start the animation
        main.animate_move_steps = how_much_to_move
        main.animate_move_direction = f_or_b

        main.animate_player_step()
    def frame_new_plus_board_game(main):
        main.check_win()
        main.game = tk.Frame(main.root)
        main.game.place(relx=0, rely=0, relheight=1, relwidth=1)
        main.rolleddicebuttonlabel = tk.Label(
            main.game,
            text="-",
            font=("Arial", 17),
            bg="black",
            fg="white"
        )
        main.rolleddicebuttonlabel.place(x=10, y=65)
        main.rolleddicebuttonlabel.lift()
        main.tiles = []
        main.canvas_for_game = tk.Canvas(main.game, bg="black")
        main.canvas_for_game.place(relx=0, rely=0, relheight=1, relwidth=1)
        main.colours = ["blue", "red", "green", "yellow", "brown", "purple", "orange"]
        main.colours_for_tiles = []

        # Create the 64 board tiles first. Their actual size and position
        # are calculated by resize_game_layout().
        for row in range(8):
            for col in range(8):
                main.colour = r.choice(main.colours)
                main.colours_for_tiles.append(main.colour)
                main.tiles.append(
                    main.canvas_for_game.create_rectangle(
                        0, 0, 0, 0,
                        fill=main.colour
                    )
                )
        main.canvas_for_game.bind("<Configure>", main.resize_game_layout)

        def rolldicebuttoncommand():
            print("ROLL FUNCTION ENTERED")    
            print("=== ROLL ===")
            print("Before roll:", main.player_position)
            main.rolldicebutton.config(state="disabled")
            w.PlaySound(main.DICE_SOUND, w.SND_FILENAME | w.SND_ASYNC)
            main.rolleddicebuttonlabel
            # Choose the actual final dice number
            main.final_dice_number = r.randint(1, 3)

            print("Final dice:", main.final_dice_number)
            main.rolleddicebuttonlabel.config(text = main.final_dice_number)
            main.rolleddicebuttonlabel.place(x=10,y=65)
            main.rolleddicebuttonlabel.lift()
            # Start dice animation
            main.dice_animation_steps = 10
            main.dice_animation_running = True
            main.animate_dice()
        main.rolldicebutton = tk.Button(
            main.game,
            text="🎲 Roll Dice",
            font=("Arial", 17),
            bg = "black",
            fg = "white",
            command=rolldicebuttoncommand
        )

        main.rolldicebutton.place(x=10, y=10)
        main.rolldicebutton.lift()
        # Wait until animation finishes before showing the card
        def continue_blue_1():
            print("BLUE CARD 1 PRESSED")
            main.card_blue_1_frame.place_forget()
            main.game.place(relx=0, rely=0, relheight=1, relwidth=1)

            print("Position before:", main.player_position)

            main.move_f_or_b(3, "b")

            print("Position after:", main.player_position)
            main.rolldicebutton.config(state = "normal")

        def continue_blue_2():
            main.card_blue_2_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(2,"b")
            main.rolldicebutton.config(state="normal")

        def continue_blue_3():
            main.card_blue_3_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(4,"b")
            main.rolldicebutton.config(state="normal")

        def continue_blue_4():
            main.card_blue_4_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(1,"f")
            main.rolldicebutton.config(state="normal")

        def continue_blue_5():
            main.card_blue_5_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"f")
            main.rolldicebutton.config(state="normal")

        def continue_blue_6():
            main.card_blue_6_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(2,"f")
            main.rolldicebutton.config(state="normal")

        def continue_blue_7():
            main.card_blue_7_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(2,"f")
            main.rolldicebutton.config(state="normal")

        def continue_blue_8():
            main.card_blue_8_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"f")
            main.rolldicebutton.config(state="normal")

        def continue_blue_9():
            main.card_blue_9_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(2,"f")
            main.rolldicebutton.config(state="normal")
        def continue_blue_10():
            main.card_blue_10_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"f")
            main.rolldicebutton.config(state="normal")
        def continue_red_11():
            main.card_red_11_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"b")
            main.rolldicebutton.config(state="normal")
        def continue_red_12():
            main.card_red_12_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(2,"b")
            main.rolldicebutton.config(state="normal")
        def continue_red_13():
            main.card_red_13_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(4,"b")
            main.rolldicebutton.config(state="normal")
        def continue_red_14():
            main.card_red_14_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"f")
            main.rolldicebutton.config(state="normal")
        def continue_red_15():
            main.card_red_15_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(2,"f")
            main.rolldicebutton.config(state="normal")
        def continue_red_16():
            main.card_red_16_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(2,"f")
            main.rolldicebutton.config(state="normal")
        def continue_red_17():
            main.card_red_17_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"f")
            main.rolldicebutton.config(state="normal")
        def continue_red_18():
            main.card_red_18_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"f")
            main.rolldicebutton.config(state="normal")
        def continue_red_19():
            main.card_red_19_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(2,"f")
            main.rolldicebutton.config(state="normal")
        def continue_red_20():
            main.card_red_20_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"f")
            main.rolldicebutton.config(state="normal")
        def continue_green_21():
            main.card_green_21_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"b")
            main.rolldicebutton.config(state="normal")
        def continue_green_22():
            main.card_green_22_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"b")
            main.rolldicebutton.config(state="normal")
        def continue_green_23():
            main.card_green_23_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(4,"b")
            main.rolldicebutton.config(state="normal")
        def continue_green_24():
            main.card_green_24_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(2,"f")
            main.rolldicebutton.config(state="normal")
        def continue_green_25():
            main.card_green_25_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"f")
            main.rolldicebutton.config(state="normal")
        def continue_green_26():
            main.card_green_26_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"f")
            main.rolldicebutton.config(state="normal")
        def continue_green_27():
            main.card_green_27_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(2,"f")
            main.rolldicebutton.config(state="normal")
        def continue_green_28():
            main.card_green_28_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"f")
            main.rolldicebutton.config(state="normal")
        def continue_green_29():
            main.card_green_29_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(2,"f")
            main.rolldicebutton.config(state="normal")
        def continue_green_30():
            main.card_green_30_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"f")
            main.rolldicebutton.config(state="normal")
        def continue_yellow_31():
            main.card_yellow_31_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"f")
            main.rolldicebutton.config(state="normal")
        def continue_yellow_32():
            main.card_yellow_32_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"f")
            main.rolldicebutton.config(state="normal")
        def continue_yellow_33():
            main.card_yellow_33_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(2,"f")
            main.rolldicebutton.config(state="normal")
        def continue_yellow_34():
            main.card_yellow_34_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"f")
            main.rolldicebutton.config(state="normal")
        def continue_yellow_35():
            main.card_yellow_35_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"f")
            main.rolldicebutton.config(state="normal")
        def continue_yellow_36():
            main.card_yellow_36_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"f")
            main.rolldicebutton.config(state="normal")
        def continue_yellow_37():
            main.card_yellow_37_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(2,"f")
            main.rolldicebutton.config(state="normal")
        def continue_yellow_38():
            main.card_yellow_38_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"f")
            main.rolldicebutton.config(state="normal")
        def continue_yellow_39():
            main.card_yellow_39_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"f")
            main.rolldicebutton.config(state="normal")
        def continue_yellow_40():
            main.card_yellow_40_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"f")
            main.rolldicebutton.config(state="normal")
        def continue_brown_41():
            main.card_brown_41_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"f")
            main.rolldicebutton.config(state="normal")
        def continue_brown_42():
            main.card_brown_42_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"f")
            main.rolldicebutton.config(state="normal")
        def continue_brown_43():
            main.card_brown_43_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(2,"f")
            main.rolldicebutton.config(state="normal")
        def continue_brown_44():
            main.card_brown_44_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"f")
            main.rolldicebutton.config(state="normal")
        def continue_brown_45():
            main.card_brown_45_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"f")
            main.rolldicebutton.config(state="normal")
        def continue_brown_46():
            main.card_brown_46_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"f")
            main.rolldicebutton.config(state="normal")
        def continue_brown_47():
            main.card_brown_47_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(2,"f")
            main.rolldicebutton.config(state="normal")
        def continue_brown_48():
            main.card_brown_48_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"f")
            main.rolldicebutton.config(state="normal")
        def continue_brown_49():
            main.card_brown_49_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"f")
            main.rolldicebutton.config(state="normal")
        def continue_brown_50():
            main.card_brown_50_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"b")
            main.rolldicebutton.config(state="normal")
        def continue_purple_51():
            main.card_purple_51_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"f")
            main.rolldicebutton.config(state="normal")
        def continue_purple_52():
            main.card_purple_52_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(2,"f")
            main.rolldicebutton.config(state="normal")
        def continue_purple_53():
            main.card_purple_53_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"f")
            main.rolldicebutton.config(state="normal")
        def continue_purple_54():
            main.card_purple_54_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"f")
            main.rolldicebutton.config(state="normal")
        def continue_purple_55():
            main.card_purple_55_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"f")
            main.rolldicebutton.config(state="normal")
        def continue_purple_56():
            main.card_purple_56_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"f")
            main.rolldicebutton.config(state="normal")
        def continue_purple_57():
            main.card_purple_57_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(2,"f")
            main.rolldicebutton.config(state="normal")
        def continue_purple_58():
            main.card_purple_58_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"f")
            main.rolldicebutton.config(state="normal")
        def continue_purple_59():
            main.card_purple_59_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"f")
            main.rolldicebutton.config(state="normal")
        def continue_purple_60():
            main.card_purple_60_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"f")
            main.rolldicebutton.config(state="normal")
        def continue_orange_61():
            main.card_orange_61_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(2,"f")
            main.rolldicebutton.config(state="normal")
        def continue_orange_62():
            main.card_orange_62_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"f")
            main.rolldicebutton.config(state="normal")
        def continue_orange_63():
            main.card_orange_63_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"f")
            main.rolldicebutton.config(state="normal")
        def continue_orange_64():
            main.card_orange_64_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"f")
            main.rolldicebutton.config(state="normal")
        def continue_orange_65():
            main.card_orange_65_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"f")
            main.rolldicebutton.config(state="normal")
        def continue_orange_66():
            main.card_orange_66_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(2,"f")
            main.rolldicebutton.config(state="normal")
        def continue_orange_67():
            main.card_orange_67_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"f")
            main.rolldicebutton.config(state="normal")
        def continue_orange_68():
            main.card_orange_68_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"f")
            main.rolldicebutton.config(state="normal")
        def continue_orange_69():
            main.card_orange_69_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"f")
            main.rolldicebutton.config(state="normal")
        def continue_orange_70():
            main.card_orange_70_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(2,"f")
        def continue_blue_71():
            main.card_blue_71_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"b")
            main.rolldicebutton.config(state="normal")

        def continue_blue_72():
            main.card_blue_72_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(4,"b")
            main.rolldicebutton.config(state="normal")

        def continue_blue_73():
            main.card_blue_73_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(2,"b")
            main.rolldicebutton.config(state="normal")

        def continue_blue_74():
            main.card_blue_74_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"b")
            main.rolldicebutton.config(state="normal")

        def continue_blue_75():
            main.card_blue_75_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(4,"b")
            main.rolldicebutton.config(state="normal")

        def continue_red_76():
            main.card_red_76_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"b")
            main.rolldicebutton.config(state="normal")

        def continue_red_77():
            main.card_red_77_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(2,"b")
            main.rolldicebutton.config(state="normal")

        def continue_red_78():
            main.card_red_78_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"b")
            main.rolldicebutton.config(state="normal")

        def continue_red_79():
            main.card_red_79_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(4,"b")
            main.rolldicebutton.config(state="normal")

        def continue_red_80():
            main.card_red_80_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"b")
            main.rolldicebutton.config(state="normal")

        def continue_green_81():
            main.card_green_81_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(2,"b")
            main.rolldicebutton.config(state="normal")

        def continue_green_82():
            main.card_green_82_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"b")
            main.rolldicebutton.config(state="normal")

        def continue_green_83():
            main.card_green_83_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(2,"b")
            main.rolldicebutton.config(state="normal")

        def continue_green_84():
            main.card_green_84_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"b")
            main.rolldicebutton.config(state="normal")

        def continue_green_85():
            main.card_green_85_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(4,"b")
            main.rolldicebutton.config(state="normal")

        def continue_yellow_86():
            main.card_yellow_86_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"b")
            main.rolldicebutton.config(state="normal")

        def continue_yellow_87():
            main.card_yellow_87_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(2,"b")
            main.rolldicebutton.config(state="normal")

        def continue_yellow_88():
            main.card_yellow_88_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"b")
            main.rolldicebutton.config(state="normal")

        def continue_yellow_89():
            main.card_yellow_89_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(4,"b")
            main.rolldicebutton.config(state="normal")

        def continue_yellow_90():
            main.card_yellow_90_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"b")
            main.rolldicebutton.config(state="normal")

        def continue_brown_91():
            main.card_brown_91_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"b")
            main.rolldicebutton.config(state="normal")

        def continue_brown_92():
            main.card_brown_92_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(2,"b")
            main.rolldicebutton.config(state="normal")

        def continue_brown_93():
            main.card_brown_93_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(4,"b")
            main.rolldicebutton.config(state="normal")

        def continue_brown_94():
            main.card_brown_94_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"b")
            main.rolldicebutton.config(state="normal")

        def continue_brown_95():
            main.card_brown_95_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(4,"b")
            main.rolldicebutton.config(state="normal")

        def continue_purple_96():
            main.card_purple_96_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"b")
            main.rolldicebutton.config(state="normal")

        def continue_purple_97():
            main.card_purple_97_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(2,"b")
            main.rolldicebutton.config(state="normal")

        def continue_purple_98():
            main.card_purple_98_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"b")
            main.rolldicebutton.config(state="normal")

        def continue_purple_99():
            main.card_purple_99_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(4,"b")
            main.rolldicebutton.config(state="normal")

        def continue_purple_100():
            main.card_purple_100_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"b")
            main.rolldicebutton.config(state="normal")

        def continue_orange_101():
            main.card_orange_101_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(4,"b")
            main.rolldicebutton.config(state="normal")

        def continue_orange_102():
            main.card_orange_102_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"b")
            main.rolldicebutton.config(state="normal")

        def continue_orange_103():
            main.card_orange_103_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(4,"b")
            main.rolldicebutton.config(state="normal")

        def continue_orange_104():
            main.card_orange_104_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(2,"b")
            main.rolldicebutton.config(state="normal")

        def continue_orange_105():
            main.card_orange_105_frame.place_forget()
            main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
            main.move_f_or_b(3,"b")
            main.rolldicebutton.config(state="normal")
            main.rolldicebutton.config(state="normal")
        main.card_blue_1_frame = tk.Frame(main.root, bg="white", bd=5, relief="ridge")
        main.card_blue_1_title = tk.Label(main.card_blue_1_frame,
                                text="🌧 BLUE CARD",
                                font=("Arial",20,"bold"),
                                bg="white",
                                fg="blue")
        main.card_blue_1_label_middle = tk.Label(main.card_blue_1_frame,
                                        text="Strong wind.",
                                        font=("Arial",16),
                                        bg="white")
        main.card_blue_1_label_middle_down = tk.Label(main.card_blue_1_frame,
                                                  text="Move back 3 spaces spaces.",
                                                  font=("Arial",14,"bold"),
                                                  bg="white",
                                                  fg="green")
        main.card_blue_1_continue = tk.Button(main.card_blue_1_frame,text = "continue")
        main.card_blue_1_title.pack(pady=20)
        main.card_blue_1_label_middle.pack(pady=20)
        main.card_blue_1_label_middle_down.pack(pady=20)
        main.card_blue_1_continue.pack(side="bottom", pady=20)
        # ===========================
        # BLUE CARD 2
        # ===========================
        main.card_blue_2_frame = tk.Frame(main.root, bg="white", bd=5, relief="ridge")
        main.card_blue_2_title = tk.Label(main.card_blue_2_frame,
                                        text="🌧 BLUE CARD",
                                        font=("Arial",20,"bold"),
                                        bg="white",
                                        fg="blue")
        main.card_blue_2_label_middle = tk.Label(main.card_blue_2_frame,
                                                text="Wind Gust",
                                                font=("Arial",16),
                                                bg="white")
        main.card_blue_2_label_middle_down = tk.Label(main.card_blue_2_frame,
                                                    text="Move back 2 spaces.",
                                                    font=("Arial",14,"bold"),
                                                    bg="white",
                                                    fg="green")
        main.card_blue_2_continue = tk.Button(main.card_blue_2_frame,
                                            text="Continue")
        main.card_blue_2_title.pack(pady=20)
        main.card_blue_2_label_middle.pack(pady=20)
        main.card_blue_2_label_middle_down.pack(pady=20)
        main.card_blue_2_continue.pack(side="bottom", pady=20)
        # ===========================
        # BLUE CARD 3
        # ===========================
        main.card_blue_3_frame = tk.Frame(main.root, bg="white", bd=5, relief="ridge")
        main.card_blue_3_title = tk.Label(main.card_blue_3_frame,
                                        text="🌧 BLUE CARD",
                                        font=("Arial",20,"bold"),
                                        bg="white",
                                        fg="blue")
        main.card_blue_3_label_middle = tk.Label(main.card_blue_3_frame,
                                                text="Stormy air.",
                                                font=("Arial",16),
                                                bg="white")
        main.card_blue_3_label_middle_down = tk.Label(main.card_blue_3_frame,
                                                    text="Move backward 4 spaces.",
                                                    font=("Arial",14,"bold"),
                                                    bg="white",
                                                    fg="green")
        main.card_blue_3_continue = tk.Button(main.card_blue_3_frame,
                                            text="Continue")
        main.card_blue_3_title.pack(pady=20)
        main.card_blue_3_label_middle.pack(pady=20)
        main.card_blue_3_label_middle_down.pack(pady=20)
        main.card_blue_3_continue.pack(side="bottom", pady=20)
        # ===========================
        # BLUE CARD 4
        # ===========================
        main.card_blue_4_frame = tk.Frame(main.root, bg="white", bd=5, relief="ridge")
        main.card_blue_4_title = tk.Label(main.card_blue_4_frame,
                                        text="🌧 BLUE CARD",
                                        font=("Arial",20,"bold"),
                                        bg="white",
                                        fg="blue")
        main.card_blue_4_label_middle = tk.Label(main.card_blue_4_frame,
                                                text="Water reaches rich soil.",
                                                font=("Arial",16),
                                                bg="white")
        main.card_blue_4_label_middle_down = tk.Label(main.card_blue_4_frame,
                                                    text="Move forward 1 space.",
                                                    font=("Arial",14,"bold"),
                                                    bg="white",
                                                    fg="green")
        main.card_blue_4_continue = tk.Button(main.card_blue_4_frame,
                                            text="Continue")
        main.card_blue_4_title.pack(pady=20)
        main.card_blue_4_label_middle.pack(pady=20)
        main.card_blue_4_label_middle_down.pack(pady=20)
        main.card_blue_4_continue.pack(side="bottom", pady=20)
        # ===========================
        # BLUE CARD 5
        # ===========================
        main.card_blue_5_frame = tk.Frame(main.root, bg="white", bd=5, relief="ridge")
        main.card_blue_5_title = tk.Label(main.card_blue_5_frame,
                                        text="🌧 BLUE CARD",
                                        font=("Arial",20,"bold"),
                                        bg="white",
                                        fg="blue")
        main.card_blue_5_label_middle = tk.Label(main.card_blue_5_frame,
                                                text="Floodwater carries you far away.",
                                                font=("Arial",16),
                                                bg="white")
        main.card_blue_5_label_middle_down = tk.Label(main.card_blue_5_frame,
                                                    text="Move forward 3 spaces.",
                                                    font=("Arial",14,"bold"),
                                                    bg="white",
                                                    fg="green")
        main.card_blue_5_continue = tk.Button(main.card_blue_5_frame,
                                            text="Continue")
        main.card_blue_5_title.pack(pady=20)
        main.card_blue_5_label_middle.pack(pady=20)
        main.card_blue_5_label_middle_down.pack(pady=20)
        main.card_blue_5_continue.pack(side="bottom", pady=20)
        main.card_blue_6_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_blue_6_title=tk.Label(main.card_blue_6_frame,text="🌧 BLUE CARD",font=("Arial",20,"bold"),bg="white",fg="blue")
        main.card_blue_6_label_middle=tk.Label(main.card_blue_6_frame,text="Fresh water helps you survive.",font=("Arial",16),bg="white")
        main.card_blue_6_label_middle_down=tk.Label(main.card_blue_6_frame,text="Move forward 2 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_blue_6_continue=tk.Button(main.card_blue_6_frame,text="Continue")
        main.card_blue_6_title.pack(pady=20)
        main.card_blue_6_label_middle.pack(pady=20)
        main.card_blue_6_label_middle_down.pack(pady=20)
        main.card_blue_6_continue.pack(side="bottom",pady=20)
        main.card_blue_7_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_blue_7_title=tk.Label(main.card_blue_7_frame,text="🌧 BLUE CARD",font=("Arial",20,"bold"),bg="white",fg="blue")
        main.card_blue_7_label_middle=tk.Label(main.card_blue_7_frame,text="Rain washes away obstacles.",font=("Arial",16),bg="white")
        main.card_blue_7_label_middle_down=tk.Label(main.card_blue_7_frame,text="Move forward 2 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_blue_7_continue=tk.Button(main.card_blue_7_frame,text="Continue")
        main.card_blue_7_title.pack(pady=20)
        main.card_blue_7_label_middle.pack(pady=20)
        main.card_blue_7_label_middle_down.pack(pady=20)
        main.card_blue_7_continue.pack(side="bottom",pady=20)
        main.card_blue_8_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_blue_8_title=tk.Label(main.card_blue_8_frame,text="🌧 BLUE CARD",font=("Arial",20,"bold"),bg="white",fg="blue")
        main.card_blue_8_label_middle=tk.Label(main.card_blue_8_frame,text="Your seed floats to a new habitat.",font=("Arial",16),bg="white")
        main.card_blue_8_label_middle_down=tk.Label(main.card_blue_8_frame,text="Move forward 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_blue_8_continue=tk.Button(main.card_blue_8_frame,text="Continue")
        main.card_blue_8_title.pack(pady=20)
        main.card_blue_8_label_middle.pack(pady=20)
        main.card_blue_8_label_middle_down.pack(pady=20)
        main.card_blue_8_continue.pack(side="bottom",pady=20)
        main.card_blue_9_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_blue_9_title=tk.Label(main.card_blue_9_frame,text="🌧 BLUE CARD",font=("Arial",20,"bold"),bg="white",fg="blue")
        main.card_blue_9_label_middle=tk.Label(main.card_blue_9_frame,text="The current moves you quickly.",font=("Arial",16),bg="white")
        main.card_blue_9_label_middle_down=tk.Label(main.card_blue_9_frame,text="Move forward 2 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_blue_9_continue=tk.Button(main.card_blue_9_frame,text="Continue")
        main.card_blue_9_title.pack(pady=20)
        main.card_blue_9_label_middle.pack(pady=20)
        main.card_blue_9_label_middle_down.pack(pady=20)
        main.card_blue_9_continue.pack(side="bottom",pady=20)
        main.card_blue_10_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_blue_10_title=tk.Label(main.card_blue_10_frame,text="🌧 BLUE CARD",font=("Arial",20,"bold"),bg="white",fg="blue")
        main.card_blue_10_label_middle=tk.Label(main.card_blue_10_frame,text="You reach the perfect place to grow.",font=("Arial",16),bg="white")
        main.card_blue_10_label_middle_down=tk.Label(main.card_blue_10_frame,text="Move forward 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_blue_10_continue=tk.Button(main.card_blue_10_frame,text="Continue")
        main.card_blue_10_title.pack(pady=20)
        main.card_blue_10_label_middle.pack(pady=20)
        main.card_blue_10_label_middle_down.pack(pady=20)
        main.card_blue_10_continue.pack(side="bottom",pady=20)
        main.card_red_11_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_red_11_title=tk.Label(main.card_red_11_frame,text="🍎 RED CARD",font=("Arial",20,"bold"),bg="white",fg="red")
        main.card_red_11_label_middle=tk.Label(main.card_red_11_frame,text="Bird Trouble",font=("Arial",16),bg="white")
        main.card_red_11_label_middle_down=tk.Label(main.card_red_11_frame,text="Move back 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_red_11_continue=tk.Button(main.card_red_11_frame,text="Continue")
        main.card_red_11_title.pack(pady=20)
        main.card_red_11_label_middle.pack(pady=20)
        main.card_red_11_label_middle_down.pack(pady=20)
        main.card_red_11_continue.pack(side="bottom",pady=20)
        main.card_red_12_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_red_12_title=tk.Label(main.card_red_12_frame,text="🍎 RED CARD",font=("Arial",20,"bold"),bg="white",fg="red")
        main.card_red_12_label_middle=tk.Label(main.card_red_12_frame,text="Seed dropped",font=("Arial",16),bg="white")
        main.card_red_12_label_middle_down=tk.Label(main.card_red_12_frame,text="Move back 2 spaces!",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_red_12_continue=tk.Button(main.card_red_12_frame,text="Continue")
        main.card_red_12_title.pack(pady=20)
        main.card_red_12_label_middle.pack(pady=20)
        main.card_red_12_label_middle_down.pack(pady=20)
        main.card_red_12_continue.pack(side="bottom",pady=20)
        main.card_red_13_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_red_13_title=tk.Label(main.card_red_13_frame,text="🍎 RED CARD",font=("Arial",20,"bold"),bg="white",fg="red")
        main.card_red_13_label_middle=tk.Label(main.card_red_13_frame,text="Hungry bird",font=("Arial",16),bg="white")
        main.card_red_13_label_middle_down=tk.Label(main.card_red_13_frame,text="Move back 4 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_red_13_continue=tk.Button(main.card_red_13_frame,text="Continue")
        main.card_red_13_title.pack(pady=20)
        main.card_red_13_label_middle.pack(pady=20)
        main.card_red_13_label_middle_down.pack(pady=20)
        main.card_red_13_continue.pack(side="bottom",pady=20)
        main.card_red_14_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_red_14_title=tk.Label(main.card_red_14_frame,text="🍎 RED CARD",font=("Arial",20,"bold"),bg="white",fg="red")
        main.card_red_14_label_middle=tk.Label(main.card_red_14_frame,text="A monkey carries your fruit to another tree.",font=("Arial",16),bg="white")
        main.card_red_14_label_middle_down=tk.Label(main.card_red_14_frame,text="Move forward 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_red_14_continue=tk.Button(main.card_red_14_frame,text="Continue")
        main.card_red_14_title.pack(pady=20)
        main.card_red_14_label_middle.pack(pady=20)
        main.card_red_14_label_middle_down.pack(pady=20)
        main.card_red_14_continue.pack(side="bottom",pady=20)
        main.card_red_15_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_red_15_title=tk.Label(main.card_red_15_frame,text="🍎 RED CARD",font=("Arial",20,"bold"),bg="white",fg="red")
        main.card_red_15_label_middle=tk.Label(main.card_red_15_frame,text="A deer carries your seed in its fur.",font=("Arial",16),bg="white")
        main.card_red_15_label_middle_down=tk.Label(main.card_red_15_frame,text="Move forward 2 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_red_15_continue=tk.Button(main.card_red_15_frame,text="Continue")
        main.card_red_15_title.pack(pady=20)
        main.card_red_15_label_middle.pack(pady=20)
        main.card_red_15_label_middle_down.pack(pady=20)
        main.card_red_15_continue.pack(side="bottom",pady=20)
        main.card_red_16_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_red_16_title=tk.Label(main.card_red_16_frame,text="🍎 RED CARD",font=("Arial",20,"bold"),bg="white",fg="red")
        main.card_red_16_label_middle=tk.Label(main.card_red_16_frame,text="A fox brushes past and carries your seed.",font=("Arial",16),bg="white")
        main.card_red_16_label_middle_down=tk.Label(main.card_red_16_frame,text="Move forward 2 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_red_16_continue=tk.Button(main.card_red_16_frame,text="Continue")
        main.card_red_16_title.pack(pady=20)
        main.card_red_16_label_middle.pack(pady=20)
        main.card_red_16_label_middle_down.pack(pady=20)
        main.card_red_16_continue.pack(side="bottom",pady=20)
        main.card_red_17_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_red_17_title=tk.Label(main.card_red_17_frame,text="🍎 RED CARD",font=("Arial",20,"bold"),bg="white",fg="red")
        main.card_red_17_label_middle=tk.Label(main.card_red_17_frame,text="A rabbit carries your seed to a meadow.",font=("Arial",16),bg="white")
        main.card_red_17_label_middle_down=tk.Label(main.card_red_17_frame,text="Move forward 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_red_17_continue=tk.Button(main.card_red_17_frame,text="Continue")
        main.card_red_17_title.pack(pady=20)
        main.card_red_17_label_middle.pack(pady=20)
        main.card_red_17_label_middle_down.pack(pady=20)
        main.card_red_17_continue.pack(side="bottom",pady=20)
        main.card_red_18_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_red_18_title=tk.Label(main.card_red_18_frame,text="🍎 RED CARD",font=("Arial",20,"bold"),bg="white",fg="red")
        main.card_red_18_label_middle=tk.Label(main.card_red_18_frame,text="A bird drops your seed in fertile soil.",font=("Arial",16),bg="white")
        main.card_red_18_label_middle_down=tk.Label(main.card_red_18_frame,text="Move forward 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_red_18_continue=tk.Button(main.card_red_18_frame,text="Continue")
        main.card_red_18_title.pack(pady=20)
        main.card_red_18_label_middle.pack(pady=20)
        main.card_red_18_label_middle_down.pack(pady=20)
        main.card_red_18_continue.pack(side="bottom",pady=20)
        main.card_red_19_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_red_19_title=tk.Label(main.card_red_19_frame,text="🍎 RED CARD",font=("Arial",20,"bold"),bg="white",fg="red")
        main.card_red_19_label_middle=tk.Label(main.card_red_19_frame,text="An animal leaves your seed near a river.",font=("Arial",16),bg="white")
        main.card_red_19_label_middle_down=tk.Label(main.card_red_19_frame,text="Move forward 2 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_red_19_continue=tk.Button(main.card_red_19_frame,text="Continue")
        main.card_red_19_title.pack(pady=20)
        main.card_red_19_label_middle.pack(pady=20)
        main.card_red_19_label_middle_down.pack(pady=20)
        main.card_red_19_continue.pack(side="bottom",pady=20)
        main.card_red_20_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_red_20_title=tk.Label(main.card_red_20_frame,text="🍎 RED CARD",font=("Arial",20,"bold"),bg="white",fg="red")
        main.card_red_20_label_middle=tk.Label(main.card_red_20_frame,text="A herd of animals spreads your seeds widely.",font=("Arial",16),bg="white")
        main.card_red_20_label_middle_down=tk.Label(main.card_red_20_frame,text="Move forward 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_red_20_continue=tk.Button(main.card_red_20_frame,text="Continue")
        main.card_red_20_title.pack(pady=20)
        main.card_red_20_label_middle.pack(pady=20)
        main.card_red_20_label_middle_down.pack(pady=20)
        main.card_red_20_continue.pack(side="bottom",pady=20)

        main.card_green_21_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_green_21_title=tk.Label(main.card_green_21_frame,text="🌿 GREEN CARD",font=("Arial",20,"bold"),bg="white",fg="green")
        main.card_green_21_label_middle=tk.Label(main.card_green_21_frame,text="Thick Bush",font=("Arial",16),bg="white")
        main.card_green_21_label_middle_down=tk.Label(main.card_green_21_frame,text="Move back 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_green_21_continue=tk.Button(main.card_green_21_frame,text="Continue")
        main.card_green_21_title.pack(pady=20)
        main.card_green_21_label_middle.pack(pady=20)
        main.card_green_21_label_middle_down.pack(pady=20)
        main.card_green_21_continue.pack(side="bottom",pady=20)

        main.card_green_22_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_green_22_title=tk.Label(main.card_green_22_frame,text="🌿 GREEN CARD",font=("Arial",20,"bold"),bg="white",fg="green")
        main.card_green_22_label_middle=tk.Label(main.card_green_22_frame,text="Blocked Path",font=("Arial",16),bg="white")
        main.card_green_22_label_middle_down=tk.Label(main.card_green_22_frame,text="Move back 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_green_22_continue=tk.Button(main.card_green_22_frame,text="Continue")
        main.card_green_22_title.pack(pady=20)
        main.card_green_22_label_middle.pack(pady=20)
        main.card_green_22_label_middle_down.pack(pady=20)
        main.card_green_22_continue.pack(side="bottom",pady=20)

        main.card_green_23_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_green_23_title=tk.Label(main.card_green_23_frame,text="🌿 GREEN CARD",font=("Arial",20,"bold"),bg="white",fg="green")
        main.card_green_23_label_middle=tk.Label(main.card_green_23_frame,text="Hungry bird",font=("Arial",16),bg="white")
        main.card_green_23_label_middle_down=tk.Label(main.card_green_23_frame,text="Move back 4 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_green_23_continue=tk.Button(main.card_green_23_frame,text="Continue")
        main.card_green_23_title.pack(pady=20)
        main.card_green_23_label_middle.pack(pady=20)
        main.card_green_23_label_middle_down.pack(pady=20)
        main.card_green_23_continue.pack(side="bottom",pady=20)

        main.card_green_24_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_green_24_title=tk.Label(main.card_green_24_frame,text="🌿 GREEN CARD",font=("Arial",20,"bold"),bg="white",fg="green")
        main.card_green_24_label_middle=tk.Label(main.card_green_24_frame,text="The wind drops you in rich soil.",font=("Arial",16),bg="white")
        main.card_green_24_label_middle_down=tk.Label(main.card_green_24_frame,text="Move forward 2 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_green_24_continue=tk.Button(main.card_green_24_frame,text="Continue")
        main.card_green_24_title.pack(pady=20)
        main.card_green_24_label_middle.pack(pady=20)
        main.card_green_24_label_middle_down.pack(pady=20)
        main.card_green_24_continue.pack(side="bottom",pady=20)

        main.card_green_25_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_green_25_title=tk.Label(main.card_green_25_frame,text="🌿 GREEN CARD",font=("Arial",20,"bold"),bg="white",fg="green")
        main.card_green_25_label_middle=tk.Label(main.card_green_25_frame,text="A gust sends your seed across a field.",font=("Arial",16),bg="white")
        main.card_green_25_label_middle_down=tk.Label(main.card_green_25_frame,text="Move forward 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_green_25_continue=tk.Button(main.card_green_25_frame,text="Continue")
        main.card_green_25_title.pack(pady=20)
        main.card_green_25_label_middle.pack(pady=20)
        main.card_green_25_label_middle_down.pack(pady=20)
        main.card_green_25_continue.pack(side="bottom",pady=20)

        main.card_green_26_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_green_26_title=tk.Label(main.card_green_26_frame,text="🌿 GREEN CARD",font=("Arial",20,"bold"),bg="white",fg="green")
        main.card_green_26_label_middle=tk.Label(main.card_green_26_frame,text="Your parachute seed floats gently.",font=("Arial",16),bg="white")
        main.card_green_26_label_middle_down=tk.Label(main.card_green_26_frame,text="Move forward 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_green_26_continue=tk.Button(main.card_green_26_frame,text="Continue")
        main.card_green_26_title.pack(pady=20)
        main.card_green_26_label_middle.pack(pady=20)
        main.card_green_26_label_middle_down.pack(pady=20)
        main.card_green_26_continue.pack(side="bottom",pady=20)

        main.card_green_27_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_green_27_title=tk.Label(main.card_green_27_frame,text="🌿 GREEN CARD",font=("Arial",20,"bold"),bg="white",fg="green")
        main.card_green_27_label_middle=tk.Label(main.card_green_27_frame,text="A cool breeze keeps you flying.",font=("Arial",16),bg="white")
        main.card_green_27_label_middle_down=tk.Label(main.card_green_27_frame,text="Move forward 2 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_green_27_continue=tk.Button(main.card_green_27_frame,text="Continue")
        main.card_green_27_title.pack(pady=20)
        main.card_green_27_label_middle.pack(pady=20)
        main.card_green_27_label_middle_down.pack(pady=20)
        main.card_green_27_continue.pack(side="bottom",pady=20)

        main.card_green_28_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_green_28_title=tk.Label(main.card_green_28_frame,text="🌿 GREEN CARD",font=("Arial",20,"bold"),bg="white",fg="green")
        main.card_green_28_label_middle=tk.Label(main.card_green_28_frame,text="The wind carries you over a river.",font=("Arial",16),bg="white")
        main.card_green_28_label_middle_down=tk.Label(main.card_green_28_frame,text="Move forward 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_green_28_continue=tk.Button(main.card_green_28_frame,text="Continue")
        main.card_green_28_title.pack(pady=20)
        main.card_green_28_label_middle.pack(pady=20)
        main.card_green_28_label_middle_down.pack(pady=20)
        main.card_green_28_continue.pack(side="bottom",pady=20)

        main.card_green_29_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_green_29_title=tk.Label(main.card_green_29_frame,text="🌿 GREEN CARD",font=("Arial",20,"bold"),bg="white",fg="green")
        main.card_green_29_label_middle=tk.Label(main.card_green_29_frame,text="Your seed lands in a sunny clearing.",font=("Arial",16),bg="white")
        main.card_green_29_label_middle_down=tk.Label(main.card_green_29_frame,text="Move forward 2 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_green_29_continue=tk.Button(main.card_green_29_frame,text="Continue")
        main.card_green_29_title.pack(pady=20)
        main.card_green_29_label_middle.pack(pady=20)
        main.card_green_29_label_middle_down.pack(pady=20)
        main.card_green_29_continue.pack(side="bottom",pady=20)

        main.card_green_30_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_green_30_title=tk.Label(main.card_green_30_frame,text="🌿 GREEN CARD",font=("Arial",20,"bold"),bg="white",fg="green")
        main.card_green_30_label_middle=tk.Label(main.card_green_30_frame,text="The wind spreads your seeds perfectly.",font=("Arial",16),bg="white")
        main.card_green_30_label_middle_down=tk.Label(main.card_green_30_frame,text="Move forward 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_green_30_continue=tk.Button(main.card_green_30_frame,text="Continue")
        main.card_green_30_title.pack(pady=20)
        main.card_green_30_label_middle.pack(pady=20)
        main.card_green_30_label_middle_down.pack(pady=20)
        main.card_green_30_continue.pack(side="bottom",pady=20)

        main.card_yellow_31_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_yellow_31_title=tk.Label(main.card_yellow_31_frame,text="💥 YELLOW CARD",font=("Arial",20,"bold"),bg="white",fg="goldenrod")
        main.card_yellow_31_label_middle=tk.Label(main.card_yellow_31_frame,text="Your pod bursts open in the sunshine.",font=("Arial",16),bg="white")
        main.card_yellow_31_label_middle_down=tk.Label(main.card_yellow_31_frame,text="Move forward 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_yellow_31_continue=tk.Button(main.card_yellow_31_frame,text="Continue")
        main.card_yellow_31_title.pack(pady=20)
        main.card_yellow_31_label_middle.pack(pady=20)
        main.card_yellow_31_label_middle_down.pack(pady=20)
        main.card_yellow_31_continue.pack(side="bottom",pady=20)

        main.card_yellow_32_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_yellow_32_title=tk.Label(main.card_yellow_32_frame,text="💥 YELLOW CARD",font=("Arial",20,"bold"),bg="white",fg="goldenrod")
        main.card_yellow_32_label_middle=tk.Label(main.card_yellow_32_frame,text="The seed pod explodes with a pop!",font=("Arial",16),bg="white")
        main.card_yellow_32_label_middle_down=tk.Label(main.card_yellow_32_frame,text="Move forward 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_yellow_32_continue=tk.Button(main.card_yellow_32_frame,text="Continue")
        main.card_yellow_32_title.pack(pady=20)
        main.card_yellow_32_label_middle.pack(pady=20)
        main.card_yellow_32_label_middle_down.pack(pady=20)
        main.card_yellow_32_continue.pack(side="bottom",pady=20)

        main.card_yellow_33_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_yellow_33_title=tk.Label(main.card_yellow_33_frame,text="💥 YELLOW CARD",font=("Arial",20,"bold"),bg="white",fg="goldenrod")
        main.card_yellow_33_label_middle=tk.Label(main.card_yellow_33_frame,text="Your seed is launched into a meadow.",font=("Arial",16),bg="white")
        main.card_yellow_33_label_middle_down=tk.Label(main.card_yellow_33_frame,text="Move forward 2 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_yellow_33_continue=tk.Button(main.card_yellow_33_frame,text="Continue")
        main.card_yellow_33_title.pack(pady=20)
        main.card_yellow_33_label_middle.pack(pady=20)
        main.card_yellow_33_label_middle_down.pack(pady=20)
        main.card_yellow_33_continue.pack(side="bottom",pady=20)

        main.card_yellow_34_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_yellow_34_title=tk.Label(main.card_yellow_34_frame,text="💥 YELLOW CARD",font=("Arial",20,"bold"),bg="white",fg="goldenrod")
        main.card_yellow_34_label_middle=tk.Label(main.card_yellow_34_frame,text="The pod dries and suddenly bursts.",font=("Arial",16),bg="white")
        main.card_yellow_34_label_middle_down=tk.Label(main.card_yellow_34_frame,text="Move forward 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_yellow_34_continue=tk.Button(main.card_yellow_34_frame,text="Continue")
        main.card_yellow_34_title.pack(pady=20)
        main.card_yellow_34_label_middle.pack(pady=20)
        main.card_yellow_34_label_middle_down.pack(pady=20)
        main.card_yellow_34_continue.pack(side="bottom",pady=20)

        main.card_yellow_35_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_yellow_35_title=tk.Label(main.card_yellow_35_frame,text="💥 YELLOW CARD",font=("Arial",20,"bold"),bg="white",fg="goldenrod")
        main.card_yellow_35_label_middle=tk.Label(main.card_yellow_35_frame,text="Your seeds scatter in every direction.",font=("Arial",16),bg="white")
        main.card_yellow_35_label_middle_down=tk.Label(main.card_yellow_35_frame,text="Move forward 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_yellow_35_continue=tk.Button(main.card_yellow_35_frame,text="Continue")
        main.card_yellow_35_title.pack(pady=20)
        main.card_yellow_35_label_middle.pack(pady=20)
        main.card_yellow_35_label_middle_down.pack(pady=20)
        main.card_yellow_35_continue.pack(side="bottom",pady=20)

        main.card_yellow_36_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_yellow_36_title=tk.Label(main.card_yellow_36_frame,text="💥 YELLOW CARD",font=("Arial",20,"bold"),bg="white",fg="goldenrod")
        main.card_yellow_36_label_middle=tk.Label(main.card_yellow_36_frame,text="The pod splits open with force.",font=("Arial",16),bg="white")
        main.card_yellow_36_label_middle_down=tk.Label(main.card_yellow_36_frame,text="Move forward 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_yellow_36_continue=tk.Button(main.card_yellow_36_frame,text="Continue")
        main.card_yellow_36_title.pack(pady=20)
        main.card_yellow_36_label_middle.pack(pady=20)
        main.card_yellow_36_label_middle_down.pack(pady=20)
        main.card_yellow_36_continue.pack(side="bottom",pady=20)

        main.card_yellow_37_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_yellow_37_title=tk.Label(main.card_yellow_37_frame,text="💥 YELLOW CARD",font=("Arial",20,"bold"),bg="white",fg="goldenrod")
        main.card_yellow_37_label_middle=tk.Label(main.card_yellow_37_frame,text="Warm weather triggers seed release.",font=("Arial",16),bg="white")
        main.card_yellow_37_label_middle_down=tk.Label(main.card_yellow_37_frame,text="Move forward 2 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_yellow_37_continue=tk.Button(main.card_yellow_37_frame,text="Continue")
        main.card_yellow_37_title.pack(pady=20)
        main.card_yellow_37_label_middle.pack(pady=20)
        main.card_yellow_37_label_middle_down.pack(pady=20)
        main.card_yellow_37_continue.pack(side="bottom",pady=20)

        main.card_yellow_38_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_yellow_38_title=tk.Label(main.card_yellow_38_frame,text="💥 YELLOW CARD",font=("Arial",20,"bold"),bg="white",fg="goldenrod")
        main.card_yellow_38_label_middle=tk.Label(main.card_yellow_38_frame,text="Your seeds land in open ground.",font=("Arial",16),bg="white")
        main.card_yellow_38_label_middle_down=tk.Label(main.card_yellow_38_frame,text="Move forward 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_yellow_38_continue=tk.Button(main.card_yellow_38_frame,text="Continue")
        main.card_yellow_38_title.pack(pady=20)
        main.card_yellow_38_label_middle.pack(pady=20)
        main.card_yellow_38_label_middle_down.pack(pady=20)
        main.card_yellow_38_continue.pack(side="bottom",pady=20)

        main.card_yellow_39_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_yellow_39_title=tk.Label(main.card_yellow_39_frame,text="💥 YELLOW CARD",font=("Arial",20,"bold"),bg="white",fg="goldenrod")
        main.card_yellow_39_label_middle=tk.Label(main.card_yellow_39_frame,text="The pod catapults your seed away.",font=("Arial",16),bg="white")
        main.card_yellow_39_label_middle_down=tk.Label(main.card_yellow_39_frame,text="Move forward 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_yellow_39_continue=tk.Button(main.card_yellow_39_frame,text="Continue")
        main.card_yellow_39_title.pack(pady=20)
        main.card_yellow_39_label_middle.pack(pady=20)
        main.card_yellow_39_label_middle_down.pack(pady=20)
        main.card_yellow_39_continue.pack(side="bottom",pady=20)

        main.card_yellow_40_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_yellow_40_title=tk.Label(main.card_yellow_40_frame,text="💥 YELLOW CARD",font=("Arial",20,"bold"),bg="white",fg="goldenrod")
        main.card_yellow_40_label_middle=tk.Label(main.card_yellow_40_frame,text="Perfect explosion! Seeds spread everywhere.",font=("Arial",16),bg="white")
        main.card_yellow_40_label_middle_down=tk.Label(main.card_yellow_40_frame,text="Move forward 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_yellow_40_continue=tk.Button(main.card_yellow_40_frame,text="Continue")
        main.card_yellow_40_title.pack(pady=20)
        main.card_yellow_40_label_middle.pack(pady=20)
        main.card_yellow_40_label_middle_down.pack(pady=20)
        main.card_yellow_40_continue.pack(side="bottom",pady=20)

        main.card_brown_41_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_brown_41_title=tk.Label(main.card_brown_41_frame,text="🟤 BROWN CARD",font=("Arial",20,"bold"),bg="white",fg="brown")
        main.card_brown_41_label_middle=tk.Label(main.card_brown_41_frame,text="A squirrel buries your seed.",font=("Arial",16),bg="white")
        main.card_brown_41_label_middle_down=tk.Label(main.card_brown_41_frame,text="Move forward 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_brown_41_continue=tk.Button(main.card_brown_41_frame,text="Continue")
        main.card_brown_41_title.pack(pady=20)
        main.card_brown_41_label_middle.pack(pady=20)
        main.card_brown_41_label_middle_down.pack(pady=20)
        main.card_brown_41_continue.pack(side="bottom",pady=20)

        main.card_brown_42_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_brown_42_title=tk.Label(main.card_brown_42_frame,text="🟤 BROWN CARD",font=("Arial",20,"bold"),bg="white",fg="brown")
        main.card_brown_42_label_middle=tk.Label(main.card_brown_42_frame,text="A bird drops your seed far away.",font=("Arial",16),bg="white")
        main.card_brown_42_label_middle_down=tk.Label(main.card_brown_42_frame,text="Move forward 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_brown_42_continue=tk.Button(main.card_brown_42_frame,text="Continue")
        main.card_brown_42_title.pack(pady=20)
        main.card_brown_42_label_middle.pack(pady=20)
        main.card_brown_42_label_middle_down.pack(pady=20)
        main.card_brown_42_continue.pack(side="bottom",pady=20)

        main.card_brown_43_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_brown_43_title=tk.Label(main.card_brown_43_frame,text="🟤 BROWN CARD",font=("Arial",20,"bold"),bg="white",fg="brown")
        main.card_brown_43_label_middle=tk.Label(main.card_brown_43_frame,text="Your seed sticks to an animal's fur.",font=("Arial",16),bg="white")
        main.card_brown_43_label_middle_down=tk.Label(main.card_brown_43_frame,text="Move forward 2 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_brown_43_continue=tk.Button(main.card_brown_43_frame,text="Continue")
        main.card_brown_43_title.pack(pady=20)
        main.card_brown_43_label_middle.pack(pady=20)
        main.card_brown_43_label_middle_down.pack(pady=20)
        main.card_brown_43_continue.pack(side="bottom",pady=20)

        main.card_brown_44_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_brown_44_title=tk.Label(main.card_brown_44_frame,text="🟤 BROWN CARD",font=("Arial",20,"bold"),bg="white",fg="brown")
        main.card_brown_44_label_middle=tk.Label(main.card_brown_44_frame,text="A monkey carries your fruit away.",font=("Arial",16),bg="white")
        main.card_brown_44_label_middle_down=tk.Label(main.card_brown_44_frame,text="Move forward 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_brown_44_continue=tk.Button(main.card_brown_44_frame,text="Continue")
        main.card_brown_44_title.pack(pady=20)
        main.card_brown_44_label_middle.pack(pady=20)
        main.card_brown_44_label_middle_down.pack(pady=20)
        main.card_brown_44_continue.pack(side="bottom",pady=20)

        main.card_brown_45_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_brown_45_title=tk.Label(main.card_brown_45_frame,text="🟤 BROWN CARD",font=("Arial",20,"bold"),bg="white",fg="brown")
        main.card_brown_45_label_middle=tk.Label(main.card_brown_45_frame,text="An elephant drops your seed in rich soil.",font=("Arial",16),bg="white")
        main.card_brown_45_label_middle_down=tk.Label(main.card_brown_45_frame,text="Move forward 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_brown_45_continue=tk.Button(main.card_brown_45_frame,text="Continue")
        main.card_brown_45_title.pack(pady=20)
        main.card_brown_45_label_middle.pack(pady=20)
        main.card_brown_45_label_middle_down.pack(pady=20)
        main.card_brown_45_continue.pack(side="bottom",pady=20)

        main.card_brown_46_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_brown_46_title=tk.Label(main.card_brown_46_frame,text="🟤 BROWN CARD",font=("Arial",20,"bold"),bg="white",fg="brown")
        main.card_brown_46_label_middle=tk.Label(main.card_brown_46_frame,text="A deer carries your seed on its fur.",font=("Arial",16),bg="white")
        main.card_brown_46_label_middle_down=tk.Label(main.card_brown_46_frame,text="Move forward 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_brown_46_continue=tk.Button(main.card_brown_46_frame,text="Continue")
        main.card_brown_46_title.pack(pady=20)
        main.card_brown_46_label_middle.pack(pady=20)
        main.card_brown_46_label_middle_down.pack(pady=20)
        main.card_brown_46_continue.pack(side="bottom",pady=20)

        main.card_brown_47_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_brown_47_title=tk.Label(main.card_brown_47_frame,text="🟤 BROWN CARD",font=("Arial",20,"bold"),bg="white",fg="brown")
        main.card_brown_47_label_middle=tk.Label(main.card_brown_47_frame,text="A rabbit brushes past with your seed.",font=("Arial",16),bg="white")
        main.card_brown_47_label_middle_down=tk.Label(main.card_brown_47_frame,text="Move forward 2 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_brown_47_continue=tk.Button(main.card_brown_47_frame,text="Continue")
        main.card_brown_47_title.pack(pady=20)
        main.card_brown_47_label_middle.pack(pady=20)
        main.card_brown_47_label_middle_down.pack(pady=20)
        main.card_brown_47_continue.pack(side="bottom",pady=20)

        main.card_brown_48_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_brown_48_title=tk.Label(main.card_brown_48_frame,text="🟤 BROWN CARD",font=("Arial",20,"bold"),bg="white",fg="brown")
        main.card_brown_48_label_middle=tk.Label(main.card_brown_48_frame,text="A fox carries your seed to a new place.",font=("Arial",16),bg="white")
        main.card_brown_48_label_middle_down=tk.Label(main.card_brown_48_frame,text="Move forward 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_brown_48_continue=tk.Button(main.card_brown_48_frame,text="Continue")
        main.card_brown_48_title.pack(pady=20)
        main.card_brown_48_label_middle.pack(pady=20)
        main.card_brown_48_label_middle_down.pack(pady=20)
        main.card_brown_48_continue.pack(side="bottom",pady=20)

        main.card_brown_49_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_brown_49_title=tk.Label(main.card_brown_49_frame,text="🟤 BROWN CARD",font=("Arial",20,"bold"),bg="white",fg="brown")
        main.card_brown_49_label_middle=tk.Label(main.card_brown_49_frame,text="A bird eats the fruit and drops the seed.",font=("Arial",16),bg="white")
        main.card_brown_49_label_middle_down=tk.Label(main.card_brown_49_frame,text="Move forward 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_brown_49_continue=tk.Button(main.card_brown_49_frame,text="Continue")
        main.card_brown_49_title.pack(pady=20)
        main.card_brown_49_label_middle.pack(pady=20)
        main.card_brown_49_label_middle_down.pack(pady=20)
        main.card_brown_49_continue.pack(side="bottom",pady=20)

        main.card_brown_50_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_brown_50_title=tk.Label(main.card_brown_50_frame,text="🟤 BROWN CARD",font=("Arial",20,"bold"),bg="white",fg="brown")
        main.card_brown_50_label_middle=tk.Label(main.card_brown_50_frame,text="Failed explosion.",font=("Arial",16),bg="white")
        main.card_brown_50_label_middle_down=tk.Label(main.card_brown_50_frame,text="Move back 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_brown_50_continue=tk.Button(main.card_brown_50_frame,text="Continue")
        main.card_brown_50_title.pack(pady=20)
        main.card_brown_50_label_middle.pack(pady=20)
        main.card_brown_50_label_middle_down.pack(pady=20)
        main.card_brown_50_continue.pack(side="bottom",pady=20)

        main.card_purple_51_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_purple_51_title=tk.Label(main.card_purple_51_frame,text="🟣 PURPLE CARD",font=("Arial",20,"bold"),bg="white",fg="purple")
        main.card_purple_51_label_middle=tk.Label(main.card_purple_51_frame,text="You grow into a healthy young plant.",font=("Arial",16),bg="white")
        main.card_purple_51_label_middle_down=tk.Label(main.card_purple_51_frame,text="Move forward 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_purple_51_continue=tk.Button(main.card_purple_51_frame,text="Continue")
        main.card_purple_51_title.pack(pady=20)
        main.card_purple_51_label_middle.pack(pady=20)
        main.card_purple_51_label_middle_down.pack(pady=20)
        main.card_purple_51_continue.pack(side="bottom",pady=20)

        main.card_purple_52_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_purple_52_title=tk.Label(main.card_purple_52_frame,text="🟣 PURPLE CARD",font=("Arial",20,"bold"),bg="white",fg="purple")
        main.card_purple_52_label_middle=tk.Label(main.card_purple_52_frame,text="Sunlight helps you make food.",font=("Arial",16),bg="white")
        main.card_purple_52_label_middle_down=tk.Label(main.card_purple_52_frame,text="Move forward 2 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_purple_52_continue=tk.Button(main.card_purple_52_frame,text="Continue")
        main.card_purple_52_title.pack(pady=20)
        main.card_purple_52_label_middle.pack(pady=20)
        main.card_purple_52_label_middle_down.pack(pady=20)
        main.card_purple_52_continue.pack(side="bottom",pady=20)

        main.card_purple_53_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_purple_53_title=tk.Label(main.card_purple_53_frame,text="🟣 PURPLE CARD",font=("Arial",20,"bold"),bg="white",fg="purple")
        main.card_purple_53_label_middle=tk.Label(main.card_purple_53_frame,text="Your roots grow deep into the soil.",font=("Arial",16),bg="white")
        main.card_purple_53_label_middle_down=tk.Label(main.card_purple_53_frame,text="Move forward 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_purple_53_continue=tk.Button(main.card_purple_53_frame,text="Continue")
        main.card_purple_53_title.pack(pady=20)
        main.card_purple_53_label_middle.pack(pady=20)
        main.card_purple_53_label_middle_down.pack(pady=20)
        main.card_purple_53_continue.pack(side="bottom",pady=20)

        main.card_purple_54_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_purple_54_title=tk.Label(main.card_purple_54_frame,text="🟣 PURPLE CARD",font=("Arial",20,"bold"),bg="white",fg="purple")
        main.card_purple_54_label_middle=tk.Label(main.card_purple_54_frame,text="Fresh rain keeps you healthy.",font=("Arial",16),bg="white")
        main.card_purple_54_label_middle_down=tk.Label(main.card_purple_54_frame,text="Move forward 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_purple_54_continue=tk.Button(main.card_purple_54_frame,text="Continue")
        main.card_purple_54_title.pack(pady=20)
        main.card_purple_54_label_middle.pack(pady=20)
        main.card_purple_54_label_middle_down.pack(pady=20)
        main.card_purple_54_continue.pack(side="bottom",pady=20)

        main.card_purple_55_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_purple_55_title=tk.Label(main.card_purple_55_frame,text="🟣 PURPLE CARD",font=("Arial",20,"bold"),bg="white",fg="purple")
        main.card_purple_55_label_middle=tk.Label(main.card_purple_55_frame,text="You bloom into a beautiful flowering plant.",font=("Arial",16),bg="white")
        main.card_purple_55_label_middle_down=tk.Label(main.card_purple_55_frame,text="Move forward 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_purple_55_continue=tk.Button(main.card_purple_55_frame,text="Continue")
        main.card_purple_55_title.pack(pady=20)
        main.card_purple_55_label_middle.pack(pady=20)
        main.card_purple_55_label_middle_down.pack(pady=20)
        main.card_purple_55_continue.pack(side="bottom",pady=20)

        main.card_purple_56_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_purple_56_title=tk.Label(main.card_purple_56_frame,text="🟣 PURPLE CARD",font=("Arial",20,"bold"),bg="white",fg="purple")
        main.card_purple_56_label_middle=tk.Label(main.card_purple_56_frame,text="A gardener waters you every day.",font=("Arial",16),bg="white")
        main.card_purple_56_label_middle_down=tk.Label(main.card_purple_56_frame,text="Move forward 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_purple_56_continue=tk.Button(main.card_purple_56_frame,text="Continue")
        main.card_purple_56_title.pack(pady=20)
        main.card_purple_56_label_middle.pack(pady=20)
        main.card_purple_56_label_middle_down.pack(pady=20)
        main.card_purple_56_continue.pack(side="bottom",pady=20)

        main.card_purple_57_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_purple_57_title=tk.Label(main.card_purple_57_frame,text="🟣 PURPLE CARD",font=("Arial",20,"bold"),bg="white",fg="purple")
        main.card_purple_57_label_middle=tk.Label(main.card_purple_57_frame,text="Your leaves capture lots of sunlight.",font=("Arial",16),bg="white")
        main.card_purple_57_label_middle_down=tk.Label(main.card_purple_57_frame,text="Move forward 2 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_purple_57_continue=tk.Button(main.card_purple_57_frame,text="Continue")
        main.card_purple_57_title.pack(pady=20)
        main.card_purple_57_label_middle.pack(pady=20)
        main.card_purple_57_label_middle_down.pack(pady=20)
        main.card_purple_57_continue.pack(side="bottom",pady=20)

        main.card_purple_58_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_purple_58_title=tk.Label(main.card_purple_58_frame,text="🟣 PURPLE CARD",font=("Arial",20,"bold"),bg="white",fg="purple")
        main.card_purple_58_label_middle=tk.Label(main.card_purple_58_frame,text="Your flowers attract helpful bees.",font=("Arial",16),bg="white")
        main.card_purple_58_label_middle_down=tk.Label(main.card_purple_58_frame,text="Move forward 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_purple_58_continue=tk.Button(main.card_purple_58_frame,text="Continue")
        main.card_purple_58_title.pack(pady=20)
        main.card_purple_58_label_middle.pack(pady=20)
        main.card_purple_58_label_middle_down.pack(pady=20)
        main.card_purple_58_continue.pack(side="bottom",pady=20)

        main.card_purple_59_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_purple_59_title=tk.Label(main.card_purple_59_frame,text="🟣 PURPLE CARD",font=("Arial",20,"bold"),bg="white",fg="purple")
        main.card_purple_59_label_middle=tk.Label(main.card_purple_59_frame,text="Your plant grows strong and tall.",font=("Arial",16),bg="white")
        main.card_purple_59_label_middle_down=tk.Label(main.card_purple_59_frame,text="Move forward 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_purple_59_continue=tk.Button(main.card_purple_59_frame,text="Continue")
        main.card_purple_59_title.pack(pady=20)
        main.card_purple_59_label_middle.pack(pady=20)
        main.card_purple_59_label_middle_down.pack(pady=20)
        main.card_purple_59_continue.pack(side="bottom",pady=20)

        main.card_purple_60_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_purple_60_title=tk.Label(main.card_purple_60_frame,text="🟣 PURPLE CARD",font=("Arial",20,"bold"),bg="white",fg="purple")
        main.card_purple_60_label_middle=tk.Label(main.card_purple_60_frame,text="Congratulations! Your plant produces new seeds.",font=("Arial",16),bg="white")
        main.card_purple_60_label_middle_down=tk.Label(main.card_purple_60_frame,text="Move forward 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_purple_60_continue=tk.Button(main.card_purple_60_frame,text="Continue")
        main.card_purple_60_title.pack(pady=20)
        main.card_purple_60_label_middle.pack(pady=20)
        main.card_purple_60_label_middle_down.pack(pady=20)
        main.card_purple_60_continue.pack(side="bottom",pady=20)

        main.card_orange_61_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_orange_61_title=tk.Label(main.card_orange_61_frame,text="🟠 ORANGE CARD",font=("Arial",20,"bold"),bg="white",fg="orange")
        main.card_orange_61_label_middle=tk.Label(main.card_orange_61_frame,text="A warm breeze helps your plant thrive.",font=("Arial",16),bg="white")
        main.card_orange_61_label_middle_down=tk.Label(main.card_orange_61_frame,text="Move forward 2 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_orange_61_continue=tk.Button(main.card_orange_61_frame,text="Continue")
        main.card_orange_61_title.pack(pady=20)
        main.card_orange_61_label_middle.pack(pady=20)
        main.card_orange_61_label_middle_down.pack(pady=20)
        main.card_orange_61_continue.pack(side="bottom",pady=20)

        main.card_orange_62_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_orange_62_title=tk.Label(main.card_orange_62_frame,text="🟠 ORANGE CARD",font=("Arial",20,"bold"),bg="white",fg="orange")
        main.card_orange_62_label_middle=tk.Label(main.card_orange_62_frame,text="Rich soil gives you extra nutrients.",font=("Arial",16),bg="white")
        main.card_orange_62_label_middle_down=tk.Label(main.card_orange_62_frame,text="Move forward 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_orange_62_continue=tk.Button(main.card_orange_62_frame,text="Continue")
        main.card_orange_62_title.pack(pady=20)
        main.card_orange_62_label_middle.pack(pady=20)
        main.card_orange_62_label_middle_down.pack(pady=20)
        main.card_orange_62_continue.pack(side="bottom",pady=20)

        main.card_orange_63_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_orange_63_title=tk.Label(main.card_orange_63_frame,text="🟠 ORANGE CARD",font=("Arial",20,"bold"),bg="white",fg="orange")
        main.card_orange_63_label_middle=tk.Label(main.card_orange_63_frame,text="Your tree becomes full of healthy fruits.",font=("Arial",16),bg="white")
        main.card_orange_63_label_middle_down=tk.Label(main.card_orange_63_frame,text="Move forward 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_orange_63_continue=tk.Button(main.card_orange_63_frame,text="Continue")
        main.card_orange_63_title.pack(pady=20)
        main.card_orange_63_label_middle.pack(pady=20)
        main.card_orange_63_label_middle_down.pack(pady=20)
        main.card_orange_63_continue.pack(side="bottom",pady=20)

        main.card_orange_64_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_orange_64_title=tk.Label(main.card_orange_64_frame,text="🟠 ORANGE CARD",font=("Arial",20,"bold"),bg="white",fg="orange")
        main.card_orange_64_label_middle=tk.Label(main.card_orange_64_frame,text="Many animals spread your seeds.",font=("Arial",16),bg="white")
        main.card_orange_64_label_middle_down=tk.Label(main.card_orange_64_frame,text="Move forward 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_orange_64_continue=tk.Button(main.card_orange_64_frame,text="Continue")
        main.card_orange_64_title.pack(pady=20)
        main.card_orange_64_label_middle.pack(pady=20)
        main.card_orange_64_label_middle_down.pack(pady=20)
        main.card_orange_64_continue.pack(side="bottom",pady=20)

        main.card_orange_65_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_orange_65_title=tk.Label(main.card_orange_65_frame,text="🟠 ORANGE CARD",font=("Arial",20,"bold"),bg="white",fg="orange")
        main.card_orange_65_label_middle=tk.Label(main.card_orange_65_frame,text="Your seeds begin a new generation.",font=("Arial",16),bg="white")
        main.card_orange_65_label_middle_down=tk.Label(main.card_orange_65_frame,text="Move forward 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_orange_65_continue=tk.Button(main.card_orange_65_frame,text="Continue")
        main.card_orange_65_title.pack(pady=20)
        main.card_orange_65_label_middle.pack(pady=20)
        main.card_orange_65_label_middle_down.pack(pady=20)
        main.card_orange_65_continue.pack(side="bottom",pady=20)

        main.card_orange_66_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_orange_66_title=tk.Label(main.card_orange_66_frame,text="🟠 ORANGE CARD",font=("Arial",20,"bold"),bg="white",fg="orange")
        main.card_orange_66_label_middle=tk.Label(main.card_orange_66_frame,text="Your forest is growing bigger!",font=("Arial",16),bg="white")
        main.card_orange_66_label_middle_down=tk.Label(main.card_orange_66_frame,text="Move forward 2 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_orange_66_continue=tk.Button(main.card_orange_66_frame,text="Continue")
        main.card_orange_66_title.pack(pady=20)
        main.card_orange_66_label_middle.pack(pady=20)
        main.card_orange_66_label_middle_down.pack(pady=20)
        main.card_orange_66_continue.pack(side="bottom",pady=20)

        main.card_orange_67_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_orange_67_title=tk.Label(main.card_orange_67_frame,text="🟠 ORANGE CARD",font=("Arial",20,"bold"),bg="white",fg="orange")
        main.card_orange_67_label_middle=tk.Label(main.card_orange_67_frame,text="You have completed the life cycle!",font=("Arial",16),bg="white")
        main.card_orange_67_label_middle_down=tk.Label(main.card_orange_67_frame,text="Move forward 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_orange_67_continue=tk.Button(main.card_orange_67_frame,text="Continue")
        main.card_orange_67_title.pack(pady=20)
        main.card_orange_67_label_middle.pack(pady=20)
        main.card_orange_67_label_middle_down.pack(pady=20)
        main.card_orange_67_continue.pack(side="bottom",pady=20)

        main.card_orange_68_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_orange_68_title=tk.Label(main.card_orange_68_frame,text="🟠 ORANGE CARD",font=("Arial",20,"bold"),bg="white",fg="orange")
        main.card_orange_68_label_middle=tk.Label(main.card_orange_68_frame,text="A perfect season helps every seed grow.",font=("Arial",16),bg="white")
        main.card_orange_68_label_middle_down=tk.Label(main.card_orange_68_frame,text="Move forward 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_orange_68_continue=tk.Button(main.card_orange_68_frame,text="Continue")
        main.card_orange_68_title.pack(pady=20)
        main.card_orange_68_label_middle.pack(pady=20)
        main.card_orange_68_label_middle_down.pack(pady=20)
        main.card_orange_68_continue.pack(side="bottom",pady=20)

        main.card_orange_69_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_orange_69_title=tk.Label(main.card_orange_69_frame,text="🟠 ORANGE CARD",font=("Arial",20,"bold"),bg="white",fg="orange")
        main.card_orange_69_label_middle=tk.Label(main.card_orange_69_frame,text="Nature celebrates your success!",font=("Arial",16),bg="white")
        main.card_orange_69_label_middle_down=tk.Label(main.card_orange_69_frame,text="Move forward 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_orange_69_continue=tk.Button(main.card_orange_69_frame,text="Continue")
        main.card_orange_69_title.pack(pady=20)
        main.card_orange_69_label_middle.pack(pady=20)
        main.card_orange_69_label_middle_down.pack(pady=20)
        main.card_orange_69_continue.pack(side="bottom",pady=20)

        main.card_orange_70_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_orange_70_title=tk.Label(main.card_orange_70_frame,text="🟠 ORANGE CARD",font=("Arial",20,"bold"),bg="white",fg="orange")
        main.card_orange_70_label_middle=tk.Label(main.card_orange_70_frame,text="You got watered(Bonus Card)",font=("Arial",16),bg="white")
        main.card_orange_70_label_middle_down=tk.Label(main.card_orange_70_frame,text="You move 2 spaces",font=("Arial",14,"bold"),bg="white",fg="blue")
        main.card_orange_70_continue=tk.Button(main.card_orange_70_frame,text="Finish")
        main.card_orange_70_title.pack(pady=20)
        main.card_orange_70_label_middle.pack(pady=20)
        main.card_orange_70_label_middle_down.pack(pady=20)
        main.card_orange_70_continue.pack(side="bottom", pady=20)

        main.card_blue_71_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_blue_71_title=tk.Label(main.card_blue_71_frame,text="🌧 BLUE CARD",font=("Arial",20,"bold"),bg="white",fg="blue")
        main.card_blue_71_label_middle=tk.Label(main.card_blue_71_frame,text="A strong wind blows your seed away from a safe place.",font=("Arial",16),bg="white")
        main.card_blue_71_label_middle_down=tk.Label(main.card_blue_71_frame,text="Move back 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="red")
        main.card_blue_71_continue=tk.Button(main.card_blue_71_frame,text="Continue")
        main.card_blue_71_title.pack(pady=20)
        main.card_blue_71_label_middle.pack(pady=20)
        main.card_blue_71_label_middle_down.pack(pady=20)

        main.card_blue_72_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_blue_72_title=tk.Label(main.card_blue_72_frame,text="🌧 BLUE CARD",font=("Arial",20,"bold"),bg="white",fg="blue")
        main.card_blue_72_label_middle=tk.Label(main.card_blue_72_frame,text="A sudden storm pushes the seed backward across the ground.",font=("Arial",16),bg="white")
        main.card_blue_72_label_middle_down=tk.Label(main.card_blue_72_frame,text="Move back 4 spaces.",font=("Arial",14,"bold"),bg="white",fg="red")
        main.card_blue_72_continue=tk.Button(main.card_blue_72_frame,text="Continue")
        main.card_blue_72_title.pack(pady=20)
        main.card_blue_72_label_middle.pack(pady=20)
        main.card_blue_72_label_middle_down.pack(pady=20)

        main.card_blue_73_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_blue_73_title=tk.Label(main.card_blue_73_frame,text="🌧 BLUE CARD",font=("Arial",20,"bold"),bg="white",fg="blue")
        main.card_blue_73_label_middle=tk.Label(main.card_blue_73_frame,text="The wind changes direction and carries your seed away from its destination.",font=("Arial",16),bg="white")
        main.card_blue_73_label_middle_down=tk.Label(main.card_blue_73_frame,text="Move back 2 spaces.",font=("Arial",14,"bold"),bg="white",fg="red")
        main.card_blue_73_continue=tk.Button(main.card_blue_73_frame,text="Continue")
        main.card_blue_73_title.pack(pady=20)
        main.card_blue_73_label_middle.pack(pady=20)
        main.card_blue_73_label_middle_down.pack(pady=20)

        main.card_blue_74_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_blue_74_title=tk.Label(main.card_blue_74_frame,text="🌧 BLUE CARD",font=("Arial",20,"bold"),bg="white",fg="blue")
        main.card_blue_74_label_middle=tk.Label(main.card_blue_74_frame,text="Heavy rain washes the seed away from the place where it landed.",font=("Arial",16),bg="white")
        main.card_blue_74_label_middle_down=tk.Label(main.card_blue_74_frame,text="Move back 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="red")
        main.card_blue_74_continue=tk.Button(main.card_blue_74_frame,text="Continue")
        main.card_blue_74_title.pack(pady=20)
        main.card_blue_74_label_middle.pack(pady=20)
        main.card_blue_74_label_middle_down.pack(pady=20)

        main.card_blue_75_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_blue_75_title=tk.Label(main.card_blue_75_frame,text="🌧 BLUE CARD",font=("Arial",20,"bold"),bg="white",fg="blue")
        main.card_blue_75_label_middle=tk.Label(main.card_blue_75_frame,text="Strong winds blow the seed away from a good growing spot.",font=("Arial",16),bg="white")
        main.card_blue_75_label_middle_down=tk.Label(main.card_blue_75_frame,text="Move back 4 spaces.",font=("Arial",14,"bold"),bg="white",fg="red")
        main.card_blue_75_continue=tk.Button(main.card_blue_75_frame,text="Continue")
        main.card_blue_75_title.pack(pady=20)
        main.card_blue_75_label_middle.pack(pady=20)
        main.card_blue_75_label_middle_down.pack(pady=20)

        main.card_red_76_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_red_76_title=tk.Label(main.card_red_76_frame,text="🐦 RED CARD",font=("Arial",20,"bold"),bg="white",fg="red")
        main.card_red_76_label_middle=tk.Label(main.card_red_76_frame,text="An animal eats the fruit before the seed can reach the soil.",font=("Arial",16),bg="white")
        main.card_red_76_label_middle_down=tk.Label(main.card_red_76_frame,text="Move back 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="red")
        main.card_red_76_continue=tk.Button(main.card_red_76_frame,text="Continue")
        main.card_red_76_title.pack(pady=20)
        main.card_red_76_label_middle.pack(pady=20)
        main.card_red_76_label_middle_down.pack(pady=20)

        main.card_red_77_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_red_77_title=tk.Label(main.card_red_77_frame,text="🐦 RED CARD",font=("Arial",20,"bold"),bg="white",fg="red")
        main.card_red_77_label_middle=tk.Label(main.card_red_77_frame,text="An animal carrying the seed drops it far from a suitable place.",font=("Arial",16),bg="white")
        main.card_red_77_label_middle_down=tk.Label(main.card_red_77_frame,text="Move back 2 spaces.",font=("Arial",14,"bold"),bg="white",fg="red")
        main.card_red_77_continue=tk.Button(main.card_red_77_frame,text="Continue")
        main.card_red_77_title.pack(pady=20)
        main.card_red_77_label_middle.pack(pady=20)
        main.card_red_77_label_middle_down.pack(pady=20)

        main.card_red_78_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_red_78_title=tk.Label(main.card_red_78_frame,text="🐦 RED CARD",font=("Arial",20,"bold"),bg="white",fg="red")
        main.card_red_78_label_middle=tk.Label(main.card_red_78_frame,text="The animal carrying your seed runs in the wrong direction.",font=("Arial",16),bg="white")
        main.card_red_78_label_middle_down=tk.Label(main.card_red_78_frame,text="Move back 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="red")
        main.card_red_78_continue=tk.Button(main.card_red_78_frame,text="Continue")
        main.card_red_78_title.pack(pady=20)
        main.card_red_78_label_middle.pack(pady=20)
        main.card_red_78_label_middle_down.pack(pady=20)

        main.card_red_79_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_red_79_title=tk.Label(main.card_red_79_frame,text="🐦 RED CARD",font=("Arial",20,"bold"),bg="white",fg="red")
        main.card_red_79_label_middle=tk.Label(main.card_red_79_frame,text="The fruit containing your seed is picked before the seed can escape.",font=("Arial",16),bg="white")
        main.card_red_79_label_middle_down=tk.Label(main.card_red_79_frame,text="Move back 4 spaces.",font=("Arial",14,"bold"),bg="white",fg="red")
        main.card_red_79_continue=tk.Button(main.card_red_79_frame,text="Continue")
        main.card_red_79_title.pack(pady=20)
        main.card_red_79_label_middle.pack(pady=20)
        main.card_red_79_label_middle_down.pack(pady=20)

        main.card_red_80_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_red_80_title=tk.Label(main.card_red_80_frame,text="🐦 RED CARD",font=("Arial",20,"bold"),bg="white",fg="red")
        main.card_red_80_label_middle=tk.Label(main.card_red_80_frame,text="An animal buries the seed too deeply for it to grow properly.",font=("Arial",16),bg="white")
        main.card_red_80_label_middle_down=tk.Label(main.card_red_80_frame,text="Move back 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="red")
        main.card_red_80_continue=tk.Button(main.card_red_80_frame,text="Continue")
        main.card_red_80_title.pack(pady=20)
        main.card_red_80_label_middle.pack(pady=20)
        main.card_red_80_label_middle_down.pack(pady=20)

        main.card_green_81_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_green_81_title=tk.Label(main.card_green_81_frame,text="🌱 GREEN CARD",font=("Arial",20,"bold"),bg="white",fg="green")
        main.card_green_81_label_middle=tk.Label(main.card_green_81_frame,text="Your seed lands in soil that does not have enough moisture.",font=("Arial",16),bg="white")
        main.card_green_81_label_middle_down=tk.Label(main.card_green_81_frame,text="Move back 2 spaces.",font=("Arial",14,"bold"),bg="white",fg="red")
        main.card_green_81_continue=tk.Button(main.card_green_81_frame,text="Continue")
        main.card_green_81_title.pack(pady=20)
        main.card_green_81_label_middle.pack(pady=20)
        main.card_green_81_label_middle_down.pack(pady=20)

        main.card_green_82_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_green_82_title=tk.Label(main.card_green_82_frame,text="🌱 GREEN CARD",font=("Arial",20,"bold"),bg="white",fg="green")
        main.card_green_82_label_middle=tk.Label(main.card_green_82_frame,text="The soil has too few nutrients for your seed to grow well.",font=("Arial",16),bg="white")
        main.card_green_82_label_middle_down=tk.Label(main.card_green_82_frame,text="Move back 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="red")
        main.card_green_82_continue=tk.Button(main.card_green_82_frame,text="Continue")
        main.card_green_82_title.pack(pady=20)
        main.card_green_82_label_middle.pack(pady=20)
        main.card_green_82_label_middle_down.pack(pady=20)

        main.card_green_83_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_green_83_title=tk.Label(main.card_green_83_frame,text="🌱 GREEN CARD",font=("Arial",20,"bold"),bg="white",fg="green")
        main.card_green_83_label_middle=tk.Label(main.card_green_83_frame,text="The seed lands where nearby plants block the sunlight.",font=("Arial",16),bg="white")
        main.card_green_83_label_middle_down=tk.Label(main.card_green_83_frame,text="Move back 2 spaces.",font=("Arial",14,"bold"),bg="white",fg="red")
        main.card_green_83_continue=tk.Button(main.card_green_83_frame,text="Continue")
        main.card_green_83_title.pack(pady=20)
        main.card_green_83_label_middle.pack(pady=20)
        main.card_green_83_label_middle_down.pack(pady=20)

        main.card_green_84_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_green_84_title=tk.Label(main.card_green_84_frame,text="🌱 GREEN CARD",font=("Arial",20,"bold"),bg="white",fg="green")
        main.card_green_84_label_middle=tk.Label(main.card_green_84_frame,text="Too many plants are growing around your seed.",font=("Arial",16),bg="white")
        main.card_green_84_label_middle_down=tk.Label(main.card_green_84_frame,text="Move back 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="red")
        main.card_green_84_continue=tk.Button(main.card_green_84_frame,text="Continue")
        main.card_green_84_title.pack(pady=20)
        main.card_green_84_label_middle.pack(pady=20)
        main.card_green_84_label_middle_down.pack(pady=20)

        main.card_green_85_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_green_85_title=tk.Label(main.card_green_85_frame,text="🌱 GREEN CARD",font=("Arial",20,"bold"),bg="white",fg="green")
        main.card_green_85_label_middle=tk.Label(main.card_green_85_frame,text="The ground is too hard for the seed to settle properly.",font=("Arial",16),bg="white")
        main.card_green_85_label_middle_down=tk.Label(main.card_green_85_frame,text="Move back 4 spaces.",font=("Arial",14,"bold"),bg="white",fg="red")
        main.card_green_85_continue=tk.Button(main.card_green_85_frame,text="Continue")
        main.card_green_85_title.pack(pady=20)
        main.card_green_85_label_middle.pack(pady=20)
        main.card_green_85_label_middle_down.pack(pady=20)
        main.card_yellow_86_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_yellow_86_title=tk.Label(main.card_yellow_86_frame,text="🟡 YELLOW CARD",font=("Arial",20,"bold"),bg="white",fg="gold")
        main.card_yellow_86_label_middle=tk.Label(main.card_yellow_86_frame,text="The seed pod does not open, so the seeds cannot spread.",font=("Arial",16),bg="white")
        main.card_yellow_86_label_middle_down=tk.Label(main.card_yellow_86_frame,text="Move back 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="red")
        main.card_yellow_86_continue=tk.Button(main.card_yellow_86_frame,text="Continue")
        main.card_yellow_86_title.pack(pady=20)
        main.card_yellow_86_label_middle.pack(pady=20)
        main.card_yellow_86_label_middle_down.pack(pady=20)

        main.card_yellow_87_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_yellow_87_title=tk.Label(main.card_yellow_87_frame,text="🟡 YELLOW CARD",font=("Arial",20,"bold"),bg="white",fg="gold")
        main.card_yellow_87_label_middle=tk.Label(main.card_yellow_87_frame,text="The seed pod opens weakly and the seed does not travel far.",font=("Arial",16),bg="white")
        main.card_yellow_87_label_middle_down=tk.Label(main.card_yellow_87_frame,text="Move back 2 spaces.",font=("Arial",14,"bold"),bg="white",fg="red")
        main.card_yellow_87_continue=tk.Button(main.card_yellow_87_frame,text="Continue")
        main.card_yellow_87_title.pack(pady=20)
        main.card_yellow_87_label_middle.pack(pady=20)
        main.card_yellow_87_label_middle_down.pack(pady=20)

        main.card_yellow_88_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_yellow_88_title=tk.Label(main.card_yellow_88_frame,text="🟡 YELLOW CARD",font=("Arial",20,"bold"),bg="white",fg="gold")
        main.card_yellow_88_label_middle=tk.Label(main.card_yellow_88_frame,text="The pod falls before the seeds can be released properly.",font=("Arial",16),bg="white")
        main.card_yellow_88_label_middle_down=tk.Label(main.card_yellow_88_frame,text="Move back 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="red")
        main.card_yellow_88_continue=tk.Button(main.card_yellow_88_frame,text="Continue")
        main.card_yellow_88_title.pack(pady=20)
        main.card_yellow_88_label_middle.pack(pady=20)
        main.card_yellow_88_label_middle_down.pack(pady=20)

        main.card_yellow_89_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_yellow_89_title=tk.Label(main.card_yellow_89_frame,text="🟡 YELLOW CARD",font=("Arial",20,"bold"),bg="white",fg="gold")
        main.card_yellow_89_label_middle=tk.Label(main.card_yellow_89_frame,text="Some seeds remain trapped inside the pod.",font=("Arial",16),bg="white")
        main.card_yellow_89_label_middle_down=tk.Label(main.card_yellow_89_frame,text="Move back 4 spaces.",font=("Arial",14,"bold"),bg="white",fg="red")
        main.card_yellow_89_continue=tk.Button(main.card_yellow_89_frame,text="Continue")
        main.card_yellow_89_title.pack(pady=20)
        main.card_yellow_89_label_middle.pack(pady=20)
        main.card_yellow_89_label_middle_down.pack(pady=20)

        main.card_yellow_90_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_yellow_90_title=tk.Label(main.card_yellow_90_frame,text="🟡 YELLOW CARD",font=("Arial",20,"bold"),bg="white",fg="gold")
        main.card_yellow_90_label_middle=tk.Label(main.card_yellow_90_frame,text="The seed is launched toward an unsuitable area.",font=("Arial",16),bg="white")
        main.card_yellow_90_label_middle_down=tk.Label(main.card_yellow_90_frame,text="Move back 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="red")
        main.card_yellow_90_continue=tk.Button(main.card_yellow_90_frame,text="Continue")
        main.card_yellow_90_title.pack(pady=20)
        main.card_yellow_90_label_middle.pack(pady=20)
        main.card_yellow_90_label_middle_down.pack(pady=20)

        main.card_brown_91_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_brown_91_title=tk.Label(main.card_brown_91_frame,text="🟤 BROWN CARD",font=("Arial",20,"bold"),bg="white",fg="brown")
        main.card_brown_91_label_middle=tk.Label(main.card_brown_91_frame,text="The seed lands on dry ground with very little moisture.",font=("Arial",16),bg="white")
        main.card_brown_91_label_middle_down=tk.Label(main.card_brown_91_frame,text="Move back 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="red")
        main.card_brown_91_continue=tk.Button(main.card_brown_91_frame,text="Continue")
        main.card_brown_91_title.pack(pady=20)
        main.card_brown_91_label_middle.pack(pady=20)
        main.card_brown_91_label_middle_down.pack(pady=20)

        main.card_brown_92_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_brown_92_title=tk.Label(main.card_brown_92_frame,text="🟤 BROWN CARD",font=("Arial",20,"bold"),bg="white",fg="brown")
        main.card_brown_92_label_middle=tk.Label(main.card_brown_92_frame,text="Rocks prevent the seed from settling into the soil.",font=("Arial",16),bg="white")
        main.card_brown_92_label_middle_down=tk.Label(main.card_brown_92_frame,text="Move back 2 spaces.",font=("Arial",14,"bold"),bg="white",fg="red")
        main.card_brown_92_continue=tk.Button(main.card_brown_92_frame,text="Continue")
        main.card_brown_92_title.pack(pady=20)
        main.card_brown_92_label_middle.pack(pady=20)
        main.card_brown_92_label_middle_down.pack(pady=20)

        main.card_brown_93_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_brown_93_title=tk.Label(main.card_brown_93_frame,text="🟤 BROWN CARD",font=("Arial",20,"bold"),bg="white",fg="brown")
        main.card_brown_93_label_middle=tk.Label(main.card_brown_93_frame,text="Soil is washed away and carries the seed backward.",font=("Arial",16),bg="white")
        main.card_brown_93_label_middle_down=tk.Label(main.card_brown_93_frame,text="Move back 4 spaces.",font=("Arial",14,"bold"),bg="white",fg="red")
        main.card_brown_93_continue=tk.Button(main.card_brown_93_frame,text="Continue")
        main.card_brown_93_title.pack(pady=20)
        main.card_brown_93_label_middle.pack(pady=20)
        main.card_brown_93_label_middle_down.pack(pady=20)

        main.card_brown_94_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_brown_94_title=tk.Label(main.card_brown_94_frame,text="🟤 BROWN CARD",font=("Arial",20,"bold"),bg="white",fg="brown")
        main.card_brown_94_label_middle=tk.Label(main.card_brown_94_frame,text="Loose soil shifts underneath the seed and moves it away.",font=("Arial",16),bg="white")
        main.card_brown_94_label_middle_down=tk.Label(main.card_brown_94_frame,text="Move back 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="red")
        main.card_brown_94_continue=tk.Button(main.card_brown_94_frame,text="Continue")
        main.card_brown_94_title.pack(pady=20)
        main.card_brown_94_label_middle.pack(pady=20)
        main.card_brown_94_label_middle_down.pack(pady=20)

        main.card_brown_95_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_brown_95_title=tk.Label(main.card_brown_95_frame,text="🟤 BROWN CARD",font=("Arial",20,"bold"),bg="white",fg="brown")
        main.card_brown_95_label_middle=tk.Label(main.card_brown_95_frame,text="The seed becomes buried too deeply in the soil.",font=("Arial",16),bg="white")
        main.card_brown_95_label_middle_down=tk.Label(main.card_brown_95_frame,text="Move back 4 spaces.",font=("Arial",14,"bold"),bg="white",fg="red")
        main.card_brown_95_continue=tk.Button(main.card_brown_95_frame,text="Continue")
        main.card_brown_95_title.pack(pady=20)
        main.card_brown_95_label_middle.pack(pady=20)
        main.card_brown_95_label_middle_down.pack(pady=20)

        main.card_purple_96_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_purple_96_title=tk.Label(main.card_purple_96_frame,text="🟣 PURPLE CARD",font=("Arial",20,"bold"),bg="white",fg="purple")
        main.card_purple_96_label_middle=tk.Label(main.card_purple_96_frame,text="The seed reaches an area that is not suitable for its growth.",font=("Arial",16),bg="white")
        main.card_purple_96_label_middle_down=tk.Label(main.card_purple_96_frame,text="Move back 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="red")
        main.card_purple_96_continue=tk.Button(main.card_purple_96_frame,text="Continue")
        main.card_purple_96_title.pack(pady=20)
        main.card_purple_96_label_middle.pack(pady=20)
        main.card_purple_96_label_middle_down.pack(pady=20)

        main.card_purple_97_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_purple_97_title=tk.Label(main.card_purple_97_frame,text="🟣 PURPLE CARD",font=("Arial",20,"bold"),bg="white",fg="purple")
        main.card_purple_97_label_middle=tk.Label(main.card_purple_97_frame,text="Cold conditions slow the seed's progress toward germination.",font=("Arial",16),bg="white")
        main.card_purple_97_label_middle_down=tk.Label(main.card_purple_97_frame,text="Move back 2 spaces.",font=("Arial",14,"bold"),bg="white",fg="red")
        main.card_purple_97_continue=tk.Button(main.card_purple_97_frame,text="Continue")
        main.card_purple_97_title.pack(pady=20)
        main.card_purple_97_label_middle.pack(pady=20)
        main.card_purple_97_label_middle_down.pack(pady=20)

        main.card_purple_98_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_purple_98_title=tk.Label(main.card_purple_98_frame,text="🟣 PURPLE CARD",font=("Arial",20,"bold"),bg="white",fg="purple")
        main.card_purple_98_label_middle=tk.Label(main.card_purple_98_frame,text="Excessive heat makes the place unsuitable for the seed.",font=("Arial",16),bg="white")
        main.card_purple_98_label_middle_down=tk.Label(main.card_purple_98_frame,text="Move back 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="red")
        main.card_purple_98_continue=tk.Button(main.card_purple_98_frame,text="Continue")
        main.card_purple_98_title.pack(pady=20)
        main.card_purple_98_label_middle.pack(pady=20)
        main.card_purple_98_label_middle_down.pack(pady=20)

        main.card_purple_99_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_purple_99_title=tk.Label(main.card_purple_99_frame,text="🟣 PURPLE CARD",font=("Arial",20,"bold"),bg="white",fg="purple")
        main.card_purple_99_label_middle=tk.Label(main.card_purple_99_frame,text="The seed cannot find enough water where it landed.",font=("Arial",16),bg="white")
        main.card_purple_99_label_middle_down=tk.Label(main.card_purple_99_frame,text="Move back 4 spaces.",font=("Arial",14,"bold"),bg="white",fg="red")
        main.card_purple_99_continue=tk.Button(main.card_purple_99_frame,text="Continue")
        main.card_purple_99_title.pack(pady=20)
        main.card_purple_99_label_middle.pack(pady=20)
        main.card_purple_99_label_middle_down.pack(pady=20)

        main.card_purple_100_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_purple_100_title=tk.Label(main.card_purple_100_frame,text="🟣 PURPLE CARD",font=("Arial",20,"bold"),bg="white",fg="purple")
        main.card_purple_100_label_middle=tk.Label(main.card_purple_100_frame,text="Larger plants prevent the seed from getting enough resources.",font=("Arial",16),bg="white")
        main.card_purple_100_label_middle_down=tk.Label(main.card_purple_100_frame,text="Move back 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="red")
        main.card_purple_100_continue=tk.Button(main.card_purple_100_frame,text="Continue")
        main.card_purple_100_title.pack(pady=20)
        main.card_purple_100_label_middle.pack(pady=20)
        main.card_purple_100_label_middle_down.pack(pady=20)

        main.card_orange_101_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_orange_101_title=tk.Label(main.card_orange_101_frame,text="🟠 ORANGE CARD",font=("Arial",20,"bold"),bg="white",fg="orange")
        main.card_orange_101_label_middle=tk.Label(main.card_orange_101_frame,text="Too much water washes the seed away from its landing place.",font=("Arial",16),bg="white")
        main.card_orange_101_label_middle_down=tk.Label(main.card_orange_101_frame,text="Move back 4 spaces.",font=("Arial",14,"bold"),bg="white",fg="red")
        main.card_orange_101_continue=tk.Button(main.card_orange_101_frame,text="Continue")
        main.card_orange_101_title.pack(pady=20)
        main.card_orange_101_label_middle.pack(pady=20)
        main.card_orange_101_label_middle_down.pack(pady=20)

        main.card_orange_102_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_orange_102_title=tk.Label(main.card_orange_102_frame,text="🟠 ORANGE CARD",font=("Arial",20,"bold"),bg="white",fg="orange")
        main.card_orange_102_label_middle=tk.Label(main.card_orange_102_frame,text="Moving water carries the seed away from a suitable area.",font=("Arial",16),bg="white")
        main.card_orange_102_label_middle_down=tk.Label(main.card_orange_102_frame,text="Move back 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="red")
        main.card_orange_102_continue=tk.Button(main.card_orange_102_frame,text="Continue")
        main.card_orange_102_title.pack(pady=20)
        main.card_orange_102_label_middle.pack(pady=20)
        main.card_orange_102_label_middle_down.pack(pady=20)

        main.card_orange_103_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_orange_103_title=tk.Label(main.card_orange_103_frame,text="🟠 ORANGE CARD",font=("Arial",20,"bold"),bg="white",fg="orange")
        main.card_orange_103_label_middle=tk.Label(main.card_orange_103_frame,text="The seed is carried away by fast-moving water.",font=("Arial",16),bg="white")
        main.card_orange_103_label_middle_down=tk.Label(main.card_orange_103_frame,text="Move back 4 spaces.",font=("Arial",14,"bold"),bg="white",fg="red")
        main.card_orange_103_continue=tk.Button(main.card_orange_103_frame,text="Continue")
        main.card_orange_103_title.pack(pady=20)
        main.card_orange_103_label_middle.pack(pady=20)
        main.card_orange_103_label_middle_down.pack(pady=20)

        main.card_orange_104_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_orange_104_title=tk.Label(main.card_orange_104_frame,text="🟠 ORANGE CARD",font=("Arial",20,"bold"),bg="white",fg="orange")
        main.card_orange_104_label_middle=tk.Label(main.card_orange_104_frame,text="The seed becomes stuck in thick mud and loses ground.",font=("Arial",16),bg="white")
        main.card_orange_104_label_middle_down=tk.Label(main.card_orange_104_frame,text="Move back 2 spaces.",font=("Arial",14,"bold"),bg="white",fg="red")
        main.card_orange_104_continue=tk.Button(main.card_orange_104_frame,text="Continue")
        main.card_orange_104_title.pack(pady=20)
        main.card_orange_104_label_middle.pack(pady=20)
        main.card_orange_104_label_middle_down.pack(pady=20)

        main.card_orange_105_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_orange_105_title=tk.Label(main.card_orange_105_frame,text="🟠 ORANGE CARD",font=("Arial",20,"bold"),bg="white",fg="orange")
        main.card_orange_105_label_middle=tk.Label(main.card_orange_105_frame,text="The current carries the seed farther away from its destination.",font=("Arial",16),bg="white")
        main.card_orange_105_label_middle_down=tk.Label(main.card_orange_105_frame,text="Move back 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="red")
        main.card_orange_105_continue=tk.Button(main.card_orange_105_frame,text="Continue")
        main.card_orange_105_title.pack(pady=20)
        main.card_orange_105_label_middle.pack(pady=20)
        main.card_orange_105_label_middle_down.pack(pady=20)
        main.card_blue_1_continue.config(command=continue_blue_1)
        main.card_blue_2_continue.config(command=continue_blue_2)
        main.card_blue_3_continue.config(command=continue_blue_3)
        main.card_blue_4_continue.config(command=continue_blue_4)
        main.card_blue_5_continue.config(command=continue_blue_5)
        main.card_blue_6_continue.config(command=continue_blue_6)
        main.card_blue_7_continue.config(command=continue_blue_7)
        main.card_blue_8_continue.config(command=continue_blue_8)
        main.card_blue_9_continue.config(command=continue_blue_9)
        main.card_blue_10_continue.config(command=continue_red_20)
        main.card_red_11_continue.config(command=continue_red_11)
        main.card_red_12_continue.config(command=continue_red_12)
        main.card_red_13_continue.config(command=continue_red_13)
        main.card_red_14_continue.config(command=continue_red_14)
        main.card_red_15_continue.config(command=continue_red_15)
        main.card_red_16_continue.config(command=continue_red_16)
        main.card_red_17_continue.config(command=continue_red_17)
        main.card_red_18_continue.config(command=continue_red_18)
        main.card_red_19_continue.config(command=continue_red_19)
        main.card_red_20_continue.config(command=continue_red_20)
        main.card_green_21_continue.config(command=continue_green_21)
        main.card_green_22_continue.config(command=continue_green_22)
        main.card_green_23_continue.config(command=continue_green_23)
        main.card_green_24_continue.config(command=continue_green_24)
        main.card_green_25_continue.config(command=continue_green_25)
        main.card_green_26_continue.config(command=continue_green_26)
        main.card_green_27_continue.config(command=continue_green_27)
        main.card_green_28_continue.config(command=continue_green_28)
        main.card_green_29_continue.config(command=continue_green_29)
        main.card_green_30_continue.config(command=continue_green_30)
        main.card_yellow_31_continue.config(command=continue_yellow_31)
        main.card_yellow_32_continue.config(command=continue_yellow_32)
        main.card_yellow_33_continue.config(command=continue_yellow_33)
        main.card_yellow_34_continue.config(command=continue_yellow_34)
        main.card_yellow_35_continue.config(command=continue_yellow_35)
        main.card_yellow_36_continue.config(command=continue_yellow_36)
        main.card_yellow_37_continue.config(command=continue_yellow_37)
        main.card_yellow_38_continue.config(command=continue_yellow_38)
        main.card_yellow_39_continue.config(command=continue_yellow_39)
        main.card_yellow_40_continue.config(command=continue_yellow_40)
        main.card_brown_41_continue.config(command=continue_brown_41)
        main.card_brown_42_continue.config(command=continue_brown_42)
        main.card_brown_43_continue.config(command=continue_brown_43)
        main.card_brown_44_continue.config(command=continue_brown_44)
        main.card_brown_45_continue.config(command=continue_brown_45)
        main.card_brown_46_continue.config(command=continue_brown_46)
        main.card_brown_47_continue.config(command=continue_brown_47)
        main.card_brown_48_continue.config(command=continue_brown_48)
        main.card_brown_49_continue.config(command=continue_brown_49)
        main.card_brown_50_continue.config(command=continue_brown_50)
        main.card_purple_51_continue.config(command=continue_purple_51)
        main.card_purple_52_continue.config(command=continue_purple_52)
        main.card_purple_53_continue.config(command=continue_purple_53)
        main.card_purple_54_continue.config(command=continue_purple_54)
        main.card_purple_55_continue.config(command=continue_purple_55)
        main.card_purple_56_continue.config(command=continue_purple_56)
        main.card_purple_57_continue.config(command=continue_purple_57)
        main.card_purple_58_continue.config(command=continue_purple_58)
        main.card_purple_59_continue.config(command=continue_purple_59)
        main.card_purple_60_continue.config(command=continue_purple_60)
        main.card_orange_61_continue.config(command=continue_orange_61)
        main.card_orange_62_continue.config(command=continue_orange_62)
        main.card_orange_63_continue.config(command=continue_orange_63)
        main.card_orange_64_continue.config(command=continue_orange_64)
        main.card_orange_65_continue.config(command=continue_orange_65)
        main.card_orange_66_continue.config(command=continue_orange_66)
        main.card_orange_67_continue.config(command=continue_orange_67)
        main.card_orange_68_continue.config(command=continue_orange_68)
        main.card_orange_69_continue.config(command=continue_orange_69)
        main.card_orange_70_continue.config(command=continue_orange_70)
        main.card_blue_71_continue.config(command=continue_blue_71)
        main.card_blue_72_continue.config(command=continue_blue_72)
        main.card_blue_73_continue.config(command=continue_blue_73)
        main.card_blue_74_continue.config(command=continue_blue_74)
        main.card_blue_75_continue.config(command=continue_blue_75)

        main.card_red_76_continue.config(command=continue_red_76)
        main.card_red_77_continue.config(command=continue_red_77)
        main.card_red_78_continue.config(command=continue_red_78)
        main.card_red_79_continue.config(command=continue_red_79)
        main.card_red_80_continue.config(command=continue_red_80)

        main.card_green_81_continue.config(command=continue_green_81)
        main.card_green_82_continue.config(command=continue_green_82)
        main.card_green_83_continue.config(command=continue_green_83)
        main.card_green_84_continue.config(command=continue_green_84)
        main.card_green_85_continue.config(command=continue_green_85)

        main.card_yellow_86_continue.config(command=continue_yellow_86)
        main.card_yellow_87_continue.config(command=continue_yellow_87)
        main.card_yellow_88_continue.config(command=continue_yellow_88)
        main.card_yellow_89_continue.config(command=continue_yellow_89)
        main.card_yellow_90_continue.config(command=continue_yellow_90)

        main.card_brown_91_continue.config(command=continue_brown_91)
        main.card_brown_92_continue.config(command=continue_brown_92)
        main.card_brown_93_continue.config(command=continue_brown_93)
        main.card_brown_94_continue.config(command=continue_brown_94)
        main.card_brown_95_continue.config(command=continue_brown_95)

        main.card_purple_96_continue.config(command=continue_purple_96)
        main.card_purple_97_continue.config(command=continue_purple_97)
        main.card_purple_98_continue.config(command=continue_purple_98)
        main.card_purple_99_continue.config(command=continue_purple_99)
        main.card_purple_100_continue.config(command=continue_purple_100)

        main.card_orange_101_continue.config(command=continue_orange_101)
        main.card_orange_102_continue.config(command=continue_orange_102)
        main.card_orange_103_continue.config(command=continue_orange_103)
        main.card_orange_104_continue.config(command=continue_orange_104)
        main.card_orange_105_continue.config(command=continue_orange_105)
        main.rolleddicebuttonlabel.place(x=0,y=0)
        main.player_position = 0
        main.player = main.canvas_for_game.create_oval(
            0, 0, 0, 0,
            fill="#402c03",
            outline="black",
            width=2
        )

        # Put the board and player into their correct positions immediately.
        main.root.after_idle(main.resize_game_layout)
    def forget_menu_frame(main):
        main.menu.destroy()
    def start_game(main):
        main.forget_menu_frame()
        main.frame_new_plus_board_game()
    def show_menu(main):
        main.menu = tk.Frame(main.root)
        main.menu.place(relx=0, rely=0, relheight=1, relwidth=1)
        main.title = tk.Label(main.menu, text="Journey of a Seed", font=("Segoe UI", 30, "bold"))
        main.title.place(relx=0.5,rely=0.2,anchor="center")
        main.play_button = tk.Button(main.menu, text = "Play the game!", font=("Segoe UI", 25, "bold"),command = main.start_game)
        main.play_button.place(relx=0.5,rely=0.3,anchor="center")
def resource_path(relative_path):
    if getattr(sys, "frozen", False):
        base_path = sys._MEIPASS
    else:
        base_path = o.path.dirname(o.path.abspath(__file__))    
    return o.path.join(base_path, relative_path)
window=tk.Tk()
game=SeedAdventure(window)
icon = tk.PhotoImage(file=resource_path(o.path.join("Assets","Images","Supported types", "icon.png")))
window.iconphoto(True,icon)
window.geometry("1000x1000")
window.minsize(500, 500)
window.title("Journey of a seed game")
window.resizable(True, True)
game.show_menu()
window.mainloop()