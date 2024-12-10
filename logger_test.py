import unittest
import os
from logger import Logger
from virus import Virus

class TestLogger(unittest.TestCase):

    def setUp(self):
        self.file_name = "test_logger.txt"
        self.summary_file_name = "simulation_summary.txt"
        self.virus = Virus("Sniffles", 0.5, 0.12)
        self.pop_size = 1000
        self.vacc_percentage = 0.1
        self.initial_infected = 10
        self.logger = Logger(self.file_name)

    def test_write_metadata(self):
        self.logger.write_metadata(self.pop_size, self.vacc_percentage, self.virus, self.initial_infected)

        with open(self.file_name, "r") as file:
            content = file.read()

        self.assertIn("Simulation Metadata", content)
        self.assertIn(f"Initial Population Size  : {self.pop_size}", content)
        self.assertIn(f"Virus Name               : {self.virus.name}", content)
        self.assertIn(f"Reproduction Rate        : {self.virus.repro_rate}", content)
        self.assertIn(f"Mortality Rate           : {self.virus.mortality_rate}", content)
        self.assertIn(f"Initial Infected         : {self.initial_infected}", content)

    def test_log_interactions(self):
        step_number = 1
        number_of_interactions = 100
        dead_people = 0
        total_vaccinated = 50
        total_infections = 30

        self.logger.log_interactions(step_number, number_of_interactions, dead_people, total_vaccinated, total_infections)

        with open(self.file_name, "r") as file:
            content = file.read()

        self.assertIn(f"Step {step_number} Summary", content)
        self.assertIn(f"Total Interactions       : {number_of_interactions}", content)
        self.assertIn(f"Total People Dead        : {dead_people}", content)
        self.assertIn(f"Total Vaccinated         : {total_vaccinated}", content)
        self.assertIn(f"Total Infections         : {total_infections}", content)

    def test_log_simulation_summary(self):
        dead_people = 100
        total_vaccinated = 200
        total_infections = 500
        total_steps = 10
        vaccine_saves = 50
        total_interactions = 1000

        self.logger.log_simulation_summary(
            self.pop_size, dead_people, total_vaccinated, total_infections, total_steps,
            vaccine_saves, self.virus, self.initial_infected, self.vacc_percentage, total_interactions
        )

        with open(self.summary_file_name, "r") as file:
            content = file.read()

        self.assertIn("Simulation Results", content)
        self.assertIn(f"Initial Population Size  : {self.pop_size}", content)
        self.assertIn(f"Virus Name               : {self.virus.name}", content)
        self.assertIn(f"Mortality Rate           : {self.virus.mortality_rate}", content)
        self.assertIn(f"Reproductive Rate        : {self.virus.repro_rate}", content)
        self.assertIn(f"Initial Infected         : {self.initial_infected}", content)
        self.assertIn(f"Percentage of Population Who Died         : {round(dead_people / self.pop_size * 100)}%", content)
        self.assertIn(f"Total Dead                 : {dead_people}", content)
        self.assertIn(f"Total Vaccinated           : {total_vaccinated}", content)
        self.assertIn(f"Total Infections           : {total_infections}", content)

    def tearDown(self):
        if os.path.exists(self.file_name):
            os.remove(self.file_name)
        if os.path.exists(self.summary_file_name):
            os.remove(self.summary_file_name)

if __name__ == "__main__":
    unittest.main()
