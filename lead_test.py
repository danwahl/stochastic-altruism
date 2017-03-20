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
    
    # random val
    r = np.random.rand(1, n)
    
    # randomly selected data from distributions for fit (either uncorrelated or correlated)
    xd = np.array([x, np.ones(x.size)])
    #yd = np.array([stats.norm.rvs(loc=j, scale=k, size=n) for (j, k) in zip(y, se)]).T
    yd = np.array([stats.norm.ppf(k, loc=i, scale=j) for (i, j) in zip(y, se) for k in r]).T
    
    # linear regression, return slope/offset
    f = np.array([np.linalg.lstsq(xd.T, d)[0] for d in yd])
    return (f[:,0], f[:, 1])

if __name__ == '__main__':
    n = 100000
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

    lsls = {}
    lsls['Data'] = np.stack([params['lsls'][str(lsl)]['val'] for lsl in range(1, 21)]).T
    lsls['Mean'] = np.nanmean(lsls['Data'], axis=1)
    lsls['Disturbed'] = (~np.isnan(params['lsls']['Year Disturbed']['val'])).astype(float)

    sim = {}
    sim['Age'] = stats.uniform.rvs(loc=0, scale=6, size=n)
    sim['Sex'] = np.random.choice(['Male', 'Female'], n)
    sim['Life expectancy'] = np.array([np.interp(age, np.array(params['actuarial']['Exact Age']['val']), np.array(params['actuarial'][sex + ' Life expectancy']['val'])) for (age, sex) in zip(sim['Age'], sim['Sex'])])
    sim['House'] = np.random.choice(range(lsls['Data'].shape[0]), n, p=lsls['Disturbed']/np.sum(lsls['Disturbed']))
    sim['Prior IQ'] = stats.norm.rvs(loc=100, scale=15, size=n)
    sim['Prior Weight'] = np.maximum(sim['Prior IQ']*weight['Slope'] + weight['Offset'], 0)
    sim['Prior DALYs'] = sim['Life expectancy']*sim['Prior Weight']
    sim['BLL ug/dL'] = stats.lognorm.rvs(chicago['LN sd'][-1], loc=chicago['LN mean'][-1], size=n)
    sim['Expected IQ Loss'] = np.minimum(np.log(sim['BLL ug/dL'])*iq['Slope'], 0)
    sim['Expected IQ'] = sim['Prior IQ'] + sim['Expected IQ Loss']
    sim['Expected Weight'] = np.maximum(sim['Expected IQ']*weight['Slope'] + weight['Offset'], 0)
    sim['Expected DALYs'] = sim['Life expectancy']*sim['Expected Weight']
    sim['Water ppb'] = lsls['Mean'][sim['House']]
    sim['BLL ug/dL from H2O'] = np.log(sim['Water ppb'])*water['Slope'] + water['Offset']
    sim['Post IQ loss'] = np.minimum(np.log(np.maximum(sim['BLL ug/dL'] - sim['BLL ug/dL from H2O'], np.finfo(np.float64).eps))*iq['Slope'], 0)
    sim['Post IQ'] = sim['Prior IQ'] + sim['Post IQ loss']
    sim['Post Weight'] = np.maximum(sim['Post IQ']*weight['Slope'] + weight['Offset'], 0)
    sim['Post DALYs'] = sim['Life expectancy']*sim['Post Weight']   
    
    filters = {}
    filters['Slope'], filters['Offset'], _, _, _ = stats.linregress(params['filters']['TDS']['val'], params['filters']['Gallons']['val'])
    filters['Gallons/filter'] = params['filters']['Chicago TDS']['val']*filters['Slope'] + filters['Offset']
    filters['Gallons/house/day'] = params['filters']['Gallons/child/day']['val']*params['filters']['Children/house']['val']
    filters['Filter days/house'] = filters['Gallons/filter']/filters['Gallons/house/day']
    filters['Filters/intervention'] = params['filters']['Days/intervention']['val']/filters['Filter days/house']
    filters['Cost/house'] = params['filters']['Filter cost']['val']*(filters['Filters/intervention'] - params['filters']['Filters/pitcher']['val']) + \
         params['filters']['Pitcher cost']['val']
    filters['Cost/child'] = filters['Cost/house']/params['filters']['Children/house']['val']
    filters[key] = (sim['Expected DALYs'] - sim['Post DALYs'])/filters['Cost/child']*m
    
    x = np.linspace(0.0, 100.0, 100)
    filters_y, filters_x = np.histogram(filters[key], bins=x, density=True)

    plt.figure(0,  figsize=(8, 6))
    plt.plot((filters_x[:-1] + filters_x[1:])/2.0, filters_y, label='filters', linewidth=2.0, color='grey')
    plt.xlim([np.min(x), np.max(x)])
    plt.ylim([0, 0.02])
    plt.xlabel(key)
    plt.ylabel('Probability')
    plt.title('PDF of cost effectiveness')
    plt.legend(loc='upper right')
    plt.show()
    
    data = np.array([filters[key]]).transpose()
    df = pd.DataFrame(data, columns=['lead'])
    df.to_pickle('lead_data.pickle')
