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
kitalalndo_szam=szamok[random.randint(0,len(szamok))]
tipp=input("Kérek egy egész számot 1 és 100 között: ")

while(not tipp.isdecimal()):
    print("Egész számot adj meg!")
    tipp=input("Kérek egy egész számot 1 és 100 között: ")
tipp=int(tipp)
if (tipp<kitalalndo_szam):
    print("A tippelt szám kisebb, mint a kitalálandó szám.")
elif (tipp<kitalalndo_szam):
    print("A tippelt szám nagyobb, mint a kitalálandó szám.")
while(tipp!=kitalalndo_szam):
    tipp=input("Kérek egy egész számot 1 és 100 között: ")
    while(not tipp.isdecimal()):
        print("Egész számot adj meg!")
        tipp=input("Kérek egy egész számot 1 és 100 között: ")
    tipp=int(tipp)
    if (tipp<kitalalndo_szam):
        print("A tippelt szám kisebb, mint a kitalálandó szám.")
    elif (tipp<kitalalndo_szam):
        print("A tippelt szám nagyobb, mint a kitalálandó szám.")
        
print("Gratulálok, kitaláltad a számot!")
    