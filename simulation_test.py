import unittest
from simulation import Simulation
from virus import Virus

class TestSimulation(unittest.TestCase):

    def setUp(self):
        self.virus = Virus("Sniffles", 0.5, 0.12)
        self.pop_size = 1000
        self.vacc_percentage = 0.1
        self.initial_infected = 10
        self.simulation = Simulation(self.virus, self.pop_size, self.vacc_percentage, self.initial_infected)

    def test_population_creation(self):
        vaccinated_count = int(self.pop_size * self.vacc_percentage)
        unvaccinated_count = self.pop_size - vaccinated_count - self.initial_infected
        infected_count = self.initial_infected

        vaccinated = sum(1 for person in self.simulation.population if person.is_vaccinated)
        unvaccinated = sum(1 for person in self.simulation.population if not person.is_vaccinated and person.infection is None)
        infected = sum(1 for person in self.simulation.population if person.infection is not None)

        self.assertEqual(vaccinated, vaccinated_count)
        self.assertEqual(unvaccinated, unvaccinated_count)
        self.assertEqual(infected, infected_count)

    def test_simulation_should_continue(self):
        self.simulation._simulation_should_continue()
        should_continue = self.simulation._simulation_should_continue()

        self.assertTrue(should_continue)

    def test_time_step(self):
        initial_infected = self.simulation.current_infected
        initial_total_infected = self.simulation.total_infected

        self.simulation.time_step()

        self.assertNotEqual(self.simulation.current_infected, initial_infected)
        self.assertNotEqual(self.simulation.total_infected, initial_total_infected)

    def test_interaction(self):
        person = self.simulation.get_random_person()
        infected_person = self.simulation.get_random_person()
        
        initial_newly_infected = len(self.simulation.newly_infected)
        
        self.simulation.interaction(infected_person, person)
        
        self.assertGreater(len(self.simulation.newly_infected), initial_newly_infected)

    def test_simulation_completion(self):
        self.simulation.run()
        self.assertEqual(self.simulation._simulation_should_continue(), False)

if __name__ == "__main__":
    unittest.main()
