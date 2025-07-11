from tkinter import *


def timer(h, mins, sec, board, GUI):
    GUI.gui_board.delete("timer_display")
    GUI.gui_board.create_text(500, 60, text=('Time spent: ' + str(h) + ':' + str(mins) + ':' + str(sec)), font =('Arial', 30), fill = 'cyan', tag="timer_display")
    seconds = int(sec)
    minutes = int(mins)
    hours = int(h)
    if (GUI.freeze == False):
        seconds += 1
        if seconds >= 60:
            seconds = 0
            minutes += 1
        if minutes >= 60:
            minutes = 0
            hours += 1
        if seconds < 10:
            sec = '0' + str(seconds)
        elif seconds >= 10:
            sec = seconds
        if minutes < 10:
            mins = '0' + str(minutes)
        elif minutes >= 10:
            mins = minutes
        if hours < 10:
            h = '0' + str(hours)
        elif hours >= 10:
            h = hours
        if hours >= 24:
            GUI.gui_board.delete("timer_display")
            GUI.gui_board.create_text(500, 60, text=('Please, stop playing it, life is too precious'), font =('Arial', 15), fill = 'cyan', tag="timer_display")
    if board.game_over == False:
        GUI.root.after(1000, lambda: timer(h, mins, sec, board, GUI))

