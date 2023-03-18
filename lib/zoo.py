from lib.animal import Animal

class Zoo:
    all = []
    
    def __init__(self, name, location):
        self.name = name
        self.location = location
        Zoo.add_to_collection(self)
        self.animals = []
        self._animal_species = list()
    
    @classmethod
    def add_to_collection(cls, zoo):
        cls.all.append(zoo)

    def get_animal_species(self):
        return self._animal_species
    def set_animal_species(self, species):
        if species not in self.animal_species:
            self._animal_species.append(species)
    animal_species = property(get_animal_species, set_animal_species)

    def find_by_species(self, species):
        print(f"list of {species} belonging to {self.name}: {[s for s in self.animals if species is s.species]}")
        return [s for s in self.animals if species is s.species]
    
    def animal_nicknames(self):
        print(f"list of animals belonging to {self.name}: {[s.nickname for s in self.animals]}")
        return [s.nickname for s in self.animals]
    
    @classmethod
    def find_by_location(cls, location):
        print([z for z in cls.all if location == z.location])