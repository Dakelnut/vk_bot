import vk_requests
from xlrd import xldate_as_tuple
import xlrd
from time import sleep
from datetime import datetime
from itertools import cycle
from collections import Counter
import nltk
from nltk.corpus import stopwords
import string
import pymorphy2
import sys
import re
import pickle
import calendar
import listening_vk
import understand_message
import traceback
import os.path

smart_timetable = {}


main_token = ""


class TimeTableBot():

    token = ""

    api = None

    name_of_bd = 'timetable.db'

    version = "v =5.45, oauth = 1"

    key_words = 0

    listen_chat = False



    def __init__(self,*args):
        try:

            if len(args) == 1:
                token = args[0]
                self.token = token
                self.api = vk_requests.create_api(access_token=token)
            else:
                app_id = args[0]
                login = str(args[1])
                password = str(args[2])
                self.api = vk_requests.create_api(app_id=app_id, login=login, password=password)
        except Exception as e:
            print(e)
            sys.exit()


    def main_method(self):

        while True:
            try:


                while True:
                    try:
                        dict_of_messages = listening_vk.get_new_message(self.api, self.listen_chat)
                    except BaseException as a:
                        print(a)
                        sleep(0.15)
                        continue
                    else: break


                for author,message in dict_of_messages.items():
                    answer = understand_message.understand_meaning(message,self.name_of_bd)
                    sleep(1)

                    if author > 2000000000:
                        self.api.messages.send(oauth='1', v='5.45', chat_id=(author - 2000000000), message=answer)
                    else:
                        self.api.messages.send(oauth='1', v='5.45', user_id=author, message=answer)

            except BaseException as a:

                answer = "Поздравляю вы только что обнаружили ошибку, в результате которой я сломался((( Но я самостоятельный - поэтому ща перезапущусь и сможете снова задать вопросы)" + "\n"

                for author, message in dict_of_messages.items():

                    if author > 2000000000:
                        self.api.messages.send(oauth='1', v='5.45', chat_id=(author - 2000000000), message=answer)
                    else:
                        self.api.messages.send(oauth='1', v='5.45', user_id=author, message=answer)
                    sleep(0.45)


                if os.path.exists("errors.txt"):
                    f = open('errors.txt', 'a')
                else:
                    f = open('errors.txt', 'w')
                f.write("------------------------------------------------" + "\n")
                f.write(str(dict_of_messages) + "\n")
                f.write(str(traceback.format_exc()) + "\n")
                f.close()
                sleep(3)
                continue



def main():

    bot = TimeTableBot(main_token).main_method()

if "__main__" == __name__:
    main()


