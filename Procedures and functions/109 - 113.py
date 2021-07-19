#109
def Name():
    Name = input("What is your name? ")
    print(Name)
Name()
#110 There is no 110th task
#111
def Surname():
    Surname = input("What is your surname?")
    print(Surname)
print("Which question do you want me to ask? (forename or surname)")
Decision = input()
if Decision.lower() == "forename":
    Name()
elif Decision.lower() == "surname":
    Surname()
else:
    print("Did you even pick an option?")
#112
def GreaterOrLessThan5(Number):
    if Number > 5:
        print("Greater than 5")
    elif Number < 5:
        print("Less than 5")
    else:
        print("Exactly equal to 5")

Finished = False
Number = int(input("Enter a number "))
GreaterOrLessThan5(Number)
while Finished == False:
    print("Do you want to go again? ")
    Decision = input()
    if Decision.lower() == "yes":
        Number = int(input("Enter a number "))
        GreaterOrLessThan5(Number)
    elif Decision.lower() == "no":
        Finished = True
    else:
        print("Did you even pick an option? ")
#113 I wish I could use functions for this question but I can't as the code will look much cleaner 
def Name_And_Age():
    Name_Array = []
    Ages_Array = []
    Name = input("What is your name? ")
    Name_Array.append(Name)
    Age = int(input(f"{Name} how old are you? "))
    Ages_Array.append(Age)
    Name2 = input("What is your name? ")
    Name_Array.append(Name2)
    Age2 = int(input(f"{Name2} how old are you? "))
    Ages_Array.append(Age2)
    Comparion(Ages_Array,Name_Array)

def Comparion(Age_Array,Name_Array):
    if Age_Array[0] > Age_Array[1]:
        print(f"{Name_Array[0]} is older than {Name_Array[1]}")
    else:
        print(f"{Name_Array[1]} is older than {Name_Array[0]}")
Name_And_Age()
#113 but with functions
def NameAndAge():
    name = input("What is your name? ")
    age = int(input(f"{name} how old are you? "))
    return [name,age]
def Comparion2(User1Data,User2Data):
    if User1Data[1] > User2Data[1]:
        print(f"{User1Data[0]} is older than {User2Data[0]}")
    else:
        print(f"{User2Data[0]} is older than {User1Data[0]}")
User1_Data = NameAndAge()
User2_Data = NameAndAge()
Comparion2(User1_Data,User2_Data)