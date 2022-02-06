from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController 
app = Ursina()
Entity(model="Ship.obj",texture="texture.png",collider="box",double_sided=True)
for x in range(20):
    for z in range(20):
        Entity(model="cube",collider="box",color=color.white,double_sided=True)
def input(self):
    if held_keys["escape"]:
        quit()
player = FirstPersonController()
app.run()