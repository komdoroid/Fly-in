import sys
from parser import MapParser


def flyin(map_file: str) -> None:
    parser = MapParser(map_file)
    # print(parser.main_process())
    parser.main_process()


if __name__ == '__main__':
    flyin(sys.argv[1])
