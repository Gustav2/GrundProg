animal = 'cat'


def change_animal_to_dog():
    global animal
    animal = 'dog'


change_animal_to_dog()

print(animal)
