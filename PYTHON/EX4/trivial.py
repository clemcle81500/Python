try:
    from random import randint

    sauvegarde = 6 #couleur sur laquelle on commence
    dico_couleur = {'orange':1, 'jaune':2, 'vert':3, 'rose':4, 'bleu':5, 'violet':6}

    def lancer_de():
        valeur_de = randint(1, 6)
        return valeur_de

    def main():
        nbr_lancer = int(input('Combien de fois veux-tu lancer le dé?'))

        for i in range(nbr_lancer):
            resultat = lancer_de()
            print("Résultat du lancer de dé :", resultat)
            emplacement = divisiblete(resultat)
            recherche_place(emplacement)
            i += 1

    def divisiblete(resultat):
        global sauvegarde  # Utilisation de "global" pour accéder à la variable globale
        sauvegarde = sauvegarde + resultat

        if (sauvegarde % 3 == 0 and sauvegarde % 2 == 0):
            emplacement = 6
        elif (sauvegarde % 5 == 0):
            emplacement = 5
        elif (sauvegarde % 2 == 0):
            if (sauvegarde % 4 == 0):
                emplacement = 4
            else:
                emplacement = 2
        elif (sauvegarde % 3 == 0):
            emplacement = 3
        else:
            emplacement = 1

        #print("Sauvegarde:", sauvegarde)
        return emplacement

    def recherche_place(emplacement):
        couleur = [cle for cle, val in dico_couleur.items() if val == emplacement][0]
        print(f"Tu es sur le {couleur}.")

    main()

except:
    print('Erreur')