import random

def generate_random_number(min_val, max_val):
    return random.randint(min_val, max_val)

def get_user_input():
    while True:
        try:
            user_input = int(input('Введите ваше число: '))
            return user_input
        except ValueError:
            print('Пожалуйста, введите целое число.')

def check_guess(user_number, target_number):
    if user_number < target_number:
        return 'Больше'
    elif user_number > target_number:
        return 'Меньше'
    else:
        return 'Верно'

def main():
    print('Добро пожаловать в игру «Угадай число»!')
    print('Я загадал число от 1 до 100. Попробуйте угадать его!')

    target_number = generate_random_number(1, 100)
    attempts = 0

    while True:

        user_number = get_user_input()
        attempts += 1

        result = check_guess(user_number, target_number)

        if result == 'Верно':
            print(f'Поздравляю! Вы угадали число {target_number} за {attempts} попыток.')
            break
        else:
            print(result)

if __name__ == '__main__':
    main()