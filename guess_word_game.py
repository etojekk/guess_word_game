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
            start_found(listwords, random_word)
            break

def read_file(level: int, filename): #создание списка слов с нужной длиной
    wlvl = []
    with open(filename, 'r', encoding='utf-8') as f:
        for i in f:
            i = i.rstrip('\n')
            if len(i) == level:
                wlvl.append(i)
    return wlvl


def start_found(listwords, userword):
    new_word = random.choice(listwords)
    found_word(new_word, userword, listwords)

def found_word(new_word, userword, listwords):
    time.sleep(1)
    print("Сейчас он начнёт его угадывать")
    time.sleep(2)

    global all_found_time
    global index
    global found_time

    len_listwords = len(listwords)
    found_index = 0
    overlap = []
    random_letter = []
    found_time = time.time()
    # random.shuffle(listwords) делает список рандомным, на пользу не идёт

    while True:
        if new_word == userword: # Проверка на совпадение
            found_time = time.time() - found_time
            all_found_time += found_time
            index+=1
            timer = float(all_found_time) / index
            print(f"Компьютер угадал слово {userword} за {found_time}")
            print(f'Среднее время поиска {timer}')
            print(f'Количество угадываний: {index}')
            print(f'Всего {len(userword)}-ых слов {len_listwords}')
            print(f'Было проверено {len_listwords - len(listwords)} слов')
            new_game_func()
            break

        try: #Проверка на увеличение совпадений в слове
            if compare(userword, new_word) > found_index:
                found_index = compare(userword, new_word)
                random_letter = list(new_word)
                # "выставил индекс совпадения и создал список букв, если индекс у нового слова больше"
        except:
            pass

        if new_word != userword:
            if found_index == 0:
                new_word = random.choice(listwords)
                continue
            try:
                # слова не совпали
                overlap = random.sample(random_letter, int(found_index))
                new_word = found_word_in_list(listwords, *overlap)
                print(f'В слове {new_word} совпадает {compare(userword, new_word)} букв')
                # сравнил, сколько букв совпадает
            except:
                found_index-=1
                continue


def compare(userword, gameword): # ищет совпадения букв в словах
    overlap = 0
    for i in gameword:
        if i in userword:
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
        if answer == 'Да' or answer == 'да' or answer == '+':
            start()
            break
        if answer == 'Нет' or answer == 'нет':
            print('До скорых встреч!')
            break
        else:
            print('Неверный ввод')
            continue


if __name__ == "__main__":
    start()
