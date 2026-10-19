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

    def nb_drones_parse() -> None:
        ...

    def start_parse() -> None:
        ...

    def end_parse() -> None:
        ...

    def hub_parse() -> None:
        ...

    def connection_parse() -> None:
        ...

    def main_process(self) -> None:
        with open(self.map_file, 'r') as f:
            for line in f:
                content = line.partition('#')[0].strip()
                if not content:
                    continue
                if not content.startswith(
                        tuple(self.operations.keys())
                        ):
                    print('Error')


class ParseError(Exception):
    ...
