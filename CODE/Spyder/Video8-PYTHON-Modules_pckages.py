# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 17:16:29 2020

VIDEO 8
@author: Loé
"""

liste=[0,1,12,12,199,18,15,15,15,15,18,91]

# utilisation des fonctions fibonacci et classer de Projet_1

import projet_1

# clic droit 'Aller à la définition de l'objet
liste_fibo = projet_1.fibonacci(50)
print(liste_fibo)

# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# nouveau dossier pycache apparait vers projet_1 ==>
# python organise les liaisons entre les projets

# on peut donner un surnom au module qu'on veut importer
# permet de gagner du temps et écrire de manière plus courte

import projet_1 as p1 

liste_fibo = p1.fibonacci(50)
print(liste_fibo)

# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# on peut importer seulement certaines classes, fonctions, varaibles
# des modules longs on ne veut pas tout importer

from projet_1 import fibonacci

liste_fibo = fibonacci(50)
print(liste_fibo)

# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# pour importer tous ce qui existe dans un module

from projet_1 import *
# liste = classer(classeur, nombre) #  méthode classer est accessible

# Module = un document qui contient du code
# Pour mettre de l'ordre dans tous ses modules, on les regroupe en package
# ex : mapplotlib pyplot un module de mapplotlib

# Les modules de base pour faire des data sciences

# ############################################
# Module math
# ############################################
# pour les mathématiques
# ############################################
import math

print(math.pi)
# 3.141592653589793

print(math.cos(math.pi))
# -1.0

print(math.cos(2*math.pi))
# 1.0

print(math.exp(5))
# 148.4131591025766

# ############################################
# Module random
# ############################################
# Aléatoire: nbre aléatoire, liste aléatoire
# ############################################

import random

print(random.choice(liste))
print(random.choice(['Jean','Anne','Julie']))

# seed : aléatoire mais reproductible
random.seed(0)
# on aura toujours Anne qui sort

# aléatoire float : entre 0 et 1 décimal
print(random.random())

# aléatoire sur nombre entier entre 5 et 10
print(random.randint(5,10)) 

# retourner un integer dans une fourchette de nombre
print(random.randrange(100)) 

# fonction sample() retourne une liste de nombre aléatoire entre 0 et x 
# exemple :  liste de 10 nombre aléatoire entre 0 et 100
print(random.sample(range(100), 10)) 

# [33, 65, 62, 51, 38, 61, 45, 74, 27, 64]

# combinaison : ex liste d'une liste d'un nombre aléatoire d'éléments
print(random.sample(range(100), random.randrange(10))) 

# shuffle() : mélange aléatoirement les données d'une structure de données
print(random.shuffle(liste))

# ############################################
# Module statistics
# ############################################
# permet de faire des statistiques
# ############################################
import statistics

# Moyenne des valeurs d'une liste
print(statistics.mean(liste))

# 8.8

# variance de la liste
print(statistics.variance(liste))

# 121.73333333333333

# ############################################
# Module os (operating system - permet d'intéragir avec le système)
# ############################################
# 
# ############################################
import os

#  quel est le répertoire courant de travail?
print(os.getcwd())

# ############################################
# Module glob
# ############################################
# 
# ############################################
import glob

# glob() : reoutrne une liste de tous les noms des fichiers que l'on a dans le répertoire de rtavail
print(glob.glob("*"))

# filtrer par type de fichier
print(glob.glob("*.txt"))

# afficher toutes les données à la chaine

filenames = glob.glob("*.txt")

for file in filenames:
    with open(file,'r') as f:
        print(f.read())
        
# Exercice

with open('fichier.txt', 'r') as f:
    liste = f.readline().splitlines()
print(liste)

#  ou ist comprehension
liste=[line.strip() for line in open('fichier.txt', 'r')]
print(liste)
 