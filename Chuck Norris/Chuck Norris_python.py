import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()
bin_msg = ''
#msg = ''
for char in message:
    bin_msg += format(ord(char),'07b')
    #msg = format(ord(char),'b')
    #if len(msg) < 7:
    #   while(len(msg) < 7):
    #       msg = '0'+ msg
    #   bin_msg += msg
    #else:
    #   bin_msg += msg#format(ord(char),'b')    
    #print(bin_msg)
cur = bin_msg[0]
count = 1
result = ''

for i in bin_msg[1:]:
    if cur == i:
        count +=1
    else:
        if cur == '1':
            result += '0 '
        else:
            result += '00 '
        
        result +='0'*count+' '
        cur = i
        count = 1
        
if cur == '1':
      result+='0 '
else:
      result+='00 '
result+='0'*count
print(result)
