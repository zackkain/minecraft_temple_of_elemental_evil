import pathlib
import json
from typing import Literal
from .monster import Monster

type Difficulty = Literal["normal","ominous"]
DIFFICULTIES: list[Difficulty] = ["normal","ominous"]
type ArmorMaterial = Literal["leather","chainmail","iron","diamond","netherite"]
ARMOR_MATERIALS: list[ArmorMaterial] = ["leather","chainmail","iron","diamond","netherite"]
type WeaponMaterial = Literal["wooden","stone","iron","diamond","netherite"]
WEAPON_MATERIALS: list[WeaponMaterial] = ["wooden","stone","iron","diamond","netherite"]
type WeaponType = Literal["axe", "sword"]

def get_armor_material(monster: Monster):
  offset = min(monster.floor + monster.difficulty, len(ARMOR_MATERIALS) - 1)
  return ARMOR_MATERIALS[offset]

def get_weapon_material(monster: Monster):
  offset = min(monster.floor + monster.difficulty, len(WEAPON_MATERIALS) - 1)
  return WEAPON_MATERIALS[offset]

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

def with_pools(pools):
  return {
    "type": "minecraft:equipment",
    "pools": pools
  }
  
def head_pool(head):
  return {
    "rolls": 1,
    "entries": [
      {
        "type": "minecraft:item",
        "name": "minecraft:player_head",
        "functions": [
          {
            "function": "set_components",
            "components": {
              "minecraft:profile": f"MHF_{head}"
            }
          }
        ]
      }
    ]
  }

def armor_pool(material:ArmorMaterial, difficulty: Difficulty):
  return {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:loot_table",
          "value": f"temple_of_elemental_evil:equipment/{difficulty}/{material}"
        }
      ]
    }

def helmet_pool(material: ArmorMaterial, difficulty: Difficulty):
  max = 10.0 if difficulty == "normal" else 30.0
  min = 0.0 if difficulty == "normal" else 10.0
  return {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": f"minecraft:{material}_helmet",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": max,
                "min": min
              },
              "options": "#minecraft:on_random_loot"
            }
          ]
        }
      ]
    }

def weapon_pool(material:WeaponMaterial, type:WeaponType, difficulty: Difficulty):
  max = 10.0 if difficulty == "normal" else 30.0
  min = 0.0 if difficulty == "normal" else 10.0
  return {
      "rolls": 1,
      "entries": [
        {
          "type": "minecraft:item",
          "name": f"minecraft:{material}_{type}",
          "functions": [
            {
              "function": "minecraft:enchant_with_levels",
              "levels": {
                "type": "minecraft:uniform",
                "max": max,
                "min": min
              },
              "options": "#minecraft:on_random_loot"
            }
          ]
        }
      ]
    }

class Equipment:
  def _render_equipment(self, monster: Monster, difficulty: Difficulty):
    if not monster.custom_head and not monster.weapon_type and not monster.has_armor and not monster.has_helmet:
      return json.dumps(DEFAULT, indent=2)
    pools = []
    if monster.custom_head:
      pools.append(head_pool(monster.custom_head))
    if monster.has_armor:
      armor_material = get_armor_material(monster)
      pools.append(armor_pool(armor_material, difficulty))
    if monster.has_helmet:
      armor_material = get_armor_material(monster)
      pools.append(helmet_pool(armor_material, difficulty))
    if monster.weapon_type:
      weapon_material = get_weapon_material(monster)
      pools.append(weapon_pool(weapon_material, monster.weapon_type, difficulty))
    return json.dumps(with_pools(pools), indent=2)
  
  def _write_equipment(self, monster: Monster, difficulty: Difficulty, file_contents: str):
    path = pathlib.Path("data", "temple_of_elemental_evil", "loot_table", "equipment", difficulty, f"{monster.name.lower()}.json")
    with open(path, "w+", encoding="UTF-8") as file_stream:
      file_contents = self._render_equipment(monster, difficulty)
      file_stream.write(file_contents)

  def equipment(self, arguments):
    relevant_monsters = self.monsters
    if arguments.monster != "*":
      relevant_monsters = filter(lambda monster: monster.name == arguments.monster, self.monsters)

    for monster in relevant_monsters:
      for difficulty in DIFFICULTIES:
        file_contents = self._render_equipment(monster, difficulty)
        self._write_equipment(monster, difficulty, file_contents)
        self._write_equipment(monster, difficulty, file_contents)