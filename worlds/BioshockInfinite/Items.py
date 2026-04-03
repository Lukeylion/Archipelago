# So the goal here is to have a catalog of all the items in your game
# To correctly generate a games items they need to be bundled in a list
# A list in programming terms is anything in square brackets [] to put it simply

# When a list is described its described as a list of x where x is the type of variable within it
# IE: ["apple", "pear", "grape"] is a list of strings (anything inside "" OR '' are considered strings)

# Logging = output. How you'll figure out whats going wrong
import logging

# Built in AP imports
from BaseClasses import Item, ItemClassification

# These come from the other files in this example. If you want to see the source ctrl + click the name
# You can also do that ctrl + click for any functions to see what they do
from .Types import ItemData, BioshockInfiniteItem
from .Locations import get_total_locations
from typing import List, Dict, TYPE_CHECKING

# This is just making sure nothing gets confused dw about what its doing exactly
if TYPE_CHECKING:
    from . import BioshockInfiniteWorld
# If you're curious about the -> List[Item] that is a syntax to make sure you return the correct variable type
# In this instance we're saying we only want to return a list of items
# You'll see a bunch of other examples of this in other functions
# It's main purpose is to protect yourself from yourself
def create_itempool(world: "BioshockInfiniteWorld") -> List[Item]:
    # This is the empty list of items. You'll add all the items in the game to this list
    itempool: List[Item] = []

    
    # It's up to you and how you want things organized but I like to deal with victory here
    # This creates your win item and then places it at the "location" where you win
    victory = create_item(world, "Victory")
    world.multiworld.get_location("Beat Final Boss", world.player).place_locked_item(victory)

    # Then junk items are made
    # Check out the create_junk_items function for more details
    itempool += create_junk_items(world, get_total_locations(world) - len(itempool) - 1)

    return itempool

# This is a generic function to create a singular item
def create_item(world: "BioshockInfiniteWorld", name: str) -> Item:
    data = item_table[name]
    return BioshockInfiniteItem(name, data.classification, data.ap_code, world.player)

# Another generic function. For creating a bunch of items at once!
def create_multiple_items(world: "BioshockInfiniteWorld", name: str, count: int,
                          item_type: ItemClassification = ItemClassification.progression) -> List[Item]:
    data = item_table[name]
    itemlist: List[Item] = []

    for i in range(count):
        itemlist += [BioshockInfiniteItem(name, item_type, data.ap_code, world.player)]

    return itemlist

# Finally, where junk items are created
def create_junk_items(world: "BioshockInfiniteWorld", count: int) -> List[Item]:
    junk_pool: List[Item] = []
    junk_list: Dict[str, int] = {}

    # This grabs all the junk items and trap items
    for name in item_table.keys():
        # Here we are getting all the junk item names and weights
        ic = item_table[name].classification
        if ic == ItemClassification.filler:
            junk_list[name] = junk_weights.get(name)

    # Where all the magic happens of adding the junk and traps randomly
    # AP does all the weight management so we just need to worry about how many are created
    for i in range(count):
        junk_pool.append(world.create_item(
            world.random.choices(list(junk_list.keys()), weights=list(junk_list.values()), k=1)[0]))

    return junk_pool

# Time for the fun part of listing all of the items
# Watch out for overlap with your item codes
# These are just random numbers dont trust them PLEASE
# I've seen some games that dynamically add item codes such as DOOM as well
bioshock_infinite_items = {
    # Progression items
    "Shock Jockey": ItemData(100000000000, ItemClassification.progression),

    # Useful items
    "Pistol": ItemData(100000000001, ItemClassification.useful),
    "RPG": ItemData(100000000002, ItemClassification.useful),
    "Sniper Rifle": ItemData(100000000003, ItemClassification.useful),
    "Machine Gun": ItemData(100000000004, ItemClassification.useful),
    "Shotgun": ItemData(100000000005, ItemClassification.useful),
    "Carbine": ItemData(100000000006, ItemClassification.useful),
    "Hand Cannon": ItemData(100000000007, ItemClassification.useful),
    "Crank Gun": ItemData(100000000008, ItemClassification.useful),
    "Volley Gun": ItemData(100000000009, ItemClassification.useful),
    "Machine Gun": ItemData(100000000010, ItemClassification.useful),
    "Bucking Bronco": ItemData(100000000011, ItemClassification.useful),
    "Charge": ItemData(100000000012, ItemClassification.useful),
    "Undertow": ItemData(100000000013, ItemClassification.useful),
    "Return to Sender": ItemData(100000000014, ItemClassification.useful),
    "Possession": ItemData(100000000015, ItemClassification.useful),
    "Devil's Kiss": ItemData(100000000016, ItemClassification.useful),
    "Murder of Crows": ItemData(100000000017, ItemClassification.useful),

    # Victory is added here since in this organization it needs to be in the default item pool
    "Victory": ItemData(100000000018, ItemClassification.progression)
}

# I like to split up the items so that its easier to look at and since sometimes you only need to look at one specific type of list
# An example of that is in create_itempool where I simulated having a starting chapter

# In the way that I made items, I added a way to specify how many of an item should exist
# That's why junk has a 0 since how many are created is in the create_junk_items
# There is a better way of doing this but this is my jank
junk_items = {
    # Junk
    "Pistol Ammo": ItemData(100000000019, ItemClassification.filler),
    "RPG Ammo": ItemData(100000000020, ItemClassification.filler),
    "Sniper Rifle Ammo": ItemData(100000000021, ItemClassification.filler),
    "Machine Gun Ammo": ItemData(100000000022, ItemClassification.filler),
    "Shotgun Ammo": ItemData(100000000023, ItemClassification.filler),
    "Carbine Ammo": ItemData(100000000024, ItemClassification.filler),
    "Hand Cannon Ammo": ItemData(100000000025, ItemClassification.filler),
    "Crank Gun Ammo": ItemData(100000000026, ItemClassification.filler),
    "Volley Gun Ammo": ItemData(100000000027, ItemClassification.filler),
    


}

# Junk weights is just how often an item will be chosen when junk is being made
# Bigger item = more likely to show up
junk_weights = {
    "Pistol Ammo": 20,
    "RPG Ammo": 10,
    "Sniper Rifle Ammo": 10,
    "Machine Gun Ammo": 10,
    "Shotgun Ammo": 10,
    "Carbine Ammo": 10,
    "Hand Cannon Ammo": 10,
    "Crank Gun Ammo": 10,
    "Volley Gun Ammo": 10

}

# This makes a really convenient list of all the other dictionaries
# (fun fact: {} is a dictionary)
item_table = {
    **bioshock_infinite_items,
    **junk_items
}