#62
'''
x = 1
while x < 101:
    print(x * 2)
    x += 1
print("You have finished")
#63
n = 0
while n < 1000:
    if n % 2 == 0:
        print("Hey")
    else:
        print("Bye")
    n += 1
#64
f = 0
while f < 4:
    Name = input("Give me a name ")
    f += 1
print("You have enetered 4 names")
#65
password = "Aaron Mojica"
Finished = False
Number_Of_Attempts = 0
while Finished == False:
    print("What is the password?")
    User_Inputed_Password = input()
    if User_Inputed_Password == password:
        print("Correct")
        Finished = True
    else:
        print("Incorrect. Try again")
        Number_Of_Attempts += 1
    if Number_Of_Attempts == 4:
        print("LOCKED")
        Finished = True'''
#66

