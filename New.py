import random 
bomb = random.randint(1,8)
pick=int(input("Pleaseenter a number: "))

if pick == bomb:
	print("\n sorry you have gone")
else:
 	print("you won")
 	print("pick",pick)	
 	print("bomb",bomb)