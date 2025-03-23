from typing import TypedDict

class Monster(TypedDict):
  name: str
  mob: str
  count: int
  added_per_player: int
  equipment: str
  room: str
  armor: int
  damage: int
  scale: float
  zombifyable: bool

  def __call__(self, *args, **kwds):
    defaults = {
      "count": 1,
      "added_per_player": 0,
      "equipment": "nothing",
      "room": "common",
      "scale": 1.0,
      "zombifyable": False
    }
    defaults.update(kwds)
    return super().__call__(*args, defaults)