import random

class Person(object):

    def __init__(self, _id, is_vaccinated, infection=None):
        # TODO:  Finish this method.  Follow the instructions in the class documentation
        # to set the corret values for the following attributes.
        self._id = _id
        self.is_vaccinated = is_vaccinated
        self.is_alive = True #CHANGES TO FALSE if killed by infection - all START as alive
        self.infection = infection

    def did_survive_infection(self, mortality_rate):
        random_chance = random.randint(0,1)
        if random_chance < mortality_rate:
            self.is_alive = False
            self.infection = None
            return False
        else:
            self.is_vaccinated = True
            self.infection = None
            return True

# def test_person_instantiation():
#     jolie = Person("113", False, False)
#     assert jolie._id == "113"
#     assert jolie.is_vaccinated == False
#     assert jolie.infected == False
