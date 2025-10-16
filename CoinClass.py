import random

# The Coin class simulates a coin that can
# be flipped.

class Coin:
    # The _ _init_ _ method initializes the
    # sideup data attribute with 'Heads'.

    def __init__(self):      #init (initialize) is a special method that runs automatically when an object is created from a class
        self.__sideup = 'Heads'    #self is a reference to the current instance of the class. It is used to access variables that belong to the class.
        #the double underscores before sideup make it a private attribute, meaning it cannot be accessed directly from outside the class

    # The toss method generates a random number
    # in the range of 0 through 1. If the number
    # is 0, then sideup is set to 'Heads'.
    # Otherwise, sideup is set to 'Tails'.

    def toss(self):
        if random.randint(0, 1) == 0:    #randint is a method in the random module that returns a random integer between the two specified integers (inclusive)
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'


    # The get_sideup method returns the value
    # referenced by sideup.

    def get_sideup(self):
            return self.__sideup
