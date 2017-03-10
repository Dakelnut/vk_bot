from datetime import datetime, timedelta
import folder_of_meanings.sup_functions as sup

def generate_answer(date, need_date, time_of_lessons,today, c ):

    answer = ""

    row = list(c.execute('''SELECT * FROM timetable WHERE date=? ''', (need_date,)))

    if len(row) != 0:
        row = row[0][1:]
        if sup.check_weekend(row):
            answer = "В этот день выходной"
        else:

            if type(date) == str or (type(date) != str and date > 0):


                    for i in range(len(time_of_lessons)):

                        if row[i] == "---":
                            continue
                        else:
                            datetime_now = datetime.today()
                            need_date_2 = (datetime.now() + timedelta(days=date)).date()
                            t = datetime.strptime(time_of_lessons[i], "%H.%M").time()
                            datetime_time_of_lesson = datetime.combine(need_date_2, t)

                            time_left = str(datetime_time_of_lesson - datetime_now).split(':')
                            part_of_answer = time_left[0] + " ч." + time_left[1] + " м."

                            answer = "До пары" + str(need_date_2) + " осталось " + part_of_answer

                            break


            elif need_date == today:
                part_of_answer = ""


                for i in range(len(time_of_lessons)):
                    datetime_now = datetime.today()
                    d = datetime.today().date()
                    t = (datetime.strptime(time_of_lessons[i], "%H.%M") + timedelta(hours=1, minutes=30)).time()
                    datetime_time_of_lesson = datetime.combine(d, t)

                    if datetime_now <= datetime_time_of_lesson:

                        if row[i] == "---":
                            continue
                        else:

                            time_left = round((datetime_time_of_lesson - datetime_now).seconds / 60)

                            if time_left >= 60:
                                time_left = str(datetime_time_of_lesson - datetime_now).split(':')
                                part_of_answer = time_left[0] + " ч. " + time_left[1] + " м. "
                            else:
                                part_of_answer = str(time_left) + " м."
                            answer = "Пара " + row[i].strip("|")[0] + " закончится через " + part_of_answer

                            if time_left <= 5:
                                answer = "Уже скоро!)"
                            break
                    if answer == "":
                        answer = "В этот день больше нет пар"

    else:
        answer = "Вероятно это выходной"

    return answer