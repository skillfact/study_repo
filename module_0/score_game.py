import numpy as np
        
        
def score_game(game_core, start=1, end=100, quant=1000):
    '''Запускаем игру quant раз, чтобы узнать, как быстро игра угадывает число'''
    # или можно добавить input-ы
    if start > end:
        print('Ошибка ввода интервала')
        return
        
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(start,end+1, size=(quant))
    
    for number in random_array:
        count_ls.append(game_core(number, start, end))
    
    score = int(np.mean(count_ls))
    
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


def game_core_v3(number, start, end):
    '''Сначала устанвим интервал в половину возможных чисел, потом уменьшаем интервал в 2 раза пока не полчим искомое число.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    predict_high = int(end/2)
    predict_low = start  
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

            
score_game(game_core_v3,1,100,1000)