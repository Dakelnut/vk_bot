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

                answer = answer + "\t" + need_date
                for i in range(len(time_of_lessons)):
                    if row[i] == "---":
                        continue
                    else:
                        subject_class = row[i].split("|")
                        name_of_subj_and_tutor = list(c.execute('''SELECT * FROM cypher WHERE name_of_cypher=? ''', (subject_class[0],)))[0][1:]
                        answer = answer +  "\n" + time_of_lessons[i] + " " + name_of_subj_and_tutor[0] + "\nАудитория " + subject_class[1] + "\nПреподаватель: " + name_of_subj_and_tutor[1] + "\n"



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
                            subject_class = row[i].split("|")
                            name_of_subj_and_tutor = list(c.execute('''SELECT * FROM cypher WHERE name_of_cypher=? ''', (subject_class[0],)))[0][1:]
                            answer = answer + "\t" + need_date + "\n" + time_of_lessons[i] + " " + \
                                     name_of_subj_and_tutor[0] + "\nАудитория " + subject_class[
                                         1] + "\nПреподаватель " + name_of_subj_and_tutor[1] + "\n"

                    if answer == "":
                        answer = "В этот день больше нет пар"



    else:
        answer = "Вероятно это выходной"


    return answer