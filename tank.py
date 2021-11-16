import random, wrap, time
from wrap import sprite


def create_tank(x, y, costume, mosh):
    tank = sprite.add("battle_city_tanks", x, y, costume)
    tank_slovar = {"id": tank, "mosh": mosh}
    return tank_slovar


def granica(tank, left, right, top, bottom):
    top1 = sprite.get_top(tank["id"])
    bottom1 = sprite.get_bottom(tank["id"])
    left1 = sprite.get_left(tank["id"])
    right1 = sprite.get_right(tank["id"])
    if left1 <= left:
        sprite.move_left_to(tank["id"], left)
    if right1 >= right:
        sprite.move_right_to(tank["id"], right)
    if top1 <= top:
        sprite.move_top_to(tank["id"], top)
    if bottom1 >= bottom:
        sprite.move_bottom_to(tank["id"], bottom)


def povorot(tank, x, y):
    if x > 0:
        sprite.set_angle(tank["id"], 90)
    elif x < 0:
        sprite.set_angle(tank["id"], 270)
    elif y > 0:
        sprite.set_angle(tank["id"], 180)
    elif y < 0:
        sprite.set_angle(tank["id"], 0)


def vibor_bot(tank, mosh, bullet_list, id_target, top, bottom, left, right):
    x_target, y_target = sprite.get_pos(id_target)
    # y_target_top=sprite.get_top(id_target)
    # y_target_bottom=sprite.get_bottom(id_target)
    x_hunter, y_hunter = sprite.get_pos(tank["id"])
    if y_target > y_hunter:
        enemy_x = 0
        enemy_y = mosh
        bottom = y_target + sprite.get_height(tank["id"]) / 2
    elif y_target < y_hunter:
        enemy_x = 0
        enemy_y = -mosh
        top = y_target - sprite.get_height(tank["id"]) / 2
    else:
        enemy_x = 0
        enemy_y = 0
    povorot(tank["id"], enemy_x, enemy_y)
    return [enemy_x, enemy_y, top, bottom, left, right]
    # or_or = random.choice(["y", "stand", "shot"])
    # p_m = random.choice([mosh, -mosh])
    #
    # if or_or == "x":
    #     enemy_x = p_m
    #     enemy_y = 0
    # elif or_or == "y":
    #     enemy_x = 0
    #     enemy_y = p_m
    # elif or_or == "shot":
    #     enemy_y = 0
    #     enemy_x = 0
    #     shot(nomer_bota, bullet_list)
    # else:
    #     enemy_y = 0
    #     enemy_x = 0
    #
    # povorot(nomer_bota, enemy_x, enemy_y)
    # return [enemy_x, enemy_y]


def effect(x, y):
    efe = sprite.add("battle_city_items", x, y, "effect_appearance1")
    time.sleep(0.15)
    sprite.set_costume(efe, "effect_appearance2")
    time.sleep(0.15)
    sprite.set_costume(efe, "effect_appearance3")
    time.sleep(0.15)
    sprite.set_costume(efe, "effect_appearance4")
    time.sleep(0.15)
    sprite.set_costume(efe, "effect_appearance3")
    time.sleep(0.15)
    sprite.set_costume(efe, "effect_appearance2")
    time.sleep(0.15)
    sprite.set_costume(efe, "effect_appearance3")
    time.sleep(0.15)
    sprite.set_costume(efe, "effect_appearance4")
    time.sleep(0.15)

    sprite.remove(efe)
