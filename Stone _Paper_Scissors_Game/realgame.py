import random


def game():
    print(" \nRULE: \nENTER STONE, PAPER AND SCISSOR ONLY \n")
    while True:
        user_input = input("enter your choice? : ").lower()
        u = ["stone", "paper", "scissor"]
        x = random.choice(u)
        # print(x)
        if (user_input != "stone" and user_input != "paper") and user_input != "scissor":
            print("enter valid input")
            break

        if user_input == x:
            print(
                f'match draw : {user_input} VS {x} \n')
        elif (user_input == "stone" and x == "paper"):
            print(
                f'computer win : {user_input} VS {x} \n')
        elif (user_input == "paper" and x == "scissor"):
            print(
                f'computer win : {user_input} VS {x} \n')
        elif (user_input == "scissor" and x == "stone"):
            print(
                f'computer win : {user_input} VS {x} \n')
        else:
            print(
                f'user won : {user_input} VS {x} \n')


game()
