import random
import time
from fastapy_word_parser.new_create_test.db.db_functions import (random_word, found_word_args, found_len,
                                    append_words_to_overlap, first_word, add_results, add_in_select_table,
                                     drop_table_FirstWord, drop_table_OverlapWords, drop_table_SelectWords)


def update_args(firstword):

    found_index = 0
    random_letter = []
    len_overlap_table = found_len()
    randomword = random_word()
    timer = time.time()

    while True:
        if randomword == firstword:
            timer = time.time() - timer
            # print(timer)
            how_much = len_overlap_table - found_len()
            add_results(randomword, timer, how_much)
            return randomword

        compar = compare(firstword, randomword)
        if compar > found_index:
            found_index = compar
            random_letter = set(randomword)
        if found_index > len(random_letter):
            found_index = len(random_letter)

        add_in_select_table(randomword, compar)
        overlap = random.sample(random_letter, int(found_index))
        randomword = found_word_args(overlap)

        while True:
            if randomword:
                break
            found_index-=1
            if found_index == 0:
                randomword = random_word()
                break
            overlap = random.sample(random_letter, int(found_index))
            randomword = found_word_args(overlap)
            # print(f'word in found {randomword}')


def compare(userword, random_word):
    overlap = 0
    for i in userword:
        if i in random_word:
            overlap+=1
    return overlap


def start(len_word: int):
    drop_table_FirstWord()
    drop_table_SelectWords()
    drop_table_OverlapWords()
    append_words_to_overlap(len_word)
    firstword = first_word()
    update_args(firstword)


if __name__ == "__main__":
    start(20)
