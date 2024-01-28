# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 11:21:51 2023

@author: VALENTIN.LORIOU
"""

def dec_binaire(dec):
    
   resultat_bin = ""
    
   while dec >= 1 :
    #J'enchaine les division euclidienne jusqu'à ce que le reste soir égal à 1

       if dec % 2 == 0 :
           
           resultat_bin += "0"
           
       else :
           
           resultat_bin += "1"
           
       dec = dec // 2
           
   print(resultat_bin[::-1])
   #J'inverse les restes comme dans la technique sur papier

#dec_binaire(8999)

def bin_dec(binaire):
    
   nbr_de_bit = len(binaire) - 1
   resultat_dec = 0
   n = 0
     
   for i in range(nbr_de_bit + 1):

       if binaire[n] == "1" :
        #Si il y a un 1 alors il y a un calcul
                
           resultat_dec += 2 ** nbr_de_bit
           #La puissance de 2 diminue de 1 en 1 au fur et à mesur que l'on se deplace sur la droite
           n += 1
           nbr_de_bit -= 1
                
       else :
                
           n += 1
           nbr_de_bit -= 1
        
   print(resultat_dec)
    
#bin_dec("111011")

def bin_hex(binairehexa):
    
    resultat_bin_hex = ""
    n = 0
    tableau = {"0000" : " 0 ","0001" : " 1 ","0010" : " 2 ","0011" : " 3 ",
               "0100" : " 4 ","0101" : " 5 ","0110" : " 6 ","0111" : " 7 ",
               "1000" : " 8 ","1001" : " 9 ","1010" : " A ","1011" : " B ",
               "1100" : " C ","1101" : " D ","1110" : " E ","1111" : " F "}

    rev_binairehexa = binairehexa[::-1]
    #J'inverse la string afin que les 0 s'ajoute à gauche et non à droite

    while len(rev_binairehexa) % 4 != 0 :
    #Tant que la valeur saisie ne peut pas se découper en octet je rajoute des
    #0 pour pouvoir atteindre cette forme
        
        rev_binairehexa += "0"
        
    binairehexa = rev_binairehexa[::-1]
    #Je remets la string dans le bon sens pour que cela corresponde avec les valeurs du tableau
        
    for i in range(len(binairehexa) // 4):
    #La boucle se répète un nombre de fois égal au nombre d'octet
        
        resultat_bin_hex += tableau[binairehexa[n:n+4]]
        #Je fais correspondre les valeur du tableau avec le résultat et je le concatène à resultat_bin_hex
        n += 4  
            
    print(resultat_bin_hex)
        
#bin_hex("110011111001")

def hex_bin(hexabinaire):
    
    resultat_hex_bin = ""
    n = 0
    tableau = {'1': '0001',
               '2': '0010',
               '3': '0011',
               '4': '0100',
               '5': '0101',
               '6': '0110',
               '7': '0111',
               '8': '1000',
               '9': '1001',
               'A': '1010',
               'B': '1011',
               'C': '1100',
               'D': '1101',
               'E': '1110',
               'F': '1111'}

    for i in range(len(hexabinaire)):

        resultat_hex_bin += tableau[hexabinaire[n]]
        n += 1
            
    print(resultat_hex_bin)
    
#hex_bin("CAF7")   

def dec_hex(decimalhexa):
    
    tableau = {
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'}

    resultat_dec_hexa = ""
     
    while decimalhexa >= 16 :
     #J'enchaine les division euclidienne jusqu'à ce que le reste soir égal à 1

        resultat_dec_hexa += tableau[decimalhexa % 16]
        decimalhexa = decimalhexa // 16
        
    resultat_dec_hexa += tableau[decimalhexa]
            
    print(resultat_dec_hexa[::-1])
        
#dec_hex(831349)

def hex_dec(hexa_decimal):
    
    resultat_hex_dec = 0
    n = 0
    nbr_de_termes = len(hexa_decimal)
    tableau = {
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }

    for i in range(nbr_de_termes) :
        
        resultat_hex_dec += tableau[hexa_decimal[n]] * (16**(nbr_de_termes-1))
        n += 1
        nbr_de_termes -= 1

    print(resultat_hex_dec)        
    
#hex_dec("CAF75")

