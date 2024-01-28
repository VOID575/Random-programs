def dessinPendu(nb):
    """
    Fonction renvoyant un dessin ascii correspondant à un état du pendu en fonction de la valeur entrée en argument 
    """
    
    #Initialisation du tableau contenant les états du pendu en ASCII
    tab=[
    """
       +-------+
       |
       |
       |
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |
       |
       |
    ==============
    """
        ,
    """
       +-------+
       |       |
       |       O
       |       |
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       O
       |      -|-
       |      |
       |
    ==============
    """,
    """
       +-------+
       |       |
       |       0
       |      -|-
       |       |
       |      | |
       |
    ==============
    """
    ]
    #renvoi le dessin ascii correspondant à la valeur en argument 
    return tab[nb]

###########################################################################################################

def init():
   """
   Renvoie un mot choisi au hasard dans un fichier.
   """
   
   #On importe la fonction choice dans le module random, fonction servant à choisir un élément au hasard dans une liste
   from random import choice

   #Pour chaque ligne dans le fichier txt on : enlève le \n, puis le met dans la liste mots 
   mots=[line.strip() for line in open ('dico.txt','r')]
   
   mot=choice(mots) #Choix au hasard d'un mot dans le fichier avec la fonction choice
   
   return mot #On retourne le mot choisi au hasard 

############################################################################################################
   
def jeu(mot, mot_mystere, lettre_dites, state):
    """
    Renvoie 3 variables :
    ● Le mot mystère (la liste à afficher avec les tirets) mis à jour si la lettre entrée est dans le mot.
    ● "state" définissant l'état de la présence de la lettre dans le mot ou(0 : non ; 1 : oui; 2 : oui mais déjà dites)
    ●La liste "Lettre dites" contenant les lettres entrées au préalable par le joueur
    """
    
    # On demande à l'utilisateur de saisir une lettre 
    lettre = input("\nEntrer une lettre : \n").upper()
        
    #on crée une boucle qui permet de vérifier si la lettre est dans le mot
    if lettre in lettre_dites :
        
        #La lettre à déjà été dites alors on préviens le programme pour qu'il ne compte pas la lettre comme vraie ou fausse
        state = 2
        
        #on renvoie le mot mystère, le state et la liste lettres dites
        return mot_mystere, state, lettre_dites
    
    #on rajoute la lettre à la liste lettres dites
    lettre_dites.append(lettre)
    
    # On récupère les indices de toutes les occurrences de la lettre dans le mot
    indexs = [i for i, j in enumerate(mot) if j == lettre]
    

    # Si on trouve au moins une occurrence de la lettre dans le mot
    if indexs:
        
        #on initialise la valeur à 1
        state = 1
        
        # On parcourt tous les indices et on remplace les '_' par la lettre trouvée
        for index in indexs:
            
            #on remplace le tiret par la lettre dans le mot
            mot_mystere[index] = lettre
            
        # On renvoie le nouveau mot mystère et le stateéen mis à jour
        return mot_mystere, state, lettre_dites
    
    # Si on ne trouve pas l'occurrence de la lettre dans le mot
    else:
        
        #On initialise la valeur à 0
        state = 0
        
        # On renvoie le mot mystère tel qu'il était et le state boléen mis à jour
        return mot_mystere, state, lettre_dites

###########################################################################################################
#On crée une fonction AfficherListe
def AfficherListe(L):
   """
   Affiche les éléments d'une liste les uns à la suite des autres
   """
   
    
    #on initialise une boucle qui permet de traverser toute la liste
   for i in range (len(L)):
       
      #on imprime les éléments de la liste pour avoir des tirets
      print(L[i],end='')
      
##########################################################################################################   