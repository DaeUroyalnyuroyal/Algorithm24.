from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from direct.actor.Actor import Actor

app = Ursina()
mouse.visible = False

# 중앙 벽, 바닥, 천장을 생성
main_floor = Entity(model='cube', position=(0, 0, 0), scale=(10, 1, 100), color=color.gray, collider='box')
main_ceiling = Entity(model='cube', position=(0, 10, 0), scale=(10, 1, 100), color=color.gray, collider='box',texture='wall.jpg', texture_scale=(16, 10))
main_left_wall = Entity(model='cube', position=(-5, 5, -5), scale=(1, 10, 110), collider='box', texture='wall.jpg', texture_scale=(16, 10))
main_right_wall = Entity(model='cube', position=(5, 5, 5), scale=(1, 10, 110), collider='box', texture='wall.jpg', texture_scale=(16, 10))

# tiles
for i in range(-90, 90):
    tiles = Entity(model='cube', position=(0, 0.5, i*0.5), scale=(0.5, 0, 0.5), texture='yellow_tile.jpg')

# 앞쪽
front_floor = Entity(model='cube', position=(-25, 0, 55), scale=(60, 1, 10), color=color.gray, collider='box')
front_ceiling = Entity(model='cube', position=(-25, 10, 55), scale=(60, 1, 10), color=color.gray, collider='box', texture='wall.jpg', texture_scale=(3, 10))
front_left_wall = Entity(model='cube', position=(-30, 5, 50), scale=(50, 10, 1), collider='box', texture='wall.jpg', texture_scale=(16, 10))
front_right_wall = Entity(model='cube', position=(-20, 5, 60), scale=(50, 10, 1), collider='box', texture='wall.jpg', texture_scale=(16, 10))

front_floor_2 = Entity(model='cube', position=(-50, 0, 80), scale=(10, 1, 60), color=color.gray, collider='box')
front_ceiling_2 = Entity(model='cube', position=(-50, 10, 80), scale=(10, 1, 60), color=color.gray, collider='box', texture='wall.jpg', texture_scale=(3, 10))
front_left_wall_2 = Entity(model='cube', position=(-55, 5, 75), scale=(1, 10, 50), collider='box', texture='wall.jpg', texture_scale=(16, 10))
front_right_wall_2 = Entity(model='cube', position=(-45, 5, 85), scale=(1, 10, 50), collider='box', texture='wall.jpg', texture_scale=(16, 10))

# 뒷쪽
back_floor = Entity(model='cube', position=(25, 0, -55), scale=(60, 1, 10), color=color.gray, collider='box')
back_ceiling = Entity(model='cube', position=(25, 10, -55), scale=(60, 1, 10), color=color.gray, collider='box', texture='wall.jpg', texture_scale=(3, 10))
back_left_wall = Entity(model='cube', position=(30, 5, -50), scale=(50, 10, 1), collider='box', texture='wall.jpg', texture_scale=(16, 10))
back_right_wall = Entity(model='cube', position=(20, 5, -60), scale=(50, 10, 1), collider='box', texture='wall.jpg', texture_scale=(16, 10))

back_floor_2 = Entity(model='cube', position=(50, 0, -80), scale=(10, 1, 60), color=color.gray, collider='box')
back_ceiling_2 = Entity(model='cube', position=(50, 10, -80), scale=(10, 1, 60), color=color.gray, collider='box', texture='wall.jpg', texture_scale=(3, 10))
back_left_wall_2 = Entity(model='cube', position=(55, 5, -75), scale=(1, 10, 50), collider='box', texture='wall.jpg', texture_scale=(16, 10))
back_right_wall_2 = Entity(model='cube', position=(45, 5, -85), scale=(1, 10, 50), collider='box', texture='wall.jpg', texture_scale=(16, 10))

# 표지판
sign_ceiling = Entity(model='cube', position=(0, 9, 25), scale=(5.2, 1, 0.1), texture='exit_8_ceiling.jpg')
sign_wall_front = Entity(model='cube', position=(-54.4, 4.5, 55), scale=(0.1, 3.8, 2), texture='exit_0_wall.jpg')
sign_wall_back = Entity(model='cube', position=(-4.4, 4.5, -55), scale=(0.1, 3.8, 2), texture='exit_0_wall.jpg')

# 1인칭 플레이어
player = FirstPersonController()
player.position = (23.0949, 0.5, -54.972)
player.cursor.visible = False
player.gravity = 0.5
player.speed = 15

def update():
    count = 0
    if player.position.x < -25 and player.position.z > 50:
        player.set_position((
           50 + player.position.x,
           player.position.y,
           -110+ player.position.z))
    elif player.position > 25 and player.position.z < -50:
        player.set_position ((
            -50 + player.position.x,
            player.position.y,
            110+ player.position.z))

app.run()