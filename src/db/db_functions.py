import random
from sqlalchemy import *
import sqlalchemy
import time
import os
from sqlalchemy.sql.expression import func

from db.database import session, engine, base
from db.models import Words, OverlapWords, SelectWords, FirstWord, Results



def append_words(): #добавление слов в общий список
    #try:
    print(os.listdir())
    print(os.getcwd())
    if not sqlalchemy.inspect(engine).has_table(Words):
        Words.__table__.create(bind=engine, checkfirst=True)
        #base.metadata.tables['words'].create(bind = engine)
        print(base.metadata.tables.values())


    #except:
        ##pass

    # try:
    count = 1
    with open ('./db/russian_nouns.txt', 'r', encoding='utf-8') as f:
        for i in f:
            i = i.rstrip('\n')
            word = Words(name = i)
            session.add(word)
            session.commit()
            print(f'word {i} did add')
            print(count)
            count+=1
    # except:
        print('что то пошло не так append_words')
    # finally:
        session.close()


def append_words_to_overlap(level: int):
    try:
        if not sqlalchemy.inspect(engine).has_table(OverlapWords):
            OverlapWords.__table__.create(bind=engine, checkfirst=True)
    except:
        pass
    try:
        word = session.query(Words).filter(func.length(Words.name) == level).all()
        global len_overlap_table
        len_overlap_table = len(word)
        session.add_all(OverlapWords(name=i.name) for i in word)
        session.commit()
        return True
    except:
        return 'ERROR append overlap'
    finally:
        session.close()


def drop_table_FirstWord(): #удаление таблицы
    try:
        FirstWord.__table__.drop(engine)
    except:
        pass


def drop_table_OverlapWords(): #удаление таблицы
    try:
        OverlapWords.__table__.drop(engine)
    except:
        pass


def drop_table_Words(): #удаление таблицы
    try:
        Words.__table__.drop(engine)
    except:
        pass


def drop_table_SelectWords(): #удаление таблицы
    try:
        SelectWords.__table__.drop(engine)
    except:
        pass


def drop_results_table():
    try:
        Results.__table__.drop(engine)
    except:
        pass


def first_word() -> str:
    try:
        if not sqlalchemy.inspect(engine).has_table(FirstWord):
            FirstWord.__table__.create(bind=engine, checkfirst=True)
    except:
        pass

    try:
        first_word = random.choice(session.query(OverlapWords.name).all())
        add_first_word = FirstWord(name=first_word[0])
        session.add(add_first_word)
        session.commit()
        return first_word[0]
    finally:
        session.close()


def found_len():
    try:
        len = session.query(func.count(OverlapWords.name)).scalar()
        return len
    finally:
        session.close()


def found_len_words_table():
    try:
        len = session.query(func.count(Words.name)).scalar()
        return len
    finally:
        session.close()


def add_in_select_table(word, overlap):
    try:
        if not sqlalchemy.inspect(engine).has_table(SelectWords):
            SelectWords.__table__.create(bind=engine, checkfirst=True)
    except:
        pass

    try:
        add_word = SelectWords(name=word, overlap=overlap)
        session.add(add_word)
        session.commit()
    finally:
        session.close()


def found_word_args(args: list):
    global found_index
    query_str = "session.query(OverlapWords)"
    for i in args:
        query_str = query_str + f".filter(OverlapWords.name.like(f'%{i}%'))"
    query_str = query_str + ".first()"
    word = eval(query_str)
    try:
        session.delete(word)
        session.commit()
        # print(word.name + ' внутри функции аргс')
        return word.name
    except:
        pass
    finally:
        session.close()


def add_results(randomword, finaltime, how_much):
    try:
        if not sqlalchemy.inspect(engine).has_table(Results):
            Results.__table__.create(bind=engine, checkfirst=True)
    except:
        pass
    print(randomword)

    try:
        add_word = Results(name=randomword, timer=finaltime, how_much=how_much)
        session.add(add_word)
        session.commit()
    finally:
        session.close()


def list_results():
    try:
        words = session.query(Results).all()
        x = []
        for i in words:
            x.append(f'name={i.name}, overlap={i.how_much}, timer={i.timer}')
    except:
        return False
    else:
        return x
        
    #return words


def random_word():
    try:
        first_word = random.choice(session.query(OverlapWords.name).all())
        delete_word = session.get(OverlapWords, first_word)
        session.delete(delete_word)
        session.commit()
        return first_word[0]
    finally:
        session.close()


def found_len_words_table():
    try:
        len = session.query(func.count(Words.name)).scalar()
        return len
    finally:
        session.close()


#print(found_len_words_table)
# append_words('app/db/russian_nouns.txt')
# delete_table(OverlapWords)
# append_words_to_overlap(5)
# get_word(5)
# print(random_word())
# compare('малолетка')
# first_word()
# found_word_args(['р', 'т', 'в', 'м', 'й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'о'])
# print(found_len2())

# drop_results_table(Results)
#drop_table_Words()
#check_result()