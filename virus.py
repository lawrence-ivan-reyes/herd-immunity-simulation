class Virus(object):
    def __init__(self, name, repro_rate, mortality_rate):
        self.name = name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate

if __name__ == "__main__":
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.name == "HIV"
    assert virus.repro_rate == 0.8
    assert virus.mortality_rate == 0.3

    virus = Virus("Ebola", 0.3, 0.65)
    assert virus.name == "Ebola"
    assert virus.repro_rate == 0.3
    assert virus.mortality_rate == 0.65

    virus = Virus("Chicken Pox", 0.73, 0.05)
    assert virus.name == "Chicken Pox"
    assert virus.repro_rate == 0.73
    assert virus.mortality_rate == 0.05
