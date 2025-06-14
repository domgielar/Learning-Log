import pet

def main():
    pets = []
    while True:
        dec = input("Do you want to create a pet object (Y/N): ").strip().lower()
        if dec == "y":
            name = input("What is the name of your pet?")
            animal_type = input("What is the animal type of your pet?")
            age = int(input("What is the age of your pet?"))
            
            pets.append(pet.Pet(name, animal_type, age))

            for p in pets:
                print(f'{p.get_name()} is {p.get_age()} and a {p.get_animal_type()}.')
        
        if dec == 'n':
            return

if __name__ == '__main__':
    main()