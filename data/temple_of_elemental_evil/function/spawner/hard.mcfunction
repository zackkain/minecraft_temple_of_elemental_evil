# function temple_of_elemental_evil:spawner/hard {mob: String, count: Number, name: String, room: String, base_armor: Number, base_damage: Number}
# function temple_of_elemental_evil:spawner/hard {mob:"vindicator",count:2,name:"brigand",room:"common",base_armor:2,base_damage:3}
$give @p trial_spawner[block_entity_data={id:"minecraft:trial_spawner",normal_config:{total_mobs:$(count),spawn_potentials:[{data:{entity:{id:"minecraft:$(mob)",CustomName:"$(name)",CustomNameVisible:1b,CanPickUpLoot:0b,attributes:[{id:"generic.armor",base:$(base_armor),modifiers:[{amount:1,operation:"add_value"}]},{id:"generic.attack_damage",base:$(base_damage),modifiers:[{amount:0.5,operation:"add_multiplied_total"}]}]},equipment:{loot_table:"temple_of_elemental_evil:equipment/normal/$(name)",slot_drop_chances:0f}},weight:1}],loot_tables_to_eject:[{data:"temple_of_elemental_evil:spawners/normal/$(room)",weight:1}]},ominous_config:{total_mobs:$(count),spawn_potentials:[{data:{entity:{id:"minecraft:$(mob)",CustomName:"$(name)",CustomNameVisible:1b,CanPickUpLoot:0b,attributes:[{id:"generic.armor",base:$(base_armor),modifiers:[{amount:1,operation:"add_value"},{id:"generic.attack_damage",base:$(base_damage),modifiers:[{amount:0.5,operation:"add_multiplied_total"}]}]}]},equipment:{loot_table:"temple_of_elemental_evil:equipment/ominous/$(name)",slot_drop_chances:0f},weight:1}}],loot_tables_to_eject:[{data:"temple_of_elemental_evil:spawners/ominous/$(room)",weight:1}]}}]