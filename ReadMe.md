# Herd Immunity Simulation 🦠
### Ivan Reyes | ACS 1111: Object Oriented Programming | Dani Roxberry

---

### ℹ️ Program Description
The Virus Simulation program models the spread of a virus within a population, tracking key metrics such as infection rate, vaccination effects, mortality rate, and the total number of deaths over time. This simulation runs in time steps, during which infected individuals interact with unvaccinated, healthy people, potentially spreading the virus. The program logs all interactions, simulates deaths and recoveries, and provides data visualizations of the virus's progress.

**Key Features:**
- **Infection Spread**: Infected individuals interact with random unvaccinated individuals, and new infections may occur based on the virus's reproduction rate.
- **Mortality and Recovery**: Infected people either recover or die based on the virus's mortality rate. Recovered individuals become immune and vaccinated.
- **Vaccination Impact**: Vaccinated individuals cannot become infected, and the simulation tracks the number of lives saved due to vaccinations.
- **Simulation Logging**: Detailed logs of each time step’s interactions, deaths, and vaccinations are saved, enabling deeper analysis of the simulation's progression.
- **Data Visualization**: Track the virus's spread over time with charts showing infected, dead, and vaccinated individuals at each step.

---

### ❗️ How To Use
1. **Clone the repository:**
- **HTTPS**: `git clone https://github.com/lawrence-ivan-reyes/herd-immunity-simulation.git`  
- **SSH**: `git clone git@github.com:lawrence-ivan-reyes/herd-immunity-simulation.git`  
- **GitHub CLI**: `gh repo clone lawrence-ivan-reyes/herd-immunity-simulation` 

2. **Run the Program:** 
`python3 simulation.py`

You can customize the simulation's parameters in the `simulation.py` file by adjusting values such as:
- Virus name and characteristics (reproductive rate, mortality rate).
- Population size.
- Percentage of the population vaccinated.
- Initial number of infected individuals.

3. **Log Files**
`logger.txt`: Logs the simulation's metadata and interaction summaries for each time step.

4. **Data Visualization**

After running the simulation, it will generate a plot showing the progression of infections, deaths, and vaccinations over time (requires `matplotlib`).
- If you do not have `matplotlib` installed, run `pip install matplotlib` in your terminal before proceeding to run `simulation.py`.

---

### 💻 Code Structure
**Main Program Files**
- **`simulation.py`**: The main file that runs the entire simulation. Contains logic for time steps, interactions, infection spread, and logging.
- **`person.py`**: Defines the `Person` class, representing individuals in the population. Handles infection status, survival, and vaccination.
- **`virus.py`**: Defines the `Virus` class, representing the virus being simulated, with attributes like reproduction and mortality rates.
- **`logger.py`**: Provides logging functionality. Logs simulation metadata, time step summaries, and final results.
