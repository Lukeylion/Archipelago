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



@dataclass
class BioshockInfiniteOptions(PerGameCommonOptions):
    ExtraLocations:             ExtraLocations

# This is where you organize your options
# Its entirely up to you how you want to organize it
bioshock_infinite_option_groups: Dict[str, List[Any]] = {
    "General Options": [ExtraLocations],
    
}