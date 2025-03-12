def do_water(level = 0.5):
    if num_items(Items.Water) > 1 and get_water() <= level:
        use_item(Items.Water)
    return


def tiller():
    if get_ground_type() == Grounds.Grassland:
        till()


def verify_soil(type):
    if type in [Entities.Carrot, Entities.Cactus]:
        if get_ground_type() == Grounds.Grassland:
            till()
    elif get_ground_type() == Grounds.Soil:
        till()


def move_to(x, y):
    while get_pos_x() < x:
        move(East)
    while get_pos_x() > x:
        move(West)
    while get_pos_y() < y:
        move(North)
    while get_pos_y() > y:
        move(South)


def fast_move(t_x, t_y):
    x = get_pos_x()
    while x != t_x:
        if (x < t_x and t_x - x < 5) or (x > t_x and x - t_x > 5):
            move(East)
        else:
            move(West)
        x = get_pos_x()

    y = get_pos_y()
    while y != t_y:
        if (y < t_y and t_y - y < 5) or (y > t_y and y - t_y > 5):
            move(North)
        else:
            move(South)
        y = get_pos_y()
        
    

def random_from(list):
    index = random() * len(list) // 1
    return list[index]
