"""
Dog module - Represents individual dogs attending daycare
"""

from typing import List, Optional
from datetime import datetime


class PetioDog:
    """
    Represents a dog with attributes tracking physical and emotional states.
    
    Attributes:
        name (str): Dog's name
        breed (str): Dog breed
        owner (str): Owner's name
        needs (list): Special requirements (dietary, medical)
        energy (int): 0-10 scale (10 = full energy)
        hunger (int): 0-10 scale (0 = full, 10 = starving)
        happy (int): 0-10 scale (10 = ecstatic)
    """
    
    MAX_STAT = 10
    MIN_STAT = 0
    
    def __init__(self, name: str, breed: str, owner: str, needs: Optional[List[str]] = None):
        self.name = name
        self.breed = breed
        self.owner = owner
        self.needs = needs or []
        self.energy = self.MAX_STAT
        self.hunger = 5
        self.happy = 5
        self._checked_in = False
        self.location = "Home"
        self.activity_log = []
    
    @property
    def checked_in(self) -> bool:
        return self._checked_in
    
    def check_in(self) -> str:
        """Check dog into daycare"""
        self._checked_in = True
        self.location = "Reception"
        self._log_activity("Checked in")
        return f"🐕 {self.name} is here!"
    
    def check_out(self) -> str:
        """Check dog out and return to owner"""
        self._checked_in = False
        self.location = "Home"
        self._log_activity("Checked out")
        return f"🚗 {self.name} went home with {self.owner}"
    
    def eat(self, food: str = "kibble") -> str:
        """
        Feed the dog. Reduces hunger, increases energy slightly.
        
        Args:
            food: Type of food being given
            
        Returns:
            Status message
        """
        if self.hunger > 0:
            self.hunger = max(self.MIN_STAT, self.hunger - 3)
            self.energy = min(self.MAX_STAT, self.energy + 2)
            self._log_activity(f"Ate {food}")
            return f"🍖 {self.name} ate {food} (Hunger: {self.hunger})"
        return f"{self.name} is full"
    
    def play(self, game: str = "fetch") -> str:
        """
        Play activity. Reduces energy, increases happiness and hunger.
        
        Args:
            game: Type of game/activity
            
        Returns:
            Status message or rest suggestion
        """
        if self.energy >= 2:
            self.energy -= 2
            self.happy = min(self.MAX_STAT, self.happy + 1)
            self.hunger = min(self.MAX_STAT, self.hunger + 1)
            self.location = "Playground"
            self._log_activity(f"Played {game}")
            return f"🎾 {self.name} played {game} (Energy: {self.energy})"
        return f"😴 {self.name} needs a nap (Energy too low)"
    
    def sleep(self) -> str:
        """Nap time - restores energy"""
        self.energy = min(self.MAX_STAT, self.energy + 4)
        self.location = "Nap Room"
        self._log_activity("Took a nap")
        return f"💤 {self.name} napped (Energy: {self.energy})"
    
    def stats(self) -> str:
        """Current status report"""
        return (f"{self.name} ({self.breed}): "
                f"Energy={self.energy}, Hunger={self.hunger}, "
                f"Happy={self.happy}, Location={self.location}")
    
    def _log_activity(self, action: str):
        """Private method to log timestamped activities"""
        timestamp = datetime.now().strftime("%H:%M")
        self.activity_log.append(f"[{timestamp}] {action}")
    
    def get_report_card(self) -> str:
        """Generate end-of-day report"""
        report = f"\n📋 Report Card for {self.name}:\n"
        report += f"   Breed: {self.breed}\n"
        report += f"   Owner: {self.owner}\n"
        report += f"   Final Status: {self.stats()}\n"
        report += f"   Today's Activities:\n"
        for activity in self.activity_log:
            report += f"      {activity}\n"
        return report
