from BaseClasses import CollectionState


def mygame_has_key(self, state: CollectionState, player: int) -> bool:
    return state.has("Chrysler Key 7", player)
