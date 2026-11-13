import sys
from map_data import MapData
from algorithem import PathFinder
from parser import MapParser, ParseError
from simulation_engine import SimulationEngine


def flyin(map_file: str) -> None:
    parser = MapParser(map_file)
    try:
        map_data: MapData = parser.main_process()
        print(f'nb_drones: {map_data.nb_drones}')
        print(f'hub_list: {map_data.graph_structure.hub_list}')
        print(f'connection_list: {map_data.graph_structure.connection_list}')
    except (ParseError, ValueError) as e:
        print(e)
        return

    pf = PathFinder(map_data.graph_structure)
    simulation_engine = SimulationEngine(
            drone_nums=map_data.nb_drones,
            path_finder=pf)
    simulation_engine.run_all_turns()


if __name__ == '__main__':
    flyin(sys.argv[1])
