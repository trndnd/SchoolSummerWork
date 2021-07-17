#102
'''
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
    Names_File_Appending.write(f"{Name} \n")'''
#104
Numbers_File = open("Task104.txt","a")
print("How many numbers do you want to enter? ")
How_Many_Numbers_Wanted_To_Add_To_File = int(input())
for x in range(How_Many_Numbers_Wanted_To_Add_To_File):
    Number = int(input("Enter a number "))
    Numbers_File.write(f"{Number} \n")