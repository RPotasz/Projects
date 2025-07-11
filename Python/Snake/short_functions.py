import sys
import os

from tkinter import *


def freezing(GUI):
    GUI.click += 1
    GUI.switch_images()

def exit_game():
    quit()


def replay_game(GUI, waiting):
    while waiting > -1:
        GUI.freeze = True
        GUI.gui_board.delete('all')
        GUI.exit_button.destroy()
        GUI.replay_button.destroy()
        GUI.pause_button.destroy()
        GUI.gui_board.create_text(350, 375, text=('Reruning the game in: ' + str(waiting)), font =('Halvetica', 30), fill='white')
        GUI.gui_board.update()
        waiting -= 1
        GUI.root.after(1000, lambda: replay_game(GUI, waiting))
        return
    if waiting < 0:
        os.execv(sys.executable, ['python'] + sys.argv)


def left_key_pressed(event, position, GUI):
    if GUI.freeze == False:
        position.x = 0
        position.y = -1

def right_key_pressed(event, position, GUI):
    if GUI.freeze == False:
        position.x = 0
        position.y = 1

def up_key_pressed(event, position, GUI):
    if GUI.freeze == False:
        position.y = 0
        position.x = -1

def down_key_pressed(event, position, GUI):
    if GUI.freeze == False:
        position.y = 0
        position.x = 1


def display_announcement(announcement, color, position, GUI):
    GUI.gui_board.create_text(349, 375, text=announcement, font =('Halvetica', 100), fill='white', angle=45)
    GUI.gui_board.create_text(351, 375, text=announcement, font =('Halvetica', 100), fill='white', angle=45)
    GUI.gui_board.create_text(350, 374, text=announcement, font =('Halvetica', 100), fill='white', angle=45)
    GUI.gui_board.create_text(350, 376, text=announcement, font =('Halvetica', 100), fill='white', angle=45)
    GUI.gui_board.create_text(350, 375, text=announcement, font =('Halvetica', 100), fill=color, angle=45)
    if position.length > position.high_score:
        position.high_score = position.length
        file = open("Score/High_score.txt", "w")
        file.write(str(position.high_score))
        file.close()
    GUI.create_exit_button()
    GUI.create_replay_button()