class Logger(object):
    def __init__(self, file_name):
        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       basic_repro_num):
        with open(self.file_name, 'w') as f:
            f.write(f"Population Size: {pop_size}\t"
                    f"Vaccination Percentage: {vacc_percentage}\t"
                    f"Virus Name: {virus_name}\t"
                    f"Mortality Rate: {mortality_rate}\t"
                    f"Basic Reproduction Number: {basic_repro_num}\n")

    def log_interactions(self, step_number, number_of_interactions, number_of_new_infections):
        with open(self.file_name, 'a') as f:
            f.write(f"Step {step_number}:\t"
                    f"Interactions: {number_of_interactions}\t"
                    f"New Infections: {number_of_new_infections}\n")

    def log_infection_survival(self, step_number, population_count, number_of_new_fatalities):
        with open(self.file_name, 'a') as f:
            did_die_from_infection = number_of_new_fatalities > 0
            f.write(f"Step {step_number}:\t"
                    f"Population Count: {population_count}\t"
                    f"New Fatalities: {number_of_new_fatalities}\t"
                    f"Did Die From Infection: {did_die_from_infection}\n")

    # unsure if this is correct
    def log_time_step(self, time_step_number):
        with open(self.file_name, 'a') as f:
            f.write(f"Time step {time_step_number} ended.\n")
