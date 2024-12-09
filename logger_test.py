import unittest
import os
from logger import Logger

class LoggerTest(unittest.TestCase):

    def setUp(self):
        self.test_file = 'test_log.txt'
        self.logger = Logger(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_write_metadata(self):
        self.logger.write_metadata(1000, 0.5, "TestVirus", 0.1, 2.5, 100)

        with open(self.test_file, 'r') as f:
            content = f.read()
            self.assertIn("Population Size: 1000", content)
            self.assertIn("Vaccination Percentage: 0.5", content)
            self.assertIn("Virus Name: TestVirus", content)
            self.assertIn("Mortality Rate: 0.1", content)
            self.assertIn("Basic Reproduction Number: 2.5", content)
            self.assertIn("Initial Infected: 100", content)

    def test_log_interactions(self):
        self.logger.log_interactions(1, 100, 50, 10)

        with open(self.test_file, 'r') as f:
            content = f.read()
            self.assertIn("Step 1 Interaction Log:", content)
            self.assertIn("Number of Interactions: 100", content)
            self.assertIn("New Infections: 50", content)
            self.assertIn("New Fatalities: 10", content)

    def test_log_infection_survival(self):
        self.logger.log_infection_survival(2, 950, 10)

        with open(self.test_file, 'r') as f:
            content = f.read()
            self.assertIn("Step: 2", content)  
            self.assertIn("Total Population: 950", content)
            self.assertIn("New Fatalities: 10", content)

    def test_log_final_results(self):
        self.logger.log_final_results(1000, 800, 200, "TestVirus", 1000, 100, 500)

        with open(self.test_file, 'r') as f:
            content = f.read()
            self.assertIn("Final Results", content)
            self.assertIn("Total Steps: 1000", content)
            self.assertIn("Dead People: 800", content)
            self.assertIn("Total Vaccinated: 200", content)
            self.assertIn("Virus: TestVirus", content)
            self.assertIn("Population Size: 1000", content)
            self.assertIn("Initial Infected: 100", content)
            self.assertIn("Vaccination Percentage: 500", content)

if __name__ == '__main__':
    unittest.main()
