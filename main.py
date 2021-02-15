import re
plik = open("plikDoWczytania.txt", "r")
wynik = 0; niezmienioneHasło = 0;listazad2 = [];cyfra = 0;haslaw8 = [];zad1 = 0;k = 0;l = 1;zad15 = 0;dl = 0;b = 0
zad22 = 0;mm = 0;haselko = 0;zad33 = 0
for linie in plik:
    linie = linie.split()
    wynik += int(linie[1])
    listazad2 += linie[1]
    dlugoscListy = len(linie)
    haslaw8 = linie[2:dlugoscListy] # tablica [z haslami]
    cyfhaslaw8 = len(haslaw8) # ilosc elementow w tablicy z haslami
    listahasel = []
    for ster in range(2, cyfhaslaw8 + 2):
        haslo = linie[ster]

        if haslo not in listahasel:
            listahasel.append(haslo) # ['78u', 'Ogie', 'fwcl', '509', 'Vw5', 'U2U', 'aaa80']
    for ster in listahasel:
        if (len(ster) > 8):
            zad1 += 1
            break # zakoniczenie poniewaz jesili znajdze sie 1 haslo w zakrasie ['78u', 'Ogie', 'fwcl', '509', 'Vw5', 'U2U', 'aaa80']
    #for a in haslaw8:# ['78u'] zad2
        #lista = []
        #dl = len(a)
        #for c in a: # ['Y', '3', 'v', 'H', '2', '2', 'Z', '2', '1', 'A', 'm', '7', 'o', '8']
         #   lista.append(c)
            #for b in range(0,dl):
             #   if lista[k] == lista[l]:
              #      zad15 += 1
               #     if l == dl - 1:
                #        break
                 #   else:
                  #      k += 1
                   #     l += 1

    #zad2
    bufhas = []

    for m in range(2,cyfhaslaw8 + 2):
        haselko = linie[m]
        if haselko not in bufhas:
            bufhas.append(haselko)
    if len(bufhas) < 4:
        zad22 += 1


    #zad3
    malelitery = r"\D"

    bufhas1 = []
    for m3 in range(2, cyfhaslaw8 + 2):
        haselko1 = linie[m3]
        if haselko1 not in bufhas1:
            bufhas1.append(haselko1)
        for s in bufhas1:
            if re.search(malelitery, s):
                print("dop",s)
                zad33 += 1
            else:
                print("nie",s)


for cyfra in listazad2:
    cyfra = int(cyfra)
    if cyfra == 1:
        niezmienioneHasło += 1

#podsumowanie
odzielacz = "-----------------------------------------------------------------------"
print(odzielacz)
print("ilość haseł w pliku = ",wynik)
print(odzielacz)
print("ilość osoub które nie zmieniły hasła = ",niezmienioneHasło)
print(odzielacz)
print("ilosc osub ktore zastosowały conajmniej jedno haslo o dlugosci 8 = " ,zad1)
print(odzielacz)
print("osoby które stosowało mniej niż 4 różne hasła = ",zad22)
print(odzielacz)
print("w swoich hasłach zawarło litery = ",zad33)
print(odzielacz)