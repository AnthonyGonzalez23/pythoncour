from faker import Faker

def fichePerso():
    fake = Faker('fr_FR')
    fakeFiche = {
        'nom': fake.last_name(),
        'prénom': fake.first_name(),
        'email': fake.email(),
        'adresse': fake.address(),
        'téléphone': fake.phone_number()
    }
    for key, value in fakeFiche.items():
        print(f"{key.capitalize()}: {value}")

def main():
    while True:
        try:
            nbRow = int(input("choisissez un nombre de fiches à générer: "))
            break
        except ValueError:
            print("Veuillez entrer un nombre valide.")

    for i in range(int(nbRow)):
        fichePerso()
        print("\n")

main()