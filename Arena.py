import json
import random
from collections import deque
from Gladiator import *
from Audience import *


class Arena:
    def __init__(self):
        self.gladiators = deque([])
        self.audMembers = []
        self.generateGladiators()
        self.generateAudMembers()

    #Gladiators read in from JSON file
    def generateGladiators(self):
        with open('gladiators.json') as json_data:
            d = json.load(json_data)
        for glad in d:
            if not glad['name'].isspace():
                name = glad['name']
                age = glad['age']
                birthplace = glad['birthplace']
                health = glad['health']
                gladiator = Gladiator(name, age, birthplace, health)
                if gladiator not in self.gladiators:
                    self.gladiators.appendleft(gladiator)

    def generateAudMembers(self):
        #Creates 100 audience members
        for i in range(100):
            audMember = Audience()
            self.audMembers.append(audMember)

    def startTournament(self):
        numMatches = 0
        while len(self.gladiators) != 1:
            self.enterTheRing()
            for member in self.audMembers:
                member.setResponse() # audience response changes randomly per match
            numMatches += 1
            for gladiator in self.gladiators:
                gladiator.clearAllObservers() # deregisters all audience members from gladiator after match
            print()
            print("---------------Match " + str(numMatches) + "---------------")
        print(str(self.gladiators[0].name) + " of " + str(self.gladiators[0].birthplace) + " is the final winner")
        print("ARE YOU NOT ENTERTAINED?!!!")


    def enterTheRing(self):
        glad1 = self.gladiators.pop() #select glad 1 each round
        glad2 = self.gladiators.pop() #select glad 2 each round
        for member in self.audMembers:
            audiencePick = random.choice([glad1, glad2])
            member.registerSubject(audiencePick)
            audiencePick.registerObserver(member)  #all audience members register as observers
        self.battle(glad1, glad2)

    def battle(self, glad1, glad2):
        glad1Health = glad1.health
        glad2Health = glad2.health
        winner = glad1
        loser = glad2
        round = 0
        while glad1.health > 0 and glad2.health > 0:  #battle event loops till one gladiator has 0 health
            round += 1
            print()
            print("[Round " + str(round) + "]")
            winner = self.spar(glad1, glad2)
        vote = 0
        for member in self.audMembers:
            member.setVote()
            vote += member.vote
        if vote > (len(self.audMembers) / 2): #audience indicates thumbs up or thumbs down after match
            print("---------------Audience Voted Encore Match---------------")
            glad1.health = glad1Health
            glad2.health = glad2Health
            self.battle(glad1, glad2)
        else:
            if winner == glad1:
                print(str(glad2.name) + " has lost")
                glad1.health = glad1Health
                self.gladiators.appendleft(glad1)
            elif winner == glad2:
                glad2.health = glad1Health
                print(str(glad1.name) + " has lost")
                self.gladiators.appendleft(glad2)

        return winner

    def spar(self, glad1, glad2):
        self.assessPower(glad1)
        self.assessPower(glad2)
        loserHealthPenalty = random.choice([5, 10, 15])
        loser = glad2
        winner = glad1

        if glad1.totalPower > glad2.totalPower:
            loser = glad2
            winner = glad1
        elif glad1.totalPower < glad2.totalPower:
            loser = glad1
            winner = glad2
        else:
            loser = random.choice([glad1, glad2])
            if loser == glad1:
                winner = glad2
            else:
                winner = glad1
        print("    " + str(winner.name) + " won against " + str(str(loser.name)))
        winner.addWin()
        loser.loseHealth(loserHealthPenalty)
        print(str(loser.name) + " lost " + str(loserHealthPenalty) + " health points")
        return winner

    # Determines a gladiator's ability based off attributes and small chance
    def assessPower(self, glad):
        totalPower = 0
        totalPower += (glad.health / 10)
        if glad.age > 20 and glad.age < 40:
            totalPower += 20
        totalPower += (glad.numOfWins * 5)
        totalPower += random.randrange(0, 10)
        glad.totalPower = totalPower
