try:
    # Fonction pour lire l'entrée à partir d'un fichier
    def lire_entree_de_fichier(nom_fichier):
        liste = {}  # Dictionnaire pour stocker l'inventaire

        with open(nom_fichier, 'r') as fichier:
            N = int(fichier.readline().strip())  # Nombre d'articles
            for _ in range(N):
                ligne = fichier.readline().strip().split() #lis la première ligne
                nom_produit, prix_produit = ligne[0], int(ligne[1])

                if nom_produit in liste:
                    liste[nom_produit] += prix_produit
                else:
                    liste[nom_produit] = prix_produit

        return liste

    # Fonction pour trouver les produits les plus chers
    def produits_plus_chers(liste):
        max_prix = max(liste.values())  # Trouver le prix le plus élevé
        produits = [nom for nom, prix in liste.items() if prix == max_prix]
        return produits

    # Fonction principale
    def main():
        nom_fichier = 'inventaire.txt' #Mettre le fichier souhaité
        liste = lire_entree_de_fichier(nom_fichier)
        produits_chers = produits_plus_chers(liste)
        print(' '.join(produits_chers))

    main()

except:
    print('Erreur')