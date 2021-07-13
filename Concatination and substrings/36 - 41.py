#36
print("What's your favourite hobby? ")
Favourite_Hobby = input()
print("What's your friends favourite hobby? ")
Friends_Favourite_Hobby = input()
print(f"You favourite hobby is {Favourite_Hobby} and your friends favourite hobby is {Friends_Favourite_Hobby}")
#37
print("What's your favourite drink? ")
Favourite_Drink = input()
Favourite_Drink_Length = len(Favourite_Drink)
print(Favourite_Drink_Length)
#38
First_Name = input("What's your first name? ")
Surname = input("Whats your surname? ")
Length_Of_Both_Names_Combined = len(First_Name + Surname)
print(Length_Of_Both_Names_Combined)
#39
print("Enter the name of a color which only has 6 letters ")
Color_Choice = input()
if len(Color_Choice) == 6:
    print("Correct")
else:
    print("Incorrect")
#40