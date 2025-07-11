from tkinter import *
import random

def multiplayer(root, board, parameters, ball_parameters):

	# Initializing players' points 
	board.create_text(550, 50, text='0', font =('Halvetica', 80), fill="blue", tag="player_score")
	board.create_text(650, 50, text='0', font =('Halvetica', 80), fill="red", tag="enemy_score")

	# Control functions
	def down(event, player):
		board.delete("player")
		if player.height < 640:
			player.height += 40
		board.create_rectangle(40, player.height, 50, player.height + 100, fill="white", tag='player')

	def up(event, player):
		board.delete("player")
		if player.height > 10:
			player.height -= 40
		board.create_rectangle(40, player.height, 50, player.height + 100, fill="white", tag='player')

	def W(event, enemy):
		board.delete("enemy")
		if enemy.height < 640:
			enemy.height += 40
		board.create_rectangle(1150, enemy.height, 1160, enemy.height + 100, fill="white", tag='enemy')

	def S(event, enemy):
		board.delete("enemy")
		if enemy.height > 10:
			enemy.height -= 40
		board.create_rectangle(1150, enemy.height, 1160, enemy.height + 100, fill="white", tag='enemy')

	# The ball movement logic
	def ball(trajectory, player, enemy):
		board.delete("ball")
		trajectory.ball_width += trajectory.velocity_x
		trajectory.ball_height += trajectory.velocity_y

		# Check if the ball is in-between the play field y coordinates
		if trajectory.ball_height > 10 and trajectory.ball_height < 720:

			# Collision with player logic
			if(trajectory.ball_height + 20 > player.height and trajectory.ball_height < player.height + 100 and trajectory.ball_width < 50 and trajectory.ball_width > 30):
				if trajectory.ball_width < 50:
					trajectory.ball_width = 50
				if (trajectory.ball_height + 20 > player.height - 30) or  (trajectory.ball_height < player.height + 30):
					if (trajectory.ball_height + 20 > player.height - 10) or  (trajectory.ball_height < player.height + 10):
						if trajectory.velocity_y < 0:
							root.after(0)
							trajectory.velocity_y -= 1
						else: 
							root.after(0)
							trajectory.velocity_y += 1
					if trajectory.velocity_x < 0:
						root.after(0)
						trajectory.velocity_x = - (trajectory.velocity_x - 1)
					else: 
						root.after(0)
						trajectory.velocity_x = - (trajectory.velocity_x + 1)
				else:
					root.after(0)
					trajectory.velocity_x = - trajectory.velocity_x
			if(trajectory.ball_height + 20 > enemy.height and trajectory.ball_height < enemy.height + 100 and trajectory.ball_width > 1130 and trajectory.ball_width < 1150):
				if trajectory.ball_width > 1130:
					trajectory.ball_width = 1130
				if (trajectory.ball_height + 20 > enemy.height - 30) or  (trajectory.ball_height < enemy.height + 30):
					if (trajectory.ball_height + 20 > enemy.height - 10) or  (trajectory.ball_height < enemy.height + 10):
						if trajectory.velocity_y < 0:
							root.after(0)
							trajectory.velocity_y -= 1
						else: 
							trajectory.velocity_y += 1
					if trajectory.velocity_x < 0:
						root.after(0)
						trajectory.velocity_x = - (trajectory.velocity_x - 1)
					else: 
						trajectory.velocity_x = - (trajectory.velocity_x + 1)
				else:
					root.after(0)
					trajectory.velocity_x = - trajectory.velocity_x

			# Check for goal
			elif trajectory.ball_width < 0:
				board.create_text(615, 350, text="Player scored", font =('Halvetica', 100), fill="Red", tag="Player_point")
				root.after(500, lambda: wait())
				root.after(0, lambda: reinitialize(player, enemy, trajectory, True, 100))
			elif trajectory.ball_width > 1200:
				board.create_text(615, 350, text="Player scored", font =('Halvetica', 100), fill="Blue", tag="Player_point")
				root.after(500, lambda: wait())
				root.after(0, lambda: reinitialize(player, enemy, trajectory, False, 1100))

		# Change direction if ball is not within y coordinates of the play field
		if trajectory.ball_height < 10 or trajectory.ball_height > 720:
			if trajectory.ball_height < 10:
				trajectory.ball_height = 25
			if trajectory.ball_height > 720:
				trajectory.ball_height = 720
			trajectory.velocity_y = -trajectory.velocity_y
		board.create_oval(trajectory.ball_width, trajectory.ball_height, trajectory.ball_width + 20, trajectory.ball_height + 20, fill='green', outline='', tag='ball')

	def wait():
		board.delete("Player_point")
		return

	# update variables after goal
	def reinitialize(player, enemy, trajectory, direction_x, width):
		player.height = 325
		enemy.height = 325
		trajectory.ball_height = 365
		random_x = random.randint(3, 7)
		random_y = random.randint(2, 5)
		if direction_x == False:
			random_x = - random_x
			enemy.points += 1
		else: 
			player.points += 1
		if random.randint(0, 1) == 0:
			random_y = - random_y
		trajectory.ball_width = width
		trajectory.velocity_x = random_x
		trajectory.velocity_y = random_y
		player_point_width = 550
		enemy_point_width = 650
		if player.points > 10:
			score = player.points
			while score > 10:
				score /= 10
				if player_point_width > 0:
					player_point_width -= 30
		if enemy.points > 10:
			score = enemy.points
			while score > 10:
				score /= 10
				if enemy_point_width < 1200:
					enemy_point_width += 30
		board.delete("player")
		board.delete("enemy")
		board.delete("player_score")
		board.delete("enemy_score")
		board.create_text(player_point_width, 50, text=enemy.points, font =('Halvetica', 80), fill="blue", tag="player_score")
		board.create_text(enemy_point_width, 50, text=player.points, font =('Halvetica', 80), fill="red", tag="enemy_score")
		board.create_rectangle(40, 325, 50, 425, fill="white", tag='player')
		board.create_rectangle(1150, 325, 1160, 425, fill="white", tag="enemy")

	def initialize_parameters():
		player = parameters(325, 0)
		enemy = parameters(325, 0)
		random_x = random.randint(3, 7)
		random_y = random.randint(2, 5)
		if random.randint(0, 1) == 0:
			random_x = - random_x
		if random.randint(0, 1) == 0:
			random_y = - random_y
		trajectory = ball_parameters(365, 590, random_x, random_y)
		return player, enemy, trajectory

	# main loop
	def listen(player, enemy, trajectory):
		root.bind("<Down>", lambda event: down(event, player))
		root.bind("<Up>", lambda event: up(event, player))
		root.bind("<w>", lambda event: S(event, enemy))
		root.bind("<s>", lambda event: W(event, enemy))
		root.after(5, lambda: ball(trajectory, player, enemy))
		root.after(15, lambda: listen(player, enemy, trajectory))

	player, enemy, trajectory = initialize_parameters()
	listen(player, enemy, trajectory)