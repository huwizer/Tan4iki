import time
import wrap, random
from wrap import sprite

x1 = 50
y1 = 50
x2 = 950
y2 = 50
mosh_enemy1 = None
mosh_enemy2 = None
bullet_list=[]


def speed_size(size):
    if size < 20:
        mosh = 4
    elif size > 35:
        mosh = 1
    else:
        mosh = 2
    return mosh


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


def respawn_enemy1():
    global enemy1, mosh_enemy1,enemy1_speed_y,enemy1_speed_x
    sprite.remove(enemy1)
    coustrume = random.choice(
        ["tank_player_size1_white1", "tank_enemy_size1_yellow1", "tank_enemy_size1_green1",
         "tank_enemy_size1_purple1"])
    size = random.randint(15, 45)
    mosh_enemy1 = speed_size(size)
    effect(50, 50)
    enemy1 = sprite.add("battle_city_tanks", x1, y1, coustrume)
    enemy1_speed_x=0
    enemy1_speed_y=0
    sprite.set_height_proportionally(enemy1, size)


def respawn_enemy2():
    global enemy2, mosh_enemy2,enemy2_speed_y,enemy2_speed_x
    sprite.remove(enemy2)
    coustrume = random.choice(
        ["tank_player_size1_white1", "tank_enemy_size1_yellow1", "tank_enemy_size1_green1",
         "tank_enemy_size1_purple1"])
    size = random.randint(15, 45)
    mosh_enemy2 = speed_size(size)
    effect(950, 50)
    enemy2 = sprite.add("battle_city_tanks", x2, y2, coustrume)
    enemy2_speed_x = 0
    enemy2_speed_y = 0
    sprite.set_height_proportionally(enemy2, size)


def respawn_player():
    global player
    sprite.remove(player)
    coustrume = random.choice(
        ["tank_player_size1_white1", "tank_enemy_size1_yellow1", "tank_enemy_size1_green1",
         "tank_enemy_size1_purple1"])
    effect(500, 500)
    player = sprite.add("battle_city_tanks", 500, 500, coustrume)


wrap.world.create_world(1000, 900)
player = None
enemy1 = None
enemy2 = None
respawn_enemy1()
respawn_enemy2()
respawn_player()


def granica(id):
    top = sprite.get_top(id)
    bottom = sprite.get_bottom(id)
    left = sprite.get_left(id)
    right = sprite.get_right(id)
    if left <= 0:
        sprite.move_left_to(id, 0)
    if right >= 1000:
        sprite.move_right_to(id, 1000)
    if top <= 0:
        sprite.move_top_to(id, 0)
    if bottom >= 900:
        sprite.move_bottom_to(id, 900)


enemy1_speed_x = 0
enemy1_speed_y = 0
enemy2_speed_x = 0
enemy2_speed_y = 0
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
        x = -3
        y = 0
    else:
        x = 0
        y = 0

    povorot(player, x, y)
    sprite.move(player, x, y)
    granica(player)


@wrap.always(2000)
def bot_action():
    global enemy2_speed_x, enemy2_speed_y, enemy1_speed_x, enemy1_speed_y
    enemy2_speed_x, enemy2_speed_y = vibor_bot(enemy2, mosh_enemy2)
    enemy1_speed_x, enemy1_speed_y = vibor_bot(enemy1, mosh_enemy1)



def shot(nomer):
    global bul
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

    bullet_list.append(bul)

@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def shot_player():
    shot(player)


@wrap.always(100)
def move_bullet():
    for n_bul in bullet_list:
        sprite.move_at_angle_dir(n_bul,25)


@wrap.always(20)
def bot_move():
    sprite.move(enemy2, enemy2_speed_x, enemy2_speed_y)
    granica(enemy2)

    sprite.move(enemy1, enemy1_speed_x, enemy1_speed_y)
    granica(enemy1)


def vibor_bot(nomer_bota, mosh):
    or_or = random.choice(["x", "y", "stand", "shot"])
    p_m = random.choice([mosh, -mosh])

    if or_or == "x":
        enemy_x = p_m
        enemy_y = 0
    elif or_or == "y":
        enemy_x = 0
        enemy_y = p_m
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
    global bullet_list
    global bul, enemy1
    for n_bul in bullet_list:
        to = wrap.sprite.is_collide_any_sprite(n_bul, [enemy1, enemy2, player])
        if to != None:
            sprite.remove(n_bul)
            bullet_list.remove(n_bul)
            if to == enemy1:
                respawn_enemy1()
            if to == enemy2:
                respawn_enemy2()
            if to == player:
                respawn_player()
