# Практическая работа - Двуязычный словарь в Python (использование dict())
#  Эстонский язык 🇪🇪
#  Русский язык 🇷🇺
# Описание задачи:
# Создайте программу, позволяющую пользователю работать с двуязычным эстонско-русским словарем.
# Словарь хранится в Python в виде структуры данных dict().
# Основные функции программы:
#  Перевод с эстонского на русский
#  Перевод с русского на эстонский
#  Добавление нового слова в словарь
#  Исправление слова в словаре
#  Если пользователь заметит, что слово написано неправильно, его можно исправить.
#     Если пользователь заметил неправильно написанное слово, оно исправляется. Если пользователь нашел неправильно написанное слово, оно исправляется.
#         Пользователь вводит перевод.
#         Программа сообщает, правильным или неправильным был ответ.
#  В конце теста выводится процент правильных ответов (%).
# Дополнительные пункты:
#  При желании добавьте функцию, которая читает слово вслух (text-to-speech). 🎤 🎤
# Структура программы:
#  Данные изначально хранятся в Python в виде dict():
#  sonastik = {
#  'dog': 'dog',
#  'cat': 'cat',
#  'house': 'house',
#  'car': 'car',
#  'sun': 'солнце'
#  }
#  Программа должна содержать не менее 5 отдельных функций, например:
#  tolgi_est_rus(sona)
#  tolgi_rus_est(sona)
#  lisa_sona()
#  paranda_sona()
#  testi_tewissen()
#  Программа должна работать в бесконечном цикле, пока пользователь не решит выйти.
# Programmi näidis:
# Tere tulemast eesti-vene sõnastikku!

# Valikud:
# 1 - Tõlgi eesti -> vene
# 2 - Tõlgi vene -> eesti
# 3 - Lisa uus sõna
# 4 - Paranda sõna
# 5 - Testi teadmisi
# 6 - Välju
# Tee oma valik: 1

# Sisesta sõna eesti keeles: koer
# Tõlge vene keelde: собака

# Tee oma valik: 3
# Sisesta uus sõna eesti keeles: arvuti
# Sisesta selle sõna vene tõlge: компьютер
# Sõna lisatud!

# Tee oma valik: 5
# Testi teadmisi alustatakse!
# Sisesta vene tõlge sõnale 'maja': дом
# Õige!
# Sisesta vene tõlge sõnale 'päike': солнце
# Õige!
# Test lõppenud! Sinu tulemus: 100%
EE=dict()
RU=dict()

#1
def tolgi_est_rus(EE: dict, sona: str):
    """
    """
    sona=str(input("Введите слово которое хотите перевести ")).strip().lower()
    print(EE.get(sona))

#2
def tolgi_rus_est(RU: dict, sona: str):
    """
    """
    sona=str(input("Введите слово которое хотите перевести ")).strip().lower()
    print(RU.get(sona))

#3
def lisa_sona(EE: dict, RU: dict, est: str, rus: str):
    """
    """
    est=str(input("Введите слово на естонском")).strip().lower()
    rus=str(input("Введите слово на русском")).strip().lower()
    EE["est"] = "rus"
    RU["rus"] = "est"
    return est, rus

#4
def paranda_sona():
    """
    """
    S=str(input("Введите слово которое хотите изменить ")).strip().lower()

    EE["est"] = "rus"
    RU["rus"] = "est"

 # testi_tewissen()
