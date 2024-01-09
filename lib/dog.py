#!/usr/bin/env python3


class Dog:
    APPROVED_BREEDS = [
        "Mastiff",
        "Chihuahua",
        "Corgi",
        "Shar Pei",
        "Beagle",
        "French Bulldog",
        "Pug",
        "Pointer"
    ]
    def __init__(self, name="Fido", breed="Beagle"):
        self.name = name
        self.breed = breed

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 25):
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = name

    def get_breed(self):
        return self._breed
    
    def set_breed(self, value):
        if value not in self.APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
        else:
            self._breed = value

    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)
    
guido = Dog("Fido", "Beagle")

guido.name = 1
guido.breed = "Jack"

print(guido.name)
print(guido.breed)
