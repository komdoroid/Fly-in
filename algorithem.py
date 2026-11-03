import heapq


class SimulationEngine():
    def get_shortest_path(
            self,
            graph,
            start) -> tuple[dict[str, float], dict[str, str]]:
        # 必要変数
        # 隣接リスト：dict[name: list[next_zone]]
        # 到達コスト保持：dict[name: tuple[cost, pre_zone]]
        # RETURN：STARTからGOALまでの移動ZONE名リストlist[str]
        # 開始条件：スタート地点（共通）
        # 継続条件：隣接リストから到達可能なzoneを取得
        # コストを計算
        # 最低コストで到達コストを更新
        # 終了条件：ゴール地点（共通）

        min_turns: dict[str, float] = {node: float('inf') for node in graph}
        min_turns[start] = 0

        # 経路復元用：直前のZoneを保持
        prev: dict[str, str] = {}

        # 優先度付きキュー
        queue: list[tuple[float, str]] = [(0, start)]

        while queue:
            cost, zone = heapq.heappop(queue)
            if cost > min_turns[zone]:
                continue

            for v, weight in graph[zone]:
                new_cost = cost + weight
                if new_cost < min_turns[v]:
                    min_turns[v] = new_cost
                    prev[v] = zone
                    heapq.heappush(queue, (new_cost, v))

        return min_turns, prev
