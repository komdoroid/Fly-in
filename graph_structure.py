from map_data import (
        HubRole,
        MapData,
        GraphStructure,
        Hub,
        Connection
        )


class Drone:
    def __init__(self) -> None:
        self.id: int
        self.place: Hub | tuple[str, str]
        self.path: list[str]
        self.next_hub_index: int


class SimulationEngine:
    def __init__(self) -> None:
        self.drones: list[Drone]
        self.drone_nums
