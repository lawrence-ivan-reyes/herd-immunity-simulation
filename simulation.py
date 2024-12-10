import random
from person import Person
from logger import Logger
from virus import Virus

class Simulation(object):
    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
        self.logger = Logger("logger.txt")
        self.virus = virus
        self.pop_size = pop_size
        self.vacc_percentage = vacc_percentage
        self.initial_infected = initial_infected

        self.newly_infected = []
        self.dead_people_list = []
        self.time_step_counter = 0
        self.current_infected = initial_infected
        self.total_infected = initial_infected
        self.total_dead = 0
        self.total_vaccinated = 0
        self.total_interactions = 0
        self.total_lives_saved_with_vaccine = 0

        self.population = self._create_population(initial_infected)

    def _create_population(self, initial_infected):
        population = []
        num_vaccinated = int(self.pop_size * self.vacc_percentage)
        num_unvaccinated = self.pop_size - num_vaccinated - initial_infected

        for i in range(num_vaccinated):
            population.append(Person(i, True))
        for i in range(num_unvaccinated):
            population.append(Person(i + num_vaccinated, False))
        for i in range(initial_infected):
            population.append(Person(i + num_vaccinated + num_unvaccinated, False, self.virus))

        self.logger.write_metadata(self.pop_size, self.vacc_percentage, self.virus.name, self.virus.mortality_rate, self.virus.repro_rate, self.initial_infected)
        return population

    def _simulation_should_continue(self):
        for person in self.population:
            if person.is_alive and not person.is_vaccinated:
                return True
        return False

    def run(self):
        time_step_counter = 0
        should_continue = self._simulation_should_continue()
        while should_continue:
            self.time_step()
            time_step_counter += 1
            self.logger.log_interactions(time_step_counter, self.total_interactions, self.total_dead, self.total_vaccinated, self.current_infected)
            should_continue = self._simulation_should_continue()
        self.logger.log_final_results(time_step_counter, self.total_dead, self.total_vaccinated, self.virus.name, self.pop_size, self.initial_infected, self.vacc_percentage)
        print(f"Time steps: {time_step_counter}")

    def time_step(self):
        for person in self.population:
            if person.infection and person.is_alive:
                for _ in range(100):
                    random_person = self.get_random_person()
                    self.interaction(person, random_person)
                survived = person.did_survive_infection()
                if survived:
                    self.total_vaccinated += 1
                else:
                    self.total_dead += 1
                self.current_infected -= 1
        self._infect_newly_infected()

    def interaction(self, infected_person, random_person):
        self.total_interactions += 1
        if random_person.is_vaccinated:
            self.total_lives_saved_with_vaccine += 1
        elif not random_person.infection and random_person.is_alive:
            if random.random() < self.virus.repro_rate:
                self.newly_infected.append(random_person._id)
                self.current_infected += 1
                self.total_infected += 1

    def get_random_person(self):
        random_person = random.choice(self.population)
        while not random_person.is_alive or random_person._id == random.choice(self.population)._id:
            random_person = random.choice(self.population)
        return random_person

    def _infect_newly_infected(self):
        for person_id in self.newly_infected:
            for person in self.population:
                if person._id == person_id:
                    person.infection = self.virus
        self.newly_infected = []

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
