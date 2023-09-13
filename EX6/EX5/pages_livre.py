try:
    def pagination(h_images):
        nbr_pages = 1
        h_page = 10

        for h_image in h_images:
            if h_image <= h_page:
                h_page -= h_image
            else:
                nbr_pages += 1
                h_page = 10 - h_image

        return nbr_pages

    # Lecture des hauteurs des images depuis un fichier
    def code():
        with open('fichiers/input1.txt', 'r') as file:
            h_images = [] #tableau
            for ligne in file:
                ligne = ligne.split()
                for li in ligne:
                    h_images.append(int(li))

            print(pagination(h_images))

    code()

except:
    print('Erreur')