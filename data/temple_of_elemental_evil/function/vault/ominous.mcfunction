# function temple_of_elemental_evil:vault/ominous { room: Number }
# function temple_of_elemental_evil:vault/ominous { room: 100 }
$give @p vault[block_state={ominous:"true"},block_entity_data={id:"minecraft:vault",config:{key_item:{count:1,id:"minecraft:ominous_trial_key"},loot_table:"temple_of_elemental_evil:vaults/ominous/$(room)"}}]