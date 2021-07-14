#31
print("What's the color of the traffic light? ")
Traffic_Light_Colour = input()
if Traffic_Light_Colour.lower() == "red":
    print("STOP")
elif Traffic_Light_Colour.lower() == "yellow":
    print("Get ready")
elif Traffic_Light_Colour.lower() == "green":
    print("GO")
else:
    print("error")
#Also 31
print("What's the color of the traffic light? ")
Traffic_Light_Colour = input()
Traffic_Light_Colour_Dictionary = {
    "red":"STOP",
    "yellow":"Get ready",
    "green":"GO"
}
Response = Traffic_Light_Colour_Dictionary.get(Traffic_Light_Colour, "error")
print(Response)
#32
username = "Hello"
Password = "World"
print("What is your username? ")
Inputted_username = input()
print("What is your password? ")
Inputted_password = input()
if username == Inputted_password and Password == Inputted_password:
    print("Logged in!")
else:
    print("Incorrect try again!")
#33
print("Do you play games on pc?")
Pc_Answer = input()
print("Do you play games on console?")
Console_Answer = input()
if Pc_Answer.lower() == "yes" and Console_Answer.lower() == "yes":
    print("Game master")
elif Pc_Answer.lower() == "yes" and Console_Answer.lower() == "no":
    print("Pc master")
elif Console_Answer.lower() == "yes" and Pc_Answer.lower() == "no":
    print("Console master")
else:
    print("Error")
#34 
print("How old are you? ")
Age = int(input())
if 12 < Age < 20:
    print("You are a teenager")
elif 11 == Age  or Age == 12:
    print("You are a tween")
else:
    print("Invalid age")
#35
print("What is the current temperature? ")
Temperature = int(input())
print("Is it raining? (yes or no)")
Raining_Or_Not = input()
if Temperature < 12 and Raining_Or_Not.lower() == "yes":
    print("Wear a coat and bring an umbrella")
elif Temperature < 12 and Raining_Or_Not.lower() == "no":
    print("Wear a coat")
elif Temperature >= 12 and Raining_Or_Not.lower() == "yes":
    print("Bring an umbrella")
elif Temperature >= 12 and Raining_Or_Not.lower() == "no":
    print("You don't need either a coat or an umbrella")
else:
    print("Error")
