guard_presentense = {"1":False,"2":False,"3":False,"4":False,"5":True,"6":True,
"18":True,"19":False,"20":True,"21":True,"22":False,"23":False}
hour=input("please enter a hour:")
if hour.isnumeric()==False or int(hour) > 23 or int(hour) < 0 :
	print('wrong hour format, must be 0 ... 23')
elif int(hour) > 6 and int(hour) < 18  :
	print('It is working time, you can in')
elif hour in guard_presentense and guard_presentense.get(hour) == True :
	print('Now campus is closed but you can enter')
else :
	print('Sorry, campus is closed, you can\'t in right now, pls try another time')