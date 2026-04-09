#!/usr/bin/env python3
"""
Command-line interface for Petio Dog Daycare
Run this for an interactive demo: python src/cli.py
"""

from dog import PetioDog
from daycare import Daycare


def main():
    print("🏢 PETIO DOG DAYCARE SYSTEM")
    print("=" * 50)
    
    # Initialize
    dc = Daycare("Petio Paws")
    
    # Create dogs
    dogs = [
        PetioDog("Biscuit", "Golden Retriever", "Sarah", ["Allergic to chicken"]),
        PetioDog("Max", "Beagle", "Mike"),
        PetioDog("Luna", "Husky", "Emma", ["High energy - needs extra play"]),
        PetioDog("Rocky", "Bulldog", "Tom")
    ]
    
    # Register
    for dog in dogs:
        print(dc.register(dog))
    
    # Check in
    print("\n📥 Morning Check-in:")
    for dog in dogs:
        print(dc.check_in(dog.name))
    
    # Schedule
    print("\n🎾 9:00 AM - Group Play (Fetch)")
    print(dc.group_play("fetch"))
    
    print("\n🍖 12:00 PM - Lunch Time")
    print(dc.feed_all())
    
    print("\n🏃 2:00 PM - Afternoon Activities")
    # Individual attention
    print(dc.pups["Biscuit"].play("agility course"))
    print(dc.pups["Luna"].play("frisbee"))
    print(dc.pups["Luna"].play("sprint"))  # Double play!
    print(dc.pups["Rocky"].play("tug-of-war"))
    
    print("\n💤 3:30 PM - Nap Time (Auto-detect tired dogs)")
    print(dc.nap_time())
    
    print("\n🍪 4:00 PM - Snack Time")
    print(dc.pups["Biscuit"].eat("peanut butter treats"))
    
    # Status check
    print(dc.get_status())
    
    # Check out
    print("\n📤 5:00 PM - Pick Up Time:")
    for dog in dogs:
        print(dc.check_out(dog.name))
        print("-" * 40)
    
    print(f"\n💵 Total Revenue Today: ${dc.revenue}")


if __name__ == "__main__":
    main()
