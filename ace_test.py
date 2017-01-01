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
    if p['dist'] == 'norm':
        return stats.norm.rvs(loc=p['loc'], scale=p['scale'], size=n)
    else:
        return p['val']

def mult_norm(n1, n2, div=False):
    n3 = {'dist': 'norm'}
    
    # mean
    if div:
        n3['loc'] = n1['loc']/n2['loc']
    else:
        n3['loc'] = n1['loc']*n2['loc']
    
    # std
    try:
        n3['scale'] = n3['loc']*np.sqrt(np.power(n1['scale']/n1['loc'], 2) + np.power(n2['scale']/n2['loc'], 2))
    except ZeroDivisionError:
        n3['scale'] = 0
    
    return n3

if __name__ == '__main__':
    n = 100000
    m = 1000.0
    key = 'DALYs per $' + str(m) 
    
    #meat = ['Beef', 'Pork', 'Chicken', 'Turkey', 'Fish']
    meat = ['Beef', 'Pork', 'Chicken']
    types = ['meat', 'dairy', 'eggs']
    
    with open('ace_params.json') as fp:    
        params = json.load(fp)
    
    animals = params['Animals']
    donations = params['Donations']
    
    for a in animals.keys():
        # sentience and weight adjustment
        animals[a]['eq'] = animals[a]['brain']['val']/(0.12*np.power(animals[a]['body']['val'], 2.0/3.0))  
        animals[a]['f'] = animals[a]['weight']['val']*animals[a]['eq']/HUMAN_EQ             
        
        # cumulative elasticity factor
        animals[a]['CEF'] = {'dist': 'norm', 'loc': animals[a]['PES']['loc']/(animals[a]['PES']['loc'] - animals[a]['PED']['loc'])}
        animals[a]['CEF']['scale'] = np.power(animals[a]['CEF']['loc'], 2)*np.abs(animals[a]['PED']['loc']/animals[a]['PES']['loc'])* \
            np.sqrt(np.power(animals[a]['PED']['scale']/animals[a]['PED']['loc'], 2) + np.power(animals[a]['PES']['scale']/animals[a]['PES']['loc'], 2))
    
        # AEPY*CEF
        animals[a]['X1'] = mult_norm(animals[a]['AEPY'], animals[a]['CEF'])
        
        # adjust for sentience and weight
        animals[a]['X1']['loc'] *= animals[a]['f']
        animals[a]['X1']['scale'] *= animals[a]['f']
        
        # AEPY*CEF*AYLA
        animals[a]['X2'] = mult_norm(animals[a]['X1'], animals[a]['AYLA'])        

    for d in donations.keys():
        # "Sum (AEPY*CEF)
        donations[d]['Y1'] = {
            'meat': {'dist': 'norm', 'loc': np.sum([animals[a]['X1']['loc'] for a in meat]), 'scale': np.sqrt(np.sum([np.power(animals[a]['X1']['scale'], 2) for a in meat]))}, \
            'dairy': {'dist': 'norm', 'loc': animals['Dairy']['X1']['loc'], 'scale': animals['Dairy']['X1']['scale']}, \
            'eggs': {'dist': 'norm', 'loc': animals['Eggs']['X1']['loc'], 'scale': animals['Eggs']['X1']['scale']}
        }
        
        # Sum(AEPY*CEF*AYLA)
        donations[d]['Y2'] = {
            'meat': {'dist': 'norm', 'loc': np.sum([animals[a]['X2']['loc'] for a in meat]), 'scale': np.sqrt(np.sum([np.power(animals[a]['X2']['scale'], 2) for a in meat]))}, \
            'dairy': {'dist': 'norm', 'loc': animals['Dairy']['X2']['loc'], 'scale': animals['Dairy']['X2']['scale']}, \
            'eggs': {'dist': 'norm', 'loc': animals['Eggs']['X2']['loc'], 'scale': animals['Eggs']['X2']['scale']}
        }
        
        donations[d]['Z1'] = {}
        donations[d]['Z2'] = {}
        for t in types:
            # PLX*Sum(AEPY*CEF)
            donations[d]['Z1'][t] = mult_norm(donations[d][t], donations[d]['Y1'][t])
 
            # PLX*Sum(AEPY*CEF)
            donations[d]['Z2'][t] = mult_norm(donations[d][t], donations[d]['Y2'][t])
        
        # Sum (PLL/C * Sum (AEPY * CEF))
        donations[d]['S1'] = {'dist': 'norm', 'loc': np.sum([donations[d]['Z1'][t]['loc'] for t in types]), \
            'scale': np.sqrt(np.sum([np.power(donations[d]['Z1'][t]['scale'], 2) for t in types]))}
        
        # Sum(PLL/C*Sum(AEPY*CEF*AYLA))
        donations[d]['S2'] = {'dist': 'norm', 'loc': np.sum([donations[d]['Z2'][t]['loc'] for t in types]), \
            'scale': np.sqrt(np.sum([np.power(donations[d]['Z2'][t]['scale'], 2) for t in types]))}
        
        # Total animal reduction on farms (per dollar)
        donations[d]['RFA'] = mult_norm(mult_norm(donations[d]['S1'], donations[d]['AYL']), donations[d]['CPX'], div=True)
        
        # Reduction in factory-farmed years (per dollar)
        donations[d]['RFY'] = mult_norm(mult_norm(donations[d]['S2'], donations[d]['AYL']), donations[d]['CPX'], div=True)

        # dalys per m        
        donations[d][key] = {'dist': 'norm'}
        donations[d][key]['loc'] = m*donations[d]['RFY']['loc']
        donations[d][key]['scale'] = m*donations[d]['RFY']['scale']
    
    ads_rvs = get_rvs(donations['Ads'][key], n)
    leaflets_rvs = get_rvs(donations['Leaflets'][key], n)
        
    '''
    x = np.linspace(0.0, 25.0, 100)
    ads_y, ads_x = np.histogram(donations['Ads'][key], bins=x, density=True)
    leaflets_y, leaflets_x = np.histogram(donations['Leaflets'][key], bins=x, density=True)

    plt.figure(0,  figsize=(8, 6))
    plt.plot((ads_x[:-1] + ads_x[1:])/2.0, ads_y, label='ads', linewidth=2.0, color='w')
    plt.plot((leaflets_x[:-1] + leaflets_x[1:])/2.0, leaflets_y, label='leaflets', linewidth=2.0, color='c')
    plt.xlim([np.min(x), np.max(x)])
    plt.xlabel(key)
    plt.ylabel('Probability')
    plt.title('PDF of cost effectiveness')
    plt.legend(loc='upper right')
    plt.show()
    '''
    
    data = np.array([ads_rvs, leaflets_rvs]).transpose()
    df = pd.DataFrame(data, columns=['ads', 'leaflets'])
    df.to_pickle('ace_data.pickle')
