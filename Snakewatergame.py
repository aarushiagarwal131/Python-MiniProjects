#--------------------------------------------------------SNAKE WATER GUN GAME--------------------------------------------------------------

import emojis
import random
import time

a = emojis.encode(":snake:")
b = emojis.encode(":gun:")
c = emojis.encode(":sweat_drops:")
e = emojis.encode(" :fire: ")
print(a * 10, b * 10, c * 10, end=" ")
print("  Welcome to the Snake Water Gun ", end=" ")
print(c * 10, b * 10, a * 10)
var = ["S", "W", "G"]
print()
d = input("Your good name :- ")
print()
print("Hi, ", d)
print()
print("\U0001F93A " * 10, " \U0001F91D Let's Play  \U0001F91D ", "\U0001F93A " * 10)
print()
print("                            Total  Rounds  ::  5  ")
print()
print(e * 10, "  START ", e * 10)
print()
print("                                          5  ")
time.sleep(0.5)
print("                                          4  ")
time.sleep(0.5)
print("                                          3 ")
time.sleep(0.5)
print("                                          2  ")
time.sleep(0.5)
print("                                          1  ")
print("                              ->>>>>>     GO    <<<<<<-")
print("\U0001F490 " * 10, "  ************  Round  ::  1  ************  ", "\U0001F490 " * 10)
print()
n = 5
pu = 0
pc = 0
while n > 0:
    print("Press        S  ::  Snake")
    print("Press        W  ::  Water")
    print("Press        G  ::  Gun")
    f = input()
    g = random.choice(var)
    print(g)
    if f == "W":
        print(" " * 10, c, end=" ")
    elif f == "S":
        print(" " * 10, a, end="  ")
    else:
        print(" " * 10, b, end="  ")
    if g == "W":
        print(c, end=" ")
    elif g == "S":
        print(a, "  ", end=" ")
    else:
        print(b, "  ", end=" ")

    print()
    if f == "G" and g == "S":
        pu = pu + 1
        print(emojis.encode(":+1:") * pu)
    elif f == "S" and g == "W":
        pu = pu + 1
        print(emojis.encode(":+1:"))
    elif f == "W" and g == "G":
        pu = pu + 1
        print(emojis.encode(":+1:") * pu)
    elif f == g:
        print(emojis.encode(":+1:") * pu)

    else:
        pc = pc + 1
        print("\U0001F44E " * pu)
    print(" " * 10, "  Your  Score  ::  ", pu)
    print(" " * 10, "  Opponent  Score  ::  ", pc)
    print()
    print()
    n = n - 1
    if n > 0:
        print("\U0001F490 " * 10, "  ***************  Round  :: ", 5 - n + 1, "  ************", "\U0001F490 " * 10)
    print()
print("\U0001F389 " * 10, "   :- Game Over -:  ", "\U0001F389 " * 10)
print()
if pu > pc:
    print("\U0001F4AB " * 10, " ", d, " ::  \U0001F478	", "\U0001F4AB " * 10)
    print()
    print("\U0001F947 " * 10, "   You Won  by ", pu - pc, " points ", " \U0001F947 " * 10)
    print()
    time.sleep(2)
    print("                       ", d, " :: \U0001F3C6")
elif pc > pu:
    print("\U0001F44E " * 10, "  You Lost!  by ", pc - pu, " points ", " \U0001F44E " * 10)
else:
    print("\U0001F917 " * 10, "    Tie   ", "\U0001F917 " * 10)
