import sys
from parser import MapParser, ParseError


def flyin(map_file: str) -> None:
    parser = MapParser(map_file)
    try:
        parser.main_process()
        print(f'nb_drones: {parser.nb_drones}')
        print(f'hub_list: {parser.hub_list}')
        print(f'connection_list: {parser.connection_list}')
    except (ParseError, ValueError) as e:
        print(e)


if __name__ == '__main__':
    flyin(sys.argv[1])
