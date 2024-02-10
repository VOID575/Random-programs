import time

# Définition du chemin du fichier CSV
fichier_csv = 'blackbox.csv'

# Fonction pour ajouter une nouvelle valeur au fichier CSV
def ajouter_valeur(valeur):
   
    # Ouvre le fichier CSV en mode ajout
    with open(fichier_csv, 'a') as fichier:
        
        # Écrit la nouvelle valeur dans le fichier
        fichier.write(str(valeur) + '\n')

# Fonction pour maintenir un maximum de 85 valeurs dans le fichier CSV
def gerer_limitation_valeurs():
    # Lit toutes les valeurs du fichier CSV dans une liste
    valeurs = []
    with open(fichier_csv, 'r') as fichier:
        for ligne in fichier:
            valeurs.append(ligne.strip())
            print(len(valeurs))
    
    # Si le nombre de valeurs dépasse 85, cela supprime les premières valeurs
    if len(valeurs) >= 80:
        valeurs = valeurs[-80:]
    
    # Réécrit le fichier CSV avec les valeurs mises à jour
    with open(fichier_csv, 'w') as fichier:
        for valeur in valeurs:
            fichier.write(str(valeur) + '\n')



