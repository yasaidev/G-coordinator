import numpy as np
import math
from path_generator import *

'''
NOZZLE = 0.8
LAYER = 0.7
Print_speed = 700
Ext_multiplier = 1.4
'''

LAYER=100
base_rad = 50




def object_modeling():
    full_object=[]
    for height in range(LAYER):
        arg = np.linspace(0, np.pi*2,203)
        amp = 2
        rad = base_rad+amp*np.sin(arg*50.5+np.pi*height) 
        x = rad*np.cos(arg )
        y = rad*np.sin(arg )
        z = np.linspace(height*0.7,(height+1)*0.7,203)
        wave_wall = Path(x, y, z)
        full_object.append(wave_wall)

        if height <2:
            arg = np.linspace(0, np.pi*2,401)
            rad = base_rad-2
            x = rad*np.cos(arg )
            y = rad*np.sin(arg )
            z = np.full_like(arg, height*0.7+0.7)
            inner_wall = Path(x, y, z)
            full_object.append(inner_wall)
            bottom = Transform.fill(inner_wall, offset = -0.4, infill_distance = 1, angle = np.pi/4 + np.pi/2 *height)
            full_object.append(bottom)

            
            
            


        
        

    return full_object

