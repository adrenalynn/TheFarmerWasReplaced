import util


def full_planting():
    newly_planted = []
    for x in range(FIELD_SIZE):
        for y in range(FIELD_SIZE):
            util.fast_move(x, y)
            util.tiller()
            plant(Entities.Pumpkin)
            util.do_water(0.2)
            newly_planted.append((x, y))
    return newly_planted


def replant_missing(current):
    newly_planted = []
    for x, y in current:
        util.fast_move(x, y)
        if get_entity_type() != Entities.Pumpkin:
            plant(Entities.Pumpkin)
            util.do_water(0.4)
            newly_planted.append((x, y))
    return newly_planted


def wait_last_one():
    while not can_harvest():
        util.do_water(1.0)
        if get_entity_type() != Entities.Pumpkin:
            plant(Entities.Pumpkin)
        use_item(Items.Fertilizer)


# MAIN
FIELD_SIZE = get_world_size()
clear()
while num_items(Items.Pumpkin) < 100000:
#while True:
    remaining = full_planting()
    while len(remaining) > 0:
        remaining = replant_missing(remaining)
    wait_last_one()
    harvest()
