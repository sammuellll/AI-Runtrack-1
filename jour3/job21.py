# Ecrire un programme qui parcours le fichier “data.txt” et qui compte le nombre d’occurence de chaque lettre(Minuscules et Capitales comptent pour la même lettre) en début de mot. A l’aide du module MatPlotLib, générer un histogramme représentant le pourcentage de présence de chaque lettre en début de mot.
# "Data.txt" dosyasını tarayan ve kelimenin başındaki her harfin geçtiği sayıları (Küçük ve Büyük Harfler aynı harf olarak sayılır) sayan bir program yazın. MatPlotLib modülünü kullanarak, bir kelimenin başındaki her harfin var olma yüzdesini temsil eden bir histogram oluşturun.
import matplotlib.pyplot as plt
from itertools import permutations

liste = []
fichier = open('data.txt', 'r')
for line in fichier:
    line = line.lower()
    x = line.split()
    liste.extend(x)

fichier.close()

liste2 = []
for mot in liste:
    y = list(mot)
    liste2.append(''.join(y[0:2]))


alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",  "x", "y", "z"]
print(len(alphabet))

lstAlphabet = []
comb = permutations(alphabet, 2)
for i in list(comb):
    lstAlphabet.append(''.join(i))

liste3 = []
for alfa in lstAlphabet:
    cnt = 0
    for harf in liste2:
        if harf in alfa:
            cnt = cnt + 1
    liste3.append(cnt)

print(liste3)
print(len(liste3))

liste4 = []
for alfa in alphabet:
    lst = []
    for harf in lstAlphabet:
        if harf[0] == alfa:
            lst.append(harf)
    liste4.append(lst)

#     total = sum(i)
# for chiffre in liste3:
#     cnt = chiffre*100/total
#     liste4.append(cnt)

print(liste4)
