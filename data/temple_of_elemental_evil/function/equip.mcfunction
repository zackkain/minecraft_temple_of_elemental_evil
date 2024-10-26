# function temple_of_elemental_evil:equip { player_name: String, equipment_name: String }
# function temple_of_elemental_evil:equip { player_name: "@s", equipment_name: "2024" }
$loot give $(player_name) loot temple_of_elemental_evil:equipment/player/$(equipment_name)