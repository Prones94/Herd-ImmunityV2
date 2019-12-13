from Simulation import Simulation
from Virus import Virus
import pytest


def test_constructor():
    virus = Virus("AIDS", 0.12, 0.56)
    env = Simulation(20, .6, virus, 3)

    assert env.population_size == 50
    assert env.virus == virus
    assert env.initial_infected == 4


def test_simulation_should_continue():
    virus = Virus("AIDS", 0.12, 0.56)
    env = Simulation(20, .6, virus, 3)

    assert env.simulation_should_continue()


def test_infect_newly():
    virus = Virus("AIDS", 0.12, 0.56)
    env = Simulation(20, .6, virus, 3)
    env.infect_newly_infected()
    assert env.initial_infected == 4


def test_create_population():
    virus = Virus("AIDS", 0.12, 0.56)
    env = Simulation(20, .6, virus, 3)

    vaccination_count = 0
    infection_count = 0

    for person in env.population:
        assert person.is_alive == True

        if person.is_vaccinated:
            vaccination_count += 1
        if person.infection is not None:
            infection_count += 1

    assert vaccination_count == 5
    assert infection_count == 2
    assert len(env.population) == 10