#11/12/25

class GameCharacter: #Parent Class
    def __init__(self,name,health):
        self.name = name
        self.health = health

    def show_stats(self):
        print(f"Name -> {self.name} | Health -> {self.health}")

class Warrior(GameCharacter): #Child Class
    def __init__(self,name,health,weapon):
        super().__init__(name,health) #Calls from parent class
        self.weapon = weapon

    def attack(self):
        print(f"{self.name} uses their {self.weapon}")

class Mage(GameCharacter): #Child Class
    def __init__(self,name,health,spell):
        super().__init__(name,health) #Calls from parent class
        self.spell = spell

    def attack(self):
        print(f"{self.name} uses their {self.spell}")

hero1 = Warrior("Conan",150,"Great Axe")
hero2 = Warrior("Xena",120,"Golden Sword")
hero3 = Mage("Gandalf",80,"Fireball")
hero4 = Mage("Yennefer",90,"Lightning Bolt")

hero2.show_stats()
hero2.attack()

hero4.show_stats()
hero4.attack()


