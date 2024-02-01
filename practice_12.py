import random
easy_level = 10
hard_level = 5
def check(guess , answer , turns):
    if guess > answer:
        print("too high")
        return turns - 1
    elif guess < answer:
        print("too low")
        return turns - 1
    else:
        print(f"you got it your number is {answer}")
def game_level():
    level = input("type easy or hard")
    if level == "easy":
        return easy_level
    else:
        return hard_level 
def game():
    answer = random.randint(1,100)
    turns = game_level()
    print("welcome to our number guessing game")
    print("please guess a number between 1-100")
    guess = 0
    while guess != answer:
        print(f"you have {turns} atempt ")
        guess = int(input("guess a number"))
        turns = check(guess,answer , turns)
        if turns == 0:
            print("you loose the game")
            return
        elif guess != answer:
            print("guess again")
game()