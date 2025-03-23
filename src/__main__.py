import argparse
import sys
from .temple_of_elemental_evil import TempleOfElementalEvil

def get_parser(temple_of_elemental_evil: TempleOfElementalEvil):
  parser = argparse.ArgumentParser(description="Temple of Elemental Evil")
  subparsers = parser.add_subparsers(required=True)

  spawner_parser = subparsers.add_parser("spawner", help="Generate Spawner MC Functions")
  spawner_parser.add_argument("--monster", "-m", type=str, default="*")
  spawner_parser.set_defaults(func=temple_of_elemental_evil.spawner)

  equipment_parser = subparsers.add_parser("equipment", help="Generate Equipment Loot Tables")
  equipment_parser.add_argument("--monster", "-m", type=str, default="*")
  equipment_parser.set_defaults(func=temple_of_elemental_evil.equipment)

  all_parser = subparsers.add_parser("all", help="Render Everything")
  all_parser.add_argument("--monster", "-m", type=str, default="*")
  all_parser.set_defaults(func=temple_of_elemental_evil.all)

  return parser

def main():
  temple_of_elemental_evil = TempleOfElementalEvil()
  arguments = get_parser(temple_of_elemental_evil).parse_args()
  arguments.func(arguments)
  return 0

if __name__ == "__main__":
  sys.exit(main())
