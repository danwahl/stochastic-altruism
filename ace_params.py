# -*- coding: utf-8 -*-
"""
Created on Sun Nov 06 22:39:42 2016

@author: dan

AEPY = average animal equivalents consumed per person per year
AYLA = average life years per animal
PED = price elasticity of demand
PES = price elasticity of supply
CPX = cost per leaflet/click
PLX = average product limiters per leaflet/click
"""

import json

if __name__ == '__main__':
    # animals
    beef = {'AEPY': {'dist': 'norm', 'loc': 0.118, 'scale': 0.004}, \
        'AYLA': {'dist': 'norm', 'loc': 1.25, 'scale': 0.04}, \
        'PED': {'dist': 'norm', 'loc': -0.610, 'scale': 0.215}, \
        'PES': {'dist': 'norm', 'loc': 1.252, 'scale': 0.451}, \
        'brain': {'dist': 'const', 'val': 430}, \
        'body': {'dist': 'const', 'val': 470e3}, \
        'natural': {'dist': 'lognorm', 'shape': 22.5, 'scale': 2.5}, \
        'weight': {'dist': 'const', 'val': 0.4}
    }
    
    dairy = {'AEPY': {'dist': 'norm', 'loc': 0.0043, 'scale': 0.0005}, \
        'AYLA': {'dist': 'norm', 'loc': 4.50, 'scale': 0.25}, \
        'PED': {'dist': 'norm', 'loc': -1.470, 'scale': 0.430}, \
        'PES': {'dist': 'norm', 'loc': 0.650, 'scale': 0.510}, \
        'brain': {'dist': 'const', 'val': 430}, \
        'body': {'dist': 'const', 'val': 470e3}, \
        'natural': {'dist': 'lognorm', 'shape': 22.5, 'scale': 2.5}, \
        'weight': {'dist': 'const', 'val': 0.72}
    }
    
    pork = {'AEPY': {'dist': 'norm', 'loc': 0.373, 'scale': 0.018}, \
        'AYLA': {'dist': 'norm', 'loc': 0.5, 'scale': 0.0417}, \
        'PED': {'dist': 'norm', 'loc': -0.647, 'scale': 0.116}, \
        'PES': {'dist': 'norm', 'loc': 2.1035, 'scale': 1.0483}, \
        'brain': {'dist': 'const', 'val': 180}, \
        'body': {'dist': 'const', 'val': 70e3}, \
        'natural': {'dist': 'lognorm', 'shape': 11.0, 'scale': 1.0}, \
        'weight': {'dist': 'const', 'val': 0.72}
    }
    
    chicken = {'AEPY': {'dist': 'norm', 'loc': 24.65, 'scale': 0.19}, \
        'AYLA': {'dist': 'norm', 'loc': 0.1245, 'scale': 0.0048}, \
        'PED': {'dist': 'norm', 'loc': -0.14, 'scale': 0.07}, \
        'PES': {'dist': 'norm', 'loc': 0.2355, 'scale': 0.0818}, \
        'brain': {'dist': 'uniform', 'loc': 2.6, 'scale': 4.4}, \
        'body': {'dist': 'const', 'val': 2.63e3}, \
        'natural': {'dist': 'lognorm', 'shape': 7.0, 'scale': 2.0}, \
        'weight': {'dist': 'const', 'val': 0.72}
    }
    
    eggs = {'AEPY': {'dist': 'norm', 'loc': 1.7443, 'scale': 0.2272}, \
        'AYLA': {'dist': 'norm', 'loc': 1.27, 'scale': 0.14}, \
        'PED': {'dist': 'norm', 'loc': -0.225, 'scale': 0.0375}, \
        'PES': {'dist': 'norm', 'loc': 1.0, 'scale': 0.25}, \
        'brain': {'dist': 'uniform', 'loc': 2.6, 'scale': (4.4 - 2.6)}, \
        'body': {'dist': 'const', 'val': 2.63e3}, \
        'natural': {'dist': 'lognorm', 'shape': 10.0, 'scale': 2.0}, \
        'weight': {'dist': 'const', 'val': 1.0}
    }
    '''   
    turkey = {'AEPY': {'dist': 'norm', 'loc': 0.779, 'scale': 0.014}, \
        'AYLA': {'dist': 'norm', 'loc': 0.3127, 'scale': 0.0136}, \
        'PED': {'dist': 'norm', 'loc': -0.63, 'scale': 0.27}, \
        'PES': {'dist': 'norm', 'loc': 0.2453, 'scale': 0.1226}
    }
    
    fish = {'AEPY': {'dist': 'norm', 'loc': 2.895, 'scale': 0.4125}, \
        'AYLA': {'dist': 'norm', 'loc': 1.5, 'scale': 0.25}, \
        'PED': {'dist': 'norm', 'loc': -1.05, 'scale': 0.48}, \
        'PES': {'dist': 'norm', 'loc': 0.8, 'scale': 0.265}, \
        'brain': {'dist': 'const', 'val': 430}, \
        'body': {'dist': 'const', 'val': 470e3}, \
        'weight': {'dist': 'const', 'val': 0.36}
    }
    
    shellfish = {'AEPY': {'dist': 'norm', 'loc': 118.0, 'scale': 7.08}, \
        'AYLA': {'dist': 'norm', 'loc': 0.2055, 'scale': 0.1028}, \
        'PED': {'dist': 'norm', 'loc': -2.15, 'scale': 0.36}, \
        'PES': {'dist': 'norm', 'loc': 0.98, 'scale': 0.46}, \
        'brain': {'dist': 'const', 'val': 430}, \
        'body': {'dist': 'const', 'val': 470e3}
    }
    '''   
    # donations
    leaflets = {'AYL': {'dist': 'norm', 'loc': 7.03, 'scale': 0.8}, \
        'CPX': {'dist': 'norm', 'loc': 0.35, 'scale': 0.0305}, \
        'meat': {'dist': 'norm', 'loc': 0.011, 'scale': 0.0048}, \
        'dairy': {'dist': 'norm', 'loc': 0.0071, 'scale': 0.0038}, \
        'eggs': {'dist': 'norm', 'loc': 0.0051, 'scale': 0.0032}
    }
    
    ads = {'AYL': leaflets['AYL'], \
        'CPX': {'dist': 'norm', 'loc': 0.25, 'scale': 0.0625}, \
        'meat': {'dist': 'norm', 'loc': 0.007, 'scale': 0.0049}, \
        'dairy': {'dist': 'norm', 'loc': 0.0, 'scale': 0.0}, \
        'eggs': {'dist': 'norm', 'loc': 0.0, 'scale': 0.}
    }
    
    # parameters
    params = {'Animals': {'Beef': beef, 'Dairy': dairy, 'Pork': pork, \
        'Chicken': chicken, 'Eggs': eggs},
        'Donations': {'Leaflets': leaflets, 'Ads': ads}
    }
    
    with open('ace_params.json', 'w') as fp:
        json.dump(params, fp, indent=4)