import tkinter as tk
import random as r
import winsound as w
import os as o


class SeedAdventure:
    GRID_SIZE = 8
    TILE_SIZE = 100
    BOARD_ORIGIN_X = 100
    BOARD_ORIGIN_Y = 150
    WIN_TILE = 63

    def __init__(self, root):
        self.root = root
        self.player_position = 0
        self.game_won = False
        self.menu = None
        self.game = None
        self.win_frame = None
        self.tree_image = None
        self.canvas_for_game = None
        self.player = None
        self.tiles = []
        self.colours = ["blue", "red", "green", "yellow", "brown", "purple", "orange"]
        self.colours_for_tiles = []
        self.check_running = False

    # ----------------------------
    # Small helpers
    # ----------------------------
    def asset_path(self, *parts):
        return o.path.join(*parts)

    def stop_all_sounds(self):
        try:
            w.PlaySound(None, 0)
        except Exception:
            pass

    def play_sound(self, path, loop=False):
        flags = w.SND_FILENAME | w.SND_ASYNC
        if loop:
            flags |= w.SND_LOOP
        w.PlaySound(path, flags)

    def pos_to_xy(self, position):
        row = position // self.GRID_SIZE
        col = position % self.GRID_SIZE
        x = self.BOARD_ORIGIN_X + col * self.TILE_SIZE + 35
        y = self.BOARD_ORIGIN_Y + row * self.TILE_SIZE + 35
        return x, y

    def update_player_canvas(self):
        if self.canvas_for_game is None or self.player is None:
            return
        x, y = self.pos_to_xy(self.player_position)
        self.canvas_for_game.coords(self.player, x, y, x + 30, y + 30)

    def move_f_or_b(self, how_much_to_move, f_or_b):
        if f_or_b == "f":
            self.player_position += how_much_to_move
        elif f_or_b == "b":
            self.player_position -= how_much_to_move

        if self.player_position < 0:
            self.player_position = 0
        if self.player_position > self.WIN_TILE:
            self.player_position = self.WIN_TILE

        self.update_player_canvas()
        self.check_win()

    def return_to_board(self, card_frame, steps=0, direction="f", finish=False):
        card_frame.place_forget()
        if self.game is not None:
            self.game.place(relx=0, rely=0, relheight=1, relwidth=1)
        if finish:
            self.show_win_screen()
            return
        if steps:
            self.move_f_or_b(steps, direction)

    # ----------------------------
    # Win screen
    # ----------------------------
    def check_win(self):
        if self.game_won:
            return
        if self.player_position >= self.WIN_TILE:
            self.show_win_screen()
            return
        if not self.check_running:
            self.check_running = True
            self.root.after(100, self._check_win_tick)

    def _check_win_tick(self):
        self.check_running = False
        if self.game_won:
            return
        if self.player_position >= self.WIN_TILE:
            self.show_win_screen()
            return
        self.check_win()

    def show_win_screen(self):
        if self.game_won:
            return
        self.game_won = True
        self.stop_all_sounds()

        if self.game is not None:
            self.game.place_forget()
        if self.menu is not None:
            self.menu.place_forget()

        self.play_sound(self.asset_path("Assets", "Sounds", "Wav", "win.wav"))

        self.win_frame = tk.Frame(self.root, bg="#c8f7c5")
        self.win_frame.place(relwidth=1, relheight=1, relx=0, rely=0)

        tk.Label(
            self.win_frame,
            text="🏆 YOU WIN! 🏆",
            font=("Segoe UI", 30, "bold"),
            bg="#c8f7c5",
            fg="darkgreen"
        ).pack(pady=20)

        tree_file = self.asset_path("Assets", "Images", "Supported types", "tree.png")
        self.tree_image = tk.PhotoImage(file=tree_file)
        self.tree_image = self.tree_image.subsample(2, 2)

        tk.Label(self.win_frame, image=self.tree_image, bg="#c8f7c5").pack()

        tk.Label(
            self.win_frame,
            text=(
                "Congratulations!\n"
                "You successfully guided the seed\n"
                "through its amazing journey.\n\n"
                "The seed has now grown into\na beautiful tree! 🌳"
            ),
            font=("Segoe UI", 18),
            bg="#c8f7c5",
            justify="center"
        ).pack(pady=20)

        tk.Button(
            self.win_frame,
            text="🔄 Play Again",
            font=("Segoe UI", 18, "bold"),
            bg="black",
            fg="white",
            activebackground="gray20",
            activeforeground="white",
            command=self.start_game
        ).pack(pady=10)

        tk.Button(
            self.win_frame,
            text="❌ Exit",
            font=("Segoe UI", 16),
            bg="darkred",
            fg="white",
            command=self.root.destroy
        ).pack(pady=5)

    # ----------------------------
    # Cards / board generation
    # ----------------------------
    def build_card(self, parent, title, title_fg, middle, move_text, button_text="Continue"):
        frame = tk.Frame(parent, bg="white", bd=5, relief="ridge")
        tk.Label(frame, text=title, font=("Arial", 20, "bold"), bg="white", fg=title_fg).pack(pady=20)
        tk.Label(frame, text=middle, font=("Arial", 16), bg="white", wraplength=430, justify="center").pack(pady=20)
        tk.Label(frame, text=move_text, font=("Arial", 14, "bold"), bg="white", fg="green").pack(pady=20)
        btn = tk.Button(frame, text=button_text)
        btn.pack(side="bottom", pady=20)
        return frame, btn

    def make_cards(self):
        self.card_blue_1_frame, self.card_blue_1_continue = self.build_card(self.root, "🌧 BLUE CARD", "blue", "Heavy rain helps you grow.", "Move forward 2 spaces.")
        self.card_blue_2_frame, self.card_blue_2_continue = self.build_card(self.root, "🌧 BLUE CARD", "blue", "A river carries your seed safely.", "Move forward 3 spaces.")
        self.card_blue_3_frame, self.card_blue_3_continue = self.build_card(self.root, "🌧 BLUE CARD", "blue", "A gentle stream spreads your seeds.", "Move forward 2 spaces.")
        self.card_blue_4_frame, self.card_blue_4_continue = self.build_card(self.root, "🌧 BLUE CARD", "blue", "Water reaches rich soil.", "Move forward 1 space.")
        self.card_blue_5_frame, self.card_blue_5_continue = self.build_card(self.root, "🌧 BLUE CARD", "blue", "Floodwater carries you far away.", "Move forward 3 spaces.")
        self.card_blue_6_frame, self.card_blue_6_continue = self.build_card(self.root, "🌧 BLUE CARD", "blue", "Fresh water helps you survive.", "Move forward 2 spaces.")
        self.card_blue_7_frame, self.card_blue_7_continue = self.build_card(self.root, "🌧 BLUE CARD", "blue", "Rain washes away obstacles.", "Move forward 2 spaces.")
        self.card_blue_8_frame, self.card_blue_8_continue = self.build_card(self.root, "🌧 BLUE CARD", "blue", "Your seed floats to a new habitat.", "Move forward 3 spaces.")
        self.card_blue_9_frame, self.card_blue_9_continue = self.build_card(self.root, "🌧 BLUE CARD", "blue", "The current moves you quickly.", "Move forward 2 spaces.")
        self.card_blue_10_frame, self.card_blue_10_continue = self.build_card(self.root, "🌧 BLUE CARD", "blue", "You reach the perfect place to grow.", "Move forward 3 spaces.")

        self.card_red_11_frame, self.card_red_11_continue = self.build_card(self.root, "🍎 RED CARD", "red", "A bird eats your fruit and carries the seed.", "Move forward 3 spaces.")
        self.card_red_12_frame, self.card_red_12_continue = self.build_card(self.root, "🍎 RED CARD", "red", "A squirrel buries your seed.", "Move forward 2 spaces.")
        self.card_red_13_frame, self.card_red_13_continue = self.build_card(self.root, "🍎 RED CARD", "red", "An elephant drops your seed far away.", "Move forward 3 spaces.")
        self.card_red_14_frame, self.card_red_14_continue = self.build_card(self.root, "🍎 RED CARD", "red", "A monkey carries your fruit to another tree.", "Move forward 3 spaces.")
        self.card_red_15_frame, self.card_red_15_continue = self.build_card(self.root, "🍎 RED CARD", "red", "A deer carries your seed in its fur.", "Move forward 2 spaces.")
        self.card_red_16_frame, self.card_red_16_continue = self.build_card(self.root, "🍎 RED CARD", "red", "A fox brushes past and carries your seed.", "Move forward 2 spaces.")
        self.card_red_17_frame, self.card_red_17_continue = self.build_card(self.root, "🍎 RED CARD", "red", "A rabbit carries your seed to a meadow.", "Move forward 3 spaces.")
        self.card_red_18_frame, self.card_red_18_continue = self.build_card(self.root, "🍎 RED CARD", "red", "A bird drops your seed in fertile soil.", "Move forward 3 spaces.")
        self.card_red_19_frame, self.card_red_19_continue = self.build_card(self.root, "🍎 RED CARD", "red", "An animal leaves your seed near a river.", "Move forward 2 spaces.")
        self.card_red_20_frame, self.card_red_20_continue = self.build_card(self.root, "🍎 RED CARD", "red", "A herd of animals spreads your seeds widely.", "Move forward 3 spaces.")

        self.card_green_21_frame, self.card_green_21_continue = self.build_card(self.root, "🌿 GREEN CARD", "green", "A strong wind carries your seed far away.", "Move forward 3 spaces.")
        self.card_green_22_frame, self.card_green_22_continue = self.build_card(self.root, "🌿 GREEN CARD", "green", "Your winged seed glides safely.", "Move forward 2 spaces.")
        self.card_green_23_frame, self.card_green_23_continue = self.build_card(self.root, "🌿 GREEN CARD", "green", "A breeze lifts your seed over a hill.", "Move forward 3 spaces.")
        self.card_green_24_frame, self.card_green_24_continue = self.build_card(self.root, "🌿 GREEN CARD", "green", "The wind drops you in rich soil.", "Move forward 2 spaces.")
        self.card_green_25_frame, self.card_green_25_continue = self.build_card(self.root, "🌿 GREEN CARD", "green", "A gust sends your seed across a field.", "Move forward 3 spaces.")
        self.card_green_26_frame, self.card_green_26_continue = self.build_card(self.root, "🌿 GREEN CARD", "green", "Your parachute seed floats gently.", "Move forward 3 spaces.")
        self.card_green_27_frame, self.card_green_27_continue = self.build_card(self.root, "🌿 GREEN CARD", "green", "A cool breeze keeps you flying.", "Move forward 2 spaces.")
        self.card_green_28_frame, self.card_green_28_continue = self.build_card(self.root, "🌿 GREEN CARD", "green", "The wind carries you over a river.", "Move forward 3 spaces.")
        self.card_green_29_frame, self.card_green_29_continue = self.build_card(self.root, "🌿 GREEN CARD", "green", "Your seed lands in a sunny clearing.", "Move forward 2 spaces.")
        self.card_green_30_frame, self.card_green_30_continue = self.build_card(self.root, "🌿 GREEN CARD", "green", "The wind spreads your seeds perfectly.", "Move forward 3 spaces.")

        self.card_yellow_31_frame, self.card_yellow_31_continue = self.build_card(self.root, "💥 YELLOW CARD", "goldenrod", "Your pod bursts open in the sunshine.", "Move forward 3 spaces.")
        self.card_yellow_32_frame, self.card_yellow_32_continue = self.build_card(self.root, "💥 YELLOW CARD", "goldenrod", "The seed pod explodes with a pop!", "Move forward 3 spaces.")
        self.card_yellow_33_frame, self.card_yellow_33_continue = self.build_card(self.root, "💥 YELLOW CARD", "goldenrod", "Your seed is launched into a meadow.", "Move forward 2 spaces.")
        self.card_yellow_34_frame, self.card_yellow_34_continue = self.build_card(self.root, "💥 YELLOW CARD", "goldenrod", "The pod dries and suddenly bursts.", "Move forward 3 spaces.")
        self.card_yellow_35_frame, self.card_yellow_35_continue = self.build_card(self.root, "💥 YELLOW CARD", "goldenrod", "Your seeds scatter in every direction.", "Move forward 3 spaces.")
        self.card_yellow_36_frame, self.card_yellow_36_continue = self.build_card(self.root, "💥 YELLOW CARD", "goldenrod", "The pod splits open with force.", "Move forward 3 spaces.")
        self.card_yellow_37_frame, self.card_yellow_37_continue = self.build_card(self.root, "💥 YELLOW CARD", "goldenrod", "Warm weather triggers seed release.", "Move forward 2 spaces.")
        self.card_yellow_38_frame, self.card_yellow_38_continue = self.build_card(self.root, "💥 YELLOW CARD", "goldenrod", "Your seeds land in open ground.", "Move forward 3 spaces.")
        self.card_yellow_39_frame, self.card_yellow_39_continue = self.build_card(self.root, "💥 YELLOW CARD", "goldenrod", "The pod catapults your seed away.", "Move forward 3 spaces.")
        self.card_yellow_40_frame, self.card_yellow_40_continue = self.build_card(self.root, "💥 YELLOW CARD", "goldenrod", "Perfect explosion! Seeds spread everywhere.", "Move forward 3 spaces.")

        self.card_brown_41_frame, self.card_brown_41_continue = self.build_card(self.root, "🟤 BROWN CARD", "saddlebrown", "A worm helps the soil become rich.", "Move forward 2 spaces.")
        self.card_brown_42_frame, self.card_brown_42_continue = self.build_card(self.root, "🟤 BROWN CARD", "saddlebrown", "The ground is soft and safe.", "Move forward 3 spaces.")
        self.card_brown_43_frame, self.card_brown_43_continue = self.build_card(self.root, "🟤 BROWN CARD", "saddlebrown", "Great soil helps you sprout.", "Move forward 1 space.")
        self.card_brown_44_frame, self.card_brown_44_continue = self.build_card(self.root, "🟤 BROWN CARD", "saddlebrown", "The roots grow deeper.", "Move forward 3 spaces.")
        self.card_brown_45_frame, self.card_brown_45_continue = self.build_card(self.root, "🟤 BROWN CARD", "saddlebrown", "The soil keeps you warm.", "Move forward 2 spaces.")
        self.card_brown_46_frame, self.card_brown_46_continue = self.build_card(self.root, "🟤 BROWN CARD", "saddlebrown", "You find hidden minerals.", "Move forward 3 spaces.")
        self.card_brown_47_frame, self.card_brown_47_continue = self.build_card(self.root, "🟤 BROWN CARD", "saddlebrown", "Strong roots anchor your plant.", "Move forward 1 space.")
        self.card_brown_48_frame, self.card_brown_48_continue = self.build_card(self.root, "🟤 BROWN CARD", "saddlebrown", "The soil is perfect today.", "Move forward 3 spaces.")
        self.card_brown_49_frame, self.card_brown_49_continue = self.build_card(self.root, "🟤 BROWN CARD", "saddlebrown", "Rain mixes with soil nutrients.", "Move forward 2 spaces.")
        self.card_brown_50_frame, self.card_brown_50_continue = self.build_card(self.root, "🟤 BROWN CARD", "saddlebrown", "You are ready for the next stage.", "Move forward 3 spaces.")

        self.card_purple_51_frame, self.card_purple_51_continue = self.build_card(self.root, "🟣 PURPLE CARD", "purple", "A shady place protects your seed.", "Move forward 2 spaces.")
        self.card_purple_52_frame, self.card_purple_52_continue = self.build_card(self.root, "🟣 PURPLE CARD", "purple", "Cool air helps you travel.", "Move forward 3 spaces.")
        self.card_purple_53_frame, self.card_purple_53_continue = self.build_card(self.root, "🟣 PURPLE CARD", "purple", "A mist carries tiny seeds.", "Move forward 1 space.")
        self.card_purple_54_frame, self.card_purple_54_continue = self.build_card(self.root, "🟣 PURPLE CARD", "purple", "The forest helps spread seeds.", "Move forward 3 spaces.")
        self.card_purple_55_frame, self.card_purple_55_continue = self.build_card(self.root, "🟣 PURPLE CARD", "purple", "You drift to a new home.", "Move forward 2 spaces.")
        self.card_purple_56_frame, self.card_purple_56_continue = self.build_card(self.root, "🟣 PURPLE CARD", "purple", "Shade keeps you safe.", "Move forward 3 spaces.")
        self.card_purple_57_frame, self.card_purple_57_continue = self.build_card(self.root, "🟣 PURPLE CARD", "purple", "Your seed finds a cozy spot.", "Move forward 1 space.")
        self.card_purple_58_frame, self.card_purple_58_continue = self.build_card(self.root, "🟣 PURPLE CARD", "purple", "Soft wind carries you on.", "Move forward 3 spaces.")
        self.card_purple_59_frame, self.card_purple_59_continue = self.build_card(self.root, "🟣 PURPLE CARD", "purple", "The journey continues smoothly.", "Move forward 2 spaces.")
        self.card_purple_60_frame, self.card_purple_60_continue = self.build_card(self.root, "🟣 PURPLE CARD", "purple", "You are almost there.", "Move forward 3 spaces.")

        self.card_orange_61_frame, self.card_orange_61_continue = self.build_card(self.root, "🟠 ORANGE CARD", "orange", "A warm season helps you grow.", "Move forward 2 spaces.")
        self.card_orange_62_frame, self.card_orange_62_continue = self.build_card(self.root, "🟠 ORANGE CARD", "orange", "Fruits drop and spread seeds.", "Move forward 3 spaces.")
        self.card_orange_63_frame, self.card_orange_63_continue = self.build_card(self.root, "🟠 ORANGE CARD", "orange", "Your tree becomes full of healthy fruits.", "Move forward 3 spaces.")
        self.card_orange_64_frame, self.card_orange_64_continue = self.build_card(self.root, "🟠 ORANGE CARD", "orange", "Many animals spread your seeds.", "Move forward 3 spaces.")
        self.card_orange_65_frame, self.card_orange_65_continue = self.build_card(self.root, "🟠 ORANGE CARD", "orange", "Your seeds begin a new generation.", "Move forward 3 spaces.")
        self.card_orange_66_frame, self.card_orange_66_continue = self.build_card(self.root, "🟠 ORANGE CARD", "orange", "The season is perfect for growth.", "Move forward 2 spaces.")
        self.card_orange_67_frame, self.card_orange_67_continue = self.build_card(self.root, "🟠 ORANGE CARD", "orange", "You have completed the life cycle!", "Move forward 3 spaces.")
        self.card_orange_68_frame, self.card_orange_68_continue = self.build_card(self.root, "🟠 ORANGE CARD", "orange", "A perfect season helps every seed grow.", "Move forward 3 spaces.")
        self.card_orange_69_frame, self.card_orange_69_continue = self.build_card(self.root, "🟠 ORANGE CARD", "orange", "Nature celebrates your success!", "Move forward 3 spaces.")
        self.card_orange_70_frame, self.card_orange_70_continue = self.build_card(self.root, "🟠 ORANGE CARD", "orange", "You got watered (Bonus Card).", "You move 2 spaces.", button_text="Finish")

        # easy lookup table for continue actions
        self.continue_actions = {
            self.card_blue_1_continue: lambda: self.return_to_board(self.card_blue_1_frame, 2, "f"),
            self.card_blue_2_continue: lambda: self.return_to_board(self.card_blue_2_frame, 3, "f"),
            self.card_blue_3_continue: lambda: self.return_to_board(self.card_blue_3_frame, 1, "b"),
            self.card_blue_4_continue: lambda: self.return_to_board(self.card_blue_4_frame, 1, "f"),
            self.card_blue_5_continue: lambda: self.return_to_board(self.card_blue_5_frame, 3, "f"),
            self.card_blue_6_continue: lambda: self.return_to_board(self.card_blue_6_frame, 2, "f"),
            self.card_blue_7_continue: lambda: self.return_to_board(self.card_blue_7_frame, 2, "f"),
            self.card_blue_8_continue: lambda: self.return_to_board(self.card_blue_8_frame, 3, "f"),
            self.card_blue_9_continue: lambda: self.return_to_board(self.card_blue_9_frame, 2, "f"),
            self.card_blue_10_continue: lambda: self.return_to_board(self.card_blue_10_frame, 3, "f"),

            self.card_red_11_continue: lambda: self.return_to_board(self.card_red_11_frame, 3, "f"),
            self.card_red_12_continue: lambda: self.return_to_board(self.card_red_12_frame, 2, "f"),
            self.card_red_13_continue: lambda: self.return_to_board(self.card_red_13_frame, 3, "f"),
            self.card_red_14_continue: lambda: self.return_to_board(self.card_red_14_frame, 3, "f"),
            self.card_red_15_continue: lambda: self.return_to_board(self.card_red_15_frame, 2, "f"),
            self.card_red_16_continue: lambda: self.return_to_board(self.card_red_16_frame, 2, "f"),
            self.card_red_17_continue: lambda: self.return_to_board(self.card_red_17_frame, 3, "f"),
            self.card_red_18_continue: lambda: self.return_to_board(self.card_red_18_frame, 3, "f"),
            self.card_red_19_continue: lambda: self.return_to_board(self.card_red_19_frame, 2, "f"),
            self.card_red_20_continue: lambda: self.return_to_board(self.card_red_20_frame, 3, "f"),

            self.card_green_21_continue: lambda: self.return_to_board(self.card_green_21_frame, 3, "f"),
            self.card_green_22_continue: lambda: self.return_to_board(self.card_green_22_frame, 2, "f"),
            self.card_green_23_continue: lambda: self.return_to_board(self.card_green_23_frame, 3, "f"),
            self.card_green_24_continue: lambda: self.return_to_board(self.card_green_24_frame, 2, "f"),
            self.card_green_25_continue: lambda: self.return_to_board(self.card_green_25_frame, 3, "f"),
            self.card_green_26_continue: lambda: self.return_to_board(self.card_green_26_frame, 3, "f"),
            self.card_green_27_continue: lambda: self.return_to_board(self.card_green_27_frame, 2, "f"),
            self.card_green_28_continue: lambda: self.return_to_board(self.card_green_28_frame, 3, "f"),
            self.card_green_29_continue: lambda: self.return_to_board(self.card_green_29_frame, 2, "f"),
            self.card_green_30_continue: lambda: self.return_to_board(self.card_green_30_frame, 3, "f"),

            self.card_yellow_31_continue: lambda: self.return_to_board(self.card_yellow_31_frame, 3, "f"),
            self.card_yellow_32_continue: lambda: self.return_to_board(self.card_yellow_32_frame, 3, "f"),
            self.card_yellow_33_continue: lambda: self.return_to_board(self.card_yellow_33_frame, 2, "f"),
            self.card_yellow_34_continue: lambda: self.return_to_board(self.card_yellow_34_frame, 3, "f"),
            self.card_yellow_35_continue: lambda: self.return_to_board(self.card_yellow_35_frame, 3, "f"),
            self.card_yellow_36_continue: lambda: self.return_to_board(self.card_yellow_36_frame, 3, "f"),
            self.card_yellow_37_continue: lambda: self.return_to_board(self.card_yellow_37_frame, 2, "f"),
            self.card_yellow_38_continue: lambda: self.return_to_board(self.card_yellow_38_frame, 3, "f"),
            self.card_yellow_39_continue: lambda: self.return_to_board(self.card_yellow_39_frame, 3, "f"),
            self.card_yellow_40_continue: lambda: self.return_to_board(self.card_yellow_40_frame, 3, "f"),

            self.card_brown_41_continue: lambda: self.return_to_board(self.card_brown_41_frame, 2, "f"),
            self.card_brown_42_continue: lambda: self.return_to_board(self.card_brown_42_frame, 3, "f"),
            self.card_brown_43_continue: lambda: self.return_to_board(self.card_brown_43_frame, 1, "f"),
            self.card_brown_44_continue: lambda: self.return_to_board(self.card_brown_44_frame, 3, "f"),
            self.card_brown_45_continue: lambda: self.return_to_board(self.card_brown_45_frame, 2, "f"),
            self.card_brown_46_continue: lambda: self.return_to_board(self.card_brown_46_frame, 3, "f"),
            self.card_brown_47_continue: lambda: self.return_to_board(self.card_brown_47_frame, 1, "f"),
            self.card_brown_48_continue: lambda: self.return_to_board(self.card_brown_48_frame, 3, "f"),
            self.card_brown_49_continue: lambda: self.return_to_board(self.card_brown_49_frame, 2, "f"),
            self.card_brown_50_continue: lambda: self.return_to_board(self.card_brown_50_frame, 3, "f"),

            self.card_purple_51_continue: lambda: self.return_to_board(self.card_purple_51_frame, 2, "f"),
            self.card_purple_52_continue: lambda: self.return_to_board(self.card_purple_52_frame, 3, "f"),
            self.card_purple_53_continue: lambda: self.return_to_board(self.card_purple_53_frame, 1, "f"),
            self.card_purple_54_continue: lambda: self.return_to_board(self.card_purple_54_frame, 3, "f"),
            self.card_purple_55_continue: lambda: self.return_to_board(self.card_purple_55_frame, 2, "f"),
            self.card_purple_56_continue: lambda: self.return_to_board(self.card_purple_56_frame, 3, "f"),
            self.card_purple_57_continue: lambda: self.return_to_board(self.card_purple_57_frame, 1, "f"),
            self.card_purple_58_continue: lambda: self.return_to_board(self.card_purple_58_frame, 3, "f"),
            self.card_purple_59_continue: lambda: self.return_to_board(self.card_purple_59_frame, 2, "f"),
            self.card_purple_60_continue: lambda: self.return_to_board(self.card_purple_60_frame, 3, "f"),

            self.card_orange_61_continue: lambda: self.return_to_board(self.card_orange_61_frame, 2, "f"),
            self.card_orange_62_continue: lambda: self.return_to_board(self.card_orange_62_frame, 3, "f"),
            self.card_orange_63_continue: lambda: self.return_to_board(self.card_orange_63_frame, 3, "f"),
            self.card_orange_64_continue: lambda: self.return_to_board(self.card_orange_64_frame, 3, "f"),
            self.card_orange_65_continue: lambda: self.return_to_board(self.card_orange_65_frame, 3, "f"),
            self.card_orange_66_continue: lambda: self.return_to_board(self.card_orange_66_frame, 2, "f"),
            self.card_orange_67_continue: lambda: self.return_to_board(self.card_orange_67_frame, 3, "f"),
            self.card_orange_68_continue: lambda: self.return_to_board(self.card_orange_68_frame, 3, "f"),
            self.card_orange_69_continue: lambda: self.return_to_board(self.card_orange_69_frame, 3, "f"),
            self.card_orange_70_continue: lambda: self.return_to_board(self.card_orange_70_frame, finish=True),
        }

        for button, command in self.continue_actions.items():
            button.config(command=command)

    def make_board(self):
        self.game = tk.Frame(self.root)
        self.game.place(relx=0, rely=0, relheight=1, relwidth=1)

        self.canvas_for_game = tk.Canvas(self.game, bg="black")
        self.canvas_for_game.place(relx=0, rely=0, relheight=1, relwidth=1)

        self.tiles = []
        self.colours_for_tiles = []
        x = self.BOARD_ORIGIN_X
        y = self.BOARD_ORIGIN_Y
        for row in range(self.GRID_SIZE):
            x = self.BOARD_ORIGIN_X
            for col in range(self.GRID_SIZE):
                colour = r.choice(self.colours)
                self.colours_for_tiles.append(colour)
                self.tiles.append(self.canvas_for_game.create_rectangle(x, y, x + self.TILE_SIZE, y + self.TILE_SIZE, fill=colour, outline="black"))
                x += self.TILE_SIZE
            y += self.TILE_SIZE

        self.player_position = 0
        self.player = self.canvas_for_game.create_oval(135, 185, 165, 215, fill="#402c03", outline="black", width=2)
        self.update_player_canvas()

    # ----------------------------
    # Main gameplay
    # ----------------------------
    def show_card(self, card_frame):
        if self.game is not None:
            self.game.place_forget()
        card_frame.place(relx=0.5, rely=0.5, anchor="center", width=500, height=350)

    def roll_dice(self):
        dice_sound = self.asset_path("Assets", "Sounds", "Wav", "dice_sound.wav")
        card_sound = self.asset_path("Assets", "Sounds", "Wav", "Card_pop_sound.wav")

        self.play_sound(dice_sound)
        dice = r.randint(1, 3)

        self.player_position += dice
        if self.player_position > self.WIN_TILE:
            self.player_position = self.WIN_TILE
        self.update_player_canvas()

        current_colour = self.colours_for_tiles[self.player_position]
        cards_by_colour = {
            "blue": [
                self.card_blue_1_frame, self.card_blue_2_frame, self.card_blue_3_frame, self.card_blue_4_frame,
                self.card_blue_5_frame, self.card_blue_6_frame, self.card_blue_7_frame, self.card_blue_8_frame,
                self.card_blue_9_frame, self.card_blue_10_frame,
            ],
            "red": [
                self.card_red_11_frame, self.card_red_12_frame, self.card_red_13_frame, self.card_red_14_frame,
                self.card_red_15_frame, self.card_red_16_frame, self.card_red_17_frame, self.card_red_18_frame,
                self.card_red_19_frame, self.card_red_20_frame,
            ],
            "green": [
                self.card_green_21_frame, self.card_green_22_frame, self.card_green_23_frame, self.card_green_24_frame,
                self.card_green_25_frame, self.card_green_26_frame, self.card_green_27_frame, self.card_green_28_frame,
                self.card_green_29_frame, self.card_green_30_frame,
            ],
            "yellow": [
                self.card_yellow_31_frame, self.card_yellow_32_frame, self.card_yellow_33_frame, self.card_yellow_34_frame,
                self.card_yellow_35_frame, self.card_yellow_36_frame, self.card_yellow_37_frame, self.card_yellow_38_frame,
                self.card_yellow_39_frame, self.card_yellow_40_frame,
            ],
            "brown": [
                self.card_brown_41_frame, self.card_brown_42_frame, self.card_brown_43_frame, self.card_brown_44_frame,
                self.card_brown_45_frame, self.card_brown_46_frame, self.card_brown_47_frame, self.card_brown_48_frame,
                self.card_brown_49_frame, self.card_brown_50_frame,
            ],
            "purple": [
                self.card_purple_51_frame, self.card_purple_52_frame, self.card_purple_53_frame, self.card_purple_54_frame,
                self.card_purple_55_frame, self.card_purple_56_frame, self.card_purple_57_frame, self.card_purple_58_frame,
                self.card_purple_59_frame, self.card_purple_60_frame,
            ],
            "orange": [
                self.card_orange_61_frame, self.card_orange_62_frame, self.card_orange_63_frame, self.card_orange_64_frame,
                self.card_orange_65_frame, self.card_orange_66_frame, self.card_orange_67_frame, self.card_orange_68_frame,
                self.card_orange_69_frame, self.card_orange_70_frame,
            ],
        }

        self.play_sound(card_sound)
        chosen_card = r.choice(cards_by_colour[current_colour])
        self.show_card(chosen_card)

    def frame_new_plus_board_game(self):
        self.game_won = False
        self.player_position = 0
        self.make_cards()
        self.make_board()
        self.check_win()

        self.rolldicebutton = tk.Button(
            self.canvas_for_game,
            command=self.roll_dice,
            text="Roll Dice",
            font=("Arial", 20),
            bg="black",
            fg="white",
            activebackground="black",
            activeforeground="white"
        )
        self.rolldicebutton.place(x=10, y=10)

    # ----------------------------
    # Menu
    # ----------------------------
    def forget_menu_frame(self):
        if self.menu is not None:
            self.menu.destroy()
            self.menu = None

    def start_game(self):
        self.forget_menu_frame()
        if self.win_frame is not None:
            self.win_frame.destroy()
            self.win_frame = None
        if self.game is not None:
            self.game.destroy()
            self.game = None
        self.frame_new_plus_board_game()

    def show_menu(self):
        if self.win_frame is not None:
            self.win_frame.destroy()
            self.win_frame = None
        if self.game is not None:
            self.game.destroy()
            self.game = None

        self.game_won = False
        self.menu = tk.Frame(self.root)
        self.menu.place(relx=0, rely=0, relheight=1, relwidth=1)

        self.title = tk.Label(self.menu, text="Journey of a Seed", font=("Segoe UI", 30, "bold"))
        self.title.place(relx=0.5, rely=0.2, anchor="center")

        self.play_button = tk.Button(self.menu, text="Play the game!", font=("Segoe UI", 25, "bold"), command=self.start_game)
        self.play_button.place(relx=0.5, rely=0.3, anchor="center")


if __name__ == "__main__":
    window = tk.Tk()
    window.geometry("1000x1000")
    window.title("Journey of a seed game")
    window.resizable(False, False)

    game = SeedAdventure(window)
    game.show_menu()
    window.mainloop()
