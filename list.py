item = 0
mylist=[]
while item != '-1':
	item = input("Enter next item or -1 for print all items: ");
	if item.isnumeric()==True:
		item = int(item)
	mylist.append(item)
for list_item in mylist:
	print(list_item)