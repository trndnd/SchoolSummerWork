#26
Number = int(input("Input a number "))
if Number > 100:
    print("Too large")
elif Number < 100:
    print("Too small")
#27
Football_Team = input("Enter a football team ")
if Football_Team.lower() == "Chelsea":
    print("Blue")
elif Football_Team.lower() == "Liverpool":
    print("Red")
else:
    print("Team not registered")
#28
Number1 = int(input("What is your first number? "))
Number2 = int(input("What is your second number? "))
if Number1 > 10:
    print(Number1 + Number2)
else:
    print(Number1 * Number2)
#29
First_Number = int(input("What is your first number? "))
Second_Number = int(input("What is your second number? "))
Operation_Wanted = input("What operation do you want to perform on it? (Multiply or Add) ")
if Operation_Wanted.lower() == "multiply":
    print(First_Number * Second_Number)
elif Operation_Wanted.lower() == "add":
    print(First_Number + Second_Number)
else:
    print("Operation not available!")
#30
print("Would you rather take the red pill or the blue pill? ")
Pill_Choice = input("")
if Pill_Choice.lower() == "red":
    print("Red is the colour of blood")
elif Pill_Choice.lower() == "blue":
    print("Are you sick? ")
else:
    print("I don't like that color ")