from pydantic import BaseModel, Field, ValidationError, model_validator
from enum import Enum


class HubRole(Enum):
    '''hubの役割をまとめたEnum

    Attributes:
        HUB: 通常のハブ
        START: スタートポイント
        END: エンドポイント
    '''
    HUB = 'hub'
    START = 'start'
    END = 'end'


class ZoneType(Enum):
    '''Zoneの種類をまとめたEnum

    Attributes:
        NORMAL: 通常のZone 
        BLOCKED: 立ち入り禁止Zone
        RESTRICTED: 移動に2ターンかかるZone
        PRIORITY: 優先的に使用されるZone
    '''
    NORMAL = 'normal'
    BLOCKED = 'blocked'
    RESTRICTED = 'restricted' 
    PRIORITY = 'priority'


class MapData(BaseModel):
    '''
    Mapのデータを保持するデータクラス
    '''
    nb_drones: int = Field(ge=1)
    graph_structure: GraphStructure


class GraphStructure(BaseModel):
    '''
    MapのGraph構造を保持するデータクラス
    '''
    hub_list: list[Hub] = Field(min_length=2)
    connection_list: list[Connection] = Field(min_length=1)


class Hub(BaseModel):
    '''
    Hubの情報を保持するデータクラス
    '''
    name: str = Field(max_length=256)
    cordinates: tuple[int, int]
    color: str = Field(max_length = 256)
    hub_role: HubRole = HubRole.HUB
    zone_type: ZoneType = ZoneType.NORMAL
    max_drones: int | None = 1


class Connection(BaseModel):
    '''
    Connectionの情報を保持するデータクラス
    '''
    connected_hub: tuple[str, str]
    max_link_capacity: int | None = 1
