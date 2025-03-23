import pathlib
import json
from typing import Literal, TypeAlias
from .monster import Monster

DEFAULT = {
  "type": "minecraft:equipment",
  "pools": [
    {
      "rolls": 0,
      "entries": [
      ]
    }
  ]
}

type Difficulty = Literal["normal","ominous"]

class Equipment:
  def _render_equipment(self):
    return json.dumps(DEFAULT, indent=2)
  
  def _write_equipment(self, monster: Monster, difficulty: Difficulty, file_contents: str):
    path = pathlib.Path("data", "temple_of_elemental_evil", "loot_table", "equipment", difficulty, f"{monster['name'].lower()}.json")
    with open(path, "w+", encoding="UTF-8") as file_stream:
      file_contents = self._render_equipment()
      file_stream.write(file_contents)

  def equipment(self, arguments):
    relevant_monsters = self.monsters
    if arguments.monster != "*":
      relevant_monsters = filter(lambda monster: monster['name'] == arguments.monster, self.monsters)

    for monster in relevant_monsters:
      file_contents = self._render_equipment()
      self._write_equipment(monster, "normal", file_contents)
      self._write_equipment(monster, "ominous", file_contents)