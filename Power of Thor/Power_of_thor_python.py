import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
tx = iniial_tx
ty = iniial_ty
lx = light_x
ly = light_y
# game loop
while True:
    dx = ""
    dy = ""
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    if tx > lx:
        tx = tx - 1
        dx = "W"
    elif tx < lx:
        tx = tx + 1
        dx = "E"
    if ty > ly:
        ty = ty - 1
        dy = "S"
    elif ty < ly:
        ty = ty + 1
        dy = "N"
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)


    # A single line providing the move to be made: N NE E SE S SW W or NW
    print(dx,dy)
