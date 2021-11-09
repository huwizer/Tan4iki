import random, wrap, time
from wrap import sprite


def granica(id, left, right, top, bottom):
    top1 = sprite.get_top(id)
    bottom1 = sprite.get_bottom(id)
    left1 = sprite.get_left(id)
    right1 = sprite.get_right(id)
    if left1 <= left:
        sprite.move_left_to(id, left)
    if right1 >= right:
        sprite.move_right_to(id, right)
    if top1 <= top:
        sprite.move_top_to(id, top)
    if bottom1 >= bottom:
        sprite.move_bottom_to(id, bottom)


def povorot(id, x, y):
    if x > 0:
        sprite.set_angle(id, 90)
    elif x < 0:
        sprite.set_angle(id, 270)
    elif y > 0:
        sprite.set_angle(id, 180)
    elif y < 0:
        sprite.set_angle(id, 0)


def vibor_bot(nomer_bota, mosh, bullet_list, id_target, top, bottom, left, right):
    x_target, y_target = sprite.get_pos(id_target)
    x_hunter, y_hunter = sprite.get_pos(nomer_bota)
    if y_target > y_hunter:
        enemy_x = 0
        enemy_y = mosh
        bottom = y_target
    elif y_target < y_hunter:
        enemy_x = 0
        enemy_y = -mosh
        top = y_target
    else:
        enemy_x = 0
        enemy_y = 0
    povorot(nomer_bota, enemy_x, enemy_y)
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


def shot(nomer, bullet_list):
    schet = 0
    for n_bull in bullet_list:
        if n_bull["id_tanka"] == nomer:
            schet += 1
    if schet == 2:
        return

    x, y = wrap.sprite.get_pos(nomer)
    ugol = wrap.sprite.get_angle(nomer)
    if ugol == 90:
        right = sprite.get_right(nomer)
        bul = wrap.sprite.add("battle_city_items", right + 10, y, "bullet")
        wrap.sprite.set_angle(bul, 90)
    elif ugol == 180:
        bottom = sprite.get_bottom(nomer)
        bul = wrap.sprite.add("battle_city_items", x, bottom + 10, "bullet")
        wrap.sprite.set_angle(bul, 180)
    elif ugol == -90:
        left = sprite.get_left(nomer)
        bul = wrap.sprite.add("battle_city_items", left - 10, y, "bullet")
        wrap.sprite.set_angle(bul, -90)
    elif ugol == 0:
        top = sprite.get_top(nomer)
        bul = wrap.sprite.add("battle_city_items", x, top - 10, "bullet")
        wrap.sprite.set_angle(bul, 0)

    bullet_slovar = {"bullet": bul, "id_tanka": nomer}
    bullet_list.append(bullet_slovar)

    print("")
    for n_bull in bullet_list:
        print(n_bull)


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


def proverka_granici_puli(bullet_list):
    for n_bull in bullet_list:
        x, y = sprite.get_pos(n_bull["bullet"])
        if x > 1000 or x < 0 or y > 1000 or y < 0:
            sprite.remove(n_bull["bullet"])
            bullet_list.remove(n_bull)
    print("")
    for n_bull in bullet_list:
        print(n_bull)
