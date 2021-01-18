# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 17:19:28 2020

VIDEO 8 - PROJET_1
@author: Loé
"""

def fibonacci(n):
    """
    Suite de Fibonacci jusqu'à n.

    Parameters
    ----------
    n : TYPE int
        DESCRIPTION. nombre

    Returns
    -------
    fib : la liste de la suite de fibonacci jusqu'à n.
    """
    a,b = 0, 1
    fib=[]
    while a<n:
        fib.append(a)
        a, b = b, a+b
    return fib

def classer(classeur, nombre):
    """
    Range le nombre transmis dans positif ou négatif

    Parameters
    ----------
    classeur : dictionnaire contenant 2 listes
               positif et négatif.
    nombre : entier, nimbre à classe

    Returns
    -------
    classeur : dictionnaire, nombre rangé dans = ou -
    """
    if nombre>=0:
        classeur['positif'].append(nombre)
    else:
        classeur['negatif'].append(nombre)
    return classeur