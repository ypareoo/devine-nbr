# Créé par Admin, le 30/01/2021 en Python 3.7
import random as ra
from pathlib import*
from turtle import*


def actscore(score,pseudo):

    score=str(score)
    #print(len(score))
    while len(score)<3: #pour avoir des scores à 3 chiffres
        score="0"+score
    #print(score)
    scoreint=int(score) #faut faire deux variables car int(045) --> 45

    out=False
    listevar=["a","b","c","d","e","f","g","h","i",'j']
    liste=[1,2,3,4,5,6,7,8,9,10]
    #print(score)
    with open ("score.txt","r") as sco:  #lit les scores du tableau des scores, (le premier caractère) puis rempli "liste"
        for i in range(10):
            liste[i]=int(sco.readline()[:3])


    with open ("score.txt","r") as sco: #lit chaque lignes du tableau des scores puis rempli "listevar"
        for i in range(10):
            listevar[i]=sco.readline()



    with open ("score.txt","r") as sco: #compare le score entré en paramètre et insert au bon endroit (une seule fois) dans "listevar" score+pseudo
        for z in range(10):
            if scoreint>=int(liste[z]) and out==False: #fait les comparaison avec scoreint et rempli avec score
                listevar.insert(z,str(score)+pseudo)
                out=True

    for i in range(len(listevar)):  #supprime si nécessaire "\n" (cela peut engendrer des interférences)
        if listevar[i][-1]=="\n":
            listevar[i]=listevar[i][:-1]

    with open ("score.txt","w") as sco:  #réecrit dans le tableau des scores en fonction de "listevar"
        for y in range(10):
            sco.write(str(listevar[y])+"\n")

    with open ("score.txt","r") as sco:  #print chaque ligne du tableau des scores
        for i in range(len("score.txt")+1):
            print(sco.readline(),end="")
    return
