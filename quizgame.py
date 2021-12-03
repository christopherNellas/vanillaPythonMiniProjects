from math import inf
import random as r
import itertools as i
import quizgamequestions as qq

print("Welcome to my Quiz Game")
order = []
for orders in i.count(start=0):
    randomNumber = r.randrange(0,4)
    if len(order) == 4:
        break
    elif randomNumber in order:
        continue
    else:
        order.append(randomNumber)
print(order)

index = 0
while index < 4:
    qq.question(index)
    index += 1