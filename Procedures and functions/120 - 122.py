#120
def NewBooking():
    print("You have chosen A,you are now in the new booking section")
def AmendBooking():
    print("You have chosen option B, you are now in the amending section")
def CancelBooking():
    print("You have chosen option C, you are now in the canceling section")

Finished = False
while Finished == False:
    print("Enter A for booking system, Enter B to amend your booking, Enter C to cancel your book")
    Decision = input().upper()
    if Decision == "A":
        print("You have entered a valid choice ")
        NewBooking()
        Finished = True
    elif Decision == "B":
        print("You have entered a valid choice ")
        AmendBooking()
        Finished = True
    elif Decision == "C":
        print("You have entered a valid choice ")
        CancelBooking()
        Finished = True
    else:
        print("Invalid decision")
#121
x = 2
y = 3
def Multiplication(num1,num2):
    return num1 * num2
def division(num1,num2):
    return num1 / num2
def Addition(num1,num2):
    return num1 + num2
def Subtraction(num1,num2):
    return num1 - num2
number = int(input("What is your first number? "))
number2 = int(input("What is your second number? "))
Valid_Operator = False
while Valid_Operator == False:
    print("A for Addition,S for subtraction,M for multiplication,D for division")
    Operation = input("").upper()
    if Operation == "A":
        print(Addition(number,number2))
        Valid_Operator = True
    elif Operation == "S":
        print(Subtraction(number,number2))
        Valid_Operator = True
    elif Operation == "D":
        print(division(number,number2))
        Valid_Operator = True
    elif Operation == "M":
        print(Multiplication(number,number2))
        Valid_Operator = True
    else:
        print("Not a valid operator")
#122
def VerifyingUsername(Inputted_Username):
    if 2 < len(Inputted_Username) < 20:
        print("Valid Username")
        return True
    print("Invalid username")
    return False
def VerifyingPassword(Inputted_Password):
    if len(Inputted_Password) > 2:
        print("Valid password")
        return True
    print("Invalid password")
    return False
def Asking_To_Type_The_Password_Again(Inputted_Password):
    print("Type the password again for verification purposes")
    Re_Typed_Password = input()
    if Re_Typed_Password == InputtedPassword:
        print("You succesfully created an account!")
    else:
        print("Not the same password!")
print("Enter a username")
InputtedUsername = input()
Checking_Username = VerifyingUsername(InputtedUsername)
if Checking_Username:
    print("Enter a password")
    InputtedPassword = input()
    Checking_Password = VerifyingPassword(InputtedPassword)
    if Checking_Password:
        Asking_To_Type_The_Password_Again(InputtedPassword)