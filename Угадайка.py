import random as rdm

def guess_game():
    print("Добро пожаловать в Угадайку! Чтобы начать играть, введите число от 1 до 100. Чтобы выйти из неё - введите '-1'")
    guess = int(input())
    num = rdm.randint(0, 100)
    if guess != -1:
        while guess != num:
            if guess > num:
                print(f"Неправильно. {guess} больше")
                guess = int(input())
            elif guess < num:
                print(f"Неправильно. {guess} меньше")
                guess = int(input())
        print(f"Правильно! Вы угадали. Ответ: {num}")
        guess_game()


guess_game()
print('Игра окончена. Возвращайтесь снова')


