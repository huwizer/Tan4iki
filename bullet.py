import wrap, random, tank
from wrap import sprite


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


def proverka_granici_puli(bullet_list):
    for n_bull in bullet_list:
        x, y = sprite.get_pos(n_bull["bullet"])
        if x > 1000 or x < 0 or y > 1000 or y < 0:
            sprite.remove(n_bull["bullet"])
            bullet_list.remove(n_bull)
    print("")
    for n_bull in bullet_list:
        print(n_bull)
