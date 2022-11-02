curr_queue = ['Alice1','Alise2','Alise3','Alise4','Alise5']
action = 0;
while action != "E":
	action = input("What is the action: Join to the end (J), Join to the front (F), Leave queue (L), Quit program (Q)");
	name = input("What is your name?")
	if(action == "J"):
		curr_queue.append(name)
	elif(action == "F"):
		curr_queue.insert(0,name)
	elif(action == "L"):
		curr_queue.remove(name)
	elif(action == "Q"):
		print("Bye! See you soon!")
	else:
		print('Action is unknown')
	print("current queue")
	for women in curr_queue:
		print(women + " > ")
