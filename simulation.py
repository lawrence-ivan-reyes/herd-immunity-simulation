import random
from person import Person
from logger import Logger
from virus import Virus

class Simulation:
    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
        self.virus = virus
        self.pop_size = pop_size
        self.vacc_percentage = vacc_percentage
        self.initial_infected = initial_infected
        self.newly_infected_list = []
        self.time_step_counter = 0
        self.current_infected = initial_infected
        self.total_infected = initial_infected
        self.total_vaccinated = 0
        self.total_dead = 0
        self.total_interactions = 0
        self.logger = Logger("logger.txt")
        self.population = self._create_population()

    def _create_population(self):
        population_list = []
        vaccinated_count = int(self.pop_size * self.vacc_percentage)
        unvaccinated_count = self.pop_size - vaccinated_count - self.initial_infected
        for _ in range(vaccinated_count):
            population_list.append(Person(len(population_list), True, None))
        for _ in range(unvaccinated_count):
            population_list.append(Person(len(population_list), False, None))
        for _ in range(self.initial_infected):
            population_list.append(Person(len(population_list), False, self.virus))
        self.logger.write_metadata(self.pop_size, self.vacc_percentage, self.virus.name, self.virus.mortality_rate, 
                                self.virus.repro_rate, self.initial_infected)
        return population_list

    def _simulation_should_continue(self):
        for person in self.population:
            if person.is_alive and not person.is_vaccinated:
                return True
        return False

    def run(self):
        should_continue = True
        while should_continue:
            self.time_step()
            should_continue = self._simulation_should_continue()
            self.time_step_counter += 1
            self.logger.log_interactions(self.time_step_counter, self.total_interactions, self.total_dead, self.total_vaccinated, self.current_infected)
            if not should_continue:
                self.logger.log_final_results(self.time_step_counter, self.total_dead, self.total_vaccinated, self.virus.name, 
                                              self.pop_size, self.initial_infected, self.vacc_percentage)
        print(f"Time steps: {self.time_step_counter}")
        print(f"Total interactions: {self.total_interactions}")
        print(f"Total deaths: {self.total_dead}")
        print(f"Total vaccinated: {self.total_vaccinated}")
        print(f"Current infected: {self.current_infected}")

    def _get_random_person(self):
        random_person = random.choice(self.population)
        while not random_person.is_alive or random_person.is_vaccinated or random_person.infection is not None:
            random_person = random.choice(self.population)
        return random_person

    def time_step(self):
        for person in self.population:
            if person.infection and person.is_alive:
                for _ in range(100):
                    self.interaction(person, self._get_random_person())

                if person.did_survive_infection() == True:
                    self.current_infected -= 1
                    person.is_vaccinated = True
                    self.total_vaccinated += 1

                else:
                    person.is_alive = False
                    self.total_dead += 1
                    self.current_infected -= 1

        self._infect_newly_infected()

    def interaction(self, infected_person, random_person):
        self.total_interactions += 1

        if random_person.is_vaccinated == True:
            self.total_lives_saved_with_vaccine += 1
        elif random_person.is_vaccinated == False and random_person.infection == None and random_person.is_alive == True:
            if random.random() < self.virus.repro_rate: 
                self.newly_infected_list.append(random_person)
                self.population.remove(random_person)

    def _infect_newly_infected(self):
        for person in self.newly_infected_list:
            person.infection = self.virus
            self.population.append(person)
            self.current_infected += 1
            self.total_infected += 1
        self.newly_infected_list = []

if __name__ == "__main__":
    virus_name = "Sniffles"
    repro_num = 0.5
    mortality_rate = 0.12
    virus = Virus(virus_name, repro_num, mortality_rate)
    pop_size = 1000
    vacc_percentage = 0.1
    initial_infected = 10
    sim = Simulation(virus, pop_size, vacc_percentage, initial_infected)
    sim.run()
