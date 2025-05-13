import random
from time import process_time

random_number = random.randint(1, 101)
print(random_number)

start = int(input("Добро пожаловать в игру «Угадай число»!\n"
      "Я загадал число от 1 до 100.\n"
      "У тебя есть 5 попыток угадать правильное число.\n\n"
      "Выбери уровень сложности:\n"
      "1. Легкий (10 попыток)\n"
      "2. Средний (5 попыток)\n"
      "3. Сложный (3 попытки)\n\n"
      "Введи свой выбор\n"
      ">>>"))

attempts = None

if start == 1:
    attempts = 10
    print("Отлично! Ты выбрал легкий уровень сложности.\n"
            "Давай начнем игру!")
    while attempts is not None and attempts != 0:
        guess = int(input("Введи своё предположение\n>>>"))
        if attempts == 1 and guess != random_number:
            print(f"Ты не угадал. Число было {random_number}\nПопробуй еще раз!")
        else:
            if guess == random_number:
                winner_attempt = 11 - attempts
                attempts = 1
                print(f"Поздравляю! Ты угадал правильное число с {winner_attempt} попытки")
            else:
                print("Неверно!")
                if guess > random_number:
                    print(f"Число меньше {guess}")
                else:
                    print(f"Число больше {guess}")
        attempts -= 1
elif start == 2:
    attempts = 5
    print("Отлично! Ты выбрал средний уровень сложности.\n"
            "Давай начнем игру!")
    while attempts is not None and attempts != 0:
        guess = int(input("Введи своё предположение\n>>>"))
        if attempts == 1 and guess != random_number:
            print(f"Ты не угадал. Число было {random_number}\nПопробуй еще раз!")
        else:
            if guess == random_number:
                winner_attempt = 6 - attempts
                attempts = 1
                print(f"Поздравляю! Ты угадал правильное число с {winner_attempt} попытки")
            else:
                print("Неверно!")
                if guess > random_number:
                    print(f"Число меньше {guess}")
                else:
                    print(f"Число больше {guess}")
        attempts -= 1
elif start == 3:
    attempts = 3
    print("Отлично! Ты выбрал сложный уровень сложности.\n"
            "Давай начнем игру!")
    while attempts is not None and attempts != 0:
        guess = int(input("Введи своё предположение\n>>>"))
        if attempts == 1 and guess != random_number:
            print(f"Ты не угадал. Число было {random_number}\nПопробуй еще раз!")
        else:
            if guess == random_number:
                winner_attempt = 4 - attempts
                attempts = 1
                print(f"Поздравляю! Ты угадал правильное число с {winner_attempt} попытки")
            else:
                print("Неверно!")
                if guess > random_number:
                    print(f"Число меньше {guess}")
                else:
                    print(f"Число больше {guess}")
        attempts -= 1
else:
    print("Нужно ввести число! Перезапусти программу.")