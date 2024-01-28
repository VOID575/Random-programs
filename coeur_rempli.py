# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 23:50:02 2023

@author: Valentin
"""

coeur_rempli = [2,0,3,0,5,0,6,0]

n=1
for i in range(7):

    coeur_rempli.append(n)
    coeur_rempli.append(1)
    n += 1 


n=1
for i in range(7):

    coeur_rempli.append(n)
    coeur_rempli.append(2)
    n += 1 

n = 1
for i in range(7):

    coeur_rempli.append(n)
    coeur_rempli.append(3)
    n += 1 

n = 2
for i in range(5):

    coeur_rempli.append(n)
    coeur_rempli.append(4)
    n += 1 
    
n = 3
for i in range(3):

    coeur_rempli.append(n)
    coeur_rempli.append(5)
    n += 1 
    
coeur_rempli.append(4)
coeur_rempli.append(6)

print(coeur_rempli)