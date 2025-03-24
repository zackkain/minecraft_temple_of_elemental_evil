from dataclasses import dataclass

@dataclass
class Monster():
  name: str
  mob: str
  # 0-30
  armor: int = 2
  # 0-2048
  damage: int = 2
  count: int = 1
  added_per_player: int = 0
  equipment: str = "nothing"
  room: str = "common"
  # 0.0625-16
  scale: float = 1.0
  zombifyable: bool = False
  custom_head: str = None
  weapon_type: str = None
  has_armor: bool = False
  has_helmet: bool = False
  # Compared to other mobs on the same floor
  # 0: Weak
  # 1: Medium
  # 2: Strong
  difficulty: int = 0
  # 0: Floor 1
  # 1: Floor 2
  # 2: Floor 3
  # 3: Floor 4
  floor: int = 0
