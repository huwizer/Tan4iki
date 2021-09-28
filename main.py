import wrap, random
from wrap import sprite

x1 = 50
y1 = 50
x2 = 950
y2 = 50


def respawn_enemy1():
    global enemy1
    sprite.remove(enemy1)
    coustrume = random.choice(
        ["tank_player_size1_white1", "tank_enemy_size1_yellow1", "tank_enemy_size1_green1",
         "tank_enemy_size1_purple1"])
    size = random.randint(15, 60)
    enemy1 = sprite.add("battle_city_tanks", x1, y1, coustrume)
    sprite.set_height_proportionally(enemy1, size)


def respawn_enemy2():
    global enemy2
    sprite.remove(enemy2)
    coustrume = random.choice(
        ["tank_player_size1_white1", "tank_enemy_size1_yellow1", "tank_enemy_size1_green1",
         "tank_enemy_size1_purple1"])
    size = random.randint(15, 60)
    enemy2 = sprite.add("battle_city_tanks", x2, y2, coustrume)
    sprite.set_height_proportionally(enemy2, size)



wrap.world.create_world(1000, 1000)
player = sprite.add("battle_city_tanks", 500, 500, "tank_player_size1_white1")
enemy1 = None
enemy2 = None
respawn_enemy1()
respawn_enemy2()

def granica():
    global enemy1, enemy2, player
    top=sprite.get_top(player)
    bottom=sprite.get_bottom(player)
    left=sprite.get_left(player)
    right=sprite.get_right(player)
    if left<=0:
        sprite.move_left_to(player,0)


enemy1_x = 0
enemy1_y = 0
enemy2_x = 0
enemy2_y = 0
bul = None


def povorot(id, x, y):
    if x > 0:
        sprite.set_angle(id, 90)
    elif x < 0:
        sprite.set_angle(id, 270)
    elif y > 0:
        sprite.set_angle(id, 180)
    elif y < 0:
        sprite.set_angle(id, 0)


@wrap.on_key_always(wrap.K_w, wrap.K_s, wrap.K_d, wrap.K_a)
def move(keys):
    if wrap.K_w in keys:
        x = 0
        y = -3
    elif wrap.K_s in keys:
        x = 0
        y = 3
    elif wrap.K_d in keys:
        x = 3
        y = 0
    elif wrap.K_a in keys:
        x = -13
        y = 0
    else:
        x = 0
        y = 0

    povorot(player, x, y)
    sprite.move(player, x, y)
    granica()

@wrap.always(2000)
def bot_action():
    global enemy2_x, enemy2_y, enemy1_x, enemy1_y
    enemy2_x, enemy2_y = vibor_bot(enemy2)
    enemy1_x, enemy1_y = vibor_bot(enemy1)


def shot(nomer):
    global bul
    x, y = wrap.sprite.get_pos(nomer)
    ugol = wrap.sprite.get_angle(nomer)
    if ugol == 90:
        bul = wrap.sprite.add("battle_city_items", x + 22, y, "bullet")
        wrap.sprite.set_angle(bul, 90)
    elif ugol == 180:
        bul = wrap.sprite.add("battle_city_items", x, y + 22, "bullet")
        wrap.sprite.set_angle(bul, 180)
    elif ugol == -90:
        bul = wrap.sprite.add("battle_city_items", x - 22, y, "bullet")
        wrap.sprite.set_angle(bul, -90)
    elif ugol == 0:
        bul = wrap.sprite.add("battle_city_items", x, y - 22, "bullet")
        wrap.sprite.set_angle(bul, 0)


@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def shot_player():
    shot(player)


@wrap.always(100)
def move_bullet():
    if bul != None:
        sprite.move_at_angle_dir(bul, 15)


@wrap.always(20)
def bot_move():
    sprite.move(enemy2, enemy2_x, enemy2_y)
    sprite.move(enemy1, enemy1_x, enemy1_y)


def vibor_bot(nomer_bota):
    or_or = random.choice(["x", "y", "stand", "shot"])
    or_or = random.choice(["stand"])
    ra = random.randint(-2, 2)

    if or_or == "x":
        enemy_x = ra
        enemy_y = 0
    elif or_or == "y":
        enemy_x = 0
        enemy_y = ra
    elif or_or == "shot":
        enemy_y = 0
        enemy_x = 0
        shot(nomer_bota)
    else:
        enemy_y = 0
        enemy_x = 0

    povorot(nomer_bota, enemy_x, enemy_y)
    return [enemy_x, enemy_y]




@wrap.always(10)
def colizia_bullet():
    global bul, enemy1
    if bul != None:
        to = wrap.sprite.is_collide_any_sprite(bul, [enemy1, enemy2])
        if to != None:
            sprite.remove(bul)
            bul = None
            if to == enemy1:
                respawn_enemy1()
            if to == enemy2:
                respawn_enemy2()






    # a = x_left = sprite.get_left(enemy1)
    # x1, y1 = sprite.get_pos(enemy1)
    # x2, y2 = sprite.get_pos(enemy2)
    # if x1 >= 1000:
    #     x1 = 1000
    # if x1 <= 0:
    #     x1 = 0
