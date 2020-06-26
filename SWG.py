import random
lst = ['s','w','g']

chance = 10
no_of_chance = 0
computer_point = 0
Your_point = 0

print(" \t \t \t \t Snake,Water,Gun Game\n \n")
print("s for snake \nw for water \ng for gun \n")

# making the game in while
while no_of_chance < chance:
    _input = input('Snake,Water,Gun:')
    _random = random.choice(lst)

    if _input == _random:
        print("Tie both got 0 points \n ")

    # if user enter s
    elif _input == "s" and _random == "g":
        computer_point = computer_point + 1
        print(f"Your guess is {_input} and computer's guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer's points total  are {computer_point} and Your points total is {Your_point} \n ")

    elif _input == "s" and _random == "w":
        Your_point = Your_point + 1
        print(f"Your guess is {_input} and computer's guess is {_random} \n")
        print("you wins 1 point \n")
        print(f"computer's points total is {computer_point} and Your points total is {Your_point} \n")

    # if user enter w
    elif _input == "w" and _random == "s":
        computer_point = computer_point + 1
        print(f"Your guess is {_input} and computer guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point total is {computer_point} and Your points total is {Your_point} \n ")

    elif _input == "w" and _random == "g":
        Your_point = Your_point + 1
        print(f"Your guess {_input} and computer guess is {_random} \n")
        print("You wins 1 point \n")
        print(f"computer_points total  is {computer_point} and Your points total is {Your_point} \n")

    # if user enter g

    elif _input == "g" and _random == "s":
        Your_point = Your_point + 1
        print(f"Your guess is {_input} and computer guess is {_random} \n")
        print("You wins 1 point \n")
        print(f"computer's points total {computer_point} and Your point total is {Your_point} \n")


    elif _input == "g" and _random == "w":
        computer_point = computer_point + 1
        print(f"Your guess is {_input} and computer's guess is {_random} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {computer_point} and Your point is {Your_point} \n ")

    else:
        print("you have input wrong \n")

    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} is left out of {chance} \n")

print("Game over")

if computer_point==Your_point:
    print("Tie")

elif computer_point > Your_point:
    print("Computer wins and you loose")

else:
    print("you win and computer loose")

print(f"Your points are {Your_point} and computer's points are {computer_point}")