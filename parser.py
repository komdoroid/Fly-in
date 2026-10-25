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

        Args:
            nb_drone(str): Mapファイルから読み取ったnb_dronesの値

        Returns:
            int: intに変換したnb_dronesの値。

        Raises:
            ParseError: nb_dronesに数字以外が設定されているnb_dronesの値が負の値。

        Examples:
            使用例を記載する（doctest形式も可能）。
        """
        if not nb_drones.isdigit():
            raise ParseError("Values must be specified as numbers.")
        return int(nb_drones)

    def _additional_info_parse(self, info: str) -> tuple[str, str, str]:
        ''' Hubの追加条件をパースする

        Args:
            info(str): Mapファイルから読み取ったHubの追加情報全文

        Returns:
            dict: 追加情報(xxxx=yyyy)をkey/valueに分割して格納した辞書。

        Raises:
            ParseError: nb_dronesに数字以外が設定されているnb_dronesの値が負の値。

        Examples:
            使用例を記載する（doctest形式も可能）。
        '''

    def _hub_parse(self, value: str, role: HubRole) -> None:
        """ starting zoneの情報をパースする

        Args:
            start_hub(str): Mapファイルから読み取ったstart_hubの値

        Returns:
            int: intに変換したnb_dronesの値。

        Raises:
            ParseError: nb_dronesに数字以外が設定されているnb_dronesの値が負の値。

        Examples:
            使用例を記載する（doctest形式も可能）。
        """
        # ' 'でsplit()しようとすると、追加情報[xxx xxx]もsplitされるので
        # 先に[xxx xxx]情報があるかどうかを調べる
        mandatory_info, _, additional_info = value.partition('[')
        # [xxx xxx]が含まれているの場合はこれをパース
        meta = self._additional_info_parse(additional_info.strip(']')

        kwargs: dict[str: Any] = {}
        if 'zone' in meta:
            kwargs['zone_type'] = meta['zone']
        if 'color' in meta:
            kwargs['color'] = meta['color']
        if 'max_drones' in meta:
            kwargs['max_drones'] = meta['max_drones']
        # 前後の空白を除いたうえで、' 'で分割
        splited_shub = mandatory_info.strip().split(' ')
        if len(splited_shub) != 3:
            raise ParseError('Please enter it in the following format: (start_hub: name 0 0)')
        try:
            x_coord = int(splited_shub[1])
            y_coord = int(splited_shub[2])
        except Error as e:
            print(e)
        return Hub(name=splited_shub[0],
                   cordinates=(x_coord, y_coord),
                   hub_role=role,
                   **kwargs
                   )


    def start_parse(self, start_hub: str) -> None:
        """ start zoneの情報をパースする

        Args:
            start_hub(int): Mapファイルから読み取ったstart_hubの値

        Returns:
            Hub: パースした情報から作成した、Hubインスタンス

        Raises:
            ParseError: 
            ValidationError:

        Examples:
            使用例を記載する（doctest形式も可能）。
        """
        return _parse_zone(start_hub, HubRole.start) 


    def end_parse(self, end_hub: str) -> None:
        """ start zoneの情報をパースする

        Args:
            start_hub(int): Mapファイルから読み取ったstart_hubの値

        Returns:
            Hub: パースした情報から作成した、Hubインスタンス

        Raises:
            ParseError: 
            ValidationError:

        Examples:
            使用例を記載する（doctest形式も可能）。
        """
       return _parse_zone(end_hub, HubRole.END) 

    def hub_parse(self, hub: str) -> None:
        """ zoneの情報をパースする

        Args:
            hub(int): Mapファイルから読み取ったhubの値

        Returns:
            Hub: パースした情報から作成した、Hubインスタンス

        Raises:
            ParseError: 
            ValidationError:

        Examples:
            使用例を記載する（doctest形式も可能）。
        """
       return _parse_zone(end_hub, HubRole.HUB) 

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
