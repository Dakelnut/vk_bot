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

                    iter = 0
                    for elem in row:
                        if elem != "---":
                            iter = iter + 1

                        else: continue

                    answer = "Количество пар на " + need_date + " - " + str(iter)




            elif need_date == today:


                    iter = 0

                    for i in range(len(time_of_lessons)):

                        datetime_now = datetime.today()

                        d = datetime.today().date()

                        t = datetime.strptime(time_of_lessons[i], "%H.%M").time()

                        datetime_time_of_lesson = datetime.combine(d, t)

                        if datetime_now <= datetime_time_of_lesson:

                            if row[i] == "---":

                                continue

                            else:

                                iter = iter + 1


                    if iter == 0:
                        answer = "В этот день больше не осталось пар "
                    else:
                        answer = "Сегодня тебе осталось прожить ещё " + str(iter) + " пар "

                    if answer == "":
                        answer = "В этот день больше нет пар "


    else:
        answer = "Вероятно это выходной"

    return answer