

class Gladiator:
    def __init__(self, name, age, birthplace, health):
        self.name = name.title()
        self.age = age
        self.birthplace = birthplace.title()
        self.health = health
        self.numOfWins = 0
        self.totalPower = 0
        self.observers = []

    def loseHealth(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.notify('death')
            for observer in self.observers:
                self.removeObserver(observer)
        else:
            self.notify('health')

    def addWin(self):
        self.numOfWins += 1
        self.notify('win')

    #Observer pattern gladiator is subject 
    def registerObserver(self, observer):
        self.observers.append(observer)

    def removeObserver(self, observer):
        self.observers.remove(observer)

    def clearAllObservers(self):
        self.observers[:] = []

    def notify(self, event):
        for member in self.observers:
            member.update(event)
