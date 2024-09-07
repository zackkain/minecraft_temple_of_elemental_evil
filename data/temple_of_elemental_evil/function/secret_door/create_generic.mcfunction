# function temple_of_elemental_evil:secret_door/create_generic {bottom:resource_location, top: resource_location}
# function temple_of_elemental_evil:secret_door/create_generic {bottom:chiseled_stone_bricks, top:stone_bricks}
$execute align xyz run summon block_display ~ ~ ~ {block_state:{Name:$(bottom)},Tags:["secret_door"]}
$execute align xyz run summon block_display ~ ~1 ~ {block_state:{Name:$(top)},Tags:["secret_door"]}