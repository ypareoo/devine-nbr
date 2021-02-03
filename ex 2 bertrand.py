# Créé par Paul Bosseboeuf, le 27/01/2021 en Python 3.7
#faire deviner un nombre au programme entre 1 et 100

tabl=[]
fin=False

for i in range (0,101):     #crée un tableau de valeur de 0 à 100
    tabl.append(i)

debut=1
fin=100
reponse=False

print("Voici les règles du jeu :\n*choisi un nombre dans ta tête (entre 1 et 100)\n*Albert, l'ordinateur va essayer de deviner ton nombre\n*Indique lui par '+' ou '-' ou '=' par rapport à ce qu'il donne")
while reponse!="=":         #tant que l'utilisateur n'est pas satisfait du nombre du programme (!= "=")
    milieu=(debut+fin)//2

    if debut>=fin:          #vérifie si l'utilisateur dit n'importe quoi
        print("Pourquoi tu mens ???")
    if reponse == "+" :     #si réponse == + --> le champ de possible est réduit
        debut=milieu+1
        print("Est-ce "+str(tabl[(debut+fin)//2])+"?")
    if reponse == "-" :     #si réponse == - --> le champ de possible est réduit
        fin=milieu-1
        print("Est-ce "+str(tabl[(debut+fin)//2])+"?")
    if reponse == False :   #donne le premier nombre (toujours le même)
        print("Est-ce "+"50"+"?")
    reponse=input()
    print(debut,fin)

print( "Super, J'ai gagné, t'es trop nul.le")
print( "note : ce programme a été réalisé dans des conditions particulières sur un ordinateur du lycée\nmerci de votre indulgence vis-à-vis des défauts éventuelles de ce programme")


