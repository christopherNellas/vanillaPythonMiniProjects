def question(order):
    if order == 0:
        answer = int(input('''
            First Question:
            What is the sum of 10 + 40? '''))
        if answer == 50:
            print("Correct!")
        else:
            print("Incorrect!")
    elif order == 1:
        answer = int(input('''
            Second Question:
            What is the difference of 50 - 10? '''))
        if answer == 40:
            print("Correct!")
        else:
            print("Incorrect!")
    elif order == 2:
        answer = int(input('''
            First Question:
            What is the product of 10 x 10? '''))
        if answer == 100:
            print("Correct!")
        else:
            print("Incorrect!")
    elif order == 3:
        answer = int(input('''
            First Question:
            What is the quotient of 100 / 5? '''))
        if answer == 20:
            print("Correct!")
        else:
            print("Incorrect!")