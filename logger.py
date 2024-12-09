class Logger(object):
    def __init__(self, file_name):
        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num, initial_infected):
        with open(self.file_name, 'w') as f:
            f.write(f"Before simulation:\n")
            f.write(f"Population Size: {pop_size}\n")
            f.write(f"Vaccination Percentage: {vacc_percentage}\n")
            f.write(f"Virus Name: {virus_name}\n")
            f.write(f"Mortality Rate: {mortality_rate}\n")
            f.write(f"Basic Reproduction Number: {basic_repro_num}\n")
            f.write(f"Initial Infected: {initial_infected}\n")
            f.write(f"----------------------------------------------------------------------\n")

    def log_interactions(self, step_number, number_of_interactions, dead_people, total_vaccinated, total_infections):
        with open(self.file_name, 'a') as f:
            f.write(f"\nStep {step_number} Interaction Log:\n")
            f.write(f"Number of Interactions: {number_of_interactions}\n")
            f.write(f"New Infections: {total_infections}\n") 
            f.write(f"New Fatalities: {dead_people}\n")  
            f.write(f"Total Vaccinated: {total_vaccinated}\n")
            f.write(f"----------------------------------------------------------------------\n")
            
    def log_infection_survival(self, step_number, population_count, number_of_new_fatalities):
        with open(self.file_name, 'a') as f:
            f.write(f"Step: {step_number}\n")
            f.write(f"Total Population: {population_count}\n")
            f.write(f"New Fatalities: {number_of_new_fatalities}\n")
            f.write(f"----------------------------------------------------------------------\n")

    def log_step_summary(self, step_number, current_infected, total_dead, total_vaccinated):
        with open(self.file_name, 'a') as f:
            f.write(f"Step {step_number} Summary:\n")
            f.write(f"Current Infected: {current_infected}\n")
            f.write(f"Total Dead: {total_dead}\n")
            f.write(f"Total Vaccinated: {total_vaccinated}\n")
            f.write(f"----------------------------------------------------------------------\n")

    def log_final_results(self, total_steps, total_dead, total_vaccinated, virus_name, pop_size, initial_infected, vacc_percentage):
        with open(self.file_name, 'a') as f:
            f.write(f"Final Results:\n")
            f.write(f"Total Steps: {total_steps}\n")
            f.write(f"Dead People: {total_dead}\n")
            f.write(f"Total Vaccinated: {total_vaccinated}\n")
            f.write(f"Virus: {virus_name}\n")
            f.write(f"Population Size: {pop_size}\n")
            f.write(f"Initial Infected: {initial_infected}\n")
            f.write(f"Vaccination Percentage: {vacc_percentage}\n")
            f.write(f"----------------------------------------------------------------------\n")
