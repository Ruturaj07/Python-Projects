print("....rock....")
print("....paper....")
print("....scissors....")


py1 = input("Enter player one's choice :")
py2 = input("Enter player two's choice :")


if py1 == "rock" and py2 =="paper":
	print("Player two wins")
elif py1 == "rock" and py2 =="scissors":
	print("Player one wins")
elif py1 == "paper" and py2 =="rock":
	print("Player one wins")
elif py1 == "paper" and py2 =="scissors":
	print("Player two wins")
elif py1 == "scissors" and py2 =="paper":
	print("Player one wins")
elif py1 == "scissors" and py2 =="rock":
	print("Player two wins")
elif py1 == py2 :
	print("Its a Tie!!")
else:
	print("Something went wrong")
