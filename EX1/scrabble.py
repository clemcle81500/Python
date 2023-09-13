    # Créé par Clément, le 06/09/2023 en Python 3.7

try:
    with open('data1.txt', 'r') as file:
         #Lis la première ligne
        tableau_point = file.readline().strip().split()

        #Dictionnaire qui associe la lettre à son point
        dictionnaire_points = {letter: int(points) for letter, points in zip(tableau_point[::2], tableau_point[1::2])}

        #Lis le reste de la ligne
        liste_mots = file.read().splitlines()

    for mot in liste_mots:
        points = 0
        for lettre in mot:
            if lettre in dictionnaire_points:
                points += dictionnaire_points[lettre]
        print(f"Le mot {mot} compte", points, "points")
        score = (mot, points)
        liste_score = [score]

except:
    print("Erreur")