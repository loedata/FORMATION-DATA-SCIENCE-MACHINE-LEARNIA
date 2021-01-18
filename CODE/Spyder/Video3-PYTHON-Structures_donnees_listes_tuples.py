# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 19:21:23 2020

VIDEO 3
@author: LOE
"""

# =======================================
# STRUCTURES DE DONNEES : SEQUENCES
# =======================================

#  LISTES

liste_1 = [1, 4, 2, 7, 5, 84]
villes=['Paris', 'Berlin', 'Londres', 'Bruxelles']
liste_2 =[liste_1, villes]
liste_3=[]

#  TUPLES
#  Non modifiable - protégé - utilise moins de mémoire

tuple_1=(1, 2 ,6, 1, 7)

#  String

prenom='Loe'

#  séquence = ensemble ordonné, les valeurs sont ondexés
#  premier index : le 0

# =======================================
# TECHNIQUE D'INDEXING
# =======================================

# premier élément de la liste : index 0
print(villes[0])
# deuxième élément de la liste : index 1
print(villes[1])
# avant dernier élément de la liste : index -2
print(villes[-2])
# dernier élément de la liste : index -1
print(villes[-1])

# =======================================
# TECHNIQUE DE SLICING
# =======================================
#  Liste [debut, fin ,pas]
print(villes[0:3])
#  inex 0 pas forcément à préciser
print(villes[:3])
#  tous les éléments de  2 à la fin
print(villes[2:])
# index début et fin
print(villes[2:3])
# pas de 1 à la fin avec pas 2
print(villes[1::2])
# pas négatif parcours toute la liste à l'envers
print(villes[::1])

prenom='Nicolas'
print(prenom[1:3])

villes[0]='Dublin' # remplace Paris par Dublin