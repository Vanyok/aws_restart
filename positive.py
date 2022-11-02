all_sum=0
count=0
current=0
average=0
while current != "-1":
	current=input('Pls enter number ( -1 for end) ')
	if(current != "-1"):
		all_sum += int(current)
		count += 1
if(count > 0):
	average = all_sum / count
print('average = '+str(average))