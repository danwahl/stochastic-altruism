# -*- coding: utf-8 -*-
"""
Created on Mon Nov 07 21:08:07 2016

@author: dan
"""

import json
import scipy.stats as stats
import numpy as np

import matplotlib.pyplot as plt
plt.style.use('ggplot')

import pandas as pd

HUMAN_EQ = 7.41

def get_rvs(p, n):
    if p['dist'] == 'uniform':
        return stats.uniform.rvs(loc=p['loc'], scale=p['scale'], size=n)
    elif p['dist'] == 'norm':
        return stats.norm.rvs(loc=p['loc'], scale=p['scale'], size=n)
    elif p['dist'] == 'lognorm':
        return stats.lognorm.rvs(p['shape'], scale=p['scale'], size=n)
    elif p['dist'] == 'array':
        return np.random.choice(p['val'], n)
    else:
        return p['val']

def get_input(key, params):
    inputs = {}
    for k in params[key].keys():
        d = {}
        for p in params[key][k].keys():
            d[p] = get_rvs(params[key][k][p], n)
        inputs[k] = d
    return inputs

if __name__ == '__main__':
    n = 1000000
    
    amount = 1000
    #meat = ['Beef', 'Pork', 'Chicken', 'Turkey', 'Fish']
    meat = ['Beef', 'Pork', 'Chicken']
    
    with open('ace_params.json') as fp:    
        params = json.load(fp)
    
    animals = get_input('Animals', params)
    donations = get_input('Donations', params)
    
    for a in animals.keys():
        # eq
        animals[a]['eq'] = animals[a]['brain']/(0.12*np.power(animals[a]['body'], 2.0/3.0))                
        
        # cumulative elasticity factor
        animals[a]['CEF'] = animals[a]['PES']/(animals[a]['PES'] - animals[a]['PED'])
    
        # AEPY*CEF
        animals[a]['X1'] = animals[a]['AEPY']*animals[a]['CEF']*animals[a]['eq']/HUMAN_EQ
        
        # AEPY*CEF*AYLA
        animals[a]['X2'] = animals[a]['X1']*animals[a]['AYLA']
    
    for d in donations.keys():
        # "Sum (AEPY*CEF)
        donations[d]['Y1'] = {
            'meat': sum([animals[a]['X1'] for a in meat]), \
            'dairy': animals['Dairy']['X1'], \
            'eggs': animals['Eggs']['X1']
        }
        
        # Sum(AEPY*CEF*AYLA)
        donations[d]['Y2'] = {
            'meat': sum([animals[a]['X2'] for a in meat]), \
            'dairy': animals['Dairy']['X2'], \
            'eggs': animals['Eggs']['X2']
        }
        
        donations[d]['Z1'] = {}
        donations[d]['Z2'] = {}
        donations[d]['S1'] = donations[d]['S2'] = 0
        for t in ['meat', 'dairy', 'eggs']:
            # PLX*Sum(AEPY*CEF)
            donations[d]['Z1'][t] = donations[d][t]*donations[d]['Y1'][t]
            donations[d]['S1'] += donations[d]['Z1'][t]
            
            # PLX*Sum(AEPY*CEF*AYLA)
            donations[d]['Z2'][t] = donations[d][t]*donations[d]['Y2'][t]
            donations[d]['S2'] += donations[d]['Z2'][t]
        
        # Total animal reduction on farms
        donations[d]['RFA'] = donations[d]['S1']*donations[d]['AYL']*amount/donations[d]['CPX']
        
        # Reduction in factory-farmed years
        donations[d]['RFY'] = donations[d]['S2']*donations[d]['AYL']*amount/donations[d]['CPX']
    
    x = np.linspace(-10.0, 50.0, 50)
    ads_y, ads_x = np.histogram(donations['Ads']['RFY'], bins=x, density=True)
    leaflets_y, leaflets_x = np.histogram(donations['Leaflets']['RFY'], bins=x, density=True)

    plt.figure(0,  figsize=(8, 6))
    #plt.plot((cash_x[:-1] + cash_x[1:])/2.0, cash_y, label='cash', color='k')
    plt.plot((ads_x[:-1] + ads_x[1:])/2.0, ads_y, label='ads', color='b')
    plt.plot((leaflets_x[:-1] + leaflets_x[1:])/2.0, leaflets_y, label='leaflets', color='g')
    plt.xlim([np.min(x), np.max(x)])
    #plt.xlabel('X as cost effective as Cash')
    #plt.ylabel('Probability')
    #plt.title('PDF of cost effectiveness')
    plt.legend(loc='upper right')
    plt.show()

    key = 'RFY'    
    data = np.array([donations['Ads'][key], donations['Leaflets'][key]]).transpose()
    df = pd.DataFrame(data, columns=['ads', 'leaflets'])
    df.to_pickle('ace_data.pickle')