import random, sys
random.seed(42)
from person import Person
from logger import Logger

class Simulation(object):

    def __init__(self, population_size, vacc_percentage, virus_name,
                 mortality_rate, basic_repro_rate, initial_infected):
                 #trying to take out total_infected after basic_repro_rate to see if that does anything
        self.population_size = population_size
        self.population = []
        self.vacc_percentage = vacc_percentage
        self.total_infected = 0
        self.initial_infected = initial_infected
        self.current_infected = 0
        self.next_person_id = 0
        self.virus_name = virus_name
        self.infected_count = initial_infected
        self.killed = 0 #Not in instructions - Anwar's idea
        self.mortality_rate = mortality_rate
        self.basic_repro_rate = basic_repro_rate
        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(
            virus_name, population_size, vacc_percentage, initial_infected)
        self.logger = Logger(self.file_name)
        self.newly_infected = []
        self.population = self._create_population(initial_infected)

    def _create_population(self, initial_infected):
        population = []
        for person in range(initial_infected):
            new_person = Person(person, False, self.virus_name)
            population.append(new_person)
            # print(person) #simple print test
        for person in range(initial_infected, self.population_size - initial_infected):
            if random.random() < vacc_percentage:
                population.append(Person(person, True))
            else:
                population.append(Person(person, False))
        return population
        # print(str(population[0])) #simple print test

    def _simulation_should_continue(self):
        if self.killed == self.population_size or self.infected_count== 0:
            return False
        return True

    def run(self):
        time_step_counter = 0
        should_continue = self._simulation_should_continue()
        should_continue = True #Maybe cut this
        while should_continue:
            time_step_counter += 1
            self.logger.log_time_step(time_step_counter)
            self.time_step()
            should_continue = self._simulation_should_continue()
            pass
        # print('The simulation has ended after {time_step_counter} turns.'.format(time_step_counter))

    def time_step(self):
        pandemic = []
        for person in self.population:
            if person.infection != None:
                pandemic.append(person._id)
                # print(str(pandemic[person._id]) + " is a person's ID!")
        for sickly in pandemic:
            for meeting in range(100):
                stranger = None
                while stranger == None:
                    someone = self.population[random.randint(0, len(self.population) - 1)]
                    if someone.is_alive:
                        stranger = someone
                    pandemic.append(stranger._id)
                self.interaction(self.population[sickly], stranger)

        for sickly in pandemic:
            person = self.population[sickly]
            # print(person) #test
            did_survive = person.did_survive_infection(self.mortality_rate)
            self.logger.log_infection_survival(person, did_survive)
            if(not did_survive):
                self.killed+=1
            self.infected_count-=1
        self._infect_newly_infected()

    def interaction(self, sickly, stranger):
        assert sickly.is_alive == True
        assert stranger.is_alive == True
        if not stranger.is_vaccinated:
            if stranger.infection == None:
                if random.random() < self.basic_repro_rate:
                    self.newly_infected.append(stranger._id)
                    self.logger.log_interaction(sickly, stranger, True, False, False)
                else:
                    self.logger.log_interaction(sickly, stranger, False, False, False)
            else:
                self.logger.log_interaction(sickly, stranger, False, False, True)
        else:
            self.logger.log_interaction(sickly, stranger, False, True, False)

    def _infect_newly_infected(self):
        self.infected_count = len(self.newly_infected)
        for everyone in self.newly_infected:
            person = self.population[everyone]
            person.infected = self.virus_name
        self.newly_infected = [] #resets array after iterating thru it

if __name__ == "__main__":
    params = sys.argv[1:]
    population_size = int(params[0])
    vacc_percentage = float(params[1])
    virus_name = str(params[2])
    mortality_rate = float(params[3])
    basic_repro_rate = float(params[4])
    if len(params) == 6:
        initial_infected = int(params[5])
    else:
        initial_infected = 1
    simulation = Simulation(population_size, vacc_percentage, virus_name, mortality_rate, basic_repro_rate, initial_infected)
    simulation.run()
