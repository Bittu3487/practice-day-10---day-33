import random
from data_entry import data
def format_data(acount):
    acount_name = acount["name"]
    acount_des= acount["description"]
    acount_country = acount["country"]
    return f"{acount_name}, a {acount_des} , from {acount_country}"
def check_answer(guess , a_follower_count , b_follower_count):
    if a_follower_count > b_follower_count:
        return guess == "a"
    else:
        return guess == "b"
score = 0
is_on = True
while is_on:
    acount_a = random.choice(data)
    acount_b = random.choice(data)
    if acount_a == acount_b:
        acount_b = random.choice(data)
    print(f"compare A: {format_data(acount_a)}")
    print(f"compare B: {format_data(acount_b)}")
    guess = input("who has more follower ? type 'A' or 'B' ")
    a_follower_count = acount_a["follower"]
    b_follower_count = acount_b["follower"]
    is_correct = check_answer(guess , a_follower_count , b_follower_count)
    if is_correct:
        score += 1
        print(f"you got it your score is {score}")
    else:
        is_on = False
        print(f"you loose the game your score is {score}")
       
