from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from direct.actor.Actor import Actor

app = Ursina()
mouse.visible = False

# 중앙 벽, 바닥, 천장을 생성
main_floor = Entity(model='cube', position=(0, 0, 0), scale=(20, 1, 100), color=color.gray, collider='box')#바닥
main_ceiling = Entity(model='cube', position=(0, 10, 0), scale=(20, 1, 100), color=color.gray, collider='box',texture='wall.jpg', texture_scale=(16, 10))#천장
main_left_wall = Entity(model='cube', position=(-5, 5, -5), scale=(1, 10, 110), collider='box', texture='wall.jpg', texture_scale=(16, 10))#벽
main_right_wall = Entity(model='cube', position=(10, 5, 5), scale=(1, 10, 110), collider='box', texture='wall.jpg', texture_scale=(16, 10))

# tiles
for i in range(-90, 90):
    tiles = Entity(model='cube', position=(0, 0.5, i*0.5), scale=(0.5, 0, 0.5), texture='yellow_tile.jpg')

# 뒷쪽 (앞뒤넓이, 높이, 양옆넓이)
front_floor = Entity(model='cube', position=(3, 0, 55), scale=(15, 1, 10), color=color.gray, collider='box')#바닥
front_ceiling = Entity(model='cube', position=(3, 10, 55), scale=(15, 1, 10), color=color.gray, collider='box', texture='wall.jpg', texture_scale=(3, 10)) #천장
front_ceiling = Entity(model='cube', position=(-3, 13, 55), scale=(3, 6, 10), color=color.gray, collider='box', texture='wall.jpg', texture_scale=(3, 10)) #천장
front_floor = Entity(model='cube', position=(-6, 1, 55), scale=(3, 1, 9), color=color.gray, collider='box')
front_floor = Entity(model='cube', position=(-9, 2, 55), scale=(3, 1, 10), color=color.gray, collider='box')
front_floor = Entity(model='cube', position=(-12, 3, 55), scale=(3, 1, 10), color=color.gray, collider='box')
front_floor = Entity(model='cube', position=(-15, 4, 55), scale=(3, 1, 10), color=color.gray, collider='box')
front_floor = Entity(model='cube', position=(-18, 5, 55), scale=(3, 1, 10), color=color.gray, collider='box')
front_floor = Entity(model='cube', position=(-21, 6, 55), scale=(3, 1, 10), color=color.gray, collider='box') #계단
front_ceiling = Entity(model='cube', position=(-20, 16, 55), scale=(60, 1, 10), color=color.gray, collider='box', texture='wall.jpg', texture_scale=(3, 10))#천장
front_left_wall = Entity(model='cube', position=(-30, 5, 50), scale=(51, 22, 1), collider='box', texture='wall.jpg', texture_scale=(16, 10))#벽
front_right_wall = Entity(model='cube', position=(-15, 5, 60), scale=(61, 22, 1), collider='box', texture='wall.jpg', texture_scale=(16, 10))
back_floor = Entity(model='cube', position=(-40, 6, 55), scale=(40, 1, 10), color=color.gray, collider='box')# 계단위바닥
front_floor_2 = Entity(model='cube', position=(-50, 6, 80), scale=(10, 1, 60), color=color.gray, collider='box')#계단위코너 바닥
front_ceiling_2 = Entity(model='cube', position=(-50, 16, 80), scale=(10, 1, 60), color=color.gray, collider='box', texture='wall.jpg', texture_scale=(3, 10))#천장
front_left_wall_2 = Entity(model='cube', position=(-55, 5, 75), scale=(1, 22, 50), collider='box', texture='wall.jpg', texture_scale=(16, 10))#벽
front_right_wall_2 = Entity(model='cube', position=(-45, 5, 85), scale=(1, 22, 50), collider='box', texture='wall.jpg', texture_scale=(16, 10))

# 앞쪽 (앞뒤넓이, 높이, 양옆넓이)
back_floor = Entity(model='cube', position=(53, -6, -55), scale=(15, 1, 10), color=color.gray, collider='box')#내려가는 계단바닥
front_floor = Entity(model='cube', position=(44, -5, -55), scale=(3, 1, 9), color=color.gray, collider='box')
front_floor = Entity(model='cube', position=(41, -4, -55), scale=(3, 1, 10), color=color.gray, collider='box')
front_floor = Entity(model='cube', position=(38, -3, -55), scale=(3, 1, 10), color=color.gray, collider='box')
front_floor = Entity(model='cube', position=(35, -2, -55), scale=(3, 1, 10), color=color.gray, collider='box')
front_floor = Entity(model='cube', position=(32, -1, -55), scale=(3, 1, 10), color=color.gray, collider='box')
front_floor = Entity(model='cube', position=(29, 0, -55), scale=(3, 1, 10), color=color.gray, collider='box') #계단
back_floor = Entity(model='cube', position=(10, 0, -55), scale=(40, 1, 10), color=color.gray, collider='box')# 계단위바닥
back_left_wall = Entity(model='cube', position=(30, 5, -50), scale=(51, 22, 1), collider='box', texture='wall.jpg', texture_scale=(16, 10))#벽
back_right_wall = Entity(model='cube', position=(20, 5, -60), scale=(51, 22, 1), collider='box', texture='wall.jpg', texture_scale=(16, 10))
front_ceiling = Entity(model='cube', position=(53, 4, -55), scale=(15, 1, 10), color=color.gray, collider='box', texture='wall.jpg', texture_scale=(3, 10)) #천장
front_ceiling = Entity(model='cube', position=(47, 7, -55), scale=(3, 6, 10), color=color.gray, collider='box', texture='wall.jpg', texture_scale=(3, 10)) #천장
front_ceiling = Entity(model='cube', position=(20, 10, -55), scale=(60, 1, 10), color=color.gray, collider='box', texture='wall.jpg', texture_scale=(3, 10))

front_ceiling_2 = Entity(model='cube', position=(50.5, 4, -80), scale=(10, 1, 60), color=color.gray, collider='box', texture='wall.jpg', texture_scale=(3, 10))#천장

back_floor_2 = Entity(model='cube', position=(50, -6, -80), scale=(10, 1, 60), color=color.gray, collider='box')#코너바닥
back_left_wall_2 = Entity(model='cube', position=(55, 5, -75), scale=(1, 22, 50), collider='box', texture='wall.jpg', texture_scale=(16, 10))#벽
back_right_wall_2 = Entity(model='cube', position=(45, 5, -85), scale=(1, 22, 50), collider='box', texture='wall.jpg', texture_scale=(16, 10))


# 표지판
sign_ceiling = Entity(model='cube', position=(0, 9, 25), scale=(5.2, 1, 0.1), texture='exit_8_ceiling.jpg')
sign_wall_front = Entity(model='cube', position=(-54.4, 4.5, 55), scale=(0.1, 3.8, 2), texture='exit_0_wall.jpg')
sign_wall_back = Entity(model='cube', position=(-4.4, 4.5, -55), scale=(0.1, 3.8, 2), texture='exit_0_wall.jpg')


# 1인칭 플레이어
player = FirstPersonController()
#player.position = (23.0949, 0.5, -54.972)
player.position =(-21, 6, 55)
player.cursor.visible = False
player.gravity = 0.5
player.speed = 15

'''def update():
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
            110+ player.position.z))'''

app.run()