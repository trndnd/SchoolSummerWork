#78 and 79
'''
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
print(f"{Female_Counter} females")'''
#83
class Game_Menu:
    def __init__(self,Games_Array):
        self.Games_Array = Games_Array

x = 0
while x < 1:
    print("Do you want to add,edit,delete a game or print all of your games? ")
    Decision = input()
    
