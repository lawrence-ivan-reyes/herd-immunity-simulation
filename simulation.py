import random
from person import Person
from logger import Logger
from virus import Virus
import matplotlib.pyplot as plt  # stretch challenge #3 (graphing visualization with matplotlib)

class Simulation(object):
    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):
        self.virus = virus
        self.pop_size = pop_size
        self.vacc_percentage = vacc_percentage
        self.initial_infected = initial_infected

        self.newly_infected = []
        self.deceased_population = []

        self.time_step_counter = 0
        self.current_infected = 0
        self.total_infected = 0
        self.vaccinated_counter = 0
        self.total_vaccinated = 0
        self.death_count = 0
        self.total_interactions = 0
        self.total_lives_saved_with_vaccine = 0

        self.logger = Logger("logger.txt")
        self.population = self._create_population()

        # stretch challenge #3 (graphing visualization with matplotlib): track simulation data over time
        self.time_steps = []
        self.infected_over_time = []
        self.deaths_over_time = []
        self.vaccinated_over_time = []

    def _create_population(self):
        population_list = []

        vaccinated_count = int(self.pop_size * self.vacc_percentage)
        unvaccinated_count = self.pop_size - self.initial_infected - vaccinated_count
        infected_count = self.initial_infected

        self.vaccinated_counter = vaccinated_count

        individual_id = 0

        for _ in range(vaccinated_count):
            individual_id += 1
            self.vaccinated_counter += 1
            person = Person(individual_id, True, None)
            population_list.append(person)

        for _ in range(unvaccinated_count):
            individual_id += 1
            person = Person(individual_id, False, None)
            population_list.append(person)

        for _ in range(infected_count):
            individual_id += 1
            self.current_infected += 1
            self.total_infected += 1
            person = Person(individual_id, False, self.virus)
            population_list.append(person)

        self.logger.write_metadata(self.pop_size, self.vacc_percentage, self.virus, self.initial_infected)
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
            self.logger.log_interactions(self.pop_size, self.time_step_counter, len(self.newly_infected), self.death_count, self.total_vaccinated, self.current_infected, self.total_interactions)

        # stretch challenge #3 (graphing visualization with matplotlib): visualization code
        self.plot_results()

        self.logger.log_simulation_summary(self.pop_size, self.death_count, self.total_vaccinated, self.total_infected, self.time_step_counter, self.total_lives_saved_with_vaccine, self.virus, self.initial_infected, self.vacc_percentage, self.total_interactions)

        print(f"Simulation complete. Time steps: {self.time_step_counter}")
        print(self.time_step_counter, self.total_interactions, self.death_count, self.total_vaccinated, self.current_infected)

    def time_step(self):
        for person in self.population:
            if person.infection and person.is_alive:
                for _ in range(100):
                    self.interaction(person, self.get_random_person())

                if person.did_survive_infection():
                    self.current_infected -= 1
                    person.is_vaccinated = True
                    self.total_vaccinated += 1
                else:
                    person.is_alive = False
                    self.death_count += 1
                    self.current_infected -= 1

        self._infect_newly_infected()

        # stretch challenge #3 (graphing visualization with matplotlib): tracking data after each time step
        self.time_steps.append(self.time_step_counter)
        self.infected_over_time.append(self.current_infected)
        self.deaths_over_time.append(self.death_count)
        self.vaccinated_over_time.append(self.total_vaccinated)

    def get_random_person(self):
        selected_person = random.choice(self.population)
        while not selected_person.is_alive or selected_person.is_vaccinated:
            selected_person = random.choice(self.population)
        return selected_person

    def interaction(self, infected_person, random_person):
        self.total_interactions += 1

        if random_person.is_vaccinated:
            self.total_lives_saved_with_vaccine += 1
        elif random_person.infection is None and random_person.is_alive:
            if random.random() < self.virus.repro_rate:
                self.newly_infected.append(random_person)
                self.population.remove(random_person)

    def _infect_newly_infected(self):
        for person in self.newly_infected:
            person.infection = self.virus
            self.current_infected += 1
            self.total_infected += 1
            self.population.append(person)

        self.newly_infected = []

    # stretch challenge #3 (graphing visualization with matplotlib): method to plot results
    def plot_results(self):
        plt.figure(figsize=(10, 6))

        # infections over time
        plt.plot(self.time_steps, self.infected_over_time, label='Infected', color='red')

        # deaths over time
        plt.plot(self.time_steps, self.deaths_over_time, label='Deaths', color='black')

        # vaccinations over time
        plt.plot(self.time_steps, self.vaccinated_over_time, label='Vaccinated', color='green')

        # labels, title, and legend
        plt.title('Simulation Results Over Time')
        plt.xlabel('Time Steps')
        plt.ylabel('Population Count')
        plt.legend()

        # display plot
        plt.show()

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
