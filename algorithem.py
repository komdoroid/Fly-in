import heapq
from enum import Enum
from map_data import (
        HubRole,
        MapData,
        ZoneType,
        Hub,
        Connection,
        GraphStructure,
        MapData
        )


class PathFinder:
    def __init__(self, graph_structure: GraphStructure) -> None:
        # GraphStructure()にstart, end hubを追加しておくこと
        # このアルゴリズムが意図したとおりに動くことを確認する事
        # SimulationEngineを実装して全体のドローンの動きを制御する事
        self.start_hub = graph_structure.start_hub
        self.end_hub = graph_structure.end_hub
        self.hubs_by_name: dict[str, Hub] = self._build_hubs_by_name(
                graph_structure.hub_list)
        self.adjacency_list: dict[str, list[str]] = self._build_adjacency_list(
                graph_structure)

    def _build_hubs_by_name(self, hub_list: list[Hub]) -> dict[str, Hub]:
        hubs_by_name: dict[str, Hub] = {}
        for hub in hub_list:
            hubs_by_name[hub.name] = hub

        return hubs_by_name

    def _build_adjacency_list(
            self,
            gs: GraphStructure
            ) -> dict[str, list[str]]:
        adj_list: dict[str, list[str]] = {}
        for hub in gs.hub_list:
            if hub.zone_type == ZoneType.BLOCKED:
                continue
            adj_list[hub.name] = []
        for connection in gs.connection_list:
            zone1, zone2 = connection.connected_hub
            # 現在のHub.nameが含まれている、かつ、その接続先を取得する
            if (self.hubs_by_name[zone1].zone_type == ZoneType.BLOCKED
                    or self.hubs_by_name[zone2].zone_type == ZoneType.BLOCKED):
                continue
            adj_list[zone1].append(zone2)
            adj_list[zone2].append(zone1)

        return adj_list

    def build_path_info(
            self,
            graph: dict[str, list[str]],
            start: str) -> tuple[dict[str, float], dict[str, str]]:

        min_turns: dict[str, float] = {node: float('inf') for node in graph}
        min_turns[start] = 0

        # 経路復元用：直前のZoneを保持
        prev: dict[str, str] = {}

        # 優先度付きキュー
        queue: list[tuple[float, int, str]] = [(0, 0, start)]

        while queue:
            cost, priority_index, zone = heapq.heappop(queue)

            # すでにより短い経路が見つかっている場合はこのデータは無視
            if cost > min_turns[zone]:
                continue

            for v in graph[zone]:
                zone_type = self.hubs_by_name[v].zone_type
                if zone_type == ZoneType.NORMAL:
                    weight = 1
                if zone_type == ZoneType.RESTRICTED:
                    weight = 2
                if zone_type == ZoneType.PRIORITY:
                    # tupleの要素は前から評価して、ソートされる
                    weight = 1
                    priority_index -= 1
                new_cost = cost + weight

                # 同じコストで到達可能な場合は先に評価したルートが優先される
                # つまり'priority_index'が小さい方が優先
                if new_cost < min_turns[v]:
                    min_turns[v] = new_cost
                    prev[v] = zone
                    heapq.heappush(queue, (new_cost, priority_index, v))
        return min_turns, prev

    def find_path(self) -> None | list[str]:
        start_to_end: list[str] = [self.end_hub]
        # start_hubとend_hubのnameはGraphStructureに保持しておくべき
        # それに伴ってHubRole()は意味をなさなくなるので削除
        min_turns, prev = self.build_path_info(
                self.adjacency_list,
                self.start_hub
                )
        while start_to_end[-1] == self.start_hub:
            if start_to_end[-1] not in prev:
                return None
            start_to_end.append(prev[start_to_end[-1]])
        start_to_end.reverse()
        return start_to_end
