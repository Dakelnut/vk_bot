from datetime import datetime, timedelta
import folder_of_meanings.sup_functions as sup

def generate_answer(date, need_date, today, c ):

    answer = ""


    row = list(c.execute('''SELECT * FROM timetable WHERE date=? ''', (need_date,)))

    if len(row) != 0:
        row = row[0][1:]
        if sup.check_weekend(row):
            answer = "В этот день выходной"
        else:

            if type(date) == str or (type(date) != str and date > 0):

                    for elem in row:
                        if elem != "---":
                            campus = sup.understand_what_campus(elem)
                            answer = "Пары в " + campus
                            break
                        else: continue


            elif need_date == today:


                    for elem in row:
                        if elem != "---":
                            campus = sup.understand_what_campus(elem)
                            answer = "Сегодня пары в " + campus
                            break
                        else:
                            continue

    else:
        answer = "Вероятно это выходной"

    return  answer


