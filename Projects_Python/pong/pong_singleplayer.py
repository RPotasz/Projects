from tkinter import *
import random
import copy

def singleplayer(root, board, parameters, ball_parameters):

	class control:
		def __init__(self, waiting):
			self.waiting = waiting

	# Initializing players' points 
	board.create_text(550, 50, text='0', font =('Halvetica', 80), fill="blue", tag="player_score")
	board.create_text(650, 50, text='0', font =('Halvetica', 80), fill="red", tag="enemy_score")

	# Control / movement functions
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

	def move_up(enemy, follow):
		board.delete("enemy")
		enemy.height -= 40
		board.create_rectangle(1150, enemy.height, 1160, enemy.height + 100, fill="white", tag='enemy')

	def move_down(enemy, follow):
		board.delete("enemy")
		enemy.height += 40
		board.create_rectangle(1150, enemy.height, 1160, enemy.height + 100, fill="white", tag='enemy')

	# The ball movement logic
	def ball(trajectory, player, enemy, computer_player):
		board.delete("ball")
		trajectory.ball_width += trajectory.velocity_x
		trajectory.ball_height += trajectory.velocity_y

		# Check if the ball is in-between the play field y coordinates
		if trajectory.ball_height > 10 and trajectory.ball_height < 720:
			# Collision with players logic
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
				trajectory.ball_height = 20
			if trajectory.ball_height > 720:
				trajectory.ball_height = 720
			trajectory.velocity_y = -trajectory.velocity_y
		board.create_oval(trajectory.ball_width, trajectory.ball_height, trajectory.ball_width + 20, trajectory.ball_height + 20, fill='green', outline='', tag='ball')
		
		# Program controlled player logic
		follow = copy.deepcopy(trajectory)
		if follow.velocity_x > 0:

			# Find interception position, use pretty much the same logic as for ball movement
			while(follow.ball_width < 1130):
				if follow.ball_height > 10 and follow.ball_height < 720:
					if follow.ball_height < 10:
						follow.ball_height = 20
					if follow.ball_height > 720:
						follow.ball_height = 720
				if trajectory.ball_height < 10 or follow.ball_height > 720:
					follow.velocity_y = -follow.velocity_y
				follow.ball_height = follow.ball_height + follow.velocity_y
				follow.ball_width = follow.ball_width + follow.velocity_x
		# Correct position if necessary
		if (abs(follow.ball_height) - 20 < enemy.height and enemy.height > 10 and trajectory.velocity_x) > 0:
			computer_player.waiting += 1

			# Slow down the computer player
			if computer_player.waiting %8 == 0:
				root.after(1, lambda: move_up(enemy, follow))
		if (abs(follow.ball_height) - 80 > enemy.height and enemy.height < 640 and trajectory.velocity_x > 0):
			computer_player.waiting += 1
			if computer_player.waiting %8 == 0:
				root.after(1, lambda: move_down(enemy, follow))


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
		computer_player = control(0)
		random_x = random.randint(3, 7)
		random_y = random.randint(2, 5)
		if random.randint(0, 1) == 0:
			random_x = - random_x
		if random.randint(0, 1) == 0:
			random_y = - random_y
		trajectory = ball_parameters(365, 590, random_x, random_y)
		return player, enemy, trajectory, computer_player

	# main loop
	def listen_single(player, enemy, trajectory, computer_player):
		root.bind("<Down>", lambda event: down(event, player))
		root.bind("<Up>", lambda event: up(event, player))
		root.after(5, lambda: ball(trajectory, player, enemy, computer_player))
		root.after(15, lambda: listen_single(player, enemy, trajectory, computer_player))

	player, enemy, trajectory, computer_player = initialize_parameters()
	listen_single(player, enemy, trajectory, computer_player)