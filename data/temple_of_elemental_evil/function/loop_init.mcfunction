# function temple_of_elemental_evil:loop_init {start: Number, end: Number, function_name: String, function_args: Object}
$scoreboard players set heap $(loop_index_current_name) $(start)
$scoreboard players set heap $(loop_index_end_name) $(end)
function datapack:for_loop { function_name:$(function_name),function_args:$(function_args),loop_index_current_name:$(loop_index_current_name),loop_index_end_name:$(loop_index_end_name) }