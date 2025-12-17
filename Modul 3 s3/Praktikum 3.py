class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def showInfo(self):
        print("showinfo di class hero")
        print("{} health: {}". format(
            self.name,
            self.health
            )
        )

class hero_intelligent(Hero):
    def __init__(self, name):
        super().__init__(name, 100)

    def showInfo(self):
        print("showinfo di subclass Hero_intellgent")
        print("{} \n\tTipe: intellgent, \n\thealth: {}".format(
            self.name,
            self.health
            )
        )

class Hero_strength(Hero):
    def __init__(self, name):
        super().__init__(name, 200)

lina = hero_intelligent('lina')
axe = Hero_strength('axe')

lina.showInfo()
