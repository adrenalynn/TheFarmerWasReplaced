import util


def init_size_dict():
    result = {}
    for i in range(15, 6, -1):
        result[i] = []
    return result


def first_planting(first_run=False):
    for x in range(FIELD_SIZE):
        for y in range(FIELD_SIZE):
            util.fast_move(x, y)
            if first_run:
                till()
            plant(Entities.Sunflower)
            SIZES[measure()].append((x, y))
            util.do_water(0.6)


def replant_all():
    for x in range(FIELD_SIZE):
        for y in range(FIELD_SIZE):
            util.fast_move(x, y)
            util.tiller()
            plant(Entities.Sunflower)
            SIZES[measure()].append((x, y))
            util.do_water(0.4)


# MAIN
clear()
FIELD_SIZE = get_world_size()
SIZES = init_size_dict()
first_planting(True)
while num_items(Items.Power) < 100000:
    for size in range(15, 6, -1):
        for x, y in SIZES[size]:
            util.fast_move(x, y)
            if can_harvest():
                harvest()
            if not can_harvest():
                use_item(Items.Fertilizer)
                harvest()
        SIZES[size] = []
    replant_all()
