import numpy as np


def game_core_v2(number):
    number = np.random.randint(1, 101)  # загадали число
    print("Загадано число от 1 до 100: ", number)

    '''Сначала устанавливаем любое random число, а потом уменьшаем 
    или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''

    count = 0
    first_number = 0
    last_number = 101
    while True:
        predict = (first_number + last_number) // 2
        print("Предполагаемое число: ", predict)
        count += 1
        if number > predict:
            first_number = predict
        elif number < predict:
            last_number = predict
        else:
            print("Количество попыток", count)
            print("------------------------------")
            return (count)  # выход из цикла, если угадали


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число
    Функция принимает функцию, которая реализует игру.
    Функция возвращает среднее количествово попыток.
    '''
    count_list = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы эксперимент был воспроизводим
    random_numbers = np.random.randint(1, 101, size=(1000))

    for number in random_numbers:
        count_list.append(game_core(number))
    score = int(np.mean(count_list))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return (score)


score_game(game_core_v2)