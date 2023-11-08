from random import randint




def start_game():
    random_number = randint(0,9)
    health = 3
    print()
    print("Добро пожаловать в игру 'угадай число'")
    game_play(random_number,health)

def game_play(random_number,health):
    print()
    print("загадано число от 0 до 9")
    while health > 0:
        print()
        print(f"кол-во жизней: {health}")
        number = int(input("укажите число: "))
        if number == random_number:
            print()
            print(f"вы угадали! загаданное число {random_number}. кол-во оставшихся жизней: {health}")
            print()
            if input("сыграть заново? 'да' - 1.   'нет'- все остальное ") == "1":
                start_game()
            break
        elif number > random_number:
            print("Загаданное число меньше")
        elif number < random_number:
            print("Загаданное число больше")
        health -= 1
    else:
        print()
        print(f"вы проиграли!! загаданное число {random_number}")
        print()
        if input("сыграть заново? 'да' - 1.   'нет'- все остальное ") == "1":
            start_game()

start_game()