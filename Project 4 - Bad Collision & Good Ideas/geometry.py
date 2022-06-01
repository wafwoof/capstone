#################
# Geometry File #
#################

from ursina import *

if __name__ == "__main__":
    print("\n!!! DO NOT RUN THIS FILE !!! PLEASE LAUNCH game.py DIRECTLY -- THIS IS FOR DEBUG ONLY !!!\n")
    exec(open('game.py').read()) # DEBUG ONLY -- REMOVE UPON RELEASE
    #exit()
else:
    def generateSkybox():
        sky_texture = load_texture('assets/skybox.png')

        class Sky(Entity):
            def __init__(self):
                super().__init__(
                    parent = scene,
                    rotation_x = 40,
                    position = (100,100,0),
                    model = 'sphere',
                    texture = sky_texture,
                    scale = 500,
                    double_sided = True)

        sky = Sky()


    def generateGeometry():
        #Color Palette
        color.player = rgb(0,0,200)
        color.sidewalk = rgb(101,103,112)
        color.road = rgb(111,99,119)
        color.building = rgb(143,145,146)
        color.park = rgb(34,139,34)

        # ROADS
        # The Four Roads
        southRoad = Entity(model='cube', texture='assets/horizontalRoad.png', scale_x=200, scale_y=10, scale_z=0, position=(100,5,0))
        westRoad = Entity(model='cube', texture='assets/verticalRoad.png', scale_x=10, scale_y=200, scale_z=0, position=(5,100,0))
        northRoad = Entity(model='cube', texture='assets/horizontalRoad.png', scale_x=200, scale_y=10, scale_z=0, position=(100,195,0))
        eastRoad = Entity(model='cube', texture='assets/verticalRoad.png', scale_x=10, scale_y=200, scale_z=0, position=(195,100,0))
        # 1st Road
        westRoad = Entity(model='cube', texture='assets/verticalRoad.png', scale_x=10, scale_y=200, scale_z=0, position=(55,100,0))
        # Main Road
        southRoad = Entity(model='cube', texture='assets/horizontalRoad.png', scale_x=200, scale_y=10, scale_z=0, position=(100,55,0))
        # west Block Road
        southRoad = Entity(model='cube', texture='assets/horizontalRoadShort.png', scale_x=40, scale_y=10, scale_z=0, position=(30,125,0))
        # east Block Ave
        southRoad = Entity(model='cube', texture='assets/verticalRoadShort.png', scale_x=10, scale_y=40, scale_z=0, position=(145,30,0))
        # northie Road
        northieRoad = Entity(model='cube', texture='assets/horizontalRoad130x10.png', scale_x=130, scale_y=10, scale_z=0, position=(125,145,0))
        # central Road
        centralRoad = Entity(model='cube', texture='assets/verticalRoad10x80.png', scale_x=10, scale_y=80, scale_z=0, position=(145,100,0))

        # BUILDINGS & Stuff
        southWestApartmentBlock = Entity(model='cube', color=color.sidewalk, scale_x=40, scale_y=40, scale_z=0, position=(30,30,0))
        southWestApartmentTower = Entity(model='cube', color=color.building, scale_x=30, scale_y=30, scale_z=30, position=(30,30,0), collider='box')

        eastPlazaBlock = Entity(model='cube', color=color.sidewalk, scale_x=40, scale_y=60, scale_z=0, position=(30,90,0))
        eastPlazaTower = Entity(model='cube', color=color.building, scale_x=30, scale_y=50, scale_z=40, position=(30,90,0), collider='box')
        eastPlazaTowerPoint = Entity(model='cube', color=rgb(153,155,156), scale_x=3, scale_y=3, scale_z=65, position=(30,90,0), collider='box')

        southStripBlock = Entity(model='cube', color=color.sidewalk, scale_x=80, scale_y=40, scale_z=0, position=(100,30,0))
        southStripTower1 = Entity(model='cube', color=color.building, scale_x=30, scale_y=30, scale_z=35, position=(80,30,0), collider='box')
        southStripTower2 = Entity(model='cube', color=color.building, scale_x=30, scale_y=30, scale_z=30, position=(120,30,0), collider='box')

        northWestPark = Entity(model='cube', texture='assets/park.png', scale_x=40, scale_y=60, scale_z=0, position=(30,160,0))

        southEastBlock = Entity(model='cube', color=color.sidewalk, scale_x=40, scale_y=40, scale_z=0, position=(170,30,0))
        southEastTower = Entity(model='cube', color=color.building, scale_x=30, scale_y=30, scale_z=15, position=(170,30,0), collider='box')

        northBlock = Entity(model='cube', color=color.sidewalk, scale_x=130, scale_y=40, scale_z=0, position=(125,170,0))
        northTower1 = Entity(model='cube', color=color.building, scale_x=40, scale_y=30, scale_z=25, position=(85,170,0), collider='box')
        northLiquorStore = Entity(model='cube', color=color.building, scale_x=30, scale_y=30, scale_z=15, position=(125,170,0), collider='box')
        northTower2 = Entity(model='cube', color=color.building, scale_x=40, scale_y=30, scale_z=25, position=(165,170,0), collider='box')

        citySquareBlock = Entity(model='cube', color=color.sidewalk, scale_x=80, scale_y=80, scale_z=0, position=(100,100,0))
        citySquareTower1 = Entity(model='cube', color=color.building, scale_x=30, scale_y=30, scale_z=40, position=(80,80,0), collider='box')
        citySquareTower2 = Entity(model='cube', color=color.building, scale_x=30, scale_y=30, scale_z=35, position=(120,80,0), collider='box')
        #citySquareTower3 = Entity(model='cube', color=color.building, scale_x=30, scale_y=30, scale_z=45, position=(80,120,0), collider='box')
        citySquareTower4 = Entity(model='cube', color=color.building, scale_x=30, scale_y=30, scale_z=55, position=(120,120,0), collider='box')

        eastBlock = Entity(model='cube', color=color.sidewalk, scale_x=40, scale_y=80, scale_z=0, position=(170,100,0))
        eastBlockTower = Entity(model='cube', color=color.building, scale_x=30, scale_y=30, scale_z=25, position=(170,120,0), collider='box')

