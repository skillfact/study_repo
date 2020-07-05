import numpy as np
        
        
def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    
    for number in random_array:
        count_ls.append(game_core(number))
    
    score = int(np.mean(count_ls))
    
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


def game_core_v3(number):
    '''Сначала устанвим интервал в половину возможных чисел, потом уменьшаем интервал в 2 раза пока не полчим искомое число.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    predict_high = 50
    predict_low = 1  
    tmp = 0
    
    while number != predict_high and number != predict_low:
        count+=1
        if number not in range(predict_low,predict_high+1): 
            # сдвинем интервал 
            tmp = predict_low
            predict_low = predict_high
            predict_high += predict_high - tmp
        # сократим интервал поиска
        predict_high -= int((predict_high - predict_low)/2)
    
    return(count) # выход из цикла, если угадали

            
score_game(game_core_v3)