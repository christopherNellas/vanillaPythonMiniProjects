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
index = 0
while index < 4:
    qq.question(index)
    index += 1
totalScore = qq.score
if totalScore == 4:
    print(f"{totalScore}/4: You scored perfect!!!")
elif totalScore == 3:
    print(f"{totalScore}/4: You almost got it..")
elif totalScore == 2:
    print(f"{totalScore}/4: You can do it next time..")
elif totalScore == 1:
    print(f"{totalScore}/4: You can do better than this.")
else:
    print(f"{totalScore}/4: Try again..")