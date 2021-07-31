import random

lifes_left = 3

while True:
    random_number = random.randint(1,10)
    user = int(input("Please enter a number range(1,10): "))

    if user == random_number:
        print("You have guessed correctly")
        break

    else:

        lifes_left = lifes_left - 1
        print(f'You have {lifes_left} lives left')

        if lifes_left == 0:
            print("You have no lives left, please restart the game")
            break

    print(f'The random number was {random_number}')