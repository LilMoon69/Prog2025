import random

szamok=[]
#100 elemű lista feltöltése 1-99 közötti véletlenszamokkal

#........... szam generalasa

for i in range(100):
    rszam= random.randint(1,100)
    szamok.append(rszam)
print(szamok)
jatek_szam = 0
nem_talaltDB= 0
kitalalndo_szam= random.randint(1,100)