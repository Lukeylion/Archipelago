from typing import List, Dict, Any
from dataclasses import dataclass
from worlds.AutoWorld import PerGameCommonOptions
from Options import Choice, OptionGroup, Toggle, Range

# If youve ever gone to an options page and seen how sometimes options are grouped
# This is that
def create_option_groups() -> List[OptionGroup]:
    option_group_list: List[OptionGroup] = []
    for name, options in bioshock_infinite_option_groups.items():
        option_group_list.append(OptionGroup(name=name, options=options))

    return option_group_list



class ExtraLocations(Toggle):
    """
    This will enable the extra locations option. Toggle is just true or false.
    """
    display_name = "Add Extra Locations"

class VigorsRando(Choice):
    """
    This will randomize the vigors. Choice is a multiple choice option where you can only pick one of the options.
    """
    display_name = "Vigors Randomization"
    option_only_shock_jockey = 0
    option_all_randomized = 1
    option_none_randomized = 2
    default = 1

class WeaponsRando(Choice):
    """
    This will randomize the weapons. Choice is a multiple choice option where you can only pick one of the options.
    """
    display_name = "Weapons Randomization"
    option_all_randomized = 0
    option_none_randomized = 1
    default = 0

class AmmoRando(Choice):
    """
    This will randomize the ammo drops. Choice is a multiple choice option where you can only pick one of the options.
    working_randomized is removes shotgun ammo because shotgun ammo doesnt work well.
    If using all_randomized when you get shotgun ammo only set the value to 27 because going over breaks the gun
    """
    display_name = "Ammo Randomization"
    option_working_randomized = 0
    option_all_randomized = 1
    option_none_randomized = 2
    default = 0

class WeaponsRando(Choice):
    """
    This will randomize the weapons. Choice is a multiple choice option where you can only pick one of the options.
    When changing the current weapon to the new one change the current ones value to 0 then the new one to 1 because otherwise the game crashes
    """
    display_name = "Weapons Randomization"
    option_all_randomized = 0
    option_none_randomized = 1
    default = 0


@dataclass
class BioshockInfiniteOptions(PerGameCommonOptions):
    ExtraLocations:             ExtraLocations
    WeaponsRando:               WeaponsRando
    VigorsRando:                VigorsRando

# This is where you organize your options
# Its entirely up to you how you want to organize it
bioshock_infinite_option_groups: Dict[str, List[Any]] = {
    "General Options": [ExtraLocations], 
    "Gameplay Options": [VigorsRando, WeaponsRando, AmmoRando],
}
