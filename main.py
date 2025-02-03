# main.py
from games import chifoumi, fichePerso

def main():
    print("Choisissez un jeu:")
    print("1. Chifoumi")
    print("2. Fiche Personnelle")
    choix = input("Entrez le numéro du jeu: ")

    if choix == "1":
        chifoumi.main()
    elif choix == "2":
        fichePerso.main()
    else:
        print("Choix invalide.")

if __name__ == "__main__":
    main()