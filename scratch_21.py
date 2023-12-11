import re

def ind(index):
    pattern = r'^\d{6}$'
    return re.match(pattern, index) is not None
index = input("Введите почтовый индекс: ")
if ind(index):
    print("Введенный почтовый индекс корректен.")
else:
    print("Введенный почтовый индекс некорректен.")