def ask(question: str) -> bool:
    # displays the question that is put into the parameter, takes off any trailing and leading whitespace and lowercases the response
    return input(question + " (yes/no): ").strip().lower() == 'yes'


def identify_animal():
    # checks it has feather if it does not, it will get and ask if the animal has fur, if it does not have fur it will ask if it has scales, if not it will ask if the animal has smooth skin and lives near the water
    if ask("Does it have feathers"):
        if ask("Can it fly"):
            if ask("Does it chirp"):
                print("It is a Sparrow.")
            else:
                print("It is a Hawk.")
        else:
            print("It is a Penguin.")
    else:
        if ask("Does it have fur"):
            if ask("Does it bark"):
                print("It is a Dog.")
            elif ask("Does it meow"):
                print("It is a Cat.")
            else:
                print("It is a Bear.")
        elif ask("Does it have scales"):
            if ask("Does it live in water"):
                print("It is a Fish.")
            else:
                print("It is a Lizard.")
        elif ask("Does it have smooth skin and live near water"):
            print("It is a Frog.")
        else:
            print("It is a Snake.")


identify_animal()
