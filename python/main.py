from games import chifoumi, fichePerso

def main():
    print("Choisissez un jeu:")
    print("1. Chifoumi")
    print("2. Fiche perso")
    choice = input("Entrez le numéro du jeu: ")

    if choice == '1':
        chifoumi.main()
    elif choice == '2':
        fichePerso.main()
    else:
        print("Choix invalide")

if __name__ == "__main__":
    main()