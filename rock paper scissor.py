import random
class game:
	option=("rock","paper","scissor")
	print(f"select {option}")
	run=True

	while run:
		play=None
		comp=random.choice(option)
	
		while play not in option:
			play=input("select :").lower()
			if play not in option:
					print("select a correct option")
			else:
				continue
					
		if play==comp:
			print("tie")
			print("both choose same!")
		elif play=="rock" and comp=="scissor":
			print("you win")
			print("comp choose:",comp)
		elif play=="paper" and comp=="rock":
			print("you win")
			print("comp choose:"),comp
		elif play=="scissor" and comp=="paper":
			print("you win")
			print("comp choose:",comp)
		else:
			print("comp win")
			print("comp choose:",comp)

		op=("yes","no")
	
		while True:
			player=input("play again(y/n:").lower()
			if player not in op:
				print("enter yes or no")
			elif player=="yes":
				break
			elif player=="no":
				run=False
				break
				
print("thanks for playing")

g=game
print(yuva)
	
		