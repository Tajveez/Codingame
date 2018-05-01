import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
temp = []
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
#    if ()
    temp.append(int(i))
    #temp = temp.sort()

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

if(len(temp) == 0):
    print("0")
else:
    closest = temp[0]
    for i in range(len(temp)):
        if(len(temp) == 1):
            break
        elif(abs(temp[i]) < abs(closest)):
            closest = temp[i]
        elif(abs(temp[i]) == abs(closest)):
            if temp[i] > closest:
                closest = temp[i]
        
print(closest)
