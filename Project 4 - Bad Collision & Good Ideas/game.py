#####################################
# Respect Is Everything Milestone 2 #
#####################################

from ursina import *
from geometry import *
import time

app = Ursina()

window.title = 'Respect Is Everything'  # The window title
window.borderless = False               # Show a border
window.fullscreen = False               # Do not go Fullscreen
window.exit_button.visible = False      # Do not show the in-game red X that loses the window
window.fps_counter.enabled = True       # Show the FPS (Frames per second) counter

# Calls functions from geometry.py
generateSkybox()
generateGeometry()

# Player
#playerCollider = Entity(model='cube', color=color.blue, scale_x=6, scale_y=6, scale_z=0, position=(65,120,-1), collider='box')
player = Entity(position=(100,100,-1), scale_x=6, scale_y=6)
#man = Animation("assets\walking", parent = player, autoplay=False)
playerAnimator = Animator( animations = {
  'idle': Entity(model='quad',parent=player, scale=0.75,texture='assets\walking_0', tag='player'),
  'walking': Animation("assets\walking", parent = player, autoplay=False),
})
player.collider = 'box'
player.runspeed = 0.1

def deathByFalling():
  if player.x > 200 or player.x < 0 or player.y > 200 or player.y < 0:
    player.x = 100
    player.y = 100
    

# Camera Script / Setup
camera.fov = 85

follow = SmoothFollow(target=player, offset=[0,0,-65], speed=8, rotation_speed=0, rotation_offset=(0,0,0))
camera.add_script(follow)

# On Frame
def update():
    # Debug Stuff
    #if player.intersects(playerCollider).hit:
    #    print("test")

    #print(player.x,player.y)
    if held_keys['9']:
      camera.fov = 85
      player.runspeed = 0.1
    if held_keys['8']:
      camera.fov = 160
      player.runspeed = 0.2

    # Player Animation Cycle
    if held_keys['w'] or held_keys['a'] or held_keys['s'] or held_keys['d']:
      player.y += held_keys['w'] * 2 * time.dt
      player.y -= held_keys['s'] * 2 * time.dt
      player.x -= held_keys['a'] * 2 * time.dt
      player.x += held_keys['d'] * 2 * time.dt
      playerAnimator.state = 'walking'
    else:
      playerAnimator.state = 'idle'

    deathByFalling()

    # Player Model Rotation Control Code
    if held_keys['s']:
      player.rotation_z = 180
    if held_keys['w']:
      player.rotation_z = 0
    if held_keys['d']:
      player.rotation_z = 90
    if held_keys['a']:
      player.rotation_z = 270
    if held_keys['w'] and held_keys['d']:
      player.rotation_z = 45
    if held_keys['w'] and held_keys['a']:
      player.rotation_z = 315
    if held_keys['a'] and held_keys['s']:
      player.rotation_z = 225
    if held_keys['d'] and held_keys['s']:
      player.rotation_z = 135
    
    # Player Movement Keymap
    if held_keys['shift']:
      player.runspeed = 0.2
    else:
      player.runspeed = 0.1


    player.x += held_keys['d'] * player.runspeed
    player.x -= held_keys['a'] * player.runspeed
    player.y += held_keys['w'] * player.runspeed
    player.y -= held_keys['s'] * player.runspeed


app.run()
