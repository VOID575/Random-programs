from turtle import *
from math import sqrt
from time import *

def turtle(c,nb_c,true_final = 0):
    for i in range(2):

        forward(c)
        left(90)
    
    forward(c)
    left(90)

    if nb_c != 0 :
        
        forward(c/2)
        left(45)
        c = sqrt(2*((c/2)**2))
        turtle(c,nb_c-1,true_final+1)

   
    print(true_final)
    a = 0
    final = 0
    while true_final+1 != final :
        
        if final == 0 :

            a += 1
            final += 1
            forward(a*c)
            left(45)

        elif final == 1 : 

            final += 1
            forward(a*c/sqrt(2))
            left(45)

        elif final ==  2 :
            
            a += 1
            final += 1
            forward(c)
            left(45)
        
        elif final ==  3 :
            
            final += 1
            forward(a*c/sqrt(2))
            left(45)

        # Pair
        elif final >=  4 and final % 2 == 0 : 
            
            final += 1
            forward(a*c)
            left(45)

        # Impair
        elif final >= 4 and final % 2 != 0 :

            forward(a*c*sqrt(2))
            left(45)
            a = a * 2
            final += 1
        
        print(final)
        print(a)
        

        

    sleep(5)
    exit()
    
    
speed(100)
left(45)
turtle(200,3)


