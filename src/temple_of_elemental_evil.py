import pathlib
import json
from typing import Any
import jinja2
from functools import lru_cache
from .spawner import Spawner
from .equipment import Equipment
from .monster import Monster

def _load_monsters():
  with open(pathlib.Path("src", "data", "monsters.json"), "r", encoding="UTF-8") as file_stream:
    return [ Monster(**monster) for monster in json.loads(file_stream.read()) ]

class TempleOfElementalEvil(Spawner, Equipment):
  def __init__(self):
    self.environment = jinja2.Environment(
      loader=jinja2.FileSystemLoader(pathlib.Path("src", "resources", "templates"))
    )
    self.globals = {

    }
    self.monsters = _load_monsters()

  @lru_cache(maxsize=None)
  def _template(self, file: str):
    return self.environment.get_template(file, globals=self.globals)
  
  def _render(self, template: jinja2.Template, context: Any):
    return template.render(context)
  
  def all(self, arguments):
    self.spawner(arguments)
    self.equipment(arguments)