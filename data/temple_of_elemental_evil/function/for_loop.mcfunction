# function temple_of_elemental_evil:for_loop { function_name:String,function_args:Object,loop_index_current_name:String,loop_index_end_name:String }
$function $(function_name) $(function_args)

$scoreboard players add heap $(loop_index_current) 1
$execute if score heap $(loop_index_current) < heap $(loop_index_end) run function temple_of_elemental_evil:for_loop $(function_name) $(function_args)
