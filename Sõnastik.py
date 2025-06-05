from module import *

while True:
    print("\n Menuu: \n"
    "1 - Tõlgi \n"
    "2 - Lisa uus sõna \n"
    "3 - Paranda sõna \n"
    "4 - Testi teadmisi \n"
    "5 - Välju")
    try:
        valik=int(input("Palun valige menuust üks valik(1-5): "))
        if valik==1:
            while True:
                sona=input("Sisesta sõna: ").lower().strip()
                if sona.isalpha():break
                else:
                    print("Sõna peab koosnema ainult tähtedest!")
            tulemus=tolgi("sonad.txt", sona)
            print(tulemus)
        elif valik==2:
            lisa_sona("sonad.txt")
        elif valik==3:
            paranda_sona("sonad.txt")
        elif valik==4:
            testi_tewissen("sonad.txt")
        elif valik==5:
            break
        else:
            print("Sisestage number vahemikus 1 kuni 5!")
    except:
        print("Vastus peab olema numbriline!")

        