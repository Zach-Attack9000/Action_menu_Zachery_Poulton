#Zachery Poulton
#Action Menu for the RPG
#Ms. Heuchert
#Computer Science 30

"""This program is meant to complete the build a action menu assignment for class. """

#Printing the options out for the user
print("Choose an action:")
print(">Walk Straight")
print(">Walk Back")
print(">Walk Left")
print(">Walk Right")

#Declaring the input variable so the user has a space to type 
direction = input("Choice:")

#Declaring the if statements thwich are used to give an answer back, depending on which is chosen
if direction == ("Walk Straight"):
    print("You Succesfully chose to walk straight")
    
elif direction == ("Walk Back") :
    print("You Succesfully chose to walk back")
    
elif direction == ("Walk Left"):
    print("You Succesfully chose to walk left")

elif direction == ("Walk Right"):
    print("You Succesfully chose to walk right")

else:
    print("\nPlease try again --> maybe try to capitalize your words?")

#Just repeating the same system as the last multiple choice but with actions instead of directions
print("\nChoose an action:")
print(">Grab Candle \n>Throw Rock \n>Dance On The Spot \n>Jumping Jacks")
action = input("Choice:")

if action == ("Grab Candle"):
    print("You grabbed the candle!")

elif action == ("Throw Rock"):
    print("You threw a rock!")

elif action == ("Dance On The Spot"):
    print("You start to do a boogy!")
    
elif action == ("Jumping Jacks"):
    print("You start jumping the jacks!")
    
else:
    print("\nPlease try again --> maybe try to capitalize your words?")


    