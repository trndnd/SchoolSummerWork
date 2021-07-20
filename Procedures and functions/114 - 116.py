#114 
def AverageOf2Numbers(num1,num2):
    Average =(num1 + num2)/2
    return Average

print(AverageOf2Numbers(3,4))
#115
def FutureAgeFunction(currentAge,year):
    FutureAge = currentAge + Year
    return FutureAge
Age = int(input("How old are you? "))
Year = int(input("How many years do you want to add to your current age? "))
print(FutureAgeFunction(Age,Year))
#116
def WhatIsYourNumber():
    Number = int(input("Enter a number "))
    return Number

def Multiplying3Numbers(num1,num2,num3):
    Total = num1 * num2 * num3
    return Total

Value = Multiplying3Numbers(WhatIsYourNumber(),WhatIsYourNumber(),WhatIsYourNumber())
print(Value)