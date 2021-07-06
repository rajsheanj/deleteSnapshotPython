import random

def guess(x):
    random_no = random.randint(1,x)
    guess = 0
    while guess != random_no:
        guess = int(input('Guess a number 1 and {x}: '))
        if guess < random_no:
            print ("Sorry guess again. too low")
        elif guess > random_no:
            print("sorry guess again.. too high..")
    print("yes congrats.. you guess correctly", random_no)

guess(10)