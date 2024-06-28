from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# 바닥
main_floor = Entity(model='cube', position=(0, 0, 0), scale=(10, 1, 100), color=color.gray, collider='box')

# 천장
main_ceiling = Entity(model='cube', position=(0, 10, 0), scale=(10, 1, 100), color=color.gray, collider='box')

# 왼쪽 벽
main_left_wall = Entity(model='cube', position=(-5, 5, 0), scale=(1, 10, 100), color=color.white, collider='box')

# 오른쪽 벽
main_right_wall = Entity(model='cube', position=(5, 5, 0), scale=(1, 10, 100), color=color.white, collider='box')

# 플레이어
player = FirstPersonController()
player.cursor = False
player.gravity = 0.5
player.speed = 15

app.run()