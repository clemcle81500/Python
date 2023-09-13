try:
    def lire_fichier(lien):
        with open(lien, 'r') as fichier:
            lignes = fichier.read().splitlines()
        return lignes

    def verifier_nb(livre,demande,nb_personne):
        chaine = demande.split(" ")
        lettre = chaine[0]
        num = chaine [1]
        if int(num) >= nb_personne/2:
            add_livre = ajouter_livre(lettre,livre)
            return add_livre
        else:
            return livre

    def ajouter_livre(lettre,livre):
        livre=livre+lettre
        return livre

    def menu(lien):
        liste = lire_fichier(lien)
        nb_personne=int(liste[0])
        nb_demande=int(liste[1])
        del liste[0],liste[0]
        livre=""
        for i in range(0,nb_demande):
            livre = verifier_nb(livre,liste[i],nb_personne)
        print(livre)


    fichier_lien = 'fichier1.txt'
    menu(fichier_lien)

except:
    print('Erreur')