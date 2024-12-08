import random, sys
# random.seed(42)
from person import Person
from logger import Logger
from virus import Virus

class Simulation(object):
    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
        self.virus = virus
        self.pop_size = pop_size
        self.vacc_percentage = vacc_percentage
        self.initial_infected = initial_infected
        self.logger = Logger("logger.txt")
        self.population = self._create_population()
        self.newly_infected = []
        pass

    def _create_population(self):
        population = []
        infected_count = 0

        for i in range(self.pop_size):
            if infected_count < self.initial_infected:
                population.append(Person(i, False, self.virus))
                infected_count += 1
            else:
                is_vaccinated = random.random() < self.vacc_percentage
                population.append(Person(i, is_vaccinated))

        return population

    def _simulation_should_continue(self):
        for person in self.population:
            if person.is_alive and not person.is_vaccinated:
                return True
        return False

    def run(self):
        time_step_counter = 0
        should_continue = True

        self.logger.write_metadata(self.pop_size, self.vacc_percentage, self.virus.name, self.virus.mortality_rate, self.virus.repro_rate)

        while should_continue:
            time_step_counter += 1
            self.time_step()
            should_continue = self._simulation_should_continue()

        # logging final results
        living_count = sum(1 for p in self.population if p.is_alive)
        vaccinated_count = sum(1 for p in self.population if p.is_vaccinated)
        dead_count = self.pop_size - living_count
        self.logger.log_final_results(self.pop_size, living_count, dead_count, vaccinated_count, time_step_counter)
        
    def time_step(self):
        for person in self.population:
            if person.is_alive and person.infection:
                for _ in range(100):
                    random_person = random.choice(self.population)
                    if random_person.is_alive:
                        self.interaction(person, random_person)

        self._infect_newly_infected()

    def interaction(self, infected_person, random_person):
        if random_person.is_vaccinated:
            self.logger.log_interactions(0, 0, 0) 
        elif random_person.infection:
            self.logger.log_interactions(0, 0, 0)  
        else:
            if random.random() < self.virus.repro_rate:
                self.newly_infected.append(random_person)

    def _infect_newly_infected(self):
        for person in self.newly_infected:
            person.infection = self.virus
        self.newly_infected = []

if __name__ == "__main__":
    # Test your simulation here
    virus_name = "Sniffles"
    repro_num = 0.5
    mortality_rate = 0.12
    virus = Virus(virus_name, repro_num, mortality_rate)

    # Set some values used by the simulation
    pop_size = 1000
    vacc_percentage = 0.1
    initial_infected = 10

    # Make a new instance of the imulation
    # virus = Virus(virus, pop_size, vacc_percentage, initial_infected)
    sim = Simulation(virus, pop_size, vacc_percentage, initial_infected)

    sim.run()
