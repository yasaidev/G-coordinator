import numpy as np
import math
import print_settings 
from path_generator import *
from infill_generator import *

LAYER =400
nozzle = print

def object_modeling():
    full_object=[]
    for height in range(LAYER):
        arg = np.linspace(0, np.pi*2,100)
        rad = math.sqrt(50**2 - (height * 0.2-30)**2)
        x = rad*np.cos(arg)
        y = rad*np.sin(arg)
        z = np.full_like(arg, height*print_settings.layer_height+0.2)
        wall = Path(x, y, z)
        outer_wall = Transform.offset(wall, 0.4)
        infill = gyroid_infill(wall, density = 0.6)
        full_object.append(infill)



    return full_object

