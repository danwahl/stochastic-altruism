# -*- coding: utf-8 -*-
"""
Created on Thu Jun 09 23:35:58 2016

@author: dan
"""

import json

if __name__ == '__main__':
    shared = {'Discount rate': {'dist': 'array', 'val': [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.03, 0.01, 0.05, 0.04, 0.05]}, \
        '1 DALY is equivalent to increasing ln(income) by one unit for how many years': {'dist': 'array', 'val': [1.333333333, 3.0, 4.0, 2.5, 0.65, 3.0, 0.985533532, 2.0, 3.0, 3.25, 3.0, 3.0]}, \
        'Short term health benefits, in DALY terms': {'dist': 'const', 'val': 0.001760818}, \
        'DALYs per life': {'dist': 'const', 'val': 36.53}, \
        'Intuitive maximum adjustment': {'dist': 'const', 'val': 0.05}, \
        'Cap adjustment at intuitive maximum': {'dist': 'const', 'val': 0}}
    
    cash = {'ROI of cash transfers': {'dist': 'array', 'val': [0.19, 0.15, 0.15, 0.19, 0.23, 0.1, 0.19, 0.2, 0.1, 0.19, 0.1, 0.19]}, \
        'Percentage of transfers invested': {'dist': 'array', 'val': [0.5, 0.5, 0.4, 0.5, 0.5, 0.5, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4]}, \
        'Duration of benefits in years': {'dist': 'array', 'val': [20.0, 20.0, 20.0, 40.0, 20.0, 20.0, 15.0, 20.0, 20.0, 20.0, 15.0, 20.0]}, \
        'Transfers as a percentage of total cost': {'dist': 'array', 'val': [0.808, 0.808, 0.808, 0.845, 0.808, 0.808, 0.845, 0.845, 0.845, 0.808, 0.808, 0.808]}, \
        'Average family size': {'dist': 'const', 'val': 4.7}, \
        'Large transfer size, USD': {'dist': 'const', 'val': 1085}, \
        'Control group household monthly consumption, USD PPP': {'dist': 'const', 'val': 157.40}, \
        'Size of transfer': {'dist': 'const', 'val': 1000.0}}
        
    deworming = {'External validity of deworming research': {'dist': 'array', 'val': [0.302549303, 0.616666667, 0.542124542, 0.542124542, 0.560606061, 0.504100529, 0.542124542, 0.6, 0.560606061, 0.302549303, 0.635, 0.302549303]}, \
        'Replicability adjustment for  deworming': {'dist': 'array', 'val': [0.75, 0.6, 0.6, 0.6, 0.5, 0.6, 0.6, 0.4, 0.6, 0.6, 0.33, 0.6]}, \
        '% of years of childhood in which deworming is helpful for development': {'dist': 'array', 'val': [0.5, 1.0, 0.75, 0.75, 1.0, 0.75, 0.5, 0.75, 1.0, 1.0, 1.0, 0.8]}, \
        'Number of household members that benefit': {'dist': 'array', 'val': [2.0, 1.442696146, 1.2, 1.1, 2.0, 1.1, 1.2, 2.0, 1.5, 1.442696146, 1.84, 1.442696146]}, \
        'Prevalence/intensity ratio between M&K and short term health benefit observations': {'dist': 'array', 'val': [1.0, 1.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 1.0, 2.0, 2.0]}, \
        'Short term health benefits of deworming (DALYs per person treated)': {'dist': 'array', 'val': [0.001760818, 0.001760818, 0.001760818, 0.001760818, 0.001826885, 0.001760818, 0.001826885, 0.001760818, 0.001760818, 0.001760818, 0.001826885, 0.001760818]}, \
        'Duration of long term benefits of deworming (years) - also used for iodine': {'dist': 'array', 'val': [40.0, 40.0, 40.0, 40.0, 25.0, 25.0, 15.0, 25.0, 25.0, 40.0, 35.0, 20.0]}, \
        'Proportion of dewormed children that benefit from long term gains': {'dist': 'array', 'val': [0.3, 0.3, 0.166, 0.3, 0.3, 0.3, 0.2, 0.3, 0.3, 0.3, 0.5, 0.3]}, \
        'Treatment effect of deworming on Ln(total labor earnings)': {'dist': 'const', 'val': 0.269}, \
        'Years of deworming treatment in Miguel and Kremer 2004': {'dist': 'const', 'val': 2.41}, \
        'Duration of long term benefits of deworming (years) - also used for iodine': {'dist': 'const', 'val': 35.0}}
    
    dtw = {'Prevalence/ intensity adjustment': {'dist': 'array', 'val': [1.0, 0.2124, 0.2536, 0.2536, 0.2481, 0.2536, 0.291, 0.2536, 0.2536, 0.2536, 0.2536, 0.2536]}, \
        'Leverage (dollar of impact per dollar spent)': {'dist': 'array', 'val': [1.17, 1.0, 1.17, 1.07, 1.17, 1.07, 1.08, 1.0, 1.0, 1.35, 1.0, 1.0]}, \
        'Adjustment for benefit varying by treatment frequency': {'dist': 'array', 'val': [0.666666667, 0.71, 1.0, 1.0, 0.77, 0.81, 1.2, 0.77, 0.81, 0.77, 0.958, 0.81]}, \
        'Proportion of deworming going to children': {'dist': 'array', 'val': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]}, \
        'Cost per person dewormed': {'dist': 'array', 'val': [0.51, 0.63, 0.75, 0.75, 0.51, 0.51, 0.644, 0.75, 0.8, 0.51, 0.51, 0.51]}}
        
    sci = {'Prevalence/ intensity adjustment': {'dist': 'array', 'val': [1.0, 0.259783066, 0.185691342, 0.185691342, 0.122674144, 0.185691342, 0.146, 0.185691342, 0.185691342, 0.185691342, 0.185691342, 0.185691342]}, \
        'Leverage (dollar of impact per dollar spent)': {'dist': 'array', 'val': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]}, \
        'Adjustment for benefit varying by treatment frequency': {'dist': 'array', 'val': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.3, 0.77, 1.0, 1.0, 1.244, 1.0]}, \
        'Proportion of deworming going to children': {'dist': 'array', 'val': [0.75, 0.75, 0.75, 0.75, 0.75, 0.85, 0.8, 0.8, 0.75, 0.75, 0.825, 0.75]}, \
        'Cost per person dewormed': {'dist': 'array', 'val': [0.5292, 0.72, 0.9072, 0.9072, 0.5292, 0.5292, 0.88, 0.9072, 1.26, 0.5292, 0.5292, 0.5292]}}

    bednets = {'Cost per ITN distributed (including delivery)': {'dist': 'const', 'val': 5.30}, \
        'Wastage': {'dist': 'const', 'val': 0.05}, \
        'People covered per LLIN': {'dist': 'const', 'val': 1.8}, \
        'Years of protection per person per LLIN': {'dist': 'const', 'val': 2.22}, \
        'Impact of insecticide resistance': {'dist': 'const', 'val': 0.20}, \
        'Percent of population under 5': {'dist': 'const', 'val': 0.179}, \
        'Percent of population aged 5-14': {'dist': 'const', 'val': 0.3017}, \
        'Deaths averted per protected child under 5': {'dist': 'const', 'val': 0.00553}, \
        'Under 5 all mortality rate 1995 in the countries where RCT studies were done -  Burkina Faso, Gambia, Ghana, and Kenya (per 1000)': {'dist': 'const', 'val': 142.25}, \
        'Under 5 all mortality rate 2015 (per 1000)': {'dist': 'const', 'val': 77.0}, \
        'Under 5 all mortality rate 2004 (per 1000)': {'dist': 'const', 'val': 127.0}, \
        'Decrease 2004-2015 attributed to ITNs': {'dist': 'const', 'val': 0.25}, \
        'Pre-existing ITN ownership: all': {'dist': 'const', 'val': 0.57}, \
        'Pre-existing ITN ownership: children under 5 (from DHS)': {'dist': 'const', 'val': 0.67}, \
        'Pre-existing ITN ownership: children aged 5-14 (from DHS)':  {'dist': 'const', 'val': 0.44}, \
        'Pre-existing ITN ownership: all (from AMF)': {'dist': 'const', 'val': 0.12}, \
        '% of impact of ITNs coming from community-wide effects': {'dist': 'const', 'val': 0.5}, \
        'Total amount spent':  {'dist': 'const', 'val': 1000000}, \
        'Relative value of year of deworming treatment to development benefits from year of bednet coverage':  {'dist': 'array', 'val': [2.0, 4.23564533, 2.0, 2.0, 2.0, 1.0, 2.0, 2.0, 2.0, 1.0, 2.0, 4.0]}}
        
    params = {'Shared': shared, 'Cash': cash, 'Deworming': deworming, 'DtW': dtw, 'SCI': sci, 'Bednets': bednets}
    
    with open('params.json', 'w') as fp:
        json.dump(params, fp, indent=4)