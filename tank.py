import random, wrap, time
from wrap import sprite


def create_tank(x, y, mosh, size):
    effect(x, y)
    costume = random.choice(
        ["tank_player_size1_white1", "tank_enemy_size1_yellow1", "tank_enemy_size1_green1",
         "tank_enemy_size1_purple1"])
    tank = sprite.add("battle_city_tanks", x, y, costume)
    tank_slovar = {
        "id": tank,
        "mosh": mosh,
        "speed_x": 0,
        "speed_y": 0,
        "top":0,
        "bottom":0,
        "left":0,
        "right":0
    }
    sprite.set_height_proportionally(tank, size)
    return tank_slovar

def move_bot(tank):
    povorot(tank, tank["speed_x"], tank["speed_y"])
    sprite.move(tank["id"], tank["speed_x"], tank["speed_y"])
    granica(tank, tank["left"], tank["right"], tank["top"], tank["bottom"])


def move(tank, x, y):
    povorot(tank, x, y)
    sprite.move(tank["id"], x, y)
    granica(tank, 0, 1000, 0, 900)


def move_up(tank):
    move(tank, 0, -tank["mosh"])


def move_down(tank):
    move(tank, 0, tank["mosh"])


def move_left(tank):
    move(tank, -tank["mosh"], 0)


def move_right(tank):
    move(tank, tank["mosh"], 0)


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
        tank["speed_x"] = 0
        tank["speed_y"] = mosh
        bottom = y_target + sprite.get_height(tank["id"]) / 2
    elif y_target < y_hunter:
        tank["speed_x"] = 0
        tank["speed_y"] = -mosh
        top = y_target - sprite.get_height(tank["id"]) / 2
    else:
        tank["speed_x"] = 0
        tank["speed_y"] = 0


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
