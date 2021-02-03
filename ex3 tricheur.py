# Créé par BOSSEBP, le 28/01/2021 en Python 3.4
#tant que le programme le peut, vous ne réussirez pas à trouver le nombre qu'il a en mémoire (note : il a pas de nombre en mémoire)
#note : si vous donnez la possibilité au programme d'élargir le champs des possibilités, il le fera (donc pour vous, évitez d'entrer un chiffre du style 9999999999999.99999)
#le programme prend en charge les négatifs
debut=1
fin=100
scoring=0   #pour compter le nombre d'execution de la boucle
reponse=float(input("Mais quel nombre le programme peut-il avoir en mémoire ???"))
while True :            #| tant qu'il y a plusieurs possibilités, le programme tourne
    if fin-debut == 0 : #|
        print("=")
        break
    if abs(reponse-debut) >= abs(fin-reponse) :   #si le champs des possibles est plus grand (ou égal) dans les valeurs inférieurs (1 à 100 ou plus si l'utilisateur élargi ce champs (abs pour gérer les négatifs (oui, tous est prévu pour ceux qui veulent perdre du temps)))
        print("PLUS PETIT")
        fin=reponse-1 #la fin du champs des possibles s'arrête à reponse-1
    if abs(reponse-debut) < abs(fin-reponse) :    #si le champs des possibles est plus grand (ou égal) dans les valeurs inférieurs (1 à 100 ou plus si l'utilisateur élargi ce champs (abs pour gérer les négatifs (oui, tous est prévu pour ceux qui veulent perdre du temps)))
        print("PLUS GRAND")
        debut=reponse+1 #le debut du champs des possibles commence à reponse+1
    reponse=float(input("Mais quel nombre le programme peut-il avoir en mémoire ???"))
    scoring+=1
print("Enfin, c'est pas trop tôt\nTu sais qu'il a fallu que l'ordinateur te donne "+str(scoring)+" indications ???")