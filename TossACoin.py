#Github:

"""
Toss a coin - Developed by Nripesh.
How it works:
python TossACoin.py

User is asked to call for "Heads" or "Tails"
    Enter the side of the coin :
    > Head or Tail

    Result: Head or Tail
"""
import random
import time
import sys

sides = ['head','tail']

print("Lets go for a toss")
print("Enter the side of the coin:")
call = input(">" )
print("You opted for %s"%(call))

if call.lower() not in sides:
    print("You input was invalid, Go for toss again and enter either head or tail as input")
    sys.exit()

time.sleep(5)
result = random.choice(sides)
print("its %s"%(result))
print('*'*10)

if result == call.lower():
    print("You wont the toss")
else:
    print("You lost the toss")








