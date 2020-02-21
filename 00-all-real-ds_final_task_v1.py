import numpy as np


def game_core_v1(number, predict=50, count=0):
    '''каждую итерацию уменьшаем диапазон искомого в 2 раза'''
    range=[1, 101]
    while predict != number:
        count += 1
        if predict < number:
            range[0] = predict
            predict = int((predict + range[1]) / 2)
        elif predict > number:
            range[1] = predict
            predict = int((predict + range[0]) / 2)
    return count


def score_game(game_core_v1):
    '''Запускаем игру 1000 раз, чтоб узнать как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core_v1(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return (score)


# запускаем
score_game(game_core_v1)
