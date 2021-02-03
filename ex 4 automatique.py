# Créé par Admin, le 28/01/2021 en Python 3.7


tabl=[]
fin=False

for i in range (0,101):     #crée un tableau de valeur de 0 à 100
    tabl.append(i)

debut2=1
debut3=1
fin2=100
fin3=100
reponse3=False

scoring=0   #pour compter le nombre d'execution de la boucle
#reponse2=float(input
print("Mais quel nombre '3' peut-il avoir en mémoire ???")
reponse2=50
print("Voici les règles du jeu :\n*choisi un nombre dans ta tête (entre 1 et 100)\n*Albert, l'ordinateur va essayer de deviner ton nombre\n*Indique lui par '+' ou '-' ou '=' par rapport à ce qu'il donne")
while reponse3!="=":         #tant que l'utilisateur n'est pas satisfait du nombre du programme (!= "=")
    milieu2=(debut2+fin2)//2

    #if debut>=fin:          #vérifie si l'utilisateur dit n'importe quoi
     #   print("Pourquoi tu mens ???")
    if reponse3 == "+" :     #si réponse == + --> le champ de possible est réduit
        debut2=milieu2+1
        print("2: Est-ce "+str(tabl[(debut2+fin2)//2])+"?")
    if reponse3 == "-" :     #si réponse == - --> le champ de possible est réduit
        fin2=milieu2-1
        print("2: Est-ce "+str(tabl[(debut2+fin2)//2])+"?")
    if reponse3 == False :   #donne le premier nombre (toujours le même)
        print("2: Est-ce "+"50"+"?")
    #reponse3=input()
    reponse2=tabl[(debut2+fin2)//2]

    if fin3-debut3 == 0 : #|
        print("3: =")
        reponse3="="
        break
    if abs(reponse2-debut3) >= abs(fin3-reponse2) :   #si le champs des possibles est plus grand (ou égal) dans les valeurs inférieurs (1 à 100 ou plus si l'utilisateur élargi ce champs (abs pour gérer les négatifs (oui, tous est prévu pour ceux qui veulent perdre du temps)))
        print("3: PLUS PETIT")
        reponse3="-"
        fin3=reponse2-1 #la fin du champs des possibles s'arrête à reponse-1
    if abs(reponse2-debut3) < abs(fin3-reponse2) :    #si le champs des possibles est plus grand (ou égal) dans les valeurs inférieurs (1 à 100 ou plus si l'utilisateur élargi ce champs (abs pour gérer les négatifs (oui, tous est prévu pour ceux qui veulent perdre du temps)))
        print("3: PLUS GRAND")
        reponse3="+"
        debut3=reponse2+1 #le debut du champs des possibles commence à reponse+1
    #reponse2=float(input
    print("3: Mais quel nombre '3' peut-il avoir en mémoire ???")
    scoring+=1

    #print(debut,fin)
print("3: Enfin, c'est pas trop tôt\n3: Tu sais qu'il a fallu que l'ordinateur te donne "+str(scoring)+" indications ???")
print("2: Super, J'ai gagné, t'es trop nul.le")