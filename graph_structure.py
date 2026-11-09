from map_data import (
        HubRole,
        ZoneType,
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

    def update_place(self, zone_type: ZoneType) -> None:
        # ZoneTypeがrestrictだった場合
        # かつ、現在のplaceの方がstrなら次の移動先はConnection
        # または、現在のplaceの型がtupleなら次の移動先はHub
        ...

    def increament_next_hub_index(self) -> None:
        self.next_hub_index += 1

class SimulationEngine:
    def __init__(self) -> None:
        self.drones: list[Drone] = self.build_drones()
        self.drone_nums: int
        self.path_finder: PathFinder

    def build_drones(self) -> list[Drone]:
        drones: list[Drone] = []
        for i in range(1, self.drone_nums + 1):
            path = self.path_finder.find_path()
            drone = Drone(i, self.path_finder.start_hub, path)
            self.drones.append(drone)
        return drones

    def advance_one_turn(self) -> None:
        """ 前ドローンの動きを１ターン進め、標準出力に情報を表示する。

        Args:

        Returns:

        Raises:

        Examples:
            使用例を記載する（doctest形式も可能）。
        """

    def run_all_turns(self) -> None:
        ...
        """ すべてのターンを実行する。

        Args:

        Returns:

        Raises:

        Examples:
            使用例を記載する（doctest形式も可能）。
        """
