# Créé par Clément, le 06/09/2023 en Python 3.7


#liste_mots = ["cafe", "bouton", "face", "bad", "zebra", "bug"]
liste_points = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4, "g": 2, "u": 1}

liste_mots = []
nbr_mots = int(input("Combien as-tu de mots?"))

for i in range(nbr_mots):
    mot = input("Donne moi ton mot:")
    liste_mots.append(mot)

for mot in liste_mots:
    print(f"Le mot: {mot}")
    total_points = 0
    for lettre in mot:
        total_points += liste_points.get(lettre, 0)  # Utilisez le dictionnaire pour obtenir les points de la lettre
    print(f"Points totaux: {total_points}")