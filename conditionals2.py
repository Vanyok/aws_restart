userREply = input("Do you need to ship a package? (Enter yes or no) ")
if userREply == "yes":
    print("We can help you ship that package!")
else : 
    print("Please come back when you need to ship a package. Thank you.")
userREply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ?")
if userREply == "stamps":
    print("We have many stamp designs to choose from.") 
elif userREply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userREply == "copy" :
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else :
    print("Thank you, please come again.")