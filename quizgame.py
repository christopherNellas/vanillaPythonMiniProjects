from math import inf
import random as r
import itertools as i

print("Welcome to my Quiz Game")
order = []
for orders in i.count(start=1):
    randomNumber = r.randrange(1,5)
    if len(order) == 4:
        break
    elif randomNumber in order:
        continue
    else:
        order.append(randomNumber)
print(order)

playing = input("Do you want to play? ").lower()
#print(f"{playing}")
if playing != "yes":
    print("Bye!")
    quit()
print("Okay! Let's play...")

answer = int(input('''
    First Question:
    What is the sum of 10 + 40? '''))
if answer == 50:
    print("Correct!")
else:
    print("Incorrect!")