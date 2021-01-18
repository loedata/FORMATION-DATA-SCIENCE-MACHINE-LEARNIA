# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 10:39:59 2020

VIDEO 4
@author: LOE
"""

# Création d'un dictionnaire
# les clés sont uniques
# les valeurs peuvent être utilisées plusieurs fois
traduction = {
    "chien" : "dog",
    "chat" : "cat",
    "souris" : "mouse",
    "oiseau" : "bird"
    }

inventaire = {
    "bananes" : "5000",
    "poires" : "400",
    "oranges" : "6000",
    "pommes" : "1000"
    }

dico_3 = {
    "dict_1" : traduction,
    "dict_2" : inventaire
    }

import numpy as np

parametres = {
    "W1" : np.random.randn(10,100),
    "b1" : np.random.randn(10,1),
    "W2" : np.random.randn(10,10),
    "b2" : np.random.randn(10,1)
    }