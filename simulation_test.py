import unittest
from simulation import Simulation
from person import Person
from virus import Virus

class SimulationTest(unittest.TestCase):
    def setUp(self):
        self.virus = Virus("TestVirus", 0.5, 0.5)
        self.sim = Simulation(self.virus, 100, 0.5, 10)

    def test_create_population(self):
        self.assertEqual(len(self.sim.population), 100)

        infected_count = sum(1 for person in self.sim.population if person.infection)
        self.assertEqual(infected_count, 10)

    def test_simulation_should_continue_true(self):
        self.assertTrue(self.sim._simulation_should_continue())

    def test_simulation_should_continue_false_all_dead(self):
        for person in self.sim.population:
            person.is_alive = False
        self.assertFalse(self.sim._simulation_should_continue())

    def test_simulation_should_continue_false_all_vaccinated(self):
        for person in self.sim.population:
            if person.is_alive:
                person.is_vaccinated = True
        self.assertFalse(self.sim._simulation_should_continue())

    def test_interaction_vaccinated(self):
        infected_person = Person(1, False, self.virus)
        vaccinated_person = Person(2, True)
        self.sim.interaction(infected_person, vaccinated_person)
        self.assertNotIn(vaccinated_person, self.sim.newly_infected)

    def test_interaction_infected(self):
        infected_person = Person(1, False, self.virus)
        already_infected_person = Person(2, False, self.virus)
        self.sim.interaction(infected_person, already_infected_person)
        self.assertNotIn(already_infected_person, self.sim.newly_infected)

    def test_interaction_unvaccinated(self):
        infected_person = Person(1, False, self.virus)
        unvaccinated_person = Person(2, False)
        self.sim.interaction(infected_person, unvaccinated_person)

    def test_infect_newly_infected(self):
        infected_person_1 = Person(1, False, self.virus)
        infected_person_2 = Person(2, False, self.virus)
        infected_person_3 = Person(3, False, self.virus)

        self.sim.newly_infected = [infected_person_1, infected_person_2, infected_person_3]

        self.sim._infect_newly_infected()

        for person in self.sim.newly_infected:
            self.assertIsNotNone(person.infection)  

        self.assertEqual(len(self.sim.newly_infected), 0)

if __name__ == '__main__':
    unittest.main()
