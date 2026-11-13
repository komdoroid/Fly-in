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
        self.id: int = id
        self.place: Hub | tuple[str, str] = place
        self.path: list[str] = path
        self.next_hub_index: int = 1

    def update_place(self, next_hub: Hub) -> None:
        if (next_hub.zone_type != ZoneType.RESTRICTED
                or isinstance(self.place, tuple)):
            self.place = next_hub
            return

        # Connectionに移動
        pre_hub_name: str = self.path[self.next_hub_index - 1]
        next_hub_name: str = self.path[self.next_hub_index]
        next_connection: tuple = tuple(
                sorted([pre_hub_name, next_hub_name]))
        self.place = next_connection

    def increament_next_hub_index(self) -> None:
        self.next_hub_index += 1

    def get_next_hub_name(self) -> str:
        return self.path[self.next_hub_index]


class SimulationEngine:
    def __init__(self,
                 drone_nums: int,
                 path_finder: PathFinder) -> None:
        self.drone_nums: int = drone_nums
        self.path_finder: PathFinder = path_finder
        self.drones: list[Drone] = self.build_drones()

    def build_drones(self) -> list[Drone]:
        drones: list[Drone] = []
        for i in range(1, self.drone_nums + 1):
            path = self.path_finder.find_path()
            start_hub = self.path_finder.get_start_instance()
            drone = Drone(i, start_hub, path)
            drones.append(drone)
        return drones

    def log_processor(self, drone: Drone) -> str:
        """ 移動したDroneインスタンスから標準出力のログ要素を作成する

        Args:
            drone: Drone

        Returns:
            None

        Raises:

        """
        if isinstance(drone.place, Hub):
            return f"D{drone.id}-{drone.place.name}"
        if isinstance(drone.place, tuple):
            return f"D{drone.id}-{"-".join(drone.place)}"

    def advance_one_turn(self) -> tuple[int, str]:
        """ 前ドローンの動きを１ターン進め、標準出力に情報を表示する。

        Args:

        Returns:

        Raises:

        Examples:
            使用例を記載する（doctest形式も可能）。
        """
        delivered_num: int = 0
        log_output: str = ""
        for d in self.drones:
            if d.next_hub_index == len(d.path):
                delivered_num += 1
                continue

            next_zone: Hub = self.path_finder.hubs_by_name[
                    d.get_next_hub_name()]

            d.update_place(next_zone)
            d.increament_next_hub_index()
            log_output = log_output + " " + self.log_processor(d)

        return delivered_num, log_output

    def run_all_turns(self) -> None:
        ...
        """ すべてのターンを実行する。

        Args:

        Returns:

        Raises:

        Examples:
            使用例を記載する（doctest形式も可能）。
        """
        while True:
            delivered_num, log_output = self.advance_one_turn()
            print(log_output)
            if self.drone_nums == delivered_num:
                break
