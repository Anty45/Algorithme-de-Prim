import pandas as pd
import math
import numpy as np

def euclidean_distance(coordonne):
    """
    :param coordonne: l'ensemble des coordonnees des points a notre disposition

    :return: Distance euclidienne entre les sommets du graphe

    Le graphe etant Hamiltonien, tout les sommets sont adjacents deux à deux. Les sommets du graphe sont représentés
    par les clés,valeurs(x,y) d'un dictionnaire imbriqué au sommet considéré. Ce sommet représente la clé du
    dictionnaire.

    """
    k, v, abscice, ordonne = 0, 0, 0, 0
    point = []
    arete = {}
    distance = 0
    for sommet, value in coordonne.items():
        k = sommet
        v = value
        point.append(k)
        arete[k] = {}
        for v1, v2 in v.items():
            x = v1
            y = v2
        for s_prim, b in coordonne.items():
            if s_prim != k:
                for x_prim, y_prim in b.items():
                    distance = (math.sqrt(((x - x_prim) ** 2) + ((y - y_prim) ** 2)))
                if k not in arete:
                    arete[k] = {}
                arete[k].update({s_prim: distance})
                distance = 0
    return arete,point




data = pd.read_csv("a280.tsp.txt", sep=r"[ ]{1,}", engine='python')
X, Y = data["COORD"].values, data["SECTION"].values
coordonne = {}
for i in range(len(X)):
    coordonne[i + 1] = {X[i]: Y[i]}

arete = euclidean_distance(coordonne)

distance, sommet = euclidean_distance(coordonne)
# On va faire un test sur un petit graphe :

graph = {
    'a': {'b': 5, 'f': 4},
    'c': {'b': 2, 'g': 1, 'd': 6},
    'd': {'c': 6, 'e': 6},
    'b': {'a': 5, 'f': 10, 'g': 2, 'c': 2},
    'g': {'b': 2, 'f': 8, 'e': 3, 'c': 1},
    'f': {'a': 4, 'b': 10, 'g': 8, 'e': 5},
    'e': {'f': 5, 'g': 3, 'd': 6}
}

S = ['a', 'b', 'c', 'd', 'e', 'f', 'g']


def prim(graphe, sommet, x0):
    # Initialisation

    T = {}
    #T[x0] = {}
    sommet_T = [x0]
    origine = x0
    min_arete = 0
    n = len(sommet)

    # Iteration k

    for k in range(n):

        valuation_intermediaire = []
        sommet_intermediaire_correspondant = []

        for S, fin_arete in distance.items():
            if S in sommet_T:
                for y, value in fin_arete.items():
                    if (y in sommet) and (y not in sommet_T):
                        liste = list(fin_arete.values())
                        min_arete = min(liste)
                        valuation_intermediaire.append(min_arete)
                        sommet_intermediaire_correspondant.append(y)

                ind_val_sommet = np.argmin(valuation_intermediaire)
                min_arete = valuation_intermediaire[ind_val_sommet]

                y = sommet_intermediaire_correspondant[ind_val_sommet]
                T[S] = {}
                T[S].update({y: min_arete})
                sommet_T.append(y)
                print(T)
    return T, sommet_T

t,sommet_T = prim(distance,sommet,2)