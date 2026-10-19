class MapParser:
    def __init__(self, map_file: str) -> None:
        self.map_file: str = map_file

    def main_process(self) -> None:
        with open(self.map_file, 'r') as f:
            for line in f:
                content = line.partition('#')[0].strip()
                if not content:
                    continue
                map_elements = ['nb_drones',
                                'start_hub',
                                'end_hub',
                                'hub',
                                'connection'
                                ]
                for element in map_elements:
                    if content.startwith(element):
                        break
                else:
                    ...


class ParserError():
    ...
