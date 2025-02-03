import random
from games.utils import afficher_gagnant, afficher_score

def main():
    userScore = 0
    pcScore = 0

    while True:
        moi = moiChoix()
        pc = pcChoix()
        print(f"Vous avez choisi: {moi}")
        print(f"L'ordinateur a choisi: {pc}")
        result = resultat(moi, pc)
        afficher_gagnant(result)

        if result == "Vous gagnez!":
            userScore += 1
        elif result == "L'ordinateur gagne!":
            pcScore += 1

        afficher_score(userScore, pcScore)
        print("Voulez-vous jouer une autre partie? (oui/non)")
        if input().lower() != 'oui':
            break

def moiChoix():
    choices = ['pierre', 'feuille', 'ciseaux']
    while True:
        try:
            userInput = input("Choisissez pierre, feuille ou ciseaux: ").lower()
            if userInput not in choices:
                raise ValueError("Choix invalide. Veuillez choisir parmi pierre, feuille ou ciseaux.")
            return userInput
        except ValueError as e:
            print(e)

def pcChoix():
    return random.choice(['pierre', 'feuille', 'ciseaux'])

def resultat(moi, pc):
    if moi == pc:
        return "Égalité!"
    elif (moi == 'pierre' and pc == 'ciseaux') or \
         (moi == 'feuille' and pc == 'pierre') or \
         (moi == 'ciseaux' and pc == 'feuille'):
        return "Vous gagnez!"
    else:
        return "L'ordinateur gagne!"

if __name__ == "__main__":
    main()