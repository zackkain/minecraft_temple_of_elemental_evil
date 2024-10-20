# function temple_of_elemental_evil:vault/normal { room: Number }
# function temple_of_elemental_evil:vault/normal { room: 100 }
$give @p vault[custom_name='{"text":"Room $(room) Vault"}',block_entity_data={id:"minecraft:vault",config:{key_item:{count:1,id:"minecraft:trial_key"},loot_table:"temple_of_elemental_evil:vaults/normal/$(room)"}}]