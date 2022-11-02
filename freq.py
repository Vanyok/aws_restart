import re
input_text="You can have data without information, but you cannot have information without data."
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','o','p','q','a','s','t','u','v','w','x','y','z']
lower_text = input_text.lower()
for symbol in alphabet:
	cnt=0
	for letter in lower_text:
		if(letter == symbol):
			cnt += 1
	if(cnt>0):
		print(symbol +" : "+str(cnt))
	