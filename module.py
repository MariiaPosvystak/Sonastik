import random

#1
def tolgi(fail:str, sona: str):
    """ 
    """
    s=("Seda sõna ei ole sõnaraamatus!")
    with open(fail, 'r', encoding="utf-8-sig") as f:
        sonad = []
        for rida in f:
            sonad.append(eval(rida.strip()))
    for kirje in sonad:
        if kirje['est'].lower() == sona.lower():
            s=(f"{sona} - rus: {kirje['rus']}")
            break
        elif kirje['rus'].lower()==sona.lower():
            s=(f"{sona} - est: {kirje['est']}")
            break
    return s

#2
def lisa_sona(fail: str):
    """ 
    """
    while True:
        est_sona=str(input("Sisesta sona eesti keeles:")).lower().strip()
        if est_sona.isalpha(): break
        else: 
            print("Sõna peab koosnema ainult tähtedest!")
    while True:
        rus_sona=str(input("Sisesta sona vene keeles:")).lower().strip()
        if rus_sona.isalpha(): break
        else:
             print("Sõna peab koosnema ainult tähtedest!")

    uus_sona = {'est': est_sona, 'rus': rus_sona}
    with open(fail, 'a', encoding="utf-8-sig") as f :
        f.write(str(uus_sona)+'\n')
    print("Sõna on lisatud!")

#3
def paranda_sona(fail: str):
    """
    """
    s=("Seda sõna ei ole sõnaraamatus!")
    while True:
        sona = input("Sisestage sõna, mida soovite muuta: ")
        if sona.isalpha(): break
        else:
            print("Sõna peab sisaldama ainult tähti!")
    with open(fail, 'r', encoding="utf-8-sig") as f:
        sonad = []
        for rida in f:
            sonad.append(eval(rida.strip()))
        indeks=-1
        i=0
        while i< len(sonad):
            kirje=sonad[i]
            if sona.lower() in [kirje["est"].lower(), kirje["rus"].lower()]:
                h=(f"est: {kirje['est']}, rus: {kirje['rus']}")
                indeks=i
                break
            i+=1
        print(s)
    while True:
        uus_sona_ee=str(input("Sisesta sona eesti keeles:")).lower().strip()
        if uus_sona_ee.isalpha(): break
        else: 
            print("Sõna peab koosnema ainult tähtedest!")
    while True:
        uus_sona_ru=str(input("Sisesta sona vene keeles:")).lower().strip()
        if uus_sona_ru.isalpha(): break
        else:
             print("Sõna peab koosnema ainult tähtedest!")
    sonad[i] = {'est': uus_sona_ee, 'rus': uus_sona_ru}
    with open(fail, 'w', encoding="utf-8-sig") as f :
        for kirje in sonad:
            f.write(str(kirje)+'\n')
    print("Sõna on muudatud!")

#4
def testi_tewissen(fail: str):
    """ 
    """
    with open(fail, 'r', encoding='utf-8-sig') as f:
        sonad = []
        for rida in f:
            sonad.append(eval(rida.strip()))
    print("Test")
    print("Reeglid: ma annan teile valitud keeles sõna ja te tõlgite selle teise keelde. Väljumiseks kirjutage „exit“.")
    õigesti = 0
    kõik = 0
    while True:
        random_sõnastik = random.choice(sonad)
        while True:
            language = str(input("Valige keel, millest tõlkida (est, rus): ")).strip().lower()
            if language == 'rus' or language == 'est':
                break
            else:
                print("Keel peab olema:'est' või 'rus'!")
        random_sone = random_sõnastik[language]
        while True:
            language1 = str(input("Valige keel, millesse tõlkida (est, rus): ")).strip().lower()
            if language1 == 'rus' or language1 == 'est':
                if language1 != language:
                    break
                else:
                    print("Valige keel, millesse soovite tõlkida")
            else:
                print("Keel peab olema:'est' või 'rus'!")
        print(f"Tõlgi sõna '{random_sone}' suust suhu '{language}' keelel '{language1}'")
        vastus = input("Teie vastus (või „exit“, et väljuda): ").strip().lower()
        if vastus == "exit":
           print(f"Õiged vastused: {õigesti} / {kõik}")
           print("Test on lõppenud!")
           break
        kõik = kõik + 1
        õigest_vastus = random_sõnastik[language1]
        if vastus == õigest_vastus:
            print("Õige!")
            õigesti = õigesti + 1
        else:
            print(f"Vale! Õige vastus on: {õigest_vastus}")