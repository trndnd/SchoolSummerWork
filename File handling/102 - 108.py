import random
#102
Numbers_File = open("Numbers.txt","a")
for x in range(5):
    print("What is your number? ")
    Number = int(input())
    Numbers_File.write(f"{str(Number)} \n")
#103
Names_Array = []
Names_File_Appending = open("Task103.txt","a")
for x in range(3):
    Name = input("What is your name? ")
    Names_Array.append(Name)
for Name in Names_Array:
    Names_File_Appending.write(f"{Name} \n")
#104
Numbers_File = open("Task104.txt","a")
print("How many numbers do you want to enter? ")
How_Many_Numbers_Wanted_To_Add_To_File = int(input())
for x in range(How_Many_Numbers_Wanted_To_Add_To_File):
    Number = int(input("Enter a number "))
    Numbers_File.write(f"{Number} \n")
#105
Details_File = open("Task105.txt","a")
First_Name = input("What is your first name? ")
Surname = input("What is your surname? ")
Age = int(input("How old are you? "))
Address = input("What's your address? ")
#106
MyFile_Appending = open("Task106.txt","w")
MyFile_Reading = open("Task106.txt","r")
for x in range(5):
    Name_Of_Game = input("Enter a game ")
    MyFile_Appending.write(f"{Name_Of_Game} \n")
MyFile_Appending.close()
MyString = ""
MyList_Of_Games = []
x = 0
while x < 1:
    LineValue = MyFile_Reading.readline()
    if LineValue == "":
        x = 1
    else:
        MyString += f"{LineValue.strip()},"
MyList_Of_Games.append(MyString)
print(MyList_Of_Games)
#107
Reading_File_Football_Names = open("Football_Name.txt","r")
Random_Number = random.randint(0,7)
print(Random_Number)
Content = Reading_File_Football_Names.readlines()
LineValue = Content[Random_Number].split(',')
print(f"The team is {LineValue[0]}")
Player_Name = LineValue[1].split(" ")
print(f"The first letter of in the first name is {Player_Name[0][0]}")
print(f"The first letter of the surname is {Player_Name[1][0]}")
#108
Name = input("What is your name? ")
Homework_File = open(f"{Name}.txt","w")
Homework_Tasks_They_Need_To_Complete = int(input())
for x in range(Homework_Tasks_They_Need_To_Complete):
    Homework_Name = input("What is the name of the homework task? ")
    Homework_File.write(f"Task {x + 1}: {Homework_Name} \n")
Homework_File.close()
