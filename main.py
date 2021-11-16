import time
import wrap, random, tank, bullet
from wrap import sprite


bullet_list = []


def speed_size(size):
    if size < 20:
        mosh = 4
    elif size > 35:
        mosh = 1
    else:
        mosh = 2
    return mosh


def respawn_player():
    global player
    sprite.remove(player)
    coustrume = random.choice(
        ["tank_player_size1_white1", "tank_enemy_size1_yellow1", "tank_enemy_size1_green1",
         "tank_enemy_size1_purple1"])
    player=tank.create_tank(500,500,coustrume,None)
    tank.effect(500, 500)



def respawn_enemy1():
    global enemy1, mosh_enemy1, enemy1_speed_y, enemy1_speed_x
    sprite.remove(enemy1)
    coustrume = random.choice(
        ["tank_player_size1_white1", "tank_enemy_size1_yellow1", "tank_enemy_size1_green1",
         "tank_enemy_size1_purple1"])
    size = random.randint(20, 40)
    mosh_enemy1 = speed_size(size)
    tank.effect(50, 50)
    enemy1 = tank.create_tank(50,50,coustrume,mosh_enemy1)
    enemy1_speed_x = 0
    enemy1_speed_y = 0
    sprite.set_height_proportionally(enemy1, size)


def respawn_enemy2():
    global enemy2, mosh_enemy2, enemy2_speed_y, enemy2_speed_x
    sprite.remove(enemy2)
    coustrume = random.choice(
        ["tank_player_size1_white1", "tank_enemy_size1_yellow1", "tank_enemy_size1_green1",
         "tank_enemy_size1_purple1"])
    size = random.randint(20, 40)
    mosh_enemy2 = speed_size(size)
    tank.effect(950, 50)
    enemy2 = tank.create_tank(950,50,coustrume,mosh_enemy2)
    enemy2_speed_x = 0
    enemy2_speed_y = 0
    sprite.set_height_proportionally(enemy2, size)


wrap.world.create_world(1000, 900)
player = None
enemy1 = None
enemy2 = None
respawn_enemy1()
respawn_enemy2()
respawn_player()

enemy1_speed_x = 0
enemy1_speed_y = 0
enemy2_speed_x = 0
enemy2_speed_y = 0
top_enemy1 = 0
bottom_enemy1 = 1000
left_enemy1 = 0
right_enemy1 = 1000
top_enemy2 = 0
bottom_enemy2 = 1000
left_enemy2 = 0
right_enemy2 = 1000

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

    tank.povorot(player, x, y)
    sprite.move(player["id"], x, y)
    tank.granica(player, 0, 1000, 0, 900)


@wrap.always(100)
def bot_action():
    global enemy2_speed_x, enemy2_speed_y, enemy1_speed_x, enemy1_speed_y, top_enemy1, bottom_enemy1, left_enemy1, right_enemy1, top_enemy2, bottom_enemy2, left_enemy2, right_enemy2
    # enemy2_speed_x, enemy2_speed_y, top_enemy2, bottom_enemy2, left_enemy2, right_enemy2 = tank.vibor_bot(enemy2,
    #                                                                                                       mosh_enemy2,
    #                                                                                                       bullet_list,
    #                                                                                                       player["id"], 0,
    #                                                                                                       900, 0, 1000)
    # enemy1_speed_x, enemy1_speed_y, top_enemy1, bottom_enemy1, left_enemy1, right_enemy1 = tank.vibor_bot(enemy1,
    #                                                                                                       mosh_enemy1,
    #                                                                                                       bullet_list,
    #                                                                                                       player["id"], 0,
    #                                                                                                       900, 0, 1000)


@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def shot_player():
    bullet.shot(player["id"], bullet_list)


@wrap.always(100)
def move_bullet():
    for n_bul in bullet_list:
        sprite.move_at_angle_dir(n_bul["bullet"], 25)
    bullet.proverka_granici_puli(bullet_list)


@wrap.always(20)
def bot_move():
    sprite.move(enemy2, enemy2_speed_x, enemy2_speed_y)
    #tank.granica(enemy2, left_enemy2, right_enemy2, top_enemy2, bottom_enemy2)

    # sprite.move(enemy1, enemy1_speed_x, enemy1_speed_y)
    # tank.granica(enemy1, 0, 1000, 0, 900)


@wrap.always(10)
def colizia_bullet():
    global bullet_list
    global bul, enemy1
    for n_bul in bullet_list:
        to = wrap.sprite.is_collide_any_sprite(n_bul["bullet"], [enemy1, enemy2, player["id"]])
        if to != None:
            sprite.remove(n_bul["bullet"])
            bullet_list.remove(n_bul)
            if to == enemy1:
                respawn_enemy1()
            if to == enemy2:
                respawn_enemy2()
            if to == player:
                tank.respawn_player()
