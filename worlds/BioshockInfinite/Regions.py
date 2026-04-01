from BaseClasses import Region
from .Types import BioshockInfiniteLocation
from .Locations import location_table, is_valid_location
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import BioshockInfiniteWorld

# This is where you will create your imaginary game world
# IE: connect rooms and areas together
# This is NOT where you'll add requirements for how to get to certain locations thats in Rules.py
# This is also long and tediouos
def create_regions(world: "BioshockInfiniteWorld"):
    # The functions that are being used here will be located at the bottom to view
    # The important part is that if its not a dead end and connects to another place then name it
    # Otherwise you can just create the connection. Not that naming it is bad

    # You can technically name your connections whatever you want as well
    # You'll use those connection names in Rules.py
    menu = create_region(world, "Menu")
    LightHouse = create_region_and_connect(world, "LightHouse", "Menu -> LightHouse", menu)
    TownCenter = create_region_and_connect(world, "TownCenter", "LightHouse -> TownCenter", LightHouse)
    ComstockCenterRooftops = create_region_and_connect(world, "ComstockCenterRooftops", "TownCenter -> ComstockCenterRooftops", TownCenter)
    MonumentIsland = create_region_and_connect(world, "MonumentIsland", "ComstockCenterRooftops -> MonumentIsland", ComstockCenterRooftops)
    BattleShipBay = create_region_and_connect(world, "BattleShipBay", "MonumentIsland -> BattleShipBay", MonumentIsland)
    SoldiersField = create_region_and_connect(world, "SoldiersField", "BattleShipBay -> SoldiersField", BattleShipBay)
    HallOfHeroes = create_region_and_connect(world, "HallOfHeroes", "SoldiersField -> HallOfHeroes", SoldiersField)

    # ---------------------------------- LightHouse ----------------------------------

    # ---------------------------------- TownCenter ------------------------------------------
    WelcomeCenter = create_region_and_connect(world, "WelcomeCenter", "TownCenter -> WelcomeCenter", TownCenter)
    GardenOfNewEden = create_region_and_connect(world, "GardenOfNewEden", "TownCenter -> GardenOfNewEden", TownCenter)
    NewEdenSquare = create_region_and_connect(world, "NewEdenSquare", "TownCenter -> NewEdenSquare", TownCenter)
    TheFairGrounds = create_region_and_connect(world, "TheFairGrounds", "TownCenter -> TheFairGrounds", TownCenter)
    RaffleSquare = create_region_and_connect(world, "RaffleSquare", "TownCenter -> RaffleSquare", TownCenter)
    ShadyLane = create_region_and_connect(world, "ShadyLane", "TownCenter -> ShadyLane", TownCenter)
    WelcomeCenter.connect(GardenOfNewEden, "WelcomeCenter -> GardenOfNewEden")

    # ---------------------------------- ComstockCenterRooftops ----------------------------------------
    LansdowneResidence = create_region_and_connect(world, "LansdowneResidence", "ComstockCenterRooftops -> LansdowneResidence", ComstockCenterRooftops)
    MontgomeryResidence = create_region_and_connect(world, "MontgomeryResidence", "ComstockCenterRooftops -> MontgomeryResidence", ComstockCenterRooftops)
    FraternalOrderOfTheRaven = create_region_and_connect(world, "FraternalOrderOfTheRaven", "ComstockCenterRooftops -> FraternalOrderOfTheRaven", ComstockCenterRooftops)
    TopFloor = create_region_and_connect(world, "TopFloor", "ComstockCenterRooftops -> TopFloor", ComstockCenterRooftops)
    LansdowneResidence.connect(MontgomeryResidence, "LansdowneResidence -> MontgomeryResidence")
    MontgomeryResidence.connect(FraternalOrderOfTheRaven, "MontgomeryResidence -> FraternalOrderOfTheRaven")
    FraternalOrderOfTheRaven.connect(TopFloor, "FraternalOrderOfTheRaven -> TopFloor")
    TopFloor.connect(FraternalOrderOfTheRaven, "TopFloor -> FraternalOrderOfTheRaven")

    # ---------------------------------- MonumentIsland ----------------------------------
    MonumentTower = create_region_and_connect(world, "MonumentTower", "MonumentIsland -> MonumentTower", MonumentIsland)
    Lobby = create_region_and_connect(world, "Lobby", "MonumentIsland -> Lobby", MonumentIsland)
    SpecimenObservation = create_region_and_connect(world, "SpecimenObservation", "MonumentIsland -> SpecimenObservation", MonumentIsland)
    Library = create_region_and_connect(world, "Library", "MonumentIsland -> Library", MonumentIsland)
    MonumentTower.connect(Lobby, "MonumentTower -> Lobby")
    Lobby.connect(SpecimenObservation, "Lobby -> SpecimenObservation")
    SpecimenObservation.connect(Library, "SpecimenObservation -> Library")

    # ---------------------------------- BattleShipBay ----------------------------------
    Arcade = create_region_and_connect(world, "Arcade", "BattleShipBay -> Arcade", BattleShipBay)

    # ---------------------------------- SoldiersField ----------------------------------
    SoldiersFeildWelcomeCenter = create_region_and_connect(world, "SoldiersFeildWelcomeCenter", "SoldiersField -> SoldiersFeildWelcomeCenter", SoldiersField)
    MainStreet = create_region_and_connect(world, "MainStreet", "SoldiersField -> MainStreet", SoldiersField)
    PatriotsPavilion = create_region_and_connect(world, "PatriotsPavilion", "SoldiersField -> PatriotsPavilion", SoldiersField)

    # ---------------------------------- HallOfHeroes ----------------------------------
    Plaza = create_region_and_connect(world, "Plaza", "HallOfHeroes -> Plaza", HallOfHeroes)
    MainHallway = create_region_and_connect(world, "MainHallway", "HallOfHeroes -> MainHallway", HallOfHeroes)
    Exibit-BoxerRebelion = create_region_and_connect(world, "Exibit-BoxerRebelion", "HallOfHeroes -> Exibit-BoxerRebelion", HallOfHeroes)
    Exibit-BattleOfWoundedKnee = create_region_and_connect(world, "Exibit-BattleOfWoundedKnee", "HallOfHeroes -> Exibit-BattleOfWoundedKnee", HallOfHeroes)
    Exibit-FistLadysMemorial = create_region_and_connect(world, "Exibit-FistLadysMemorial", "HallOfHeroes -> Exibit-FistLadysMemorial", HallOfHeroes)
    Courtyard = create_region_and_connect(world, "Courtyard", "HallOfHeroes -> Courtyard", HallOfHeroes)
    GiftShop = create_region_and_connect(world, "GiftShop", "HallOfHeroes -> GiftShop", HallOfHeroes)





def create_region(world: "BioshockInfiniteWorld", name: str) -> Region:
    reg = Region(name, world.player, world.multiworld)

    # When we create the region we go through all the locations we made and check if they are in that region
    # If they are and are valid, we attach it to the region
    for (key, data) in location_table.items():
        if data.region == name:
            if not is_valid_location(world, key):
                continue
            location = BioshockInfiniteLocation(world.player, key, data.ap_code, reg)
            reg.locations.append(location)
    
    world.multiworld.regions.append(reg)
    return reg

# This runs the create region function while also connecting to another region
# Just simplifies process since you woill be connecting a lot of regions
def create_region_and_connect(world: "BioshockInfiniteWorld",
                               name: str, entrancename: str, connected_region: Region) -> Region:
    reg: Region = create_region(world, name)
    connected_region.connect(reg, entrancename)
    return reg