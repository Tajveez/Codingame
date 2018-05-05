import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input()

glyphs = [str(input()) for i in range(h)]

for i in range(h):
    for ch in t:
        if ch >= 'a' and ch <= 'z':
            ch_pos = ord(ch) - ord('a')
        elif ch >= 'A' and ch <= 'Z':
            ch_pos = ord(ch) - ord('A')
        else:
            ch_pos = ord('z') - ord('a') + 1
        
        for j in range(l):
            print(glyphs[i][ch_pos*l+j], end="")

    print("")
