# function temple_of_elemental_evil:spawner/bandit {room: Number, total: Number}
# function temple_of_elemental_evil:spawner/bandit {room:"common",total: 6}
$function temple_of_elemental_evil:spawner/generic {mob:"vindicator",count:$(total),added_per_player:1,name:"Brigand",equipment:"brigand",room:$(room),armor:0,damage:3,scale:1}