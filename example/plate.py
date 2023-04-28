import numpy as np
from path_generator import *
import print_settings

nozzle = print_settings.nozzle_diameter
thickness = print_settings.layer_height

LAYER = 2
def object_modeling():
    full_object=[]
    for height in range(LAYER):
        x = np.array([100,-100,-100,100,100], dtype = float)
        y = np.array([100,100,-100,-100,100], dtype = float)
        z = np.full_like(x, (height+1)*thickness)
        wall = Path(x, y, z)
        infill = Transform.fill(wall, offset = - nozzle , infill_distance = nozzle , angle = np.pi/4 + np.pi/2 *height)
        if height == 0:
            wall.print_speed = 500
            infill.print_speed = 500
        full_object.append(wall)
        full_object.append(infill)
        
      
    return full_object