import random

from tkinter import *
from playsound import playsound


class apple_handling:
    def __init__(self, on_board, apple_x, apple_y):
        self.on_board = on_board
        self.apple_x = apple_x
        self.apple_y = apple_y


apple = apple_handling(False, -10, -10)

def apple_sound():
    playsound("sounds/snake_apple_eating_sound.m4a")


def apple_generator(board, GUI, apple, time_until):
    if GUI.freeze == False:
        GUI.gui_board.delete("time_left")
        while time_until > 0:
            if GUI.freeze == False:
                GUI.gui_board.create_text(450, 725, text=('Apple generation in [' + str(time_until)) + "]", font =('Arial', 30), fill ='cyan', tag="time_left")
                time_until -= 1
                GUI.root.after(1000, lambda: apple_generator(board, GUI, apple, time_until))
                return
        if board.game_over == False:
            # Generate apple if there is none, prevent spawning on snake coordinates
            if apple.on_board == False:
                apple.apple_x = random.randint(0, 9)
                apple.apple_y = random.randint(1, 10)
                while board.coordinates[apple.apple_x][apple.apple_y] == ' O ' or board.coordinates[apple.apple_x][apple.apple_y] == ' o ':
                    apple.apple_x = random.randint(0, 9)
                    apple.apple_y = random.randint(1, 10)
                board.coordinates[apple.apple_x][apple.apple_y] = ' + '
                apple.on_board = True
            else:
                return 
        if time_until == 0:
            GUI.gui_board.delete("time_left")
            GUI.gui_board.create_text(450, 725, text=('Apple generation in [' + str(time_until)) + "]", font =('Arial', 30), fill ='cyan', tag="time_left")
            GUI.root.after(1000, lambda: apple_generator(board, GUI, apple, 0))
    # Stop timer and wait for unfreezing
    elif GUI.freeze == True:
        GUI.root.after(1000, lambda: apple_generator(board, GUI, apple, time_until))
        return