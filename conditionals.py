num_of_bananas = input('How much bananas I have?')
while(num_of_bananas.isnumeric()==False):
	print("Error! pls enter a number!")
	num_of_bananas = input('How much bananas I have?')
if(int(num_of_bananas) > 5):
	print("I have a bunch of bananas")
elif(int(num_of_bananas) > 1):
	print("I have a small bunch of bananas")
else :
	print("I have no bananas")
