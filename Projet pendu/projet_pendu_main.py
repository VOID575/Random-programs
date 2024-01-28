#Importer le code présent dans le fichier "projet_pendu_module"
from projet_pendu_module import *

#Appeler la fonction init()
init()

#La variable nb et state sont mis à 0
nb = 0

state = 0

#Les variables lettre_dites et mot_mystere sont reconnus comme étant des listes
mot_mystere = []

lettre_dites = []

#Le résultat de la fonction init est associé à la variable mot
mot = init()

# on initialise une boucle qui permet 
for i in range(len(mot)):
        
    mot_mystere.append('-')
        
AfficherListe(mot_mystere)

while 7-nb>0:

    # Jouer une manche et mettre à jour le mot mystère, l'état du jeu et la liste des lettres déjà dites
    mot_mystere, state, lettre_dites = jeu(mot,mot_mystere,lettre_dites,state)

    # Si le joueur a trouvé une lettre
    if state == 1:

        # Afficher un message de réussite et le nombre de vies restantes
        print("\nBien joué !\nIl vous reste ",7 - nb," vie(s)")
        
        # Afficher le dessin du pendu correspondant au nombre de vies restantes
        print(dessinPendu(nb),"\n")
        
        # Afficher la liste mot_mystere avec les lettres découvertes
        AfficherListe(mot_mystere)
        
        # Afficher la liste des lettres déjà dites
        print("\nLettre(s) déjà dites : ",lettre_dites)
        
        # Si il n'y a plus de "-" dans "mot_mystere" cela veut dire que le mot est trouvé
        if '-' not in mot_mystere :
                
                # Donc on renvoie "Congratulations"
                print("""\n\n
    ╔═══╗─────────────╔╗───╔╗───╔╗
    ║╔═╗║────────────╔╝╚╗──║║──╔╝╚╗
    ║║─╚╬══╦═╗╔══╦═╦═╩╗╔╬╗╔╣║╔═╩╗╔╬╦══╦═╗╔══╗
    ║║─╔╣╔╗║╔╗╣╔╗║╔╣╔╗║║║║║║║║╔╗║║╠╣╔╗║╔╗╣══╣
    ║╚═╝║╚╝║║║║╚╝║║║╔╗║╚╣╚╝║╚╣╔╗║╚╣║╚╝║║║╠══║
    ╚═══╩══╩╝╚╩═╗╠╝╚╝╚╩═╩══╩═╩╝╚╩═╩╩══╩╝╚╩══╝
    ──────────╔═╝║
    ──────────╚══╝""")
                
                break
            
    # Si le joueur a proposé une lettre fausse
    elif state == 0 :
        
        # Augmenter le nombre de tentatives de 1
        nb += 1
        
        # Afficher un message d'échec et le nombre de vies restantes
        print("\nEh non mauvaise lettre !\nIl vous reste ",7 - nb," vie(s)\n")
        
        # Afficher le dessin du pendu correspondant au nombre de vies restantes
        print(dessinPendu(nb),"\n")
        
        # Afficher la liste mot_mystere avec les lettres découvertes
        AfficherListe(mot_mystere)
        
        # Afficher la liste des lettres déjà dites
        print("\nLettre(s) déjà dites : ",lettre_dites)
        
        # Si le joueur a utilisé toutes ses tentatives
        if nb==7:
            
            # Afficher "GAME OVER" et le mot à deviner
            
            print(""""\
                    
    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
    ███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
    ██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
    ███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
    ███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
    ██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
    ███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼
    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
    """)
            print("\nLe mot était : ", mot)
            
            break
        
    # Si le joueur a déjà proposé cette lettre
    elif state == 2 :

        # Afficher un message d'erreur et la liste des lettres déjà dites
        print("\nTu as déja dis cette lettre ! ") 
        
        print("Lettre(s) déjà dites : ",lettre_dites)
        
        