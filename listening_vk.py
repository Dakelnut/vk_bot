from time import sleep


def filtr(ls):
    if ls['message'].get('chat_id') != None:
        if ls['message']['chat_id'] == 1:
            return True
        else:
            return False
    else:
        return False

def filtr2(ls):
    if ls['message'].get('user_id') != None:
        if ls['message']['user_id'] == 404544337:
            return True
        else:
            return False
    else:
        return False



def get_new_message(api,flag):

    dict_of_messages = {}

    try:
        while True:
            m = api.messages.getDialogs(unread=1)

            if m['count'] != 0:

                for elem in m['items']:

                    if elem['message']['body'].find("бт ") != -1:

                        if elem['message'].get('chat_id') != None:
                            dict_of_messages.update([(2000000000 + elem['message']['chat_id'], elem['message']['body'])])
                            api.messages.markAsRead(peer_id=str(2000000000 + elem['message']['chat_id']), oauth=1, v=5.45)
                        else:
                            dict_of_messages.update([(elem['message']['user_id'], elem['message']['body'])])
                            api.messages.markAsRead(peer_id=str(elem['message']['user_id']), oauth=1, v=5.45)
                    else:
                        continue
                return dict_of_messages

            else:
                sleep(0.45)
    except Exception as e:
        raise e
