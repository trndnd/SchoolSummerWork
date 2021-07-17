#95
'''
myFile = open("Films.txt","w")
Films_array = ["Weathering with you","Black Panther","Endgame"]
for Movie in Films_array:
    myFile.write(f"{Movie} \n")
myFile.close()
#96
Name_File = open("Name.txt","w")
Name = input("What is your name? ")
Name_File.write(Name)
Name_File.close()
#97
Song_File_Writing = open("Songs.txt","w")
Song_File_Reading = open("Songs.txt","r")
for x in range(3):
    Song = input("Name me a song ")
    Song_File_Writing.write(f"{Song} \n")
Song_File_Writing.close()
Content = Song_File_Reading.read()
print(Content)
#98
File_Name = input("What should the file name be? ")
Sentence = input("What sentence do you want to add to this text file? ")
File_Writing = open(f"{File_Name}.txt","w")
File_Reading = open(f"{File_Name}.txt","r")
File_Writing.write(Sentence)
File_Writing.close()
Content = File_Reading.read()
print(Content.upper()) 
print(Content.lower())
#99
Writing_File = open("Task99.txt","a")#used append instead of write beacuase write kept wiping the contents of the file when opened
Reading_File = open("Task99.txt","r")
x = 0
print("Do you want to read or write? ")
Decision = input()
if Decision.lower() == "read":
    Content = Reading_File.read()
    print(Content)
elif Decision.lower() == "write":
    Sentence = input("What sentence do you want to write into the file? ")
    Writing_File.write(f"{Sentence}")
    Writing_File.close()
else:
    print("Did you even pick on option? ")'''
#100 and 101
Task100_File_Writing = open("Task100.txt","w")
Name = input("What is your first name and second name? ")
Task100_File_Writing.write(f"Full name: {Name} \n")
Task100_File_Writing.close()
Task100_File_Appending = open("Task100.txt","a")
Other_Name = input("What is your name? ")
Address = input("What is your address? ")
Task100_File_Appending.write(f"Other user's name: {Other_Name} \n")
Task100_File_Appending.write(f"Address of other user: {Address} \n")
Task100_File_Appending.write("Alex hunter \n")
