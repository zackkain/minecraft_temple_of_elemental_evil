import pathlib
from .monster import Monster

class Spawner:
  def _render_spawner(self, monster: Monster):
    return self._render(self._template("spawner.mcfunction.j2"), monster.__dict__)
  
  def _write_spawner(self, monster: Monster, file_contents: str):
    path = pathlib.Path("data", "temple_of_elemental_evil", "function", "spawner", f"{monster.name.lower()}.mcfunction")
    with open(path, "w+", encoding="UTF-8") as file_stream:
      file_stream.write(file_contents)

  def spawner(self, arguments):
    relevant_monsters: list[Monster] = self.monsters
    if arguments.monster != "*":
      relevant_monsters = filter(lambda monster: monster.name == arguments.monster, self.monsters)

    for monster in relevant_monsters:
      file_contents = self._render_spawner(monster)
      self._write_spawner(monster, file_contents)