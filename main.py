import random

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
elif start == 2:
    attempts = 5
elif start == 3:
    attempts = 3
else:
    print("Нужно ввести число! Перезапусти программу.")


for i in range(attempts):
    guess = int(input("Введи своё предположение\n>>>"))
    if attempts == 1 and guess != random_number:
        print(f"Ты не угадал. Число было {random_number}\nПопробуй еще раз!")
    else:
        if guess == random_number:
            attempts = 1
            winner_attempt = i + 1
            print(f"Поздравляю! Ты угадал правильное число с {winner_attempt} попытки")
            break
        else:
            print("Неверно!")
            if guess > random_number:
                print(f"Число меньше {guess}")
            else:
                print(f"Число больше {guess}")
    attempts -= 1