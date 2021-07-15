import random
#68
Sum_Number = 0
while Sum_Number < 100:
    Number = int(input("What is your number? "))
    print(Sum_Number)
    Sum_Number += Number
print("The sum is now greater than 100",Sum_Number)
#69
Random_Number = random.randint(1,100)
print("What is your numbert? (1,100)")
Number = int(input())
print((Random_Number + Number)/2)
#70
Random_Number = random.randint(1,100)
Number_Guessed = False
while Number_Guessed == False:
    Input_Number = int(input("Enter a numnber "))
    if Input_Number == Random_Number:
        print("Well done")
        Number_Guessed = True
    elif Input_Number > Random_Number:
        print("Too high")
    elif Input_Number < Random_Number:
        print("Too low")
#71
x = 0
while x < 5:
    Random_Number_1 = random.randint(1,10)
    Random_Number_2 = random.randint(1,10)
    Actual_Answer = Random_Number_2 * Random_Number_1
    User_Answer = int(input(f"{Random_Number_1} x {Random_Number_2} = "))
    if User_Answer == Actual_Answer:
        print("correct answer")
    else:
        print("Incorrect answer")
    x += 1