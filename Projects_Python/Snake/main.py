import threading
import random

from playsound import playsound
from tkinter import *

from short_functions import *
from apple_control import *
from timer import *


class map_blueprint:
    def __init__(self, coordinates, game_over):
        self.coordinates = coordinates
        self.game_over = game_over


class map_gui(map_blueprint):
    def __init__(self, root, gui_board, start_button, pause_button, freeze):
        self.root = root
        self.gui_board = gui_board
        self.start_button = start_button
        self.pause_button = pause_button
        self.freeze = freeze

    def create_pause_button(self):
        self.click = 0
        pause_button_image = PhotoImage(file='Images/pause_button.png')
        label = Label(image=pause_button_image)
        label.image = pause_button_image
        self.pause_button = Button(GUI.root, image=pause_button_image, width=50, height=50, command = lambda: freezing(self))
        self.pause_button.place(x=600, y=705)

    def switch_images(self):
        if self.click %2 == 0:
            self.freeze = False
            pause_button_image = PhotoImage(file='Images/pause_button.png')
            label = Label(image=pause_button_image)
            label.image = pause_button_image
            self.pause_button.config(image=pause_button_image)
            self.click = 0
        elif self.click %2 == 1:
            self.freeze = True
            resume_button_image = PhotoImage(file='Images/resume_button.png')
            label = Label(image=resume_button_image)
            label.image = resume_button_image
            self.pause_button.config(image=resume_button_image)

    def create_exit_button(self):
            exit_button_image = PhotoImage(file="Images/exit.png")
            label = Label(image=exit_button_image)
            label.image = exit_button_image
            self.exit_button = Button(GUI.root, image=exit_button_image, width=50, height=50, command=exit_game)
            self.exit_button.place(x=430, y=350)

    def create_replay_button(self):
            replay_button_image = PhotoImage(file="Images/replay.png")
            label = Label(image=replay_button_image)
            label.image = replay_button_image
            self.replay_button = Button(GUI.root, image=replay_button_image, width=50, height=50, command=lambda: replay_game(self, 3))
            self.replay_button.place(x=375, y=405)


class snake_position:
    def __init__(self, x, y, present_x, present_y, iter_x1, iter_y1, length, high_score):
        self.x = x
        self.y = y
        self.present_x = present_x
        self.present_y = present_y
        self.iter_x1 = iter_x1
        self.iter_y1 = iter_y1
        self.length = length
        self.high_score = high_score


def initalize():
    y = random.randint(-1, 1)
    x = random.randint(-1, 1)
    if abs(x) == abs(y):
        while abs(x) == abs(y):
            y = random.randint(-1, 1)
            x = random.randint(-1, 1)
    check = os.path.isfile("Score/High_score.txt")
    if check == True:
        high_score = open("Score/High_score.txt", "r").read()
        high_score = int(high_score)
    else:
        high_score = 0
    present_x = []
    present_y = []
    iter_x1 = []
    iter_y1 = []
    position = snake_position(x, y, present_x, present_y, iter_x1, iter_y1, 1, high_score)
    return position


position = initalize()


def define_map():
    a = ['X'] + ['   '] * 10 + ['X']
    b = ['X'] + ['   '] * 10 + ['X']
    c = ['X'] + ['   '] * 10 + ['X']
    d = ['X'] + ['   '] * 10 + ['X']
    e = ['X'] + ['   '] * 10 + ['X']
    f = ['X'] + ['   '] * 10 + ['X']
    g = ['X'] + ['   '] * 10 + ['X']
    h = ['X'] + ['   '] * 10 + ['X']
    i = ['X'] + ['   '] * 10 + ['X']
    j = ['X'] + ['   '] * 10 + ['X']
    map_board = [a, b, c, d, e, f, g, h, i, j]
    board = map_blueprint(map_board, False)
    return board


def define_gui():
    root = Tk()
    root.title('Snake')
    gui_board = Canvas(root, width=750, height=800, bg='blue', highlightthickness=0)
    start_button = Button(root, text = 'Start the game', width = 12, height = 4, command = lambda: start(board, GUI, position, apple), activebackground='black', activeforeground='green', bd=5, padx = 76, pady = 10)
    start_button.place(x=200, y=350)
    gui = map_gui(root, gui_board, start_button, 0, False)
    for j in range(12):
        for i in range(-1, 11):
            if j == 0 or j == 11 or i == -1 or i == 10:
                gui_board.create_rectangle(100 + (i * 50), 100 + (j * 50), (i * 50) + 150, (j * 50) + 150, fill='blue')
    for j in range(1, 11):
        for i in range(10):
            gui_board.create_rectangle(100 + (i * 50), 100 + (j * 50), (i * 50) + 150, (j * 50) + 150, fill='brown', tag ="playfield")
    gui_board.pack()
    return gui


GUI = define_gui()
board = define_map()


