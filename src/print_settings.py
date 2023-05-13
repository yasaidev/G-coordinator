import sys
import configparser
from kinematics.kin_base import *
from kinematics.kin_cartesian import *
from kinematics.kin_nozzle_tilt import *
from kinematics.kin_bed_tilt_bc import *
from kinematics.kin_bed_rotate import *

ROUTE_PATH = sys.path[1] if 2 == len(sys.path) else '.' 
CONFIG_PATH = ROUTE_PATH + '/print_setting.ini' 
print_setting = configparser.ConfigParser()
print_setting.read(CONFIG_PATH)

def reload_print_setting():
    global nozzle_diameter, filament_diameter, layer_height, \
        x_origin, y_origin, print_speed, travel_speed, fan_speed, \
        nozzle_temperature, bed_temperature, extrusion_multiplier, \
        retraction, retraction_distance, unretraction_distance, z_hop, z_hop_distance, \
        kin_name, kinematics
    print_setting.read(CONFIG_PATH)
    nozzle_diameter = float(print_setting['nozzle']['nozzle_diameter'])
    filament_diameter = float(print_setting['nozzle']['filament_diameter'])
    layer_height = float(print_setting['layer']['layer_height'])
    x_origin = int(print_setting['origin']['x_origin'])
    y_origin = int(print_setting['origin']['y_origin'])
    print_speed = int(print_setting['speed']['print_speed'])
    travel_speed = int(print_setting['speed']['travel_speed'])
    fan_speed =  int(print_setting['fan_speed']['fan_speed'])
    nozzle_temperature = int(print_setting['temperature']['nozzle_temperature'])
    bed_temperature = int(print_setting['temperature']['bed_temperature'])
    extrusion_multiplier = float(print_setting['extrusion_option']['extrusion_multiplier'])
    retraction = print_setting.getboolean('travel_option','retraction')
    retraction_distance = float(print_setting['travel_option']['retraction_distance'])
    unretraction_distance = float(print_setting['travel_option']['unretraction_distance'])
    z_hop = print_setting.getboolean('travel_option','z_hop')
    z_hop_distance = float(print_setting['travel_option']['z_hop_distance'])
    kin_name = print_setting['kinematics']['kin_name']
    if kin_name == 'Cartesian':
        kinematics = Cartesian(print_setting)
    elif kin_name == 'NozzleTilt':
        kinematics = NozzleTilt(print_setting)
    elif kin_name == 'BedTiltBC':
        kinematics = BedTiltBC(print_setting)
    elif kin_name == 'BedRotate':
        kinematics = BedRotate(print_setting)
    else:
        kinematics = Kinematics(print_setting)

nozzle_diameter = None
filament_diameter = None
layer_height = None
x_origin = None
y_origin = None
print_speed = None
travel_speed = None
fan_speed =  None
nozzle_temperature = None
bed_temperature = None
extrusion_multiplier = None
retraction = None
retraction_distance = None
unretraction_distance = None
z_hop = None
z_hop_distance = None
kin_name = None
kinematics = None

reload_print_setting()