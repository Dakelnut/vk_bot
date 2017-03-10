import normalize_message
import re
import sqlite3
import sys
from datetime import datetime, timedelta
import time
import folder_of_meanings.sup_functions as sup
import folder_of_meanings.where_what_class as mean_one
import folder_of_meanings.in_what_campus as mean_two
import folder_of_meanings.when_pairs_start as mean_three
import folder_of_meanings.what_time_pass_leave_have as mean_four
import folder_of_meanings.how_many_pairs as mean_five
import folder_of_meanings.what_pairs as mean_six
import folder_of_meanings.what_teachers as mean_seven





list_of_themes = [
    "where_what_class",

    "in_what_campus",

    'when_pairs_start',

    'what_time_pass_leave_have',

    'how_many_pairs',

    "what_pairs",

    "what_teachers"]


def understand_meaning(message,name_of_bd):


    # функция по обработке текста и преобразования его в нормализованный список
    try:
        our_list_message = normalize_message.tokenize_text(message)
    except BaseException as e:
        raise e
    conn = sqlite3.connect(name_of_bd)
    c = conn.cursor()

    dict = {}
    #Поставить проверку на то что словарь пустой
    for theme in list_of_themes:
        for elem in our_list_message:
            row = list(c.execute('''SELECT * FROM %s WHERE key_word=? ''' % theme, (elem,)))

            if len(row) != 0:
                dict.update({theme: dict.setdefault(theme, 0) + row[0][1]})
    conn.close()
    try:
        if (len(dict.values()) == 0) or dict.values() == None:
            ans = "К сожалению, я не понял того, что вы попросили, попробуйте ещё раз!"
            return ans
        else:
            result = sup.get_key(dict, max(dict.values()))
    except BaseException as e:

        raise e

    date = understanding_date(our_list_message,name_of_bd)

    return calculating_answer(result,date,name_of_bd)

def understanding_date(our_list_message,name_of_bd):

    current_day_of_week = datetime.today().isoweekday()


    conn = sqlite3.connect(name_of_bd)
    c = conn.cursor()

    iter_of_time = None
    date = None
    daydelta = None

    for elem in our_list_message:

        row = list(c.execute('''SELECT * FROM day WHERE key_word=? ''',(elem,)))

        if len(row) != 0:
            iter_of_time = float(row[0][1])


        if re.search(r'\d{1,2}.\d{2}.\d{2}', elem) != None:
            date = elem

    conn.close()



    if iter_of_time != None:

        if iter_of_time < 10:
            if iter_of_time == 0 or iter_of_time == 0.5:
                daydelta = 0
            else: daydelta = iter_of_time


        elif iter_of_time > 10:
            iter_of_time = iter_of_time - 10

            if iter_of_time > current_day_of_week:
                daydelta = iter_of_time - current_day_of_week

            elif current_day_of_week > iter_of_time:
                daydelta = (7 - current_day_of_week) + iter_of_time

            elif current_day_of_week == iter_of_time:
                daydelta = 7
    elif date != None:
        daydelta = date

    elif  iter_of_time == None and date == None and daydelta == None :
        daydelta = 0


    return daydelta


def calculating_answer(theme_of_message,date,name_of_bd):

    try:

        conn = sqlite3.connect(name_of_bd)
        c = conn.cursor()
        now = datetime.today().time().strftime("%H.%M")
        today = datetime.today().date().strftime("%d.%m.%y")
        time_of_lessons = ['9.00', '10.40', '13.00', '14.40', '16.20' , '18.00']
        answer = "Default answer"



        if type(date) != str :
            need_date = (datetime.now() + timedelta(days=date)).strftime("%d.%m.%y")
        else: need_date = date


        if theme_of_message == "where_what_class":
            answer = mean_one.generate_answer(date, need_date, time_of_lessons,today, c )

        elif theme_of_message == "in_what_campus":
            answer = mean_two.generate_answer(date, need_date, today, c)

        elif theme_of_message == 'when_pairs_start':
            answer = mean_three.generate_answer(date, need_date, time_of_lessons, today, c)

        elif theme_of_message == 'what_time_pass_leave_have':
            answer = mean_four.generate_answer(date, need_date, time_of_lessons, today, c)

        elif theme_of_message == 'how_many_pairs':
            answer = mean_five.generate_answer(date, need_date, time_of_lessons, today, c)

        elif theme_of_message == "what_pairs":
            answer = mean_six.generate_answer(date, need_date, time_of_lessons, today, c)

        elif theme_of_message == "what_teachers":
            answer = mean_seven.generate_answer(date, need_date, time_of_lessons, today, c)



        else:
            answer = "Бот не смог определить смысл сообщения("


        conn.close()


        return answer
    except BaseException as e:
        raise e



