# function temple_of_elemental_evil:armor_stand { scale: Number }
$data modify entity @e[type=minecraft:armor_stand,sort=nearest,limit=1] attributes[{id:"generic.scale"}].base set value $(scale)