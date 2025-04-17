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
from module import *
EE = laadimine_failist('EE.txt')
RU = laadimine_failist('RU.txt')

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
        continue
    if valik == 1:
        sona = str(input("Sisestage sõna, mida soovite tõlkida: ")).strip().lower()
        translation = tolgi_est_rus(EE, sona)
        print(f"Vene keeles on sõna: {translation}")
    elif valik == 2:
        sona = str(input("Sisestage sõna, mida soovite tõlkida: ")).strip().lower()
        translation = tolgi_rus_est(RU, "")
        print(f"Vene keeles on sõna: {translation}")
    elif valik == 3:
        lisa_sona(EE, RU, "", "")
        salvestamine_faili('EE.txt', EE)
        salvestamine_faili('RU.txt', RU)
    elif valik == 4:
        paranda_sona(EE, RU, "", "", "")
        salvestamine_faili('EE.txt', EE)
        salvestamine_faili('RU.txt', RU)
    elif valik == 5:
        testi_tewissen(EE, RU, "")
    elif valik == 6:
        salvestamine_faili('EE.txt', EE)
        salvestamine_faili('RU.txt', RU)
        break
        