##########################
#   AUTHOR : NehZio      #
#                        #
# leo.gaspard@outlook.fr #
##########################

from qtido import *
import random
from math import cos
from math import sin
from math import radians
import numpy as np

def poly(HEIGHT,WIDTH, n):
    l = 3*(HEIGHT-100)/n
    points = [[WIDTH//2,50]]
    angle = -180/n
    for i in range(n):
        points.append([points[i][0]+l*cos(radians(angle)), points[i][1]-l*sin(radians(angle))])
        angle -= (360/n)%360
    return points  

def main():
    HEIGHT = int(input("Window Height ?"))
    n = int(input("How many sides ?"))
    simulation = int(input("How many simultaneous simulations ?"))

    window = creer(HEIGHT,HEIGHT)
    points = poly(HEIGHT,HEIGHT, n)
    polyligne(window,points)
    couleur(window,1,0,0)
    
    count = 0
    r = np.random.randint(0,n+1,size=simulation)
    x = np.array([points[i][0] for i in r])
    y = np.array([points[i][1] for i in r])
    while True :
        count += 1
        r = np.random.randint(1,n+1,size=simulation)
        newPoints = [[points[i][j] for i in r] for j in [0,1]]
        x = (x + newPoints[0]) / 2
        y = (y + newPoints[1]) / 2
        couleur(window,0,0,0)
        rectangle(window,0,0,600,40)
        couleur(window,1,0,0)
        texte_centre(window, HEIGHT//2, 30, 20, str(count*simulation))
        for i in range(simulation):
            disque(window,x[i],y[i],0.5)
        if count*simulation%1000 == 0:
            attendre_pendant(window,0.01)
            
        

main()

        

    
    
