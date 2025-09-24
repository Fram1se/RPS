import random

def guess_number():
    print("Игра 'Угадай число'!")
    number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Угадайте число от 1 до 100: "))
            attempts += 1
            
            if guess < number:
                print("Слишком маленькое!")
            elif guess > number:
                print("Слишком большое!")
            else:
                print(f"Поздравляю! Вы угадали за {attempts} попыток!")
                break
        except ValueError:
            print("Пожалуйста, введите целое число!")

# Запускаем игру
guess_number()