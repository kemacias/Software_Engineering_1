# Kate Macias
# Software Engineering 1
# Fall 2026
#

class Stats:
    def __init__(self, strength, dexterity, constitution,
                 intelligence, wisdom, charisma):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma


class Armor:
    def __init__(self, name, ac):
        self.name = name
        self.ac = ac  # armor class


class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage  # dice notation, e.g. "1d6"


class Player:
    def __init__(self, name, stats, armor, weapon):
        self.name = name
        self.hp = 10
        self.stats = stats
        self.armor = armor    # list of Armor
        self.weapon = weapon  # Weapon

    def total_ac(self):
        return sum(piece.ac for piece in self.armor)

    def damage(self, amount):
        self.hp -= amount

    def compute_damage(self, base):
        # Pretend this is some complex thing with AC, armor, hp
        pass


p = Player(
    "Alfredo",
    Stats(9, 12, 8, 18, 10, 2),
    [Armor("iron helmet", 8), Armor("chain mail", 16)],
    Weapon("short sword", "1d6"),
)
