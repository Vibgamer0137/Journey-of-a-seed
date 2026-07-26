import tkinter as tk
import random as r
import winsound as w
import time as t
import os as o
class SeedAdventure:
    def __init__(main, root):
        main.root = root
    def move_f_or_b(main, how_much_to_move, f_or_b):
        if f_or_b == "f":
            main.player_position += how_much_to_move
        elif f_or_b == "b":
            main.player_position -= how_much_to_move

        if main.player_position < 0:
            main.player_position = 0
        if main.player_position > 63:
            main.player_position = 63
    
        row = main.player_position // 8
        col = main.player_position % 8
    
        x = 100 + col * 100 + 35
        y = 150 + row * 100 + 35
        
        # Moves the player token oval on the canvas
        main.canvas_for_game.coords(main.player, x, y, x + 30, y + 30)
    def frame_new_plus_board_game(main):
        DICE_SOUND = o.path.join("Assets","Sounds","Wav","dice_sound.wav")
        CARD_SOUND = o.path.join("Assets","Sounds","Wav","Card_pop.sound.wav")
        main.game = tk.Frame(main.root)
        main.game.place(relx=0, rely=0, relheight=1, relwidth=1)
        main.tiles = []
        main.canvas_for_game = tk.Canvas(main.game, bg="black")
        main.canvas_for_game.place(relx=0, rely=0, relheight=1, relwidth=1)
        x = 100
        y = 150
        main.colours = ["blue", "red", "green", "yellow", "brown", "purple", "orange"]
        main.colours_for_tiles = []
        for row in range(8):
            x = 100
            for col in range(8):
                main.colour = r.choice(main.colours)
                main.colours_for_tiles.append(main.colour)
                main.tiles.append(main.canvas_for_game.create_rectangle(x, y, x+100, y+100, fill=main.colour))
                x += 100
            y += 100

        def rolldicebuttoncommand():
            w.PlaySound(DICE_SOUND, w.SND_FILENAME | w.SND_ASYNC)
            t.sleep(1)
            dice = r.randint(1, 3)
            rolleddicebuttonlabel = tk.Label(main.root, text=dice, font=("Arial",17),bg="black",fg="white")
            rolleddicebuttonlabel.place(x=10, y=65)
            main.player_position += dice
            if main.player_position > 63:
                main.player_position = 63
            row = main.player_position // 8
            col = main.player_position % 8

            x = 100 + col * 100 + 35
            y = 150 + row * 100 + 35
            main.canvas_for_game.coords(main.player, x, y, x + 30, y + 30)
            current_colour = main.colours_for_tiles[main.player_position]
            if current_colour == main.colours[0]:
                rolleddicebuttonlabel.place_forget()
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
                    main.card_blue_10_frame
                ]
                main.card = r.choice(blue_cards)
                main.card.place(relx=0.5, rely=0.5, anchor="center", width=500, height=350)
                rolleddicebuttonlabel.place(x=10,y=65)
            elif current_colour == main.colours[1]:
                rolleddicebuttonlabel.place_forget()
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
                    main.card_red_20_frame
                ]
                main.card = r.choice(red_cards)
                main.card.place(relx=0.5, rely=0.5, anchor="center", width=500, height=350)
                rolleddicebuttonlabel.place(x=10,y=65)
            elif current_colour == main.colours[2]:
                rolleddicebuttonlabel.place_forget()
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
                    main.card_green_30_frame
                ]
                main.card = r.choice(green_cards)
                main.card.place(relx=0.5, rely=0.5, anchor="center", width=500, height=350)
                rolleddicebuttonlabel.place()
            elif current_colour == main.colours[3]:
                rolleddicebuttonlabel.place_forget()
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
                    main.card_yellow_40_frame
                ]
                main.card = r.choice(yellow_cards)
                main.card.place(relx=0.5, rely=0.5, anchor="center", width=500, height=350)
                rolleddicebuttonlabel.place(x=10,y=65)
            elif current_colour == main.colours[4]:
                rolleddicebuttonlabel.place_forget()
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
                    main.card_brown_50_frame
                ]
                main.card = r.choice(brown_cards)
                main.card.place(relx=0.5, rely=0.5, anchor="center", width=500, height=350)
                rolleddicebuttonlabel.place(x=10,y=65)
            elif current_colour == main.colours[5]:
                rolleddicebuttonlabel.place_forget()
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
                    main.card_purple_60_frame
                ]
                main.card = r.choice(purple_cards)
                main.card.place(relx=0.5, rely=0.5, anchor="center", width=500, height=350)
                rolleddicebuttonlabel.place(x=10,y=65)
            elif current_colour == main.colours[6]:
                rolleddicebuttonlabel.place_forget()
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
                    main.card_orange_70_frame
                ]
                main.card = r.choice(orange_cards)
                main.card.place(relx=0.5, rely=0.5, anchor="center", width=500, height=350)
                rolleddicebuttonlabel.place(x=10,y=65)
            else:
                print("Error code:5500")
            def continue_blue_1():
                main.card_blue_1_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(2,"f")

            def continue_blue_2():
                main.card_blue_2_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(3,"f")

            def continue_blue_3():
                main.card_blue_3_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(1,"b")

            def continue_blue_4():
                main.card_blue_4_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(2,"f")

            def continue_blue_5():
                main.card_blue_5_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(1,"f")

            def continue_blue_6():
                main.card_blue_6_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(2,"b")

            def continue_blue_7():
                main.card_blue_7_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(3,"f")

            def continue_blue_8():
                main.card_blue_8_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(3,"f")

            def continue_blue_9():
                main.card_blue_9_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(2,"b")

            def continue_blue_10():
                main.card_blue_10_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(3,"f")

            def continue_red_11():
                main.card_red_11_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(2,"b")

            def continue_red_12():
                main.card_red_12_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(3,"b")

            def continue_red_13():
                main.card_red_13_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(1,"f")

            def continue_red_14():
                main.card_red_14_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(2,"b")

            def continue_red_15():
                main.card_red_15_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(3,"b")

            def continue_red_16():
                main.card_red_16_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(2,"f")

            def continue_red_17():
                main.card_red_17_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(1,"b")

            def continue_red_18():
                main.card_red_18_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(3,"b")

            def continue_red_19():
                main.card_red_19_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(2,"f")

            def continue_red_20():
                main.card_red_20_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(5,"b")

            def continue_green_21():
                main.card_green_21_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(2,"f")

            def continue_green_22():
                main.card_green_22_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(1,"f")

            def continue_green_23():
                main.card_green_23_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(3,"f")

            def continue_green_24():
                main.card_green_24_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(2,"b")

            def continue_green_25():
                main.card_green_25_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(3,"f")

            def continue_green_26():
                main.card_green_26_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(1,"b")

            def continue_green_27():
                main.card_green_27_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(2,"f")

            def continue_green_28():
                main.card_green_28_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(3,"f")

            def continue_green_29():
                main.card_green_29_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(2,"b")

            def continue_green_30():
                main.card_green_30_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(3,"f")

            def continue_yellow_31():
                main.card_yellow_31_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(2,"f")

            def continue_yellow_32():
                main.card_yellow_32_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(3,"b")

            def continue_yellow_33():
                main.card_yellow_33_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(1,"f")

            def continue_yellow_34():
                main.card_yellow_34_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(3,"f")

            def continue_yellow_35():
                main.card_yellow_35_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(2,"b")

            def continue_yellow_36():
                main.card_yellow_36_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(3,"f")

            def continue_yellow_37():
                main.card_yellow_37_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(1,"b")

            def continue_yellow_38():
                main.card_yellow_38_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(3,"f")

            def continue_yellow_39():
                main.card_yellow_39_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(2,"f")

            def continue_yellow_40():
                main.card_yellow_40_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(3,"b")

            def continue_brown_41():
                main.card_brown_41_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(2,"b")

            def continue_brown_42():
                main.card_brown_42_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(3,"f")

            def continue_brown_43():
                main.card_brown_43_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(1,"b")

            def continue_brown_44():
                main.card_brown_44_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(3,"f")

            def continue_brown_45():
                main.card_brown_45_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(2,"f")

            def continue_brown_46():
                main.card_brown_46_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(3,"b")

            def continue_brown_47():
                main.card_brown_47_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(1,"f")

            def continue_brown_48():
                main.card_brown_48_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(3,"f")

            def continue_brown_49():
                main.card_brown_49_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(2,"b")

            def continue_brown_50():
                main.card_brown_50_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(3,"f")

            def continue_purple_51():
                main.card_purple_51_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(2,"f")

            def continue_purple_52():
                main.card_purple_52_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(3,"b")

            def continue_purple_53():
                main.card_purple_53_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(1,"f")

            def continue_purple_54():
                main.card_purple_54_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(3,"f")

            def continue_purple_55():
                main.card_purple_55_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(2,"b")

            def continue_purple_56():
                main.card_purple_56_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(3,"f")

            def continue_purple_57():
                main.card_purple_57_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(1,"b")

            def continue_purple_58():
                main.card_purple_58_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(3,"f")

            def continue_purple_59():
                main.card_purple_59_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(2,"f")

            def continue_purple_60():
                main.card_purple_60_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(3,"b")

            def continue_orange_61():
                main.card_orange_61_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(2,"f")

            def continue_orange_62():
                main.card_orange_62_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(3,"b")

            def continue_orange_63():
                main.card_orange_63_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(1,"f")

            def continue_orange_64():
                main.card_orange_64_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(3,"f")

            def continue_orange_65():
                main.card_orange_65_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(2,"b")

            def continue_orange_66():
                main.card_orange_66_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(3,"f")

            def continue_orange_67():
                main.card_orange_67_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(1,"b")

            def continue_orange_68():
                main.card_orange_68_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(3,"f")

            def continue_orange_69():
                main.card_orange_69_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(2,"f")

            def continue_orange_70():
                main.card_orange_70_frame.place_forget()
                main.game.place(relx=0,rely=0,relheight=1,relwidth=1)
                main.move_f_or_b(2,"f")

            # Assigning command functions to all buttons
            main.card_blue_1_continue.config(command=continue_blue_1)
            main.card_blue_2_continue.config(command=continue_blue_2)
            main.card_blue_3_continue.config(command=continue_blue_3)
            main.card_blue_4_continue.config(command=continue_blue_4)
            main.card_blue_5_continue.config(command=continue_blue_5)
            main.card_blue_6_continue.config(command=continue_blue_6)
            main.card_blue_7_continue.config(command=continue_blue_7)
            main.card_blue_8_continue.config(command=continue_blue_8)
            main.card_blue_9_continue.config(command=continue_blue_9)
            main.card_blue_10_continue.config(command=continue_blue_10)

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

            main.canvas_for_game.coords(main.player, x, y, x + 30, y + 30)

        
        # ===========================
        # BLUE CARD 1
        # ===========================
        main.card_blue_1_frame = tk.Frame(main.root, bg="white", bd=5, relief="ridge")
        main.card_blue_1_title = tk.Label(main.card_blue_1_frame,
                                        text="🌧 BLUE CARD",
                                        font=("Arial",20,"bold"),
                                        bg="white",
                                        fg="blue")
        main.card_blue_1_label_middle = tk.Label(main.card_blue_1_frame,
                                                text="Heavy rain helps you grow.",
                                                font=("Arial",16),
                                                bg="white")
        main.card_blue_1_label_middle_down = tk.Label(main.card_blue_1_frame,
                                                    text="Move forward 2 spaces.",
                                                    font=("Arial",14,"bold"),
                                                    bg="white",
                                                    fg="green")
        main.card_blue_1_continue = tk.Button(main.card_blue_1_frame,
                                            text="Continue")
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
                                                text="A river carries your seed safely.",
                                                font=("Arial",16),
                                                bg="white")
        main.card_blue_2_label_middle_down = tk.Label(main.card_blue_2_frame,
                                                    text="Move forward 3 spaces.",
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
                                                text="A gentle stream spreads your seeds.",
                                                font=("Arial",16),
                                                bg="white")
        main.card_blue_3_label_middle_down = tk.Label(main.card_blue_3_frame,
                                                    text="Move forward 2 spaces.",
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
        main.card_red_11_label_middle=tk.Label(main.card_red_11_frame,text="A bird eats your fruit and carries the seed.",font=("Arial",16),bg="white")
        main.card_red_11_label_middle_down=tk.Label(main.card_red_11_frame,text="Move forward 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_red_11_continue=tk.Button(main.card_red_11_frame,text="Continue")
        main.card_red_11_title.pack(pady=20)
        main.card_red_11_label_middle.pack(pady=20)
        main.card_red_11_label_middle_down.pack(pady=20)
        main.card_red_11_continue.pack(side="bottom",pady=20)

        main.card_red_12_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_red_12_title=tk.Label(main.card_red_12_frame,text="🍎 RED CARD",font=("Arial",20,"bold"),bg="white",fg="red")
        main.card_red_12_label_middle=tk.Label(main.card_red_12_frame,text="A squirrel buries your seed.",font=("Arial",16),bg="white")
        main.card_red_12_label_middle_down=tk.Label(main.card_red_12_frame,text="Move forward 2 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_red_12_continue=tk.Button(main.card_red_12_frame,text="Continue")
        main.card_red_12_title.pack(pady=20)
        main.card_red_12_label_middle.pack(pady=20)
        main.card_red_12_label_middle_down.pack(pady=20)
        main.card_red_12_continue.pack(side="bottom",pady=20)

        main.card_red_13_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_red_13_title=tk.Label(main.card_red_13_frame,text="🍎 RED CARD",font=("Arial",20,"bold"),bg="white",fg="red")
        main.card_red_13_label_middle=tk.Label(main.card_red_13_frame,text="An elephant drops your seed far away.",font=("Arial",16),bg="white")
        main.card_red_13_label_middle_down=tk.Label(main.card_red_13_frame,text="Move forward 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
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
        main.card_green_21_label_middle=tk.Label(main.card_green_21_frame,text="A strong wind carries your seed far away.",font=("Arial",16),bg="white")
        main.card_green_21_label_middle_down=tk.Label(main.card_green_21_frame,text="Move forward 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_green_21_continue=tk.Button(main.card_green_21_frame,text="Continue")
        main.card_green_21_title.pack(pady=20)
        main.card_green_21_label_middle.pack(pady=20)
        main.card_green_21_label_middle_down.pack(pady=20)
        main.card_green_21_continue.pack(side="bottom",pady=20)

        main.card_green_22_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_green_22_title=tk.Label(main.card_green_22_frame,text="🌿 GREEN CARD",font=("Arial",20,"bold"),bg="white",fg="green")
        main.card_green_22_label_middle=tk.Label(main.card_green_22_frame,text="Your winged seed glides safely.",font=("Arial",16),bg="white")
        main.card_green_22_label_middle_down=tk.Label(main.card_green_22_frame,text="Move forward 2 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
        main.card_green_22_continue=tk.Button(main.card_green_22_frame,text="Continue")
        main.card_green_22_title.pack(pady=20)
        main.card_green_22_label_middle.pack(pady=20)
        main.card_green_22_label_middle_down.pack(pady=20)
        main.card_green_22_continue.pack(side="bottom",pady=20)

        main.card_green_23_frame=tk.Frame(main.root,bg="white",bd=5,relief="ridge")
        main.card_green_23_title=tk.Label(main.card_green_23_frame,text="🌿 GREEN CARD",font=("Arial",20,"bold"),bg="white",fg="green")
        main.card_green_23_label_middle=tk.Label(main.card_green_23_frame,text="A breeze lifts your seed over a hill.",font=("Arial",16),bg="white")
        main.card_green_23_label_middle_down=tk.Label(main.card_green_23_frame,text="Move forward 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
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
        main.card_brown_50_label_middle=tk.Label(main.card_brown_50_frame,text="An animal helps your seed find a perfect home.",font=("Arial",16),bg="white")
        main.card_brown_50_label_middle_down=tk.Label(main.card_brown_50_frame,text="Move forward 3 spaces.",font=("Arial",14,"bold"),bg="white",fg="green")
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
        main.rolldicebutton = tk.Button(main.canvas_for_game,command=rolldicebuttoncommand,text="Roll Dice", font=("Arial",20),bg="black",fg="white",activebackground="black",activeforeground="white")
        main.rolldicebutton.place(x=10, y=10)
        main.player_position = 0
        main.player = main.canvas_for_game.create_oval(135, 185, 165, 215,fill="#402c03",outline="black",width=2)
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

        
window=tk.Tk()
game=SeedAdventure(window)
window.geometry("1000x1000")
window.title("Journey of a seed game")
window.resizable(False, False)
game.show_menu()
window.mainloop()