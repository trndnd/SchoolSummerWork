#89
import random
Singers_Array = []
for x in range(3):
    Singer = input("Name me a singer ")
    Singers_Array.append(Singer)
Random_Number = random.randint(0,2)
Chosen_Singer = Singers_Array[Random_Number]
print(f"{Chosen_Singer} has been chosen")
#90
Singer_Array = []
for x in range(3):
    Name_Of_Singer = input("Name me a singer ")
    Singer_Array.append(Name_Of_Singer)
Singer_Array.sort()
for x in range(len(Singer_Array)):
    print(f"Singer number {x + 1} is {Singer_Array[x]}")
#91
Game = input("Enter your favourite game ")
for x in range(len(Game)):
    print(x)
#92
Quote = input("Enter a quote ")
Splitted_Quote_By_Space = Quote.split(" ")
for word in Splitted_Quote_By_Space:
    print(word)
#93
Random_Number_Array = []
for x in range(5):
    Random_Number = random.randint(1,100)
    Random_Number_Array.append(Random_Number)
    print(f"The random number is {Random_Number}")
Random_Number_Array.sort()
print(Random_Number_Array)
#94
Numbers_wanting_To_Be_Generated = int(input("How many numbers do you want to generate? "))
Minimum_Number = int(input("What's the minimum value do you want it to be? "))
Maximum_Number = int(input("What's the maximum value do you want it to be? "))
Random_Numbers = []
for x in range(Numbers_wanting_To_Be_Generated):
    Random_Number = random.randint(Minimum_Number,Maximum_Number)
    Random_Numbers.append(Random_Number)
print(Random_Numbers)
print(Random_Numbers[::-1])

