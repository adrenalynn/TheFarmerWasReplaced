import util

# MAIN
FIELD_SIZE = get_world_size()
clear()
while num_items(Items.Wood) < 100000:
    for x in range(FIELD_SIZE):
        offset = x % 2
        for y in range(offset, FIELD_SIZE, 2):
            util.fast_move(x, y)
            if can_harvest():
                harvest()
            util.verify_soil(Entities.Tree)
            plant(Entities.Tree)
            util.do_water(0.8)
            (c_type, (c_x, c_y)) = get_companion()
            if c_type != None:
                util.fast_move(c_x, c_y)
                if can_harvest():
                    harvest()
                util.verify_soil(c_type)
                plant(c_type)
                    
