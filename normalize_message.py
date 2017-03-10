import nltk
import pymorphy2
import string
# функция по обработке текста и преобразования его в нормализованный список
def tokenize_text(file_text):
    morph = pymorphy2.MorphAnalyzer()
    tokens = file_text.split(" ")
    tokens = [i.lower() for i in tokens if (i not in string.punctuation)]  # удаление пунктуации
    tokens = [i.replace("«", "").replace("»", "") for i in tokens]
    for i in range(len(tokens)):
        p = morph.parse(tokens[i])[0]
        tokens[i] = p.normal_form
    return tokens

