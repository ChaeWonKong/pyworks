"""Times Table"""


while True:
	val = input("Input number between 2, 9, 'q' for quit >>")
	if val == 'q':
		break
	elif val.isnumeric():
		val = int(val)
		if val >= 2 and val <= 9:
			for i in range(1, 10):
				print(str(val) + " * " + str(i) + " = " + str(val*i))
		else:
			print("Wrong number... Try again!")
	else:
		print("Input number between 2 and 9 or 'q' for quit!")
	
print("Bye Bye")