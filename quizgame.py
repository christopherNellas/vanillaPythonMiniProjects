print("Welcome to my Quiz Game")

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