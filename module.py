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

def salvestamine_faili(Sõnastik: str, d: dict):
    with open(Sõnastik, 'w', encoding='utf-8-sig') as file:
        for key, value in d.items():
            file.write(f"{key}:{value}\n")

def laadimine_failist(Sõnastik: str):
    d = {}
    try:
        with open(Sõnastik, 'r', encoding='utf-8-sig') as file:
            for line in file:
                parts = line.strip().split(' - ')
                if len(parts) == 2:
                    key, value = line.strip().split(' - ')
                    d[key] = value
    except FileNotFoundError:
        pass
    return d

#1
def tolgi_est_rus(EE: dict, sona: str):
    """ Funktsioon tõlgib eesti keele sõna vene keelde.
    :param sona: sõna, mida soovitakse tõlkida
    :param EE: eesti keele sõnastik
    :param RU: vene keele sõnastik
    :type sona: str
    :type EE: dict
    :type RU: dict
    :return: vene keele tõlge
    """
    return EE.get(sona)

#2
def tolgi_rus_est(RU: dict, sona: str):
    """ Funktsioon tõlgib vene keele sõna eesti keede.
    :param sona: sõna, mida soovitakse tõlkida
    :param EE: eesti keele sõnastik
    :param RU: vene keele sõnastik
    :type sona: str
    :type EE: dict
    :type RU: dict
    :return: eesti keele tõlge
    """
    return RU.get(sona)

#3
def lisa_sona(EE: dict, RU: dict, est: str, rus: str):
    """ Funktsioon lisab sõna eesti-vene sõnastikku.
    :param est: eesti keele sõna
    :param rus: vene keele sõna
    :param EE: eesti keele sõnastik
    :param RU: vene keele sõnastik
    :type est: str
    :type rus: str
    :type EE: dict
    :type RU: dict
    :return: sõna lisamine sõnastikku
    """
    est=str(input("Sisestage sõna eesti keeles: ")).strip().lower()
    rus=str(input("Sisestage sõna vene keeles: ")).strip().lower()
    EE[est] = "rus"
    RU[rus] = "est"
    return est, rus

#4
def paranda_sona(EE: dict, RU: dict, s: str, new_rus: str, new_est: str):
    """ Funktsioon parandab sõna eesti-vene sõnastikus.
    :param EE: eesti keele sõnastik
    :param RU: vene keele sõnastik
    :type EE: dict
    :type RU: dict
    :return: sõna parandamine sõnastikus
    """
    s = input("Sisestage sõna, mida soovite parandada: ").strip().lower()
    if s in EE:
        print(f"Sõna leiti eesti-vene sõnastikust: {s} -> {EE[s]}")
        new_rus = input("Sisestage parandatud sõna vene keeles: ").strip().lower()
        EE[s] = new_rus 
        RU[new_rus] = s  
        print("Sõna parandati edukalt!")
    elif s in RU:
        print(f"Sõna leiti vene-eesti sõnastikust: {s} -> {RU[s]}")
        new_est = input("Sisestage parandatud sõna eesti keeles: ").strip().lower()
        RU[s] = new_est 
        EE[new_est] = s 
        print("Sõna parandati edukalt!")
    else:
        print("Sõna ei leitud sõnastikust")

#5
def testi_tewissen(EE: dict, RU: dict, answer: str):
    """ Funktsioon testib teadmisi eesti-vene sõnastikus.
    :param EE: eesti keele sõnastik
    :param RU: vene keele sõnastik
    :type EE: dict
    :type RU: dict
    :return: testi tulemused
    """
    correct=0
    total=0
    print("Testi algus\n"
          "Sisestage sõna tõlge eesti keeles")
    for est, rus in EE.items():
        total +=1
        answer=input(rus).strip().lower()
        if answer==est:
            print("Õige!")
            correct +=1
        else:
            print(f"Vale, õige vastus on - {est}")
    print(f"Test on lõppenud! Teie tulemus: {correct/total*100}%")