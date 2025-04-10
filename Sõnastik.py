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
from module1 import *
EE=dict(koer="собака", kodu="дом", päike="солнце", mets="лес", palun="пожалуйста", hommik="утро",
        kool="школа", raamat="книга", sinine="синий", taevas="небо")
RU=dict(собака="koer", дом="kodu", солнце="päike", лес="mets", пожалуйста="palun", утро="hommik",
        школа="kool", книга="raamat", синий="sinine", небо="taevas")

while True:
    print("\n Menuu: \n"
    "1 - Tõlgi eesti -> vene \n"
    "2 - Tõlgi vene -> eesti \n"
    "3 - Lisa uus sõna \n"
    "4 - Paranda sõna \n"
    "5 - Testi teadmisi \n"
    "6 - Välju")
    try:
        valik=int(input("Palun valige menuust üks valik(1-6): "))
    except ValueError:
        print("Palun, sisestage arv")
    if valik==1:
        sona=str(input("Sisestage sõna, mida soovite tõlkida: ")).strip().lower()
        if sona in EE:
            print("Vene keeles on sõna: ", EE[sona])
        else:
            print("Vene keeles pole sõna: ", sona)
    elif valik==2:
        print(tolgi_rus_est)
    elif valik==3:
        print(lisa_sona)
    elif valik==4:
        print(paranda_sona)
    elif valik==5:
        print(testi_tewissen)
    elif valik==6:
        break