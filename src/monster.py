from dataclasses import dataclass

@dataclass
class Monster():
  name: str
  mob: str
  armor: int
  damage: int
  count: int = 1
  added_per_player: int = 0
  equipment: str = "nothing"
  room: str = "common"
  scale: float = 1.0
  zombifyable: bool = False