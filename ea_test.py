# -*- coding: utf-8 -*-
"""
Created on Thu Jun 09 23:35:58 2016

@author: dan
"""

import json
import scipy.stats as stats
import numpy as np

import matplotlib.pyplot as plt
plt.style.use('ggplot')

import pandas as pd

def get_rvs(p, n):
    if p['dist'] == 'uniform':
        return stats.uniform.rvs(loc=p['loc'], scale=p['scale'], size=n)
    elif p['dist'] == 'array':
        return np.random.choice(p['val'], n)
    else:
        return p['val']

if __name__ == '__main__':
    n = 1000000
    
    with open('params.json') as fp:    
        params = json.load(fp)
    
    inputs = {}
    for k in params.keys():
        d = {}
        for p in params[k].keys():
            d[p] = get_rvs(params[k][p], n)
        inputs[k] = d
    
    bednets = {}
    bednets['Ratio of mortality rate in 2015 compared to 1995'] = \
        inputs['Bednets']['Under 5 all mortality rate 2015 (per 1000)']/ \
        inputs['Bednets']['Under 5 all mortality rate 1995 in the countries where RCT studies were done -  Burkina Faso, Gambia, Ghana, and Kenya (per 1000)']
    bednets['Ratio of mortality rate in 2004 compared to 1995'] = \
        inputs['Bednets']['Under 5 all mortality rate 2004 (per 1000)']/ \
        inputs['Bednets']['Under 5 all mortality rate 1995 in the countries where RCT studies were done -  Burkina Faso, Gambia, Ghana, and Kenya (per 1000)']
    bednets['Adjustment for ratio of current child mortality to historical child mortality when RCTs were conducted'] = \
        bednets['Ratio of mortality rate in 2015 compared to 1995'] + \
        (bednets['Ratio of mortality rate in 2004 compared to 1995'] - \
        bednets['Ratio of mortality rate in 2015 compared to 1995'])* \
        inputs['Bednets']['Decrease 2004-2015 attributed to ITNs']
    bednets['Deaths averted per protected child under 5 - adjusted for today\'s lower rates of child mortality and insecticide resistance'] = \
        inputs['Bednets']['Deaths averted per protected child under 5']* \
        bednets['Adjustment for ratio of current child mortality to historical child mortality when RCTs were conducted']* \
        (1.0 - inputs['Bednets']['Impact of insecticide resistance'])
    bednets['Pre-existing ITN ownership: children under 5 (GiveWell estimate)'] = \
        inputs['Bednets']['Pre-existing ITN ownership: all (from AMF)']* \
        inputs['Bednets']['Pre-existing ITN ownership: children under 5 (from DHS)']/ \
        inputs['Bednets']['Pre-existing ITN ownership: all']
    bednets['Pre-existing ITN ownership: children aged 5-14 (GiveWell estimate)'] = \
        inputs['Bednets']['Pre-existing ITN ownership: all (from AMF)']* \
        inputs['Bednets']['Pre-existing ITN ownership: children aged 5-14 (from DHS)']/ \
        inputs['Bednets']['Pre-existing ITN ownership: all']
    bednets['Effective pre-existing coverage of children under 5'] = \
        inputs['Bednets']['% of impact of ITNs coming from community-wide effects']* \
        inputs['Bednets']['Pre-existing ITN ownership: all (from AMF)'] + \
        (1.0 - inputs['Bednets']['% of impact of ITNs coming from community-wide effects'])* \
        bednets['Pre-existing ITN ownership: children under 5 (GiveWell estimate)']
    bednets['Effective pre-existing coverage: children aged 5-14'] = \
        inputs['Bednets']['% of impact of ITNs coming from community-wide effects']* \
        inputs['Bednets']['Pre-existing ITN ownership: all (from AMF)'] + \
        (1.0 - inputs['Bednets']['% of impact of ITNs coming from community-wide effects'])* \
        bednets['Pre-existing ITN ownership: children aged 5-14 (GiveWell estimate)']
    bednets['# of person-years of protection for children under 5, per person-year of protection for the community as a whole'] = \
        (1.0 - bednets['Effective pre-existing coverage of children under 5'])* \
        inputs['Bednets']['Percent of population under 5']/ \
        (1.0 - inputs['Bednets']['Pre-existing ITN ownership: all (from AMF)'])
    bednets['# of person-years of protection for children aged 5-14, per person-year of protection for the community as a whole'] = \
        (1.0 - bednets['Effective pre-existing coverage: children aged 5-14'])* \
        inputs['Bednets']['Percent of population aged 5-14']/ \
        (1.0 - inputs['Bednets']['Pre-existing ITN ownership: all (from AMF)'])        
    bednets['Total LLINs distributed'] = \
        (inputs['Bednets']['Total amount spent']/ \
        inputs['Bednets']['Cost per ITN distributed (including delivery)'])* \
        (1.0 - inputs['Bednets']['Wastage'])
    bednets['Total person-years of protection'] = \
        bednets['Total LLINs distributed']* \
        inputs['Bednets']['People covered per LLIN']* \
        inputs['Bednets']['Years of protection per person per LLIN']
    bednets['Total person-years of protection for children under 5'] = \
        bednets['Total person-years of protection']* \
        bednets['# of person-years of protection for children under 5, per person-year of protection for the community as a whole']
    bednets['Total person-years of protection for children aged 5-14'] = \
        bednets['Total person-years of protection']* \
        bednets['# of person-years of protection for children aged 5-14, per person-year of protection for the community as a whole']
    bednets['Total deaths averted for children under 5'] = \
        bednets['Total person-years of protection for children under 5']* \
        bednets['Deaths averted per protected child under 5 - adjusted for today\'s lower rates of child mortality and insecticide resistance']
    bednets['Cost per person-year of protection: under-14\'s only'] = \
        inputs['Bednets']['Total amount spent']/ \
        (bednets['Total person-years of protection for children under 5'] + \
        bednets['Total person-years of protection for children aged 5-14'] )
    bednets['Cost per person-year of protection, adjusted for insecticide resistance: under-14\'s only'] = \
        bednets['Cost per person-year of protection: under-14\'s only']/ \
        (1.0 - inputs['Bednets']['Impact of insecticide resistance'])
    bednets['Cost per death averted'] = \
        inputs['Bednets']['Total amount spent']/ \
        bednets['Total deaths averted for children under 5']
    bednets['Aggregate adjustment to Baird development effect'] = \
        inputs['Deworming']['Adjustment for El Nino']* \
        inputs['Deworming']['Replicability adjustment for  deworming']* \
        inputs['Deworming']['% of years of childhood in which deworming is helpful for development']* \
        inputs['Deworming']['Proportion of dewormed children that benefit from long term gains']/ \
        inputs['Bednets']['Relative value of year of deworming treatment to development benefits from year of bednet coverage']
    bednets['Adjustment to calculations'] = \
        (np.maximum(bednets['Aggregate adjustment to Baird development effect'], inputs['Shared']['Intuitive maximum adjustment']) \
        if inputs['Shared']['Cap adjustment at intuitive maximum'] else bednets['Aggregate adjustment to Baird development effect'])/ \
        bednets['Aggregate adjustment to Baird development effect']
   
    cash = {}
    cash['PPP multiplier'] = 1525.0/inputs['Cash']['Large transfer size, USD']
    cash['Control group household monthly consumption, USD'] = \
        inputs['Cash']['Control group household monthly consumption, USD PPP']/ \
        cash['PPP multiplier']
    cash['Control group per capita monthly consumption, USD'] = \
         cash['Control group household monthly consumption, USD']/ \
         inputs['Cash']['Average family size']
    cash['Control group per capita annual consumption, USD'] = \
        12.0*cash['Control group per capita monthly consumption, USD']
    cash['Size of transfer per person'] = \
        inputs['Cash']['Size of transfer']/ \
        inputs['Cash']['Average family size']
    cash['Control group household monthly consumption, USD'] = \
        inputs['Cash']['Control group household monthly consumption, USD PPP']/ \
        cash['PPP multiplier']
    cash['Control group per capita monthly consumption, USD'] = \
        cash['Control group household monthly consumption, USD']/ \
        inputs['Cash']['Average family size']
    cash['Control group per capita annual consumption, USD'] = \
        12.0*cash['Control group per capita monthly consumption, USD']
    cash['Cash flow from initial spending'] = \
        (1.0 - inputs['Cash']['% of transfers invested'])* \
        cash['Size of transfer per person']
    cash['Initial balance'] = \
        cash['Size of transfer per person'] - cash['Cash flow from initial spending']
    cash['Cash flow from investment return'] = \
        cash['Initial balance']*inputs['Cash']['ROI of cash transfers']
    cash['Sum of benefits from year 1 onward'] = \
        ((1.0 - np.power((1.0 + inputs['Shared']['Discount rate']), -(inputs['Cash']['Duration of benefits of cash transfers (years)'] - 1.0)))/ \
        inputs['Shared']['Discount rate'])*(np.log(cash['Cash flow from investment return'] + cash['Control group per capita annual consumption, USD']) - \
        np.log(cash['Control group per capita annual consumption, USD'])) + \
        (np.log((cash['Initial balance'] + cash['Cash flow from investment return']) + \
        cash['Control group per capita annual consumption, USD']) - np.log(cash['Control group per capita annual consumption, USD']))* \
        (np.power((1.0 + inputs['Shared']['Discount rate']), -inputs['Cash']['Duration of benefits of cash transfers (years)']))
    cash['Present value of the sum of future benefits from cash transfers (ln income)'] = \
        cash['Sum of benefits from year 1 onward']
    cash['Increase in current consumption from spending the transfer (Ln(income))'] = \
        (np.log(cash['Cash flow from initial spending'] + cash['Control group per capita annual consumption, USD']) - 
        np.log(cash['Control group per capita annual consumption, USD']))   
    cash['Present value of net increase in current and future consumption'] = \
        cash['Present value of the sum of future benefits from cash transfers (ln income)'] + \
        cash['Increase in current consumption from spending the transfer (Ln(income))']
    cash['Proportional increase in consumption per dollar'] = \
        cash['Present value of net increase in current and future consumption']/ \
        (cash['Size of transfer per person']/inputs['Cash']['Transfers as a percentage of total cost'])
    
    deworming = {}
    deworming['Benefit on one year\'s income (discounted back 10 years because of delay between deworming and working for income)'] = \
        inputs['Deworming']['Treatment effect of deworming on Ln(total labor earnings)']/ \
        np.power((1.0 + inputs['Shared']['Discount rate']), inputs['Deworming']['Average number of years between deworming and the beginning of long term benefits - also used for iodine'])
    deworming['Present value of the sum of the lifetime benefits per worker (in terms of Ln(income))'] = \
        deworming['Benefit on one year\'s income (discounted back 10 years because of delay between deworming and working for income)']* \
        (1.0 - 1.0/np.power((1.0 + inputs['Shared']['Discount rate']), inputs['Deworming']['Duration of long term benefits of deworming (years) - also used for iodine']))/ \
        (1.0 - 1.0/(1.0 + inputs['Shared']['Discount rate']))
    deworming['Adjusted long term benefits per year of treatment (in terms of ln $), assuming income supports household consumption'] = \
        deworming['Present value of the sum of the lifetime benefits per worker (in terms of Ln(income))']* \
        inputs['Deworming']['Number of household members that benefit']* \
        inputs['Deworming']['Adjustment for El Nino']* \
        inputs['Deworming']['% of years of childhood in which deworming is helpful for development']* \
        inputs['Deworming']['Proportion of dewormed children that benefit from long term gains']* \
        inputs['Deworming']['Replicability adjustment for  deworming']/ \
        inputs['Deworming']['Years of deworming treatment in Miguel and Kremer 2004']
    deworming['Short term health benefits (deworming only) in terms of Ln(income)'] = \
        inputs['Deworming']['Short term health benefits of deworming (DALYs per person treated)']* \
        inputs['Shared']['1 DALY is equivalent to increasing ln(income) by one unit for how many years']
    
    dtw = {}
    dtw['Aggregate adjustment to Baird development effect'] = \
        inputs['Deworming']['Adjustment for El Nino']* \
        inputs['Deworming']['Replicability adjustment for  deworming']* \
        inputs['Deworming']['% of years of childhood in which deworming is helpful for development']* \
        inputs['Deworming']['Proportion of dewormed children that benefit from long term gains']* \
        inputs['DtW']['Prevalence/ intensity adjustment']
    dtw['Adjustment to calculations'] = \
        (np.maximum(dtw['Aggregate adjustment to Baird development effect'], inputs['Shared']['Intuitive maximum adjustment']) \
        if inputs['Shared']['Cap adjustment at intuitive maximum'] else dtw['Aggregate adjustment to Baird development effect'])/ \
        dtw['Aggregate adjustment to Baird development effect']
    dtw['Adjusted total benefits, per person dewormed (Ln(income))'] = \
        inputs['DtW']['Adjustment for benefit varying by treatment frequency'] * \
        (deworming['Adjusted long term benefits per year of treatment (in terms of ln $), assuming income supports household consumption']* \
        dtw['Adjustment to calculations']* \
        inputs['DtW']['Proportion of deworming going to children']* \
        inputs['DtW']['Prevalence/ intensity adjustment'] + \
        deworming['Short term health benefits (deworming only) in terms of Ln(income)']* \
        inputs['DtW']['Prevalence/ intensity adjustment'])
    dtw['Proportional increase in consumption per dollar'] = \
        dtw['Adjusted total benefits, per person dewormed (Ln(income))']/ \
        (inputs['DtW']['Cost per person dewormed']/ \
        inputs['DtW']['Leverage (dollar of impact per dollar spent)'])
    dtw['Cost per equivalent life saved'] = \
        inputs['Shared']['1 DALY is equivalent to increasing ln(income) by one unit for how many years']* \
        inputs['Shared']['DALYs per death of a young child averted']/ \
        dtw['Proportional increase in consumption per dollar']
    dtw['X as cost effective as Cash'] = \
        dtw['Proportional increase in consumption per dollar']/cash['Proportional increase in consumption per dollar']
    #dtw_p = stats.lognorm.fit(dtw['X as cost effective as Cash'])
    #dtw_d = stats.lognorm(*dtw_p[:-2], loc=dtw_p[-2], scale=dtw_p[-1])
    
    sci = {}
    sci['Aggregate adjustment to Baird development effect'] = \
        inputs['Deworming']['Adjustment for El Nino']* \
        inputs['Deworming']['Replicability adjustment for  deworming']* \
        inputs['Deworming']['% of years of childhood in which deworming is helpful for development']* \
        inputs['Deworming']['Proportion of dewormed children that benefit from long term gains']* \
        inputs['SCI']['Prevalence/ intensity adjustment']
    sci['Adjustment to calculations'] = \
        (np.maximum(sci['Aggregate adjustment to Baird development effect'], inputs['Shared']['Intuitive maximum adjustment']) \
        if inputs['Shared']['Cap adjustment at intuitive maximum'] else sci['Aggregate adjustment to Baird development effect'])/ \
        sci['Aggregate adjustment to Baird development effect']
    sci['Adjusted total benefits, per person dewormed (Ln(income))'] = \
        inputs['SCI']['Adjustment for benefit varying by treatment frequency'] * \
        (deworming['Adjusted long term benefits per year of treatment (in terms of ln $), assuming income supports household consumption']* \
        sci['Adjustment to calculations']* \
        inputs['SCI']['Proportion of deworming going to children']* \
        inputs['SCI']['Prevalence/ intensity adjustment'] + \
        deworming['Short term health benefits (deworming only) in terms of Ln(income)']* \
        inputs['SCI']['Prevalence/ intensity adjustment'])
    sci['Proportional increase in consumption per dollar'] = \
        sci['Adjusted total benefits, per person dewormed (Ln(income))']/ \
        (inputs['SCI']['Cost per person dewormed']/ \
        inputs['SCI']['Leverage (dollar of impact per dollar spent)'])
    sci['Cost per equivalent life saved'] = \
        inputs['Shared']['1 DALY is equivalent to increasing ln(income) by one unit for how many years']* \
        inputs['Shared']['DALYs per death of a young child averted']/ \
        sci['Proportional increase in consumption per dollar']
    sci['X as cost effective as Cash'] = \
        sci['Proportional increase in consumption per dollar']/cash['Proportional increase in consumption per dollar']
    #sci_p = stats.lognorm.fit(sci['X as cost effective as Cash'])
    #sci_d = stats.lognorm(*sci_p[:-2], loc=sci_p[-2], scale=sci_p[-1])
    bednets['Proportional increase in consumption per dollar'] = \
        inputs['Bednets']['Alternative funders adjustment']* \
        ((1.0/bednets['Cost per person-year of protection, adjusted for insecticide resistance: under-14\'s only'])* \
        (1.0/inputs['Bednets']['Relative value of year of deworming treatment to development benefits from year of bednet coverage'])* \
        deworming['Adjusted long term benefits per year of treatment (in terms of ln $), assuming income supports household consumption'] + \
        (1.0/bednets['Cost per death averted'])* \
        inputs['Shared']['DALYs per death of a young child averted']* \
        inputs['Shared']['1 DALY is equivalent to increasing ln(income) by one unit for how many years'])
    bednets['Cost per equivalent life saved'] = \
        inputs['Shared']['1 DALY is equivalent to increasing ln(income) by one unit for how many years']* \
        inputs['Shared']['DALYs per death of a young child averted']/ \
        bednets['Proportional increase in consumption per dollar']
    bednets['X as cost effective as Cash'] = \
        bednets['Proportional increase in consumption per dollar']/cash['Proportional increase in consumption per dollar']
    #bednets_p = stats.lognorm.fit(bednets['X as cost effective as Cash'])
    #bednets_d = stats.lognorm(*bednets_p[:-2], loc=bednets_p[-2], scale=bednets_p[-1])
    
    iodine = {}
    iodine['Benefit on one year\'s income (discounted back 10 years because of delay between deworming and working for income)'] = \
        (inputs['Iodine']['% of benefit of iodine that lasts for the long term']* \
        inputs['Iodine']['Equivalent increase in wages from having iodine throughout childhood'])/ \
        np.power((1.0 + inputs['Shared']['Discount rate']),  inputs['Deworming']['Average number of years between deworming and the beginning of long term benefits - also used for iodine'])
    iodine['Present value of the sum of the lifetime benefits per worker (in terms of Ln(income))'] = \
        iodine['Benefit on one year\'s income (discounted back 10 years because of delay between deworming and working for income)']* \
        (1.0 - 1.0/np.power((1.0 + inputs['Shared']['Discount rate']), inputs['Deworming']['Duration of long term benefits of deworming (years) - also used for iodine']))/ \
        (1.0 - 1.0/(1.0 + inputs['Shared']['Discount rate']))
    iodine['Adjusted long term benefits per year of treatment (in terms of ln $), assuming income supports household consumption'] = \
        iodine['Present value of the sum of the lifetime benefits per worker (in terms of Ln(income))']* \
        inputs['Iodine']['Replicability']*inputs['Iodine']['External validity']* \
        inputs['Iodine']['% of children that benefit']* \
        (inputs['Iodine']['Percent of population under 15']/inputs['Iodine']['Years of Childhood (for iodine)'])* \
        inputs['Deworming']['Number of household members that benefit']
    iodine['Short term health benefits (deworming only) in terms of Ln(income)'] = 0.0
    iodine['Adjusted total benefits, per person dewormed (Ln(income))'] = \
        iodine['Adjusted long term benefits per year of treatment (in terms of ln $), assuming income supports household consumption']
    iodine['Proportional increase in consumption per dollar'] = \
        inputs['Iodine']['Probability that GAIN/ICCIDD has an impact']* \
        iodine['Adjusted total benefits, per person dewormed (Ln(income))']/ \
        (inputs['Iodine']['Cost per person per year']/inputs['Iodine']['Leverage (dollars of impact per dollars spent)'])
    iodine['X as cost effective as Cash'] = \
        iodine['Proportional increase in consumption per dollar']/cash['Proportional increase in consumption per dollar']
    
    #x = np.linspace(0.0, 30.0, 50)
    x = np.logspace(-1, 2, 100)
    #cash_y, cash_x = np.histogram(cash['Proportional increase in consumption per dollar']/np.median(cash['Proportional increase in consumption per dollar']), bins=x, density=True)
    bednets_y, bednets_x = np.histogram(bednets['X as cost effective as Cash'], bins=x, density=True)
    dtw_y, dtw_x = np.histogram(dtw['X as cost effective as Cash'], bins=x, density=True)
    sci_y, sci_x = np.histogram(sci['X as cost effective as Cash'], bins=x, density=True)
    iodine_y, iodine_x = np.histogram(iodine['X as cost effective as Cash'], bins=x, density=True)
    
    plt.figure(0,  figsize=(8, 6))
    #plt.plot((cash_x[:-1] + cash_x[1:])/2.0, cash_y, label='cash', color='k')
    plt.semilogx((bednets_x[:-1] + bednets_x[1:])/2.0, bednets_y, label='bednets', color='b')
    plt.semilogx((dtw_x[:-1] + dtw_x[1:])/2.0, dtw_y, label='dtw', color='g')
    plt.semilogx((sci_x[:-1] + sci_x[1:])/2.0, sci_y, label='sci', color='r')
    plt.semilogx((iodine_x[:-1] + iodine_x[1:])/2.0, iodine_y, label='iodine', color='m')
    plt.xlim([0, np.max(x)])
    plt.xlabel('X as cost effective as Cash')
    plt.ylabel('Probability')
    plt.title('PDF of cost effectiveness')
    plt.legend(loc='upper right')
    plt.show()
    
    key = 'X as cost effective as Cash'
    #data = np.log(np.array([bednets[key], dtw[key], sci[key], iodine[key]])).transpose()
    data = np.array([bednets[key], dtw[key], sci[key], iodine[key]]).transpose()
    #data = np.log(np.array([bednets[key], dtw[key], sci[key]])).transpose()
    df = pd.DataFrame(data, columns=['bednets', 'dtw', 'sci', 'iodine'])
    #df = pd.DataFrame(data, columns=['bednets', 'dtw', 'sci'])
    df.to_pickle('data.pickle')
    
    #x_max = np.max([bednets_d.ppf(0.9), dtw_d.ppf(0.9), sci_d.ppf(0.9)])
    #x = np.linspace(0, x_max, 100)
    #plt.plot(x, bednets_d.pdf(x), label='bednets', color='b')
    #plt.plot(x, dtw_d.pdf(x), label='dtw', color='g')
    #plt.plot(x, sci_d.pdf(x), label='sci', color='r')
    #plt.hist(sci_d.rvs(n), label='fit', bins=x, color='r')
    #plt.hist(sci['X as cost effective as Cash'], label='data', bins=x, color='w')
    #plt.xlim([0, x_max])
    #plt.legend(loc='upper right')
    #plt.show()
    