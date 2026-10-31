class SimulationEngine():
    def get_shortest_path(self) -> None:
        # 必要変数
        # 隣接リスト：dict[name: list[next_zone]]
        # 到達コスト保持：dict[name: tuple[cost, pre_zone]]
        # RETURN：STARTからGOALまでの移動ZONE名リストlist[str]
        # 開始条件：スタート地点（共通）
        # 継続条件：隣接リストから到達可能なzoneを取得
        # コストを計算
        # 最低コストで到達コストを更新
        # 終了条件：ゴール地点（共通）
