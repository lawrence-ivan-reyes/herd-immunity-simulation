import random
from virus import Virus

class Person(object):
    def __init__(self, _id, is_vaccinated, infection=None):
        self._id = _id  
        self.is_vaccinated = is_vaccinated
        self.infection = infection 
        self.is_alive = True

    def did_survive_infection(self):
        if self.infection:
            mortality_rate = self.infection.mortality_rate
            survival_chance = random.random() 
            if survival_chance < mortality_rate:
                self.is_alive = False
                self.infection = None 
                return False
            else:
                self.is_vaccinated = True
                self.infection = None 
                return True
        return False

if __name__ == "__main__":
    vaccinated_person = Person(1, True)
    assert vaccinated_person._id == 1
    assert vaccinated_person.is_alive is True
    assert vaccinated_person.is_vaccinated is True
    assert vaccinated_person.infection is None

    unvaccinated_person = Person(2, False)
    assert unvaccinated_person._id == 2
    assert unvaccinated_person.is_alive is True
    assert unvaccinated_person.is_vaccinated is False
    assert unvaccinated_person.infection is None

    virus = Virus("Dysentery", 0.7, 0.2)
    infected_person = Person(3, False, virus)
    assert infected_person._id == 3
    assert infected_person.is_alive is True
    assert infected_person.is_vaccinated is False
    assert infected_person.infection == virus

    people = []
    for i in range(1, 101):
        people.append(Person(i, False, virus))

    did_survive = 0
    did_not_survive = 0

    for person in people:
        if person.did_survive_infection():
            did_survive += 1
        else:
            did_not_survive += 1

    print(f"Survived: {did_survive}, Did not survive: {did_not_survive}")
    print(f"Mortality rate: {virus.mortality_rate}, Approx deaths: {did_not_survive / len(people):.2f}")

    # Stretch challenge! 
    uninfected_people = [Person(i, False) for i in range(101, 201)]
    newly_infected = 0

    for person in uninfected_people:
        if random.random() < virus.repro_rate:
            person.infection = virus
            newly_infected += 1

    print(f"Newly Infected: {newly_infected}, Not Infected: {len(uninfected_people) - newly_infected}")
    print(f"Infection rate: {virus.repro_rate}, Approx infections: {newly_infected / len(uninfected_people):.2f}")
