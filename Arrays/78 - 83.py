#78 and 79
Games_Array = []
for x in range(3):
    Game = input("Name a game ")
    Games_Array.append(Game)
Games_Array_Sorted = sorted(Games_Array)
print(Games_Array_Sorted)
print("Which index number would you like to see?")
IndexNumber = int(input())
print(Games_Array_Sorted[IndexNumber - 1 ])
#80
Film_Array = []
for x in range(4):
    Film_Name = input("Enter a flim name ")
    Film_Array.append(Film_Name)
LastValue = Film_Array[-1]#Value of last item in the film array so i can add it on later
Film_Array.remove(Film_Array[-1])#Removes last value of the array 
print(Film_Array)
Film_Array.append(LastValue)
print(Film_Array)
print(Film_Array[0])
#81
Numbers_Array = []
for x in range(6):
    Number = int(input("Enter a number "))
    Numbers_Array.append(Number)
print("Do you want the total or the average of these 6 numbers? ")
Decision = input()
if Decision.lower() == "total":
    print(sum(Numbers_Array))
elif Decision.lower() == "average":
    print(sum(Numbers_Array)/len(Numbers_Array))
else:
    print("not a valid decision")
#82
Finished = False
Male_Counter = 0
Female_Counter = 0
while Finished == False:
    print("What is your gender? ")
    Response = input()
    if Response.lower() == "quit":
        Finished = True
    elif Response.lower() == "female":
        Female_Counter += 1
    elif Response.lower() == "male":
        Male_Counter += 1
    else:
        print("Not a valid gender")
print(f"{Male_Counter} males")
print(f"{Female_Counter} females")
#83
class Game_Menu:
    def __init__(self):
        self.Games_Array = []

    def Adding(self):
        Game = input("What game do you want to add? ")
        self.Games_Array.append(Game)

    def Editing(self):
        print(self.Games_Array)
        Value_Being_Edited = input("Which one do you want to change? ")
        What_It_Will_Be_Changed_To = input("What would you like it to change to? ")
        Value_Being_Edited_Position = self.Games_Array.index(Value_Being_Edited)
        self.Games_Array[Value_Being_Edited_Position] = What_It_Will_Be_Changed_To

    def printing(self):
        print(self.Games_Array)

    def deleting(self):
        print(self.Games_Array)
        Game_Wanting_To_Be_Deleted = input("What game do you want to delete? ")
        self.Games_Array.remove(Game_Wanting_To_Be_Deleted)

    def Menu_Screen(self):
        x = 0
        while x < 1:
            print("Do you want to add,edit,delete a game or print all of your games? (or quit)")
            Decision = input()
            if Decision.lower() == "add":
                Game_Menu.Adding(self)
            elif Decision.lower() == "edit":
                Game_Menu.Editing(self)
            elif Decision.lower() == "print":
                Game_Menu.printing(self)
            elif Decision.lower() == "delete":
                Game_Menu.deleting(self)
            elif Decision.lower() == "quit":
                x = 1
            else:
                print("Not a valid option")
y = Game_Menu()
y.Menu_Screen()