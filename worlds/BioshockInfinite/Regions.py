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
    FinktonDocks = create_region_and_connect(world, "FinktonDocks", "HallOfHeroes -> FinktonDocks", HallOfHeroes)
    FinktonProper = create_region_and_connect(world, "FinktonProper", "FinktonDocks -> FinktonProper", FinktonDocks)
    ShantyTown = create_region_and_connect(world, "ShantyTown", "FinktonProper -> ShantyTown", FinktonProper)
    FinktonFactory = create_region_and_connect(world, "FinktonFactory", "ShantyTown -> FinktonFactory", ShantyTown)
    Emporia = create_region_and_connect(world, "Emporia", "FinktonFactory -> Emporia", FinktonFactory)
    DowntownEmporia = create_region_and_connect(world, "DowntownEmporia", "Emporia -> DowntownEmporia", Emporia)
    ComstockHouse = create_region_and_connect(world, "ComstockHouse", "DowntownEmporia -> ComstockHouse", DowntownEmporia)
    HandOfTheProphet = create_region_and_connect(world, "HandOfTheProphet", "ComstockHouse -> HandOfTheProphet", ComstockHouse)

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
    TheFellowTraveler = create_region_and_connect(world, "TheFellowTraveler", "SoldiersField -> TheFellowTraveler", SoldiersField)
    PatriotsPride = create_region_and_connect(world, "PatriotsPride", "SoldiersField -> PatriotsPride", SoldiersField)
    FirstLadysAreodrome = create_region_and_connect(world, "FirstLadysAerodrome", "SoldiersField -> FirstLadysAerodrome", SoldiersField)
    SoldiersFeildWelcomeCenter.connect(MainStreet, "SoldiersFeildWelcomeCenter -> MainStreet")
    MainStreet.connect(PatriotsPavilion, "MainStreet -> PatriotsPavilion")
    MainStreet.connect(TheFellowTraveler, "MainStreet -> TheFellowTraveler")
    PatriotsPavilion.connect(PatriotsPride, "PatriotsPavilion -> PatriotsPride")
    MainStreet.connect(FirstLadysAreodrome, "MainStreet -> FirstLadysAreodrome")


    # ---------------------------------- HallOfHeroes ----------------------------------
    Plaza = create_region_and_connect(world, "Plaza", "HallOfHeroes -> Plaza", HallOfHeroes)
    MainHallway = create_region_and_connect(world, "MainHallway", "HallOfHeroes -> MainHallway", HallOfHeroes)
    ExibitBoxerRebelion = create_region_and_connect(world, "ExibitBoxerRebelion", "HallOfHeroes -> ExibitBoxerRebelion", HallOfHeroes)
    ExibitBattleOfWoundedKnee = create_region_and_connect(world, "ExibitBattleOfWoundedKnee", "HallOfHeroes -> ExibitBattleOfWoundedKnee", HallOfHeroes)
    ExibitFistLadysMemorial = create_region_and_connect(world, "ExibitFistLadysMemorial", "HallOfHeroes -> ExibitFistLadysMemorial", HallOfHeroes)
    Courtyard = create_region_and_connect(world, "Courtyard", "HallOfHeroes -> Courtyard", HallOfHeroes)
    GiftShop = create_region_and_connect(world, "GiftShop", "HallOfHeroes -> GiftShop", HallOfHeroes)
    Plaza.connect(MainHallway, "Plaza -> MainHallway")
    MainHallway.connect(ExibitBoxerRebelion, "MainHallway -> ExibitBoxerRebelion")
    MainHallway.connect(ExibitBattleOfWoundedKnee, "MainHallway -> ExibitBattleOfWoundedKnee")
    MainHallway.connect(ExibitFistLadysMemorial, "MainHallway -> ExibitFistLadysMemorial")
    MainHallway.connect(Courtyard, "MainHallway -> Courtyard")
    MainHallway.connect(GiftShop, "MainHallway -> GiftShop")

    # ---------------------------------- FinktonDocks ----------------------------------
    BeggarsWharf = create_region_and_connect(world, "BeggarsWharf", "FinktonDocks -> BeggarsWharf", FinktonDocks)
    FortFranklin = create_region_and_connect(world, "FortFranklin", "FinktonDocks -> FortFranklin", FinktonDocks)
    BeggarsWharf.connect(FortFranklin, "BeggarsWharf -> FortFranklin")

    # ---------------------------------- FinktonProper ----------------------------------
    WorkerInductionCenter = create_region_and_connect(world, "WorkerInductionCenter", "FinktonProper -> WorkerInductionCenter", FinktonProper)
    PlazaOfZeal = create_region_and_connect(world, "PlazaOfZeal", "FinktonProper -> PlazaOfZeal", FinktonProper)
    WorkerInductionCenter.connect(PlazaOfZeal, "WorkerInductionCenter -> PlazaOfZeal")

    # ---------------------------------- ShantyTown ----------------------------------
    PathToShantyTown = create_region_and_connect(world, "PathToShantyTown", "ShantyTown -> PathToShantyTown", ShantyTown)
    GraveyardShiftBar = create_region_and_connect(world, "GraveyardShiftBar", "ShantyTown -> GraveyardShiftBar", ShantyTown)
    BullHouseImpound = create_region_and_connect(world, "BullHouseImpound", "ShantyTown -> BullHouseImpound", ShantyTown)
    BullYard = create_region_and_connect(world, "BullYard", "ShantyTown -> BullYard", ShantyTown)
    ThirdColumbia = create_region_and_connect(world, "ThirdColumbia", "ShantyTown -> ThirdColumbia", ShantyTown)
    PathToShantyTown.connect(GraveyardShiftBar, "PathToShantyTown -> GraveyardShiftBar")
    PathToShantyTown.connect(BullHouseImpound, "PathToShantyTown -> BullHouseImpound")
    BullHouseImpound.connect(BullYard, "BullHouseImpound -> BullYard")
    ThirdColumbia.connect(BullYard, "ThirdColumbia -> BullYard")
    ThirdColumbia.connect(GraveyardShiftBar, "ThirdColumbia -> GraveyardShiftBar")
    ThirdColumbia.connect(BullHouseImpound, "ThirdColumbia -> BullHouseImpound")
    ThirdColumbia.connect(PathToShantyTown, "ThirdColumbia -> PathToShantyTown")

    # ---------------------------------- FinktonFactory ----------------------------------
    FactoryCourtyard = create_region_and_connect(world, "FactoryCourtyard", "FinktonFactory -> FactoryCourtyard", FinktonFactory)
    InsideFactory = create_region_and_connect(world, "InsideFactory", "FinktonFactory -> InsideFactory", FinktonFactory)
    OfficeOfFink = create_region_and_connect(world, "OfficeOfFinkton", "FinktonFactory -> OfficeOfFinkton", FinktonFactory)
    FactoryDocks = create_region_and_connect(world, "FactoryDocks", "FinktonFactory -> FactoryDocks", FinktonFactory)
    FactoryCourtyard.connect(InsideFactory, "FactoryCourtyard -> InsideFactory")
    InsideFactory.connect(OfficeOfFink, "InsideFactory -> OfficeOfFinkton")
    InsideFactory.connect(FactoryDocks, "InsideFactory -> FactoryDocks")

    # ---------------------------------- Emporia ----------------------------------
    PortProsperity = create_region_and_connect(world, "PortProsperity", "Emporia -> PortProsperity", Emporia)
    GrandCentralDepot = create_region_and_connect(world, "GrandCentralDepot", "Emporia -> GrandCentralDepot", Emporia)
    TheSaltyOyster = create_region_and_connect(world, "TheSaltyOyster", "Emporia -> TheSaltyOyster", Emporia)
    FoundersBookstore = create_region_and_connect(world, "FoundersBookstore", "Emporia -> FoundersBookstore", Emporia)
    PortProsperity.connect(GrandCentralDepot, "PortProsperity -> GrandCentralDepot")
    GrandCentralDepot.connect(TheSaltyOyster, "GrandCentralDepot -> TheSaltyOyster")
    GrandCentralDepot.connect(FoundersBookstore, "GrandCentralDepot -> FoundersBookstore")

    # ---------------------------------- DowntownEmporia ----------------------------------
    FinancialDistrict = create_region_and_connect(world, "FinancialDistrict", "DowntownEmporia -> FinancialDistrict", DowntownEmporia)
    MarketDistrict = create_region_and_connect(world, "MarketDistrict", "DowntownEmporia -> MarketDistrict", DowntownEmporia)
    HarmonyLane = create_region_and_connect(world, "HarmonyLane", "DowntownEmporia -> HarmonyLane", DowntownEmporia)
    VictorySquare = create_region_and_connect(world, "VictorySquare", "DowntownEmporia -> VictorySquare", DowntownEmporia)
    MemorialGarden = create_region_and_connect(world, "MemorialGarden", "DowntownEmporia -> MemorialGarden", DowntownEmporia)
    GrandCentralDepot.connect(FinancialDistrict, "GrandCentralDepot -> FinancialDistrict")
    FinancialDistrict.connect(HarmonyLane, "FinancialDistrict -> HarmonyLane")
    HarmonyLane.connect(MarketDistrict, "HarmonyLane -> MarketDistrict")
    HarmonyLane.connect(VictorySquare, "HarmonyLane -> VictorySquare")
    HarmonyLane.connect(MemorialGarden, "HarmonyLane -> MemorialGarden")

    # ---------------------------------- ComstockHouse ----------------------------------
    OutsideComstockHouse = create_region_and_connect(world, "OutsideComstockHouse", "ComstockHouse -> OutsideComstockHouse", ComstockHouse)
    FirstFloor = create_region_and_connect(world, "FirstFloor", "ComstockHouse -> FirstFloor", ComstockHouse)
    SecondFloor = create_region_and_connect(world, "SecondFloor", "ComstockHouse -> SecondFloor", ComstockHouse)
    ThirdFloor = create_region_and_connect(world, "ComstockHouse -> ThirdFloor", ComstockHouse)
    SecurityCenter = create_region_and_connect(world, "SecurityCenter", "ComstockHouse -> SecurityCenter", ComstockHouse)
    WardensOffice = create_region_and_connect(world, "WardensOffice", "ComstockHouse -> WardensOffice", ComstockHouse)
    OperatingTheater = create_region_and_connect(world, "OperatingTheater", "ComstockHouse -> OperatingTheater", ComstockHouse)
    ComstockHouseRoof = create_region_and_connect(world, "ComstockHouseRoof", "ComstockHouse -> ComstockHouseRoof", ComstockHouse)
    OutsideComstockHouse.connect(FirstFloor, "OutsideComstockHouse -> FirstFloor")
    FirstFloor.connect(SecondFloor, "FirstFloor -> SecondFloor")
    SecondFloor.connect(ThirdFloor, "SecondFloor -> ThirdFloor")
    ThirdFloor.connect(SecurityCenter, "ThirdFloor -> SecurityCenter")
    ThirdFloor.connect(WardensOffice, "ThirdFloor -> WardensOffice")
    ThirdFloor.connect(OperatingTheater, "ThirdFloor -> OperatingTheater")
    ThirdFloor.connect(ComstockHouseRoof, "ThirdFloor -> ComstockHouseRoof")









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