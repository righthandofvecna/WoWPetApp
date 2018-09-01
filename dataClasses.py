class Quest (object):
    name = None
    pets = []
    strategy = []

    def __init__(self, name, pets, strategy):
        self.name = name
        self.pets = pets
        self.strategy = strategy


class Pet (object):
    name = None
    skills = None
    breed = None

    def __init__(self, name, skills, breed):
        self.name = name
        self.skills = skills
        self.breed = breed

