"""
Usage file
"""

from src.daycare import Daycare
from src.dog import PetioDog

# Initialize daycare
dc = Daycare("Petio Paws")

# Register dogs
biscuit = PetioDog("Biscuit", "Golden Retriever", "Sarah", ["Allergic to chicken"])
dc.register(biscuit)

# Run daily operations
dc.check_in("Biscuit")
dc.group_play("fetch")
dc.feed_all()
print(dc.check_out("Biscuit"))
