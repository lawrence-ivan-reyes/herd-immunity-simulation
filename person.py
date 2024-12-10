import random
from virus import Virus

class Person(object):
    def __init__(self, _id, is_vaccinated, infection=None):
        self._id = _id
        self.is_vaccinated = is_vaccinated
        self.is_alive = True
        self.infection = infection

    def did_survive_infection(self):
        if self.infection:
            random_survival_chance = random.random()
            if random_survival_chance > self.infection.mortality_rate:
                self.is_alive = True
                self.is_vaccinated = True
                self.infection = None
                return True
            else:
                self.is_alive = False
                return False
        return self.is_alive

if __name__ == "__main__":
    virus = Virus("Dysentery", 0.7, 0.2)

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

    infected_person = Person(3, False, infection=virus)
    assert infected_person._id == 3
    assert infected_person.is_alive is True
    assert infected_person.is_vaccinated is False
    assert infected_person.infection is virus

    people = []
    for i in range(1, 101):
        people.append(Person(i, False, infection=virus))

    survived = 0
    did_not_survive = 0

    for person in people:
        if person.did_survive_infection():
            survived += 1
        else:
            did_not_survive += 1

    print(f"People who survived: {survived}")
    print(f"People who did not survive: {did_not_survive}")

    uninfected_people = [Person(i, False) for i in range(101, 201)]
    for person in uninfected_people:
        if random.random() < virus.infection_rate:
            person.infection = virus

    infected_count = sum(1 for person in uninfected_people if person.infection)
    uninfected_count = len(uninfected_people) - infected_count

    print(f"Infected people: {infected_count}")
    print(f"Uninfected people: {uninfected_count}")