def display_board(current_number, current_letter, board, position, GUI):
    if position.length >= 99:
        display_announcement('You won!', 'Green', position, GUI)
        board.game_over = True
        return
    if board.coordinates[current_letter][current_number] == ' o ':
        board.game_over = True
        playsound("sounds/snake_wall_hitting_sound.m4a")
        display_announcement('You lost', 'red', position, GUI)
        return
    if board.game_over == False:
        iter = 1
        if position.length > 1:
            for iter in range(position.length - 1):
                iter_x = position.y
                iter_y = position.x
                x_new = current_number - iter_y
                y_new = current_letter - iter_x
                position.iter_x1[-1] = x_new
                position.iter_y1[-1] = y_new
                board.coordinates[current_letter - position.y][current_number - position.x] = ' o '
                board.coordinates[current_letter][current_number] = ' O '
        if position.length == 1:
            board.coordinates[current_letter][current_number] = ' O '
        bond = len(position.present_x)
        GUI.gui_board.delete("playfield")
        for j in range(12):
            for i in range(-1, 11):
                if j == 0 or j == 11 or i == -1 or i == 10:
                    GUI.gui_board.create_rectangle(100 + (i * 50), 100 + (j * 50), (i * 50) + 150, (j * 50) + 150, fill='blue', tag="playfield")
        for j in range(1, 11):
            for i in range(10):
                if board.coordinates[i][j] == '   ':
                    GUI.gui_board.create_rectangle(100 + (i * 50), 100 + (j * 50), (i * 50) + 150, (j * 50) + 150, fill='brown', tag="playfield")
                if board.coordinates[i][j] == ' + ':
                    GUI.gui_board.create_rectangle(100 + (i * 50), 100 + (j * 50), (i * 50) + 150, (j * 50) + 150, fill='orange', tag="playfield")
                    apple_photo = PhotoImage(file="Images/apple.png")
                    label = Label(image=apple_photo)
                    label.image = apple_photo
                    GUI.gui_board.create_image(125 + (i * 50), 125 + (j * 50), image=apple_photo)
                if board.coordinates[i][j] == ' O ':
                    GUI.gui_board.create_rectangle(100 + (i * 50), 100 + (j * 50), (i * 50) + 150, (j * 50) + 150, fill='black', tag="playfield")
                if board.coordinates[i][j] == ' o ':
                    GUI.gui_board.create_rectangle(100 + (i * 50), 100 + (j * 50), (i * 50) + 150, (j * 50) + 150, fill='green', tag="playfield")
        GUI.gui_board.pack()
        if position.length > 1:
            for iter in range(bond):
                board.coordinates[position.present_y[-position.length]][position.present_x[-position.length]] = '   '
                position.present_x = position.present_x[-position.length:]
                position.present_y = position.present_y[-position.length:]
        if position.length == 1:
            board.coordinates[current_letter][current_number] = '   '
        GUI.gui_board.create_text(160, 60, text=(('snake length: ') + str(position.length)), font =('Arial', 30), fill = 'cyan', tag="playfield")
        GUI.gui_board.create_text(160, 725, text=(('High Score: ') + str(position.high_score)), font=('Arial', 30), fill='cyan', tag="high_score")
        if position.length > position.high_score:
            GUI.gui_board.delete("high_score")
            GUI.gui_board.create_text(160, 725, text=(('High Score: ') + str(position.length)), font=('Arial', 30), fill='cyan', tag="high_score")
        GUI.gui_board.pack()
        main(board, GUI, current_number, current_letter, position, apple)

def process_movement(board, GUI, current_number, current_letter, position, apple):
    if apple.on_board == True and apple.apple_y == current_number and apple.apple_x == current_letter:
        position.length += 1
        apple.on_board = False
        threading.Thread(target=apple_sound).start()
        threading.Thread(target = apple_generator, args=(board, GUI, apple, 3)).start()
        position.iter_y1.append('')
        position.iter_x1.append('')
        board.coordinates[apple.apple_x][apple.apple_y] = ' o '
        iter_x = position.y
        iter_y = position.x
    if position.x == 1:
        current_number += 1
    if position.x == -1:
        current_number -= 1
    if position.y == 1:
        current_letter += 1
    if position.y == -1:
        current_letter -= 1
    if current_number <= 0 or current_number > 10 or current_letter < 0 or current_letter >= 10:
        board.game_over = True
        playsound("sounds/snake_wall_hitting_sound.m4a")
        display_announcement('You lost', 'red', position, GUI)
        return
    position.present_y.append(current_letter)
    position.present_x.append(current_number)
    display_board(current_number, current_letter, board, position, GUI)


def main(board, GUI, current_number, current_letter, position, apple):
    if GUI.freeze == True:
        GUI.root.after(250, lambda: main(board, GUI, current_number, current_letter, position, apple)) 
    GUI.root.bind("<Left>", lambda event: left_key_pressed(event, position, GUI))
    GUI.root.bind("<Right>", lambda event: right_key_pressed(event, position, GUI))
    GUI.root.bind("<Up>", lambda event: up_key_pressed(event, position, GUI))
    GUI.root.bind('<Down>', lambda event: down_key_pressed(event, position, GUI))
    GUI.root.bind("<a>", lambda event: left_key_pressed(event, position, GUI))
    GUI.root.bind("<d>", lambda event: right_key_pressed(event, position, GUI))
    GUI.root.bind("<w>", lambda event: up_key_pressed(event, position, GUI))
    GUI.root.bind('<s>', lambda event: down_key_pressed(event, position, GUI))
    if GUI.freeze == False:
        GUI.root.after(250, lambda: process_movement(board, GUI, current_number, current_letter, position, apple))


def start(board, GUI, position, apple):
    GUI.start_button.destroy()
    GUI.create_pause_button()
    threading.Thread(target = timer, args=("00", "00", "00", board, GUI,)).start()
    threading.Thread(target = main, args=(board, GUI, 4, 4, position, apple)).start()
    threading.Thread(target = apple_generator, args=(board, GUI, apple, 3)).start()


GUI.root.mainloop()