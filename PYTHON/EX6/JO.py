try:
    p = 46
    mois = 4

    def puissance():
        global p

        for i in range(mois):
            if p % 3 == 0:
                p = p // 3
            elif p % 2 == 0:
                p = p // 2
            else:
                p = p - 1
            i += 1

    def main():
        puissance()
        print('Au bout de', mois, ' mois, la puissance sera de', p)

    main()

except:
    print('Erreur')