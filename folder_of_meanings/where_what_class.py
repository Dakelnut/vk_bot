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

                answer = "\tРасписание на "+ need_date + " \n"
                for i in range(len(row)):
                    answer = answer + time_of_lessons[i] + " " + row[i] + " \n"


            elif need_date == today:

                    for i in range(len(time_of_lessons)):
                        datetime_now = datetime.today()
                        d = datetime.today().date()
                        t = datetime.strptime(time_of_lessons[i], "%H.%M").time()
                        datetime_time_of_lesson = datetime.combine(d, t)

                        if datetime_now <= datetime_time_of_lesson:

                            if row[i] == "---":
                                continue
                            else:
                                row_list = row[i].split("|")
                                answer = "Пара " + row[0] + " в аудитории " + row[1]
                                break
                    if answer == "":
                        answer = "Уточни дату, на сегодня нет пар)"

    else:
        answer = "Вероятно это выходной"


    return answer

