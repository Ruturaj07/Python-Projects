age = input("What is your age : ")

if age:
	age = int(age)
	if age >=21 :
		print("You are allowed to Drink!")
	elif age >=18 :
		print("Party's waiting for you, but make sure not to Drink!!")
	else :
		print("Too young, comeback when you are a real man!!!")
else:
	print("Please enter your age!!")