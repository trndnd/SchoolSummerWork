#62
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
        Finished = True
#66
password = "Hello world"
Correct_Input = False
while Correct_Input == False:
    Inputed_Password = input("What is the password? ")
    if password == Inputed_Password:
        print("Correct")
        Correct_Input = True
    else:
        print("Incorrect")
#67
Valid_Username = False
while Valid_Username == False:
    print("Waht is your username? ")
    Inputed_Username = input()
    if len(Inputed_Username) > 8:
        print("Valid username")
        Valid_Username = True
    else:
        print("Invalid username, enter a different username")
Valid_Password = False
while Valid_Password == False:
    print("Waht is your password? ")
    Inputed_Password = input()
    if 8 <= len(Inputed_Password) <= 15:
        print("Valid password")
        Valid_Password = True
    else:
        print("Invalid password, enter a different password")
