class Animal:
    all = []
    def __init__(self, species, weight, nickname, zoo):
        self.species = species
        self.weight = weight
        self.nickname = nickname
        self.zoo = zoo
        zoo.animals.append(self)
        zoo.set_animal_species(species)
        self.add_to_collection(self)
    
    @classmethod
    def add_to_collection(cls, animal):
        cls.all.append(animal)
    
    @classmethod
    def find_by_species(cls, species):
        print(f"all instances of {species}: {[s for s in cls.all if s.species == species]}")
        return f"all instances of {species}: {[s for s in cls.all if s.species == species]}"