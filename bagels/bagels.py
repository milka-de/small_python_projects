''' Бэйглз
 Правила игры:
 необходимо по подсказкам угадать секретное число из трёх цифр
 pico - если угадана цифра на неправильном месте 
 fermi - если правильная цифра на правильном месте
 bagels - если не содержится правильных цифр
 на угадывание десять попыток'''

import random

num_digits = 10 # константа сколькизначное число
max_guesses = 10 # константа количество попыток

def main():
    print(''' Бэйглз
 Правила игры:
 необходимо по подсказкам угадать секретное число из {} цифр
 pico - если угадана цифра на неправильном месте 
 fermi - если правильная цифра на правильном месте
 bagels - если не содержится правильных цифр'''.format(num_digits))

    while True: # Основной цикл игры
        secret_num = get_secret_num() # число, которое должен угадать игрок
        print('Я загадал число')
        print('У тебя есть {} попыток, чтобы угадать его'.format(max_guesses))

        num_guesses=1
        while num_guesses <= max_guesses:
            guess= ''
            # продолжаем итерации до получения правильной догадки:
            while len(guess) != num_digits or not guess.isdecimal():
                print('Попытка №{}:'.format(num_guesses))
                guess=input('> ')
            clues = get_clues(guess, secret_num)
            print(clues)
            num_guesses +=1

            if guess == secret_num:
                break # число угадано, выходим из цикла
            if num_guesses > max_guesses:
                print('У тебя закончились попытки')
                print('Ответ был {}'.format(secret_num))
        # спрашиваем иигрока, хочет ли он сыграть ещё раз
        print('хочешь ссыграть ещё раз? (да или нет)')
        if not input('> ').lower().startswith('д'):
            break
    print('Спасибо за игру!')

# функция возвращающая строку из num_digits уникальных случайных цифр
def get_secret_num():
    numbers=list('0123456789') 
    random.shuffle(numbers)

    secret_num=''
    for i in range(num_digits):
        secret_num += str(numbers[i])
    return secret_num

# функция возвращающая строку с подсказками
def get_clues(guess, secret_num):
    if guess==secret_num:
        return 'Ты выиграл!'

    clues=[]

    for i in range(len(guess)):
        if guess[i]==secret_num[i]:
            # правильная цифра на правильном месте
            clues.append(' fermi ')
        elif guess[i] in secret_num:
            # правильная цифра на неправильном месте
            clues.append(' pico ')
    if len(clues)==0:
        # правильных цифр нет вообще
        return ' bagels '
    else:
        # сортируем подсказки в алфовитном пордке, чтобы исходный порядок ни чего не выдавал
        clues.sort()
        # склеиваем список подсказок в одно строковое значение
        return ''.join(clues)

# если программа не импортируется, а запускается, производим запуск
if __name__=='__main__':
    main()
