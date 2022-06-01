#####################################
# Respect Is Everything Milestone 2 #
#####################################

from ursina import *

app = Ursina()

window.title = 'Respect Is Everything'  # The window title
window.borderless = False               # Show a border
window.fullscreen = False               # Do not go Fullscreen
window.exit_button.visible = False      # Do not show the in-game red X that loses the window
window.fps_counter.enabled = True       # Show the FPS (Frames per second) counter


# P