from datetime import datetime
import random
from Responses import *

class Audience:
    def __init__(self):
        self.id = str(datetime.now().microsecond)
        self.subject = None #gladiator object
        self.strategy = NeutralResponse()
        self.vote = 0

    def registerSubject(self, gladiator):
        self.subject = gladiator

    def setVote(self):
        self.vote = random.choice([0, 1]) #Yay or nay vote for second chance on fight


    def update(self, event):
        self.strategy.response(event)

    def setResponse(self):
        self.strategy = random.choice([NegativeResponse(), PostiveResponse(), NeutralResponse()])
