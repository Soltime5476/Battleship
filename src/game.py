from enum import Enum
# Board size: 8x8

class Board:
    '''
    Fill when shoot:
    A: Carrier
    B: Battleship
    C: Submarine/Destroyer
    P: Patrol Boat
    X: Miss
    '''
    _length: int = 10
    _width: int = 10

    def __init__(self) -> None:
        pass

    @property
    def length(self):
        return self._length
    
    @property
    def width(self):
        return self._width
    
class Ships(Enum):   
    Patrol_Boat = 2    
    Destroyer = 3
    Submarine = 3 
    Battleship = 4 
    Carrier = 5

def shoot(coord: str):
    pass 