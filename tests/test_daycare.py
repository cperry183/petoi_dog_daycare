"""
Unit tests for Petio Dog Daycare
Run with: pytest tests/
"""

import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from dog import PetioDog
from daycare import Daycare


class TestPetioDog:
    def test_dog_creation(self):
        dog = PetioDog("Test", "Lab", "Owner")
        assert dog.name == "Test"
        assert dog.energy == 10
        assert dog.hunger == 5
    
    def test_play_reduces_energy(self):
        dog = PetioDog("Test", "Lab", "Owner")
        initial_energy = dog.energy
        dog.play()
        assert dog.energy < initial_energy
    
    def test_play_increases_hunger(self):
        dog = PetioDog("Test", "Lab", "Owner")
        initial_hunger = dog.hunger
        dog.play()
        assert dog.hunger > initial_hunger
    
    def test_eat_reduces_hunger(self):
        dog = PetioDog("Test", "Lab", "Owner")
        dog.hunger = 8
        dog.eat()
        assert dog.hunger < 8
    
    def test_cannot_play_when_exhausted(self):
        dog = PetioDog("Test", "Lab", "Owner")
        dog.energy = 1
        result = dog.play()
        assert "needs a nap" in result


class TestDaycare:
    def test_daycare_creation(self):
        dc = Daycare("Test Center")
        assert dc.name == "Test Center"
        assert dc.revenue == 0
    
    def test_register_dog(self):
        dc = Daycare("Test")
        dog = PetioDog("Fido", "Mutt", "Owner")
        result = dc.register(dog)
        assert "Registered" in result
        assert "Fido" in dc.pups
    
    def test_check_in_charges_money(self):
        dc = Daycare("Test", daily_rate=50)
        dog = PetioDog("Fido", "Mutt", "Owner")
        dc.register(dog)
        dc.check_in("Fido")
        assert dc.revenue == 50
    
    def test_group_play_only_for_checked_in(self):
        dc = Daycare("Test")
        dog = PetioDog("Fido", "Mutt", "Owner")
        dc.register(dog)
        # Not checked in
        result = dc.group_play()
        assert "Nobody playing" in result or result == ""
