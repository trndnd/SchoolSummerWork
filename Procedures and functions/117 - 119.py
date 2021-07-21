#117 and 118
Valid_Number_Of_Students = False
def NumberOfStudents():
    print("How many students are you taking? ")
    Number_Of_Students = int(input())
    if Number_Of_Students < 25:
        print("Too few")
    elif Number_Of_Students > 36:
        print("Too much")
    else:
        print("valid number of students ")
        Valid_Number_Of_Students = True

Valid_Phone_Number = False

def Checking_Phone_Number():
    print("Type in your phone number")
    Phone_Number = input()
    if len(Phone_Number) == 11:
        print("Valid phone number")
        Valid_Phone_Number = True
    else:
        print("Not a valid phone number ")

#NumberOfStudents()
#Checking_Phone_Number()
#119
Valid = False
Usernames_Array = ["Trndnd","Aaron","Christian"]
def Validating_Username():
    print("Enter a username")
    Inputted_Username = input()
    if Inputted_Username in Usernames_Array:
        print("Valid username")
        return True
    else:
        print("Invalid username")
        return False

while Valid == False:
    Valid = Validating_Username()

    