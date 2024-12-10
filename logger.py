class Logger(object):
    def __init__(self, file_name):
        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus, initial_infected):
        with open(self.file_name, "w") as log:
            log.write(f"""
Simulation Metadata
-------------------
Initial Population Size  : {pop_size}
Vaccinated Percentage    : {round(vacc_percentage * 100)}%
Virus Name               : {virus.name}
Reproduction Rate        : {virus.repro_rate}
Mortality Rate           : {virus.mortality_rate}
Initial Infected         : {initial_infected}

""")

    def log_interactions(self, step_number, number_of_interactions, dead_people, total_vaccinated, total_infections):
        with open(self.file_name, "a") as log:
            log.write(f"""
Step {step_number} Summary
---------------------------
Total Interactions       : {number_of_interactions}
Total People Dead        : {dead_people}
Total Vaccinated         : {total_vaccinated}
Total Infections         : {total_infections}

""")

    def log_simulation_summary(self, pop_size, dead_people, total_vaccinated, total_infections, total_steps, vaccine_saves, virus, initial_infected, vacc_percentage, total_interactions):
        with open("simulation_summary.txt", "w") as log:
            log.write(f"""
Simulation Results
-----------------
Inputs Given:
-------------
Initial Population Size  : {pop_size}
Vaccinated Percentage    : {round(vacc_percentage * 100)}%
Virus Name               : {virus.name}
Mortality Rate           : {virus.mortality_rate}
Reproductive Rate        : {virus.repro_rate}
Initial Infected         : {initial_infected}

Key Statistics:
---------------
Percentage of Population Who Died         : {round(dead_people / pop_size * 100)}%
Percentage of Population Who Became Infected: {round(total_infections / pop_size * 100)}%
Total Times the Vaccine Saved a Person     : {vaccine_saves}

Final Results:
--------------
Total Steps                : {total_steps}
Total Interactions         : {total_interactions}
Total Dead                 : {dead_people}
Total Vaccinated           : {total_vaccinated}
Total Infections           : {total_infections}

""")
