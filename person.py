import random
# random.seed(42)
from virus import Virus


class Person(object):
    # Define a person. 
    def __init__(self, _id, is_vaccinated, infection = None):
        # A person has an id, is_vaccinated and possibly an infection
        self._id = _id  # int
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


    # You need to check the survival of an infected person. Since the chance
    # of survival is random you need to check a group of people. 
    # Create a list to hold 100 people. Use the loop below to make 100 people
    people = []
    for i in range(1, 100):
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
    uninfected_people = [Person(i + 101, False) for i in range(100)] # make another 100 ppl

    for person in uninfected_people:
        if random.random() < virus.spread_rate:
            person.infection = virus

    # count infected & uninfected ppl from this group of ppl
    infected_count = sum(1 for person in uninfected_people if person.infection is None)
    uninfected_count = len(uninfected_people) - infected_count

    print(f"Number of people infected: {infected_count}")
    print(f"Number of people uninfected: {uninfected_count}")
