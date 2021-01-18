# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 18:30:49 2020

VIDEO 9
@author: Loé
"""

# ####################################
# PROGRAMMATION ORIENTEE OBJET
# ####################################

# exmple avec abjet ndarray du module numpy

import numpy as np

# tableau à 1 dimension
tableau =  np.array([1,2,3])
print(type(tableau))

print(tableau.size)

# help(np.array)

# correction exercices

import glob

filenames = glob.glob('*.txt')

dico = {}
for file in filenames:
    with open(file,'r') as f:
        # créer des clés pour le dico
        dico[file] = f.read().splitlines()