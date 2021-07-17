#84
grades = [["Alfie Little",24,32,5],["Billy Bob Junior II", 22,22,53], ["Mark Jones",43,54,23], ["King Plonker", 23,12,32]]
#85
grades[2][3] = 76
#86
grade4 = [37,99,32,42]
for x in range(len(grade4)):
    grades[x].append(grade4[x])
print(grades)
#87
Sum_Grade = 0
for x in range(1,len(grades[0])):
    Sum_Grade += grades[0][x]

Average = Sum_Grade/(len(grades[0]) - 1)
print(Average)
#88
Pupils_Array = [["Alex Chadwick","7+"],["Seema Patel","5-"],["Dion Scott","6-"],["Emma Baldridge","8"],["Gareth Wild","8+"]]
Pupils_Array.remove(["Emma Baldridge","8"])
print(Pupils_Array)
Pupils_Array.append(["Jonathan Pierce","5+"])
print(Pupils_Array)