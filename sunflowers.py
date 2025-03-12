import util


def first_planting():
    for x in range(FIELD_SIZE):
        for y in range(FIELD_SIZE):
            util.fast_move(x, y)
            till()
            plant(Entities.Sunflower)
            SIZES[measure()].append((x, y))
            util.do_water(0.4)


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
SIZES = {15: [], 14: [], 13: [], 12: [],
11: [], 10: [], 9: [], 8: [], 7: []}

first_planting()
while num_items(Items.Power) < 100000:
    for size in range(15, 6, -1):
        for x, y in SIZES[size]:
            util.fast_move(x, y)
            if not can_harvest():
                use_item(Items.Fertilizer)
            harvest()
        SIZES[size] = []
    replant_all()
