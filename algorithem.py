import heapq
from map_data import (GraphStructure)


class PathFinder:
    def __init__(self, graph_structure: GraphStructure) -> None:
        self.adjacency_list = self._build_adjacency_list(graph_structure)

    def _build_adjacency_list(
            self,
            gs: GraphStructure
            ) -> dict[str, tuple[str, float]]:
        adj_list: dict[str, tuple[str, float]] = {}
        for hub in gs.hub_list:
            next_hub = []
            target_hub = hub.name
            for connection in gs.connection_list:
                if target_hub in connection.connected_hub:
                    if hub.name == connection.connected_hub[0]:
                        next_hub.append(connection.connected_hub[1])
                    else:
                        next_hub.append(connection.connected_hub[0])
            adj_list[target_hub] = next_hub

        return adj_list


    def get_shortest_path(
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

            for v, weight in graph[zone]:
                new_cost = cost + weight
                if new_cost < min_turns[v]:
                    min_turns[v] = new_cost
                    prev[v] = zone
                    heapq.heappush(queue, (new_cost, v))

        return min_turns, prev
