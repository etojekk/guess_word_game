import random
import time

index = 0 # количество угадываний
all_found_time = 0 # общее время поиска

def start():
    while True:
        level = input("Введите сложность от 3 до 16: ")
        try:
           level = int(level)
        except:
           print("Неверные данные, введите число от 3 до 16: ")

        if int(level) < 3 or int(level) > 16:
            print("Неверные данные, введите число от 3 до 16: ")
            continue
        else:
            listwords = read_file(level, 'russian_nouns.txt')
            random_word = random.choice(listwords)
            print(f'Компьютер загадал слово  {random_word.capitalize()}')
            time.sleep(1)
            print("Сейчас он начнёт его угадывать")
            time.sleep(2)
            found_word(random_word, listwords)
            break

def read_file(level: int, filename): #создание списка слов с нужной длиной
    listwords = []
    with open(filename, 'r', encoding='utf-8') as f:
        for i in f:
            i = i.rstrip('\n')
            if len(i) == level:
                listwords.append(i)
    return listwords

def found_word(random_word, listwords):

    global all_found_time
    global index
    global found_time

    len_listwords = len(listwords) # длина списка слов
    found_index = 0 # индекс поиска
    random_letter = {} # список букв для индекса поиска
    found_time = time.time() 
    new_word = random.choice(listwords) # рандомное слово для первого сравнения
    # random.shuffle(listwords) делает список рандомным, на пользу не идёт

    while True:
        if new_word == random_word: # Проверка на совпадение
            found_time = time.time() - found_time
            all_found_time += found_time
            index+=1
            timer = float(all_found_time) / index
            print(f"Компьютер угадал слово {random_word} за {found_time}")
            print(f'Среднее время поиска {timer}')
            print(f'Количество угадываний: {index}')
            print(f'Всего {len(random_word)}-ых слов {len_listwords}')
            print(f'Было проверено {len_listwords - len(listwords)} слов')
            new_game_func()
            break

        try: #Проверка на увеличение совпадений в слове
            if compare(random_word, new_word) > found_index:
                found_index = compare(random_word, new_word)
                random_letter = set(new_word)
                # "выставил индекс совпадения и создал список букв, если индекс у нового слова больше"
        except:
            pass

        if new_word != random_word: #поскольку из-за множества длинна списка может быть меньше индекса - надо их уровнять
            if found_index > len(random_letter):
                found_index = len(random_letter)
            if found_index == 0: #если совпадений нет - новое слово
                new_word = random.choice(listwords)
                continue
            try:
                # слова не совпали
                overlap = random.sample(random_letter, int(found_index))
                new_word = found_word_in_list(listwords, *overlap)
                print(f'В слове {new_word} совпадает {compare(random_word, new_word)} букв')
                # сравнил, сколько букв совпадает
            except:
                found_index-=1


def compare(random_word, userword): # ищет совпадения букв в словах
    overlap = 0
    for i in userword:
        if i in random_word:
            overlap+=1
    return overlap

def found_word_in_list(listwords, *args):
    # вывел список слов, зарандомил его
    for i in listwords:
        if set(args).issubset(i):
            listwords = listwords.remove(i)
            # нашел подходящее слово, убрал из списка, что бы в дальнейшем оно не учавствовало в поиске
            return i
            break

def new_game_func(): # начинает заново
        while True:
        answer = input('Начать новую игру?: ')
        if answer == 'Да' or answer == 'да' or answer == 'lf' or answer == 'LF' or answer == '+':
            start()
            break
        if answer == 'Нет' or answer == 'нет' or answer == 'ytn' or answer == '-':
            print('До скорых встреч!')
            break
        else:
            print('Неверный ввод')
            continue


if __name__ == "__main__":
    start()
