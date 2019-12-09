import random
from Virus import Virus

class Person:
    ''' The simulation will contain people who will make up a population.'''

    def __init__(self, is_vaccinated, infection=None):
        ''' We start out with is_alive = True
        All other values will be set by the simulation through the parameters when it instantiates each Person object.
        '''
        self.is_alive = True #boolean
        self.is_vaccinated = is_vaccinated #boolean
        self.infection = infection #virus object
        

    def did_survive_infection(self):
        ''' Generate a random number between 0.0 and 1.0 and compare to the virus's mortality_num.
        If the random number is smaller, person dies from the disease. Set the person's is alive attribute to False
        If Person survives, they become vaccinated and they have no infection (set the vaccinated attibute to True and the infection to None)
        Return True if they survived the infection and False if they did not. 
        '''
        mortality_number = random.uniform(0.0,1.0)
        virus_rate = self.infection.mortality_num * 100
        
        if mortality_number < virus_rate:
            self.is_vaccinated = False
            self.is_alive = False
            self.infection = None
            return False
        else:
            self.is_vaccinated = True
            self.infection = None
            return True
