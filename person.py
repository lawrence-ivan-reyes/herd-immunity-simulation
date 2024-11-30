import random
from virus import Virus


class Person(object):
    def __init__(self, _id, is_vaccinated, infection = None):
        self._id = _id  
        self.is_vaccinated = is_vaccinated
        self.infection = infection 
        self.is_alive = True

    def did_survive_infection(self):
        if self.infection is None:
            return True
        
        survival_chance = random.random() # to generate number b/w 0.0 & 1.0
        if survival_chance < self.infection.mortality_rate:
            self.is_alive = False
            return False # means they died
        else:
            self.is_vaccinated = True 
            self.infection = None
            return True
        
if __name__ == "__main__":
    vaccinated_person = Person(1, True)
    assert vaccinated_person._id == 1
    assert vaccinated_person.is_alive is True
    assert vaccinated_person.is_vaccinated is True
    assert vaccinated_person.infection is None

    unvaccinated_person = Person(2, False)
    assert unvaccinated_person._id == 2
    assert unvaccinated_person.is_alive is False
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

    for person in people:
        survived = person.did_survive_infection()

    did_survive = 0
    did_not_survive = 0

    for person in people:
        if person.is_alive:
            did_survive += 1
        else:
            did_not_survive += 1

    print(f"Number of people who survived: {did_survive}")
    print(f"Number of people who did not survive: {did_not_survive}")

    # Stretch challenge! 
    uninfected_people = []
    for i in range (101, 201): # make another 100 ppl
        person = Person(i, False)
        uninfected_people.append(person)
    
    for person in uninfected_people:
        if random.random() < virus.repro_rate:
            person.infection = virus

    infected_count = 0
    uninfected_count = 0
    for person in uninfected_people:
        if person.infection is not None:
            infected_count += 1
        else:
            uninfected_count += 1

    print("\nInfection Rate Check:")
    print(f"Infected: {infected_count} people")
    print(f"Uninfected: {uninfected_count} people")
    print(f"Percentage Infected: {infected_count / len(uninfected_count):.2f}")
