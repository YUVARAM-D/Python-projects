import random
option=("rock","paper","scissor")

print(f"select {option}")
run=True
while run:
	play=None
	comp=random.choice(option)
	
	while play not in option:
		play=input("enter:").lower()
		if play not in option:
				print("enter a correct option")
			
	if play==option:
		print("tie")
	elif play=="rock" and comp=="scissor":
		print("you win")
	elif play=="paper" and comp=="rock":
		print("you win")
	elif play=="scissor" and comp=="paper":
		print("you win")
	else:
		print("comp win")

	op=("yes","no")
	while True:
		player=input("play again(y/n:").lower()
		if player not in op:
			print("enter yes or no")
		else:
			run=False
			break	
print("thanks for playing")
	
		