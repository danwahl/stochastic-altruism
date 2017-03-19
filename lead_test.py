# -*- coding: utf-8 -*-
"""

"""

import json
import scipy.stats as stats
import numpy as np

import matplotlib.pyplot as plt
plt.style.use('ggplot')

import pandas as pd

def get_rvs(p, n):
    if p['dist'] == 'array':
        return np.random.choice(p['val'], n)
    else:
        return p['val']

def stochastic_fit(x, y, l, h, p, n):
    # z score and standard error
    z = stats.norm.ppf(p)
    se = (h - l)/(2.0*z)
    
    # randomly selected data from distributions for fit
    xd = np.array([x, np.ones(x.size)])
    yd = np.array([stats.norm.rvs(loc=j, scale=k, size=n) for (j, k) in zip(y, se)]).transpose()
    
    # linear regression, return slope/offset
    f = np.array([np.linalg.lstsq(xd.T, d)[0] for d in yd])
    return (f[:,0], f[:, 1])

if __name__ == '__main__':
    n = 1000
    m = 1000.0
    key = 'DALYs per $' + str(m) 
    
    with open('lead_params.json') as fp:    
        params = json.load(fp)
        
    inputs = {}
    for k in params.keys():
        d = {}
        for p in params[k].keys():
            d[p] = get_rvs(params[k][p], n)
        inputs[k] = d
    
    water = {}
    water['Water lead (ppb)'] = np.array(params['water']['Water lead (mg/L)']['val'])*1000
    (water['Slope'], water['Offset']) = stochastic_fit( \
        np.log(water['Water lead (ppb)']), \
        np.array(params['water']['Increase in BPb ug/dl']['val']), \
        np.array(params['water']['95% CI low']['val']), \
        np.array(params['water']['95% CI High']['val']), \
        0.95, n)
    
    iq = {}
    (iq['Slope'], iq['Offset']) = stochastic_fit( \
        np.log(np.array(params['iq']['Concurrent blood lead (ug/dL)']['val'])), \
        np.array(params['iq']['IQ']['val']), \
        np.array(params['water']['95% CI low']['val']), \
        np.array(params['water']['95% CI High']['val']), \
        0.95, n)
    
    weight = {}
    weight['IQ avg'] = (np.array(params['weight']['IQ low']['val']) + np.array(params['weight']['IQ high']['val']))/2.0
    (weight['Slope'], weight['Offset']) = stochastic_fit( \
        weight['IQ avg'], \
        np.array(params['weight']['Weight']['val']), \
        np.array(params['weight']['CI high']['val']), \
        np.array(params['weight']['CI low']['val']), \
        0.95, n)
    
    chicago = {}
    chicago['Z-Score 5'] = stats.norm.ppf(1.0 - np.array(params['chicago']['BLL > 5 ug/dL']['val']))
    chicago['Z-Score 10'] = stats.norm.ppf(1.0 - np.array(params['chicago']['BLL > 10 ug/dL']['val']))
    (chicago['LN sd'], chicago['LN mean']) = np.array([np.dot(np.linalg.inv(np.array([[z5, 1], [z10, 1]])), np.array([np.log(5), np.log(10)]).T) for (z5, z10) in zip(chicago['Z-Score 5'], chicago['Z-Score 10'])]).T

    sim = {}
    sim['Age'] = stats.uniform.rvs(loc=0, scale=6, size=n)
    sim['Sex'] = np.random.choice(['Male', 'Female'], n)
    sim['Life expectancy'] = np.array([np.interp(age, np.array(params['actuarial']['Exact Age']['val']), np.array(params['actuarial'][sex + ' Life expectancy']['val'])) for (age, sex) in zip(sim['Age'], sim['Sex'])])
    sim['Prior IQ'] = stats.norm.rvs(loc=100, scale=15, size=n)
    sim['Prior Weight'] = np.maximum(sim['Prior IQ']*weight['Slope'] + weight['Offset'], 0)
    
    #filters_rvs = get_rvs(filters[key], n)
        
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
    
    #data = np.array([filters_rvs]).transpose()
    #df = pd.DataFrame(data, columns=['lead'])
    #df.to_pickle('lead_data.pickle')
