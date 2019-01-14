from random import randint
r_n = randint(1,10)

choice = ""
while choice != "n":
	u_n = int(input("Guess a number 1 and 10 :"))
	if u_n == r_n:
		print("You win!")
		choice = input("Do you want to keep playing (y/n) : ")
	else:
		if u_n < r_n:
			print("No. too low")
			choice = input("Do you want to keep playing (y/n) : ")
		else:
			print("No. too High")
			choice = input("Do you want to keep playing (y/n) : ")
