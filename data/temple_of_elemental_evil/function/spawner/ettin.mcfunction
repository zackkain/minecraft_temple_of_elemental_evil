# function temple_of_elemental_evil:spawner/ettin { room: String, count: Number }
# function temple_of_elemental_evil:spawner/ettin { room: "common", count: 1 }
$function temple_of_elemental_evil:spawner/generic {mob:"husk",count:$(count),added_per_player:1,name:"Ettin",equipment:"leather",room:$(room),armor:8,damage:8,scale:1.2f}