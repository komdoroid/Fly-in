from typing import Any
from enum import Enum
from map_data import (
        HubRole,
        ZoneType,
        MapData,
        GraphStructure,
        Hub,
        Connection
        )


class MapKeyType(Enum):
    NB_DRONES = 'nb_drones'
    START_HUB = 'start_hub'
    END_HUB = 'end_hub'
    HUB = 'hub'
    CONNECTION = 'connection'


UNIQU_KEYS: set[MapKeyType, MapKeyType, MapKeyType] = set(
        MapKeyType.NB_DRONES,
        MapKeyType.START_HUB,
        MapKeyType.END_HUB
        )


class MapParser:
    def __init__(self, map_file: str) -> None:
        self.map_file: str = map_file
        self.nb_drones: int
        self.hub_list: list[Hub] = []
        self.connection_list: list[Hub] = []

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

    def _additional_info_parse(self, info: str) -> dict[str, Any]:
        ''' Hubの追加条件をパースする

        Args:
            info(str): Mapファイルから読み取ったHubの追加情報全文

        Returns:
            dict: 追加情報(xxxx=yyyy)をkey/valueに分割して格納した辞書。

        Raises:
            ParseError: 'key1=value1 key2=value2'の形式でない場合

        Examples:
            使用例を記載する（doctest形式も可能）。
        '''
        try:
            return dict(pair.split('=') for pair in info.split())
        except ValueError as e:
            raise ParseError(e)

    def _parse_zone(self, value: str, role: str) -> Hub:
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
        meta: dict[str, Any] = self._additional_info_parse(
            additional_info.strip(']'))

        kwargs: dict[str, Any] = {}
        if 'zone' in meta:
            kwargs['zone_type'] = meta['zone']
        if 'color' in meta:
            kwargs['color'] = meta['color']
        if 'max_drones' in meta:
            kwargs['max_drones'] = meta['max_drones']
        # 前後の空白を除いたうえで、' 'で分割
        splited_shub = mandatory_info.strip().split(' ')
        if len(splited_shub) != 3:
            raise ParseError(
                    'Please enter it in the following format'
                    ': (start_hub: name 0 0)'
                    )
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

    def start_parse(self, start_hub: str) -> Hub:
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
        return self._parse_zone(start_hub, HubRole.START.value)

    def end_parse(self, end_hub: str) -> Hub:
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
        return self._parse_zone(end_hub, HubRole.END.value)

    def hub_parse(self, hub: str) -> Hub:
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
        return self._parse_zone(hub, HubRole.HUB.value)

    def connection_parse(self, value: str) -> Connection:
        # 追加情報があるか確認
        mandatory_info, _, additional_info = value.partition('[')
        # [xxx xxx]が含まれているの場合はこれをパース
        meta = self._additional_info_parse(additional_info.strip(']'))

        kwargs: dict[str, Any] = {}
        if 'max_link_capacity' in meta:
            kwargs['max_link_capacity'] = meta['max_link_capacity']
        splited_connection = mandatory_info.strip().split('-')
        if len(splited_connection) != 2:
            raise ParseError(
                    'Please enter it in the following format'
                    ': (connection: hub1-roof1)'
                    )
        return Connection(
                connected_hub=splited_connection,
                **kwargs
                )

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
            seen: set[MapKeyType] = set()
            for line_nb, line in enumerate(f, start=1):
                content = line.partition('#')[0].strip()
                if not content:
                    continue
                key, sep, value = content.partition(':')
                key, value = key.strip(), value.strip()
                key_type = MapKeyType(key)
                if key_type in UNIQU_KEYS:
                    if key_type in seen:
                        raise ParseError(
                                f"line {line_nb}: "
                                f"'{key_type.value}' is defined more than once"
                                )
                    seen.add(key_type)
                if not sep:
                    raise ParseError(
                            f"{line_nb}: "
                            "The separator in the map file is incorrect")
                match key:
                    case MapKeyType.NB_DRONES.value:
                        self.nb_drones = self.nb_drones_parse(value)
                    case MapKeyType.START_HUB.value:
                        self.hub_list.append(self.start_parse(value))
                    case MapKeyType.END_HUB.value:
                        self.hub_list.append(self.end_parse(value))
                    case MapKeyType.HUB.value:
                        self.hub_list.append(self.hub_parse(value))
                    case MapKeyType.CONNECTION.value:
                        self.connection_list.append(
                                self.connection_parse(value)
                                )
                    case _:
                        raise ParseError(
                                f"{line_nb}: "
                                "The key name in the map file is incorrect")
            # ループ後にUNIQU_KEYSの中から出現しなかったものをチェック
            if not (UNIQU_KEYS - seen):
                raise ParseError(f"line {line_nb}: "
                                 "Missing required key(s) "
                                 f"{UNIQU_KEYS - seen}"
                                 )


class ParseError(Exception):
    ...
