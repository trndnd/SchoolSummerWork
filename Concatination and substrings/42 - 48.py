#42
Name = input("What is your name? ")
Upper_or_Lower = input("Do you want it to be uppercase or lowercase (upper/lower)")
if Upper_or_Lower.lower() == "upper":
    print(Name.upper())
elif Upper_or_Lower.lower() == "lower":
    print(Name.lower())
else:
    print("Invalid input")
#43
Quote = input("Enter a quote ")
Word_Wanting_To_Be_Replaced = input("What word do you want to replace? ")
Replacment_Word = input("What word do you want to replace it with? ")
Quote = Quote.replace(Word_Wanting_To_Be_Replaced,Replacment_Word)
print(Quote)
#44
Quote = input("Enter a quote ")
print(Quote.upper())
print(Quote.lower())
print(Quote.title())
temp = Quote.split()
Quote = Quote.replace(temp[0],temp[0].capitalize())
print(Quote)
#45
print("Good \nGame")
print("Good \t Game")
#46
Quote = input("Enter a quote ")
Number_Of_Time_i_Appears = Quote.count("i")
print(f"i appears {Number_Of_Time_i_Appears} times")
#47
Contains_Letter = False
Contains_Number = False
Conatins_Space = False
Quote = input("Enter a quote ")
for char in Quote:
    Ascii_Value = ord(char)
    if 96 < Ascii_Value < 123 or 64 < Ascii_Value < 91:
        Contains_Letter = True
    elif 47 < Ascii_Value < 58:
        Contains_Number = True
    elif char == " ":
        Conatins_Space = True

if Contains_Letter:
    print("Conatins a letter")
if Conatins_Space:
    print("Contains a space")
if Contains_Number:
    print("Contains a number")
#48
Favourite_Hobby = input("What is your favourite hobby? ")
Splitting_At_f = Favourite_Hobby.split("f")


