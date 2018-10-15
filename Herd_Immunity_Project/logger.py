class Logger(object):

    def __init__(self, file_name):
        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num):
        file = open(self.file_name, "w")
        file.write("Population: " + str(population_size) + "\n")
        file.write("Percent vaccinated: " + str(vacc_percentage) + "% \n")
        file.write("Virus: " + str(virus_name) + "\n")
        file.write("This virus's mortality rate: " + str(mortality_rate) + "\n")
        file.write("This virus's basic reproduction number: " + str(basic_repro_num) + "\n")

    def log_interaction(self, person1, person2, did_infect=None,
                        person2_vacc=None, person2_sick=None):
        file = open(self.file_name, "a")
        if did_infect != None:
            file.write("Person with ID " + str(person1._id) + " infected person with ID " + str(person2._id) + ". \n")
        elif person2_vacc != None:
            file.write("Person with ID " + str(person1._id) + " did not infect person with ID " + str(person2._id) + " because person with ID " + str(person2._id) + " was vaccinated. \n")
        elif person2_sick != None:
            file.write("Person with ID " + str(person1._id) + " did not infect person with ID " + str(person2._id) + " because person with ID " + str(person2._id) + " was already infected before. \n")
        else:
            file.write("Person with ID " + str(person1._id) + " did not infect person with ID " + str(person2._id) + ". \n")

    def log_infection_survival(self, person, did_die_from_infection):
        file = open(self.file_name, "a")
        if not did_die_from_infection:
            file.write("Person with ID " + str(person._id) + " survived infection. \n")
        else:
            file.write("Person with ID " + str(person._id) + " did NOT survive infection. \n")

    def log_time_step(self, time_step_number):
        file = open(self.file_name, "a")
        file.write("Start of time step #" + str(time_step_number) + "\n")
