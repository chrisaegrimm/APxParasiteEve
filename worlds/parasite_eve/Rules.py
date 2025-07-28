from typing import Dict, Callable, TYPE_CHECKING
from BaseClasses import CollectionState

if TYPE_CHECKING:
    from . import PEWorld
else:
    PEWorld = object


class PERules:
    player: int
    world: PEWorld
    location_rules: Dict[str, Callable[[CollectionState], bool]]
    region_rules: Dict[str, Callable[[CollectionState], bool]]
    end_goal: int

    def __init__(self, world: PEWorld) -> None:
        self.player = world.player
        self.world = world

        self.region_rules = {

        "Carnegie Hall: NoReqs":                         self.has_ch,
        #Carnegie Hall: Combat":
        "Carnegie Hall: Combat+TK":                      self.has_tk,
        "Carnegie Hall: Combat+RK":                      self.has_rk,
        #Carnegie Hall: Combat+RK+Boss":

        "N.Y.P.D. #17: NoReqs":                          self.has_pd,
        "N.Y.P.D. #17: LK":                              self.has_lk,
        "N.Y.P.D. #17: SK":                              self.has_sk,
        "N.Y.P.D. #17: SJ":                              self.has_sj,
        #N.Y.P.D. #17: Combat+SJ":
        #N.Y.P.D. #17: Combat+SJ+Boss":
        #N.Y.P.D. #17: Combat+SJ+Boss+UC+JunkReq":
        #N.Y.P.D. #17: Combat+SJ+Boss+UC+12RTC":
        #N.Y.P.D. #17: Combat+SJ+Boss+UC+14RTC":

        "Central Park: NoReqs":                          self.has_cp,
        #Central Park: Combat":
        "Central Park: Combat+ZK":                       self.has_zk,
        #Central Park: Combat+ZK+Boss":

        "Soho: NoReqs":                                  self.has_sh,
        "Soho: WM":                                      self.has_wm,

        "Hospital: NoReqs":                              self.has_hs,
        #Hospital: Combat":
        "Hospital: Combat+GC":                           self.has_gc,
        "Hospital: Combat+AK":                           self.has_ak,
        "Hospital: Combat+BC":                           self.has_bc,
        "Hospital: Combat+BC+Fuses":                     self.has_3f,
        "Hospital: Combat+BC+Fuses+EK+Boss":             self.has_ek,

        "Chinatown: NoReqs|Combat+GK":                   self.has_ct,
        #Chinatown: Combat|Combat+GK":
        #Chinatown: Combat+Boss|Combat+GK+Boss":
        #Chinatown: Combat|GK"

        "Subway: Combat+PK|GK":                          self.has_sg,
        #Subway: Combat+PK|Combat+GK":
        #Subway: Combat+PK+Boss|Combat+GK+Boss":

        "Warehouse: NoReqs":                             self.has_wh,
        #Warehouse: Combat":
        "Warehouse: Combat+WK":                          self.has_wk,
        #Warehouse: Combat+WK+Boss":

        "Museum: NoReqs":                                self.has_mu,
        #Museum: Combat":
        "Museum: Combat+KK":                             self.has_kk,
        #Museum: Combat+KK+Boss":
        "Cruiser":                                       self.has_3c,

        "Chrysler BLDG.: Key 1":                         self.has_c1,
        "Chrysler BLDG.: Key 2":                         self.has_c2,
        "Chrysler BLDG.: Key 3":                         self.has_c3,
        "Chrysler BLDG.: Key 4":                         self.has_c4,
        "Chrysler BLDG.: Key 5":                         self.has_c5,
        "Chrysler BLDG.: Key 6":                         self.has_c6,
        "Chrysler BLDG.: Key 7":                         self.has_c7,
        "Chrysler BLDG.: Spire":                         self.has_3c
        }




    def has_ch(self, state: CollectionState) -> bool:
        return state.has("Carnegie Hall", self.player)

    def has_tk(self, state: CollectionState) -> bool:
        return state.has("Theater Key", self.player)

    def has_rk(self, state: CollectionState) -> bool:
        return state.has("Rehearse Key", self.player)


    def has_pd(self, state: CollectionState) -> bool:
        return state.has("N.Y.P.D. #17", self.player)

    def has_lk(self, state: CollectionState) -> bool:
        return state.has("Locker Key", self.player)

    def has_sk(self, state: CollectionState) -> bool:
        return state.has("Storage Key", self.player)

    def has_sj(self, state: CollectionState) -> bool:
        return state.has("Super Junk", self.player)


    def has_cp(self, state: CollectionState) -> bool:
        return state.has("Central Park", self.player)

    def has_zk(self, state: CollectionState) -> bool:
        return state.has("Zoo Key", self.player)


    def has_sh(self, state: CollectionState) -> bool:
        return state.has("Soho", self.player)

    def has_wm(self, state: CollectionState) -> bool:
        return state.has("Weapon Memo", self.player)


    def has_hs(self, state: CollectionState) -> bool:
        return state.has("Hospital", self.player)

    def has_gc(self, state: CollectionState) -> bool:
        return state.has("Green Cardkey", self.player)

    def has_ak(self, state: CollectionState) -> bool:
        return state.has("Autopsy Key", self.player)

    def has_bc(self, state: CollectionState) -> bool:
        return state.has("Blue Cardkey", self.player)

    def has_3f(self, state: CollectionState) -> bool:
        return state.has_all(("Fuse 1", "Fuse 2", "Fuse 3"), self.player)

    def has_ek(self, state: CollectionState) -> bool:
        return state.has("Elevator Key", self.player)


    def has_ct(self, state: CollectionState) -> bool:
        return state.has("Chinatown", self.player)


    def has_sg(self, state: CollectionState) -> bool:
        return state.has_all(("Subway", "Gate Key"), self.player) or \
            state.has_all(("Subway", "Chinatown", "Pump Key"), self.player)


    def has_wh(self, state: CollectionState) -> bool:
        return state.has("Warehouse", self.player)

    def has_wk(self, state: CollectionState) -> bool:
        return state.has("Warehouse Key", self.player)


    def has_mu(self, state: CollectionState) -> bool:
        return state.has("Museum", self.player)

    def has_kk(self, state: CollectionState) -> bool:
        return state.has("Klamp Key", self.player)

    def has_c1(self, state: CollectionState) -> bool:
        return state.has("Chrysler Key 1", self.player)

    def has_c2(self, state: CollectionState) -> bool:
        return state.has("Chrysler Key 2", self.player)

    def has_c3(self, state: CollectionState) -> bool:
        return state.has("Chrysler Key 3", self.player)

    def has_c4(self, state: CollectionState) -> bool:
        return state.has("Chrysler Key 4", self.player)

    def has_c5(self, state: CollectionState) -> bool:
        return state.has("Chrysler Key 5", self.player)

    def has_c6(self, state: CollectionState) -> bool:
        return state.has("Chrysler Key 6", self.player)

    def has_c7(self, state: CollectionState) -> bool:
        return state.has("Chrysler Key 7", self.player)


    def has_3c(self, state: CollectionState) -> bool:
        return state.has_all(("Narita", "Mayoke", "Hamaya"), self.player)

    #def pe_end(self, state: CollectionState) -> bool:
        #return state.has("Resolution", self.player)




    def set_pe_rules(self) -> None:
        multiworld = self.world.multiworld
        self.world.multiworld.completion_condition[self.player] = lambda state: state.can_reach("Chrysler BLDG.: Spire", "Region", self.player)