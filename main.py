import time
import wrap, random, tank, bullet
from wrap import sprite

bullet_list = []


def speed_size(size):
    if size < 21:
        mosh = 4
    elif size > 35:
        mosh = 1
    else:
        mosh = 2
    return mosh


def respawn_player():
    global player
    if player != None:
        tank.remove(player)
    player = tank.create_tank(500, 500, 3, 32)


def respawn_enemy1():
    global enemy1
    if enemy1 != None:
        tank.remove(enemy1)
    size = random.randint(20, 40)
    mosh_enemy1 = speed_size(size)
    enemy1 = tank.create_tank(50, 50, mosh_enemy1, size)


def respawn_enemy2():
    global enemy2
    if enemy2 != None:
        tank.remove(enemy2)
    size = random.randint(20, 40)
    mosh_enemy2 = speed_size(size)
    enemy2 = tank.create_tank(950, 50, mosh_enemy2, size)


wrap.world.create_world(1000, 900)
player = None
enemy1 = None
enemy2 = None
respawn_enemy1()
respawn_enemy2()
respawn_player()



@wrap.on_key_always(wrap.K_w, wrap.K_s, wrap.K_d, wrap.K_a)
def move(keys):
    if wrap.K_w in keys:
        tank.move_up(player)
    elif wrap.K_s in keys:
        tank.move_down(player)
    elif wrap.K_d in keys:
        tank.move_right(player)
    elif wrap.K_a in keys:
        tank.move_left(player)


@wrap.always(1000)
def bot_action():
    tank.vibor_bot(enemy2, bullet_list, player["id"], 0, 900, 0, 1000)
    tank.vibor_bot(enemy1, bullet_list, player["id"], 0, 900, 0, 1000)


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
    tank.move_bot(enemy2)
 #   sprite.move(enemy1["id"], enemy1_speed_x, enemy1_speed_y)
  #  tank.granica(enemy1, 0, 1000, 0, 900)


@wrap.always(10)
def colizia_bullet():
    global bullet_list
    global bul, enemy1
    for n_bul in bullet_list:
        to = wrap.sprite.is_collide_any_sprite(n_bul["bullet"], [enemy1["id"], enemy2["id"], player["id"]])
        if to != None:
            sprite.remove(n_bul["bullet"])
            bullet_list.remove(n_bul)
            if to == enemy1["id"]:
                respawn_enemy1()
            if to == enemy2["id"]:
                respawn_enemy2()
            if to == player["id"]:
                respawn_player()
