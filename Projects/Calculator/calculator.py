from tkinter import *
from logic import *

b_width = 15
b_height = 10
x_dist = 15
y_dist = 50

class number:
	def __init__(self, number_to_calculate, operation_array, answer):
		self.number_to_calculate = number_to_calculate
		self.operation_array = operation_array
		self.answer = answer
	def display_result(self):
		background.delete("calc")
		background.create_text(40 + 5*(len(num.number_to_calculate)), 26, text=self.number_to_calculate, font =('Halvetica', 20), fill="black", tag="calc")
	def display_error(self):
		background.delete("calc")
		background.create_text(40 + 45, 26, text="Incorrect input", font =('Halvetica', 20), fill="Red", tag="calc")
		root.after(1500, self.display_result)

# setting up GUI
root = Tk()
root.title("Calculator")
root.geometry("310x360")
root.resizable(False, False)
background = Canvas(root, height = 360, width = 310, bg = "black", highlightthickness=0)
background.create_rectangle(16, 10, 292, 45, fill="white", outline="gold")

num = number("", [], "")
j = 0
vertical = 1
name = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "left_bracket", "zero", "right_bracket", "erase", "undo", "dot"]
action = ["(", "0", ")", "erase", "undo", "."]

# Initializing buttons 
for i in range(1, 16):
	if i < 10:
		element = str(i)
	else: 
		element = str(action[i - 10])
	name[i] = Button(root, text = element, width = 1, command = lambda element = element: clicked(element, num), activebackground='white', activeforeground='red', padx = b_width, pady = b_height)
	name[i].place(x = x_dist + 75 * (i - vertical), y = y_dist + 50 * (j))
	if (i %3 == 0):
		j += 1
		vertical += 3

# Most right-hand buttons
operations_names = ["add", "subtract", "multiply", "devide", "calcualte"]
signs = ["+", "-", "*", "/", "="]
for iterate in range(5):
	operation = str(signs[iterate])
	operations_names[iterate] = Button(root, text = operation, width = 1, command = lambda operation = operation: clicked(operation, num), activebackground='white', activeforeground='red', padx = b_width - 10, pady = b_height)
	operations_names[iterate].place(x=x_dist + 225, y=y_dist + 50 *(iterate))

# Answer button
Ans = Button(root, text = 'Ans', width = 4, command = lambda: clicked("Ans", num), activebackground='white', activeforeground='red', padx = 104, pady = b_height)
Ans.place(x=x_dist, y=y_dist + 250)

background.pack()
root.mainloop()