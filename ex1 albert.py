# Créé par BOSSEBP, le 18/12/2020 en Python 3.4
#devine le nombre déterminer par l'ordinateur entre 1 et 100

from random import*
import scorelib as sco
pseudo=input("Tu t'appelle comment déjà ???") #pour le tableau des scores
pseudo=" "+pseudo
#min=int(input("Quelle valeur minimale ?"))
#max=int(input("Quelle valeur maximale ?"))
prix=randint(1,100)
propo=False
tentative=0
while propo!=prix:
    propo=int(input("C'est quoi le nombre qu'a choisi Albert selon toi ????? (entre 1 et 100)"))
    if propo<prix:
        print("PLUS GRAND")
    if propo>prix:
        print("PLUS PETIT")
    tentative+=1
print("\nBravo tu as gagné !!!!!!!! \nEn "+str(tentative)+" tentatives quand même\n")
score=100/tentative

print("score = "+str(round(score))+" points")
print("tableau des scores :")
sco.actscore(round(score),pseudo)
