# Créé par valen, le 06/09/2023 en Python 3.7

def associer_valeur(ligne):
    d_lettre_valeur = {} #dictionnaire vide
    couples = ligne.split(' ')
    for i in range(0, len(couples), 2):
        d_lettre_valeur[couples[i]] = int(couples[i+1])

    return d_lettre_valeur

def calcul_score(mot, valeur_lettres):
    score = 0
    for lettre in mot:
        if lettre in valeur_lettres:
         score = score + valeur_lettres[lettre]
    return score


"""
1: lecture des données

"""



def lire_data(chemin_fichier):
    with open(chemin_fichier, 'r') as infile:
        ligne_valeurs = infile.readline().strip()
        lettre_valeur = associer_valeur(ligne_valeurs)

        liste_mots_scores = []  #liste
        for line in infile:
            mot = line.strip()
            score = calcul_score(mot, lettre_valeur)
            t_mot_score = (mot, score)
            liste_mots_scores.append(t_mot_score) #Création d'un tuple avec les ()
        return(liste_mots_scores)

"""
3 tri des données
"""

def tri(liste_mots_scores):
    liste_mots_scores.sort(key=lambda a: a[1])
    return liste_mots_scores



"""
4 affichage
"""

def affichage(liste_classee):
    for tup in liste_classee:
        print(tup[0])


"""
Parie principale (0 - scrabble)
"""

def scrabble(chemin_fichier):
    liste_classee = tri(lire_data(chemin_fichier))
    print(liste_classee)
    affichage(liste_classee)

scrabble('données_scrabble.txt')