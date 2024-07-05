# Handling methods sent by buttons
def clicked(value, num):

	# Prevent closing bracket insertion if there is no corresponding open bracket
	if (num.number_to_calculate.count("(") <= num.number_to_calculate.count(")") and value == ")"):
		num.display_error()
		return

	# Prevent insertion of multiplication / devision to an empty field
	elif(num.number_to_calculate == "" and (value == "/" or value == "*")):
		return

	# Prevent devision by zero
	elif (num.number_to_calculate == "" or num.number_to_calculate == "0") and value == "/":
		num.display_error()
		return

	elif value != "erase" and value != "Ans" and value != "=" and value != "undo" and value != "(" and value != ".":
		# Prevent calculating powers
		if value == "*" and num.operation_array[-1] == "*":
			return
		numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

		# Prefix enclosure of bracket with multiplication if necessary
		if len(num.number_to_calculate) > 0 and num.number_to_calculate[-1] == ")" and value in numbers:
			num.number_to_calculate += "*"
		num.number_to_calculate += value
		num.operation_array.append(value)
		num.display_result()

	# Calculating the equation
	elif value == "=":
		num.number_to_calculate = eval(num.number_to_calculate)
		num.number_to_calculate = str(num.number_to_calculate)
		if ("." in num.number_to_calculate and num.number_to_calculate[-1] == "0" and len(num.number_to_calculate) > 2):

			# Prevent display of too many unnecessary zeroes
			while(num.number_to_calculate[-1] == "0"):
				num.number_to_calculate = num.number_to_calculate[:-1]
				if num.number_to_calculate[-1] == "." and len(num.number_to_calculate) > 2:
					num.number_to_calculate = num.number_to_calculate[:-1]
		num.operation_array = []
		num.operation_array.extend(["=", num.number_to_calculate])
		num.display_result()
		num.number_to_calculate = ""

	# Storing previous result
	elif value == "Ans":
		if "=" in num.operation_array:
			Answer = num.operation_array[1]
		else:
			Answer = "0"
		if num.number_to_calculate == "0":
			num.number_to_calculate = Answer
		else:
			num.number_to_calculate += Answer
		num.operation_array.append(Answer)
		num.display_result()

	# Backing previous operation
	elif value == "undo":
		if len(num.operation_array) >= 0 and num.operation_array[0] != "=":
			num.operation_array.pop(-1)
			num.number_to_calculate = num.number_to_calculate[:-1]
		elif num.operation_array[0] == "=" and len(num.operation_array) > 2:
			if num.operation_array[1] == num.operation_array[2] == num.number_to_calculate:
				num.operation_array.pop(-1)
				num.number_to_calculate = ""
			else: 
				num.number_to_calculate = num.number_to_calculate[:-1]
		num.display_result()

	# Erasing entire equation but storing previous result
	elif value == "erase":
		if "=" in num.operation_array:
			Answer = num.operation_array[1]
		else: 
			Answer = 0
		num.number_to_calculate = ""
		num.operation_array = num.operation_array[:2]
		num.display_result()
	elif value == "(":
		operations = ["+", "-", "/", "*"]
		if len(num.number_to_calculate) > 0 and num.number_to_calculate[-1] not in operations and num.number_to_calculate[-1] != ".":
			num.number_to_calculate += "*("
		else:
			num.number_to_calculate += value
		num.display_result()

	# Decimal point insertion logic
	elif value == ".":
		operations = ["+", "-", "/", "*"]
		continuity = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
		highest = 0
		highest_dot = 0
		idx = 0
		finder = ""
		if "." in num.number_to_calculate:
			finder = num.number_to_calculate.rfind(".")
			if finder > highest_dot:
				highest_dot = finder

		for iter in range(4):
			if operations[iter] in num.number_to_calculate:
				idx = num.number_to_calculate.rfind(operations[iter])
				if idx > highest:
					highest = idx
		if "." in num.number_to_calculate and highest_dot >= highest:
			return
		else:
			num.operation_array.append(value)
			num.number_to_calculate += value
			num.display_result()
