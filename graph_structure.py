from map_data import (
        HubRole,
        MapData,
        GraphStructure,
        Hub,
        Connection
        )
from algorithem import PathFinder


class Drone:
    def __init__(self,
                 id,
                 place,
                 path,) -> None:
        self.id: int
        self.place: Hub | tuple[str, str]
        self.path: list[str]
        self.next_hub_index: int = 1

    def update_place(self) -> None:
        ...

    def increament_next_hub_index(self) -> None:
        self.next_hub_index += 1

class SimulationEngine:
    def __init__(self) -> None:
        self.drones: list[Drone] = self.build_drones()
        self.drone_nums: int
        self.path_finder: PathFinder

    def advance_one_turn(self) -> None:
        ...

    def build_drones(self) -> None:
        for i in range(1, self.drone_nums + 1):
            path = self.path_finder.find_path()
            drone = Drone(i, self.path_finder.start_hub, path)
            self.drones.append(drone)

    def main(self) -> None:
        # イメージができないのでとりあえず書き始める
        # すべてのDroneをインスタンス化する関数
