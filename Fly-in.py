import sys
from parser import MapParser, ParseError


def flyin(map_file: str) -> None:
    parser = MapParser(map_file)
    # print(parser.main_process())
    try:
        parser.main_process()
    except (ParseError, ValueError) as e:
        print(e)


if __name__ == '__main__':
    flyin(sys.argv[1])
