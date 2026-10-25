class MapParser:
    def __init__(self, map_file: str) -> None:
        self.map_file: str = map_file
        # self.nb_drones: int
        # self.start_hub
        # self.end_hub
        # self.hubs: dict
        # self.connection: dict
        self.operations = {
                'nb_drones': self.nb_drones_parse,
                'start_hub': self.start_parse,
                'end_hub': self.end_parse,
                'hub': self.hub_parse,
                'connection': self.connection_parse
                }

    def nb_drones_parse(self, nb_drones: str) -> int:
        """ nb_dronesの値を返す
        ここに必要に応じて、関数の詳細な説明を複数行で記述する。

        Args:
            nb_drone(int): Mapファイルから読み取ったnb_dronesの値

        Returns:
            int: intに変換したnb_dronesの値。

        Raises:
            ParseError: nb_dronesに数字以外が設定されているnb_dronesの値が負の値。

        Examples:
            使用例を記載する（doctest形式も可能）。
        """
        if not nb_drones.isdigit():
            raise ParseError("Values must be specified as numbers.")
        nb_drones = int(nb_drones)
        if nb_drones < 0:
            raise ParseError("Value must be positive")
        return int(nb_drones)

    def start_parse(self, start_hub: str) -> None:
        ...

    def end_parse(self, end_hub: str) -> None:
        ...

    def hub_parse(self, hub: str) -> None:
        ...

    def connection_parse(self, connection: str) -> None:
        ...

    def main_process(self) -> None:
        """関数の概要を1行で簡潔に記述する（サマリー行）。

        ここに必要に応じて、関数の詳細な説明を複数行で記述する。
        セクションの区切りには空行を挟む。

        Args:
            base (float): 累乗される基数（引数の説明）。
            exponent (int, optional): 累乗の指数。デフォルトは 2。

        Returns:
            float: 計算された累乗の結果（戻り値の説明）。

        Raises:
            ValueError: exponent に負の整数が指定された場合（例外の説明）。

        Examples:
            使用例を記載する（doctest形式も可能）。
        """
        with open(self.map_file, 'r') as f:
            for line_nb, line in enumerate(f, start=1):
                content = line.partition('#')[0].strip()
                if not content:
                    continue
                if not content.startswith(
                        tuple(self.operations.keys())
                        ):
                    raise ParseError("The key name in the map file is incorrect")
                key, sep, value = content.partition(':')
                if not sep:
                    raise ParseError("The separator in the map file is incorrect")
                operation = self.operations.get(key.strip())
                if not operation:
                    raise ParseError("The key name in the map file is incorrect")
                operation(value.strip())


class ParseError(Exception):
    ...
