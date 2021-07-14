#56
Quote = input("Enter a quote ").split()
for word in Quote:
    print(word[0])
#57
for x in range(1,99,2):
    print(x)
#58
Name = input("What is your name? ")
Age = int(input("What is your age? "))
for x in range(Age):
    print(Name)
#59
for x in range(6):
    Number = int(input("What is your number? "))
    print(Number + 5)
#60
def Displaying_Something(message,number):
    for x in range(number):
        print(message)


Warnings = int(input("How many warnings did you get? "))
if Warnings == 1:
    Displaying_Something("prompt",10)
elif Warnings == 2:
    Displaying_Something("reminder",50)
elif Warnings == 3:
    Displaying_Something("warning",100)
elif Warnings == 4:
    Displaying_Something("removal",500)
#61
Age = int(input("How old are you? "))
if Age > 12:
    Displaying_Something("Happy birthday",100)
else:
    Displaying_Something("Happy birthday",12)
