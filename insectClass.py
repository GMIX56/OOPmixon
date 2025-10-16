import random

class insect:
    def __init__(self):
        self.wings = 2
        self.legs = 4
        self,name = name
        self.distance = 0
    
    def flight(self):
        # method asssigns random number between 1 and 10
        self.distance = random.randint(1, 10)
    
    def get_flight(self):
        return self.distance
    
    def get_name(self):
        return self.name