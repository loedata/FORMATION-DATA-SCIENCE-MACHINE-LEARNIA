# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 19:21:23 2020

@author: LOE
"""

x = 1
print(x)
x = 2 
print(x)
x = x + 1 
print(x)
x += 1
print(x)

a = True

# commentaires

x = 1
y = 2.5

# Arithmétiques
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x ** y)

# Comparaison
print(x <= y)
print(x >= y)
print(x == y)
print(x != y)

# Logique
print(False & True) # AND
print(False | True) # OR
print(False ^ True) # XOR

# String
prenom = 'Loe'
# Ou
prenom2 = "Loe"
print(prenom2)

# Double affectations
x, y = 1, 2.5

# f(x)=x^2
f = lambda x: x**2

print(f(3))

f = lambda x, y: x**2 + y

print(f(3, 4))

# Fonctions complexes
# keyword=attribut
def e_potentielle(masse, hauteur, limite, g=9.81):
    E = masse * hauteur * g
    if (E >= limite):
        print(E, 'Joules est supérieure ou égale à :', limite,' Joules');
    else:
        print(E, 'Joules est inférieure à :', limite, 'Joules');
    return(E)
    
resultat = e_potentielle(masse=80, hauteur=5, limite=1000, g=9.81)    
resultat1 = e_potentielle(masse=80, hauteur=5, limite=5000)    