from datetime import datetime

class Logger(object):
    def __init__(self, file_name):
        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus, initial_infected):
        with open(self.file_name, "w") as log:
            log.write(f"""
Simulation Metadata
-------------------
Date                   : {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
Initial Population Size: {pop_size}
Initial Infected       : {initial_infected}
Virus Name             : {virus.name}
Reproductive Rate      : {virus.repro_rate}
Mortality Rate         : {virus.mortality_rate}
Vaccinated Percentage  : {round(vacc_percentage * 100)}%
""")

    def log_interactions(self, pop_size, step_number, newly_infected, dead_people, total_vaccinated, current_infected, total_interactions):
        with open(self.file_name, "a") as log:
            log.write(f"""
Step {step_number} Summary
---------------------------
New Infections          : {newly_infected}
New Deaths              : {dead_people}
Current Infected        : {current_infected}
Total Interactions      : {total_interactions}
Total Vaccinated        : {total_vaccinated}
---------------------------
Total Living            : {pop_size - dead_people}
Total Dead              : {dead_people}
Total Vaccinated        : {total_vaccinated}
""")

    def log_simulation_summary(self, pop_size, dead_people, total_vaccinated, total_infected, total_steps, vaccine_saves, virus, initial_infected, vacc_percentage, total_interactions):
        with open("simulation_summary.txt", "w") as log:
            log.write(f"""
Simulation Summary
-------------------
Date                   : {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
Initial Population Size: {pop_size}
Initial Infected       : {initial_infected}
Virus Name             : {virus.name}
Reproductive Rate      : {virus.repro_rate}
Mortality Rate         : {virus.mortality_rate}
Vaccinated Percentage  : {round(vacc_percentage * 100)}%

Final Statistics:
-----------------
Total Living           : {pop_size - dead_people}
Total Dead             : {dead_people}
Total Infected         : {total_infected}
Total Vaccinated       : {total_vaccinated}
Total Interactions     : {total_interactions}
Total Vaccine Saves    : {vaccine_saves}
Why Simulation Ended   : Simulation stopped due to no more unvaccinated, alive people remaining.
""")
