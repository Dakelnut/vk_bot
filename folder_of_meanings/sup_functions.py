import re

def check_weekend(row):
    it = 0
    for elem in row:
        if elem == "---":
            it = it + 1
    if it == 6:
        return True
    else: return False

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


def understand_what_campus(row):
    if re.search(r'([А]{1}\d{2,3})|(ИВЦ)', row) != None and row != "---":
        return "МИРЭА"
    elif row != "---" and re.search(r'[|]{1}\d{3}|(ФОК)', row):
        return "МГУПИ"

