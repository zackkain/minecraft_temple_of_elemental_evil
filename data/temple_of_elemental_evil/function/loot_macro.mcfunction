# function temple_of_elemental_evil:loot_macro { "player_name": "@s", "type": "currency", "item": "copper_ingot", "tag": "copper_piece", "value": 1 }
$execute store success score $(player_name) commandResult run clear $(player_name) minecraft:$(item)[minecraft:custom_data={"temple_of_elemental_evil:$(type)":"temple_of_elemental_evil:$(tag)"}] 1
$execute if score $(player_name) commandResult matches 1 run scoreboard players add $(player_name) currency $(value)
