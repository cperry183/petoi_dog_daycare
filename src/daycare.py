"""
Daycare module - Manages facility operations and dog registry
"""

from typing import Dict, Optional
from .dog import PetioDog


class Daycare:
    """
    Manages daycare operations including check-in/out, group activities,
    and revenue tracking.
    
    Attributes:
        name (str): Facility name
        pups (dict): Registry of dogs by name
        revenue (float): Daily earnings
        daily_rate (int): Price per dog per day
    """
    
    def __init__(self, name: str, daily_rate: int = 50):
        self.name = name
        self.pups: Dict[str, PetioDog] = {}
        self.revenue = 0.0
        self.daily_rate = daily_rate
    
    def register(self, dog: PetioDog) -> str:
        """
        Add new dog to registry
        
        Args:
            dog: PetioDog instance to register
            
        Returns:
            Confirmation message
        """
        if dog.name not in self.pups:
            self.pups[dog.name] = dog
            return f"✅ Registered {dog.name}"
        return f"⚠️ {dog.name} already registered"
    
    def check_in(self, name: str) -> str:
        """Check in dog and charge daily rate"""
        if name in self.pups:
            result = self.pups[name].check_in()
            self.revenue += self.daily_rate
            return f"{result} (+${self.daily_rate})"
        return f"❌ Dog '{name}' not found"
    
    def check_out(self, name: str) -> str:
        """Check out dog and print report"""
        if name in self.pups:
            dog = self.pups[name]
            result = dog.check_out()
            report = dog.get_report_card()
            return f"{result}\n{report}"
        return f"❌ Dog '{name}' not found"
    
    def group_play(self, game: str = "fetch") -> str:
        """
        Group activity - all energetic dogs play together
        
        Args:
            game: Activity type
            
        Returns:
            Summary of participation
        """
        results = []
        for dog in self.pups.values():
            if dog.checked_in and dog.energy >= 3:
                results.append(dog.play(game))
        
        if not results:
            return "Nobody playing right now"
        return "\n".join(results)
    
    def feed_all(self) -> str:
        """Feed all hungry checked-in dogs"""
        results = []
        for dog in self.pups.values():
            if dog.checked_in and dog.hunger >= 4:
                # Check special dietary needs
                food = "special diet" if dog.needs else "kibble"
                results.append(dog.eat(food))
        
        if not results:
            return "Nobody hungry right now"
        return "\n".join(results)
    
    def nap_time(self) -> str:
        """Auto-nap for tired dogs (energy <= 3)"""
        results = []
        for dog in self.pups.values():
            if dog.checked_in and dog.energy <= 3:
                results.append(dog.sleep())
        
        if not results:
            return "Nobody napping right now"
        return "\n".join(results)
    
    def get_status(self) -> str:
        """Facility status report"""
        checked_in = [d for d in self.pups.values() if d.checked_in]
        report = f"\n{'='*50}\n"
        report += f"📊 {self.name} Status\n"
        report += f"💰 Revenue: ${self.revenue}\n"
        report += f"🐕 Checked in: {len(checked_in)}/{len(self.pups)}\n"
        
        for dog in checked_in:
            report += f"   {dog.stats()}\n"
        
        return report
