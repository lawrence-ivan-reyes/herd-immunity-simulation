import pytest
from virus import Virus

def test_virus():
    virus = Virus("Ebola", 0.3, 0.65)
    assert virus.name == "Ebola"
    assert virus.repro_rate == 0.3
    assert virus.mortality_rate == 0.65

def test_virus():
    virus = Virus("Chicken Pox", 0.73, 0.05)
    assert virus.name == "Chicken Pox"
    assert virus.repro_rate == 0.73
    assert virus.mortality_rate == 0.05
