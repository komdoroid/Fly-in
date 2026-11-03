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

    def find_path(
            self,
            graph,
            start) -> tuple[dict[str, float], dict[str, str]]:

        min_turns: dict[str, float] = {node: float('inf') for node in graph}
        min_turns[start] = 0

        # 経路復元用：直前のZoneを保持
        prev: dict[str, str] = {}

        # 優先度付きキュー
        queue: list[tuple[float, str]] = [(0, start)]

        while queue:
            cost, zone = heapq.heappop(queue)

            # すでにより短い経路が見つかっている場合はこのデータは無視
            if cost > min_turns[zone]:
                continue

            for v in graph[zone]:
                zone_type = self.hubs_by_name[v].zone_type
                # tupleの要素を３に変更。priorityの場合はtupleの２つ目の項目を-1
                if (zone_type == ZoneType.NORMAL
                        or zone_type == ZoneType.PRIORITY):
                    weight = 1
                if zone_type == ZoneType.RESTRICTED:
                    weight = 2
                new_cost = cost + weight
                if new_cost < min_turns[v]:
                    min_turns[v] = new_cost
                    prev[v] = zone
                    heapq.heappush(queue, (new_cost, v))
        return min_turns, prev
