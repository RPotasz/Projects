from tkinter import *
from pong_singleplayer import *
from pong_multiplayer import *

class parameters:
	def __init__(self, height, points):
		self.height = height
		self.points = points

class ball_parameters:
	def __init__(self, ball_height, ball_width, velocity_x, velocity_y):
		self.ball_height = ball_height
		self.ball_width = ball_width
		self.velocity_x = velocity_x
		self.velocity_y = velocity_y

# Function to call pong_singleplayer
def singleplayer_chosen(root, board, parameters, ball_parameters):
	board.delete("options")
	button1.destroy()
	button2.destroy()
	singleplayer(root, board, parameters, ball_parameters)

# Function to call pong_multiplayer
def multiplayer_chosen(root, board, parameters, ball_parameters):
	board.delete("options")
	button1.destroy()
	button2.destroy()
	multiplayer(root, board, parameters, ball_parameters)

# Main window GUI
root = Tk()
root.title("Pong")
board = Canvas(root, height = 750, width = 1200, bg = "black", highlightthickness=0)
board.create_rectangle(40, 325, 50, 425, fill="white", tag='player')
board.create_rectangle(1150, 325, 1160, 425, fill="white", tag="enemy")
board.create_rectangle(0, 0, 1200, 10, fill='white')
board.create_rectangle(0, 740, 1200, 750, fill='white')
board.create_rectangle(595, 0, 605, 750, fill='white')
board.create_rectangle(400, 250, 800, 500, outline = "gray", width=5, fill="white", tag='options')
button1 = Button(root, text = 'Singleplayer', width = 10, height = 2, command = lambda: singleplayer_chosen(root, board, parameters, ball_parameters), activebackground='white', activeforeground='red', bd=5, padx = 95, pady = 10)
button1.place(x = 440, y = 300)
button2 = Button(root, text = 'Multiplayer', width = 10, height = 2, command = lambda: multiplayer_chosen(root, board, parameters, ball_parameters), activebackground='white', activeforeground='blue', bd=5, padx = 95, pady = 10)
button2.place(x = 440, y = 375)
board.pack()
root.mainloop()