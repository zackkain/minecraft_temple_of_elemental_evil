# function temple_of_elemental_evil:reset_spawner {x:Number,y:Number,z:Number}
# $say Reset Spawner $(x) $(y) $(z)
$execute if block $(x) $(y) $(z) minecraft:trial_spawner run setblock $(x) $(y) $(z) minecraft:trial_spawner replace