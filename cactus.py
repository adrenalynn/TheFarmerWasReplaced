import util

def plant_all():
    for x in range(MAX_SIZE):
        for y in range(MAX_SIZE):
            util.fast_move(x, y)
            if get_entity_type() != Entities.Cactus:
                util.tiller()
                plant(Entities.Cactus)


def sort_row(y):
    util.fast_move(0, y)
    for x1 in range(0, MAX_SIZE - 1):
        for x2 in range(1, MAX_SIZE - x1):
            util.fast_move(x2, y)
            if measure() < measure(West):
                swap(West)


def sort_col(x):
    util.fast_move(x, 0)
    for y1 in range(0, MAX_SIZE - 1):
        for y2 in range(1, MAX_SIZE - y1):
            util.fast_move(x, y2)
            if measure() < measure(South):
                swap(South)


def sort_all():
    for y in range(MAX_SIZE):
        sort_row(y)
    for x in range(MAX_SIZE):
        sort_col(x)


# MAIN
clear()
MAX_SIZE = get_world_size()
#pumpkin_cost = get_cost(Entities.Cactus)[Items.Pumpkin]
#while num_items(Items.Pumpkin) > MAX_SIZE * pumpkin_cost:
while num_items(Items.Cactus) < 100000:
    plant_all()
    sort_all()
    util.fast_move(MAX_SIZE - 1, MAX_SIZE - 1)
    harvest()
#print("Missing pumpkins")