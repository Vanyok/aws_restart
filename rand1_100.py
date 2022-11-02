import random
import math

def random_1_100():
	num=random.random()
	num = num * 100
	if(num < 10):
		num *= 10
	return num

def random_5_95():
	num=random.random()
	num = num * 100
	if(num < 5):
		num *= 10
	elif(num >95):
		num = num/10
	return num

def chinesse():
	heads=35
	legs=94
	rabbits=0
	chicckens=0
	while heads*2 < legs:
		rabbits+=1
		heads-=1
		legs-=4
	chicckens=heads
	print("chicckens: "+str(chicckens))
	print("rabbits: "+str(rabbits))

def div_7_and_5():
	numbers=[0,1,2,3,4,5,6,7,8,9,10]
	solution=random.choice(numbers)
	while solution%7 != 0 or solution%5 != 0:
		solution=random.choice(numbers)
	return solution

print("random_10_100: "+str(random_5_95()))
print("random_5_95: " + str(random_5_95()))
chinesse()
print(str(div_7_and_5()) + " is divisible by 7 and 5");
