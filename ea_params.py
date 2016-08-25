# -*- coding: utf-8 -*-
"""
Created on Thu Jun 09 23:35:58 2016

@author: dan
"""

import json

if __name__ == '__main__':
    shared = {'Discount rate': {'dist': 'array', 'val': [0.05, 0.03, 0.03, 0.03, 0.03, 0.05, 0.035, 0.05, 0.05, 0.05]}, \
        '1 DALY is equivalent to increasing ln(income) by one unit for how many years': {'dist': 'array', 'val': [4.0, 3.0, 3.0, 3.0, 5.0, 3.0, 3.0, 3.0, 4.0, 3.0]}, \
        'Short term health benefits, in DALY terms': {'dist': 'const', 'val': 0.001760818}, \
        'Intuitive maximum adjustment': {'dist': 'const', 'val': 0.05}, \
        'Cap adjustment at intuitive maximum': {'dist': 'const', 'val': 0}, \
        'DALYs per death of a young child averted': {'dist': 'array', 'val': [12.0, 30.0, 30.0, 5.0, 17.0, 36.525, 40.0, 36.525, 3.0, 36.525]}}
    
    cash = {'ROI of cash transfers': {'dist': 'array', 'val': [0.15, 0.1, 0.12, 0.19, 0.19, 0.1, 0.08, 0.1, 0.1, 0.15]}, \
        '% of transfers invested': {'dist': 'array', 'val': [0.25, 0.5, 0.35, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.25]}, \
        'Duration of benefits of cash transfers (years)': {'dist': 'array', 'val': [20.0, 20.0, 15.0, 20.0, 15.0, 20.0, 20.0, 20.0, 20.0, 15.0]}, \
        'Transfers as a percentage of total cost': {'dist': 'array', 'val': [0.828, 0.828, 0.828, 0.828, 0.8, 0.828, 0.828, 0.828, 0.828, 0.828]}, \
        'Average family size': {'dist': 'const', 'val': 4.7}, \
        'Large transfer size, USD': {'dist': 'const', 'val': 1085.0}, \
        'Control group household monthly consumption, USD PPP': {'dist': 'const', 'val': 157.40}, \
        'Size of transfer': {'dist': 'const', 'val': 1000.0}, \
        '% of investment returned after end of benefits': {'dist': 'array', 'val': [0.0, 0.1, 0.2, 0.25, 0.1, 0.25, 0.25, 0.25, 0.1, 0.15]}}
        
    deworming = {'Replicability adjustment for  deworming': {'dist': 'array', 'val': [0.5, 0.35, 0.3, 0.23, 0.6, 0.23, 0.25, 0.23, 0.6, 0.6]}, \
        '% of years of childhood in which deworming is helpful for development': {'dist': 'array', 'val': [0.75, 0.75, 0.7, 0.8, 0.6, 0.8, 0.8, 1.0, 0.8, 0.5]}, \
        'Number of household members that benefit': {'dist': 'array', 'val': [1.2, 1.1, 1.5, 1.4, 1.4, 1.4, 1.5, 1.4, 1.0, 1.4]}, \
        'Short term health benefits of deworming (DALYs per person treated)': {'dist': 'array', 'val': [0.001760818, 0.001760818, 0.001760818, 0.001760818, 0.001760818, 0.001760818, 0.001760818, 0.001760818, 0.0, 0.00168243]}, \
        'Duration of long term benefits of deworming (years) - also used for iodine': {'dist': 'array', 'val': [25.0, 20.0, 25.0, 25.0, 20.0, 40.0, 30.0, 25.0, 20.0, 20.0]}, \
        'Proportion of dewormed children that benefit from long term gains': {'dist': 'array', 'val': [0.3, 0.25, 0.25, 0.166, 0.2, 0.3, 0.3, 0.166, 0.166, 0.166]}, \
        'Treatment effect of deworming on Ln(total labor earnings)': {'dist': 'const', 'val': 0.269}, \
        'Years of deworming treatment in Miguel and Kremer 2004': {'dist': 'const', 'val': 2.41}, \
        'Adjustment for El Nino': {'dist': 'array', 'val': [0.560606061, 0.9, 0.8, 0.711538462, 0.711538462, 1.0, 0.9, 0.560606061, 0.711538462, 0.542124542]}, \
        'Average number of years between deworming and the beginning of long term benefits - also used for iodine': {'dist': 'array', 'val': [8.0, 10.0, 7.0, 5.0, 8.0, 8.0, 5.0, 8.0, 5.0, 8.0]}}
    
    dtw = {'Prevalence/ intensity adjustment': {'dist': 'array', 'val': [0.2145, 0.2496, 0.2496, 0.2496, 0.2584, 0.2496, 0.31, 0.2496, 0.1719, 0.2496]}, \
        'Leverage (dollar of impact per dollar spent)': {'dist': 'array', 'val': [1.0, 1.0, 1.0, 1.17, 1.0, 1.35, 1.0, 1.0, 1.0, 1.0]}, \
        'Adjustment for benefit varying by treatment frequency': {'dist': 'array', 'val': [1.0, 1.0, 0.77, 0.77, 1.0, 0.77, 1.0, 0.81, 0.81, 0.81]}, \
        'Proportion of deworming going to children': {'dist': 'array', 'val': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]}, \
        'Cost per person dewormed': {'dist': 'array', 'val': [0.67, 0.56, 0.7, 0.56, 0.8, 0.78, 0.68, 0.78, 0.8, 0.8]}}
        
    sci = {'Prevalence/ intensity adjustment': {'dist': 'array', 'val': [0.263, 0.1939, 0.1939, 0.1939, 0.1214, 0.1939, 0.45, 0.1939, 0.1214, 0.1939]}, \
        'Leverage (dollar of impact per dollar spent)': {'dist': 'array', 'val': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]}, \
        'Adjustment for benefit varying by treatment frequency': {'dist': 'array', 'val': [1.0, 1.0, 0.77, 0.77, 1.0, 1.0, 1.0, 0.81, 1.0, 1.0]}, \
        'Proportion of deworming going to children': {'dist': 'array', 'val': [0.75, 0.75, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.75, 0.9]}, \
        'Cost per person dewormed': {'dist': 'array', 'val': [0.72, 0.5292, 0.7, 0.5292, 0.9072, 0.9072, 1.2, 0.9072, 1.26, 1.26]}}

    bednets = {'Cost per ITN distributed (including delivery)': {'dist': 'const', 'val': 4.47}, \
        'Wastage': {'dist': 'const', 'val': 0.1}, \
        'People covered per LLIN': {'dist': 'const', 'val': 1.8}, \
        'Years of protection per person per LLIN': {'dist': 'const', 'val': 2.22}, \
        'Impact of insecticide resistance': {'dist': 'const', 'val': 0.33}, \
        'Percent of population under 5': {'dist': 'const', 'val': 0.1725}, \
        'Percent of population aged 5-14': {'dist': 'const', 'val': 0.308}, \
        'Deaths averted per protected child under 5': {'dist': 'const', 'val': 0.00553}, \
        'Under 5 all mortality rate 1995 in the countries where RCT studies were done -  Burkina Faso, Gambia, Ghana, and Kenya (per 1000)': {'dist': 'const', 'val': 142.25}, \
        'Under 5 all mortality rate 2015 (per 1000)': {'dist': 'const', 'val': 69.0}, \
        'Under 5 all mortality rate 2004 (per 1000)': {'dist': 'const', 'val': 117.0}, \
        'Decrease 2004-2015 attributed to ITNs': {'dist': 'const', 'val': 0.25}, \
        'Pre-existing ITN ownership: all': {'dist': 'const', 'val': 0.531}, \
        'Pre-existing ITN ownership: children under 5 (from DHS)': {'dist': 'const', 'val': 0.631}, \
        'Pre-existing ITN ownership: children aged 5-14 (from DHS)':  {'dist': 'const', 'val': 0.4575}, \
        'Pre-existing ITN ownership: all (from AMF)': {'dist': 'const', 'val': 0.1221}, \
        '% of impact of ITNs coming from community-wide effects': {'dist': 'const', 'val': 0.5}, \
        'Total amount spent':  {'dist': 'const', 'val': 1000000}, \
        'Relative value of year of deworming treatment to development benefits from year of bednet coverage':  {'dist': 'array', 'val': [2.0, 1.0, 1.5, 2.0, 1.0, 2.0, 3.0, 2.0, 1.5, 1.0]}, \
        'Alternative funders adjustment': {'dist': 'array', 'val': [0.75, 0.86, 0.85, 0.85, 0.86, 0.86, 0.75, 0.86, 0.86, 0.86]}}
    
    iodine = {'Cost per person per year': {'dist': 'array', 'val': [0.1, 0.1, 0.08, 0.08, 0.08, 0.08, 0.05, 0.05, 0.1, 0.1]}, \
        'Replicability': {'dist': 'array', 'val': [0.8, 0.7, 0.9, 0.8, 0.8, 0.8, 0.6, 0.6, 0.7, 0.7]}, \
        'External validity': {'dist': 'array', 'val': [0.7, 0.7, 0.7, 0.7]}, \
        'Leverage (dollars of impact per dollars spent)': {'dist': 'array', 'val': [1.0, 1.0, 2.0, 1.0, 1.0, 1.0, 1.0, 2.0, 2.0, 2.0]}, \
        '% of benefit of iodine that lasts for the long term': {'dist': 'array', 'val': [0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 1.0, 1.0, 0.4, 0.4]}, \
        'Probability that GAIN/ICCIDD has an impact': {'dist': 'array', 'val': [0.5, 0.25, 0.5, 0.5, 0.5, 0.5, 0.75, 0.75, 0.25, 0.25]}, \
        '% of children that benefit': {'dist': 'array', 'val': [0.8, 0.8, 0.8, 1.0, 0.8, 0.8, 1.0, 1.0, 0.332, 0.332]}, \
        'Equivalent increase in wages from having iodine throughout childhood': {'dist': 'array', 'val': [0.036, 0.036, 0.036, 0.036, 0.036, 0.036, 0.027, 0.027, 0.054, 0.054]}, \
        'Years of Childhood (for iodine)': {'dist': 'const', 'val': 15.0}, \
        'Percent of population under 15': {'dist': 'const', 'val': 0.431}}
    
    params = {'Shared': shared, 'Cash': cash, 'Deworming': deworming, 'DtW': dtw, 'SCI': sci, 'Bednets': bednets, 'Iodine': iodine}
    
    with open('params.json', 'w') as fp:
        json.dump(params, fp, indent=4)