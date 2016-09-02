# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 20:16:53 2016

@author: dan
"""

import numpy as np

import matplotlib.pyplot as plt
#from matplotlib.patches import Ellipse
plt.style.use('ggplot')

#import cvxopt as opt
#from cvxopt import solvers
#solvers.options['show_progress'] = False

import pandas as pd

from scipy.spatial import ConvexHull

'''
def portfolio_solver(S, p=np.empty(0), r=0.0):
    n = S.shape[0]    
    
    # quadratic solver inputs
    P = 2.0*opt.matrix(S)
    q = opt.matrix(0.0, (n, 1))
    
    # inequality constraints
    G = -opt.matrix(np.eye(n))   # negative n x n identity matrix
    h = opt.matrix(0.0, (n, 1))
    
    # equality constrations
    if p.size == n:
        A = opt.matrix(np.vstack((p, np.ones((1, n)))), (2, n))
        b = opt.matrix([r, 1.0])
    # minimum variance portfolio
    else:
        A = opt.matrix(1.0, (1, n))
        b = opt.matrix(1.0)
    
    # solver
    ret = solvers.qp(P, q, G, h, A, b)   
    
    if ret['status'] == 'optimal':
        return np.array(ret['x'])
    else:
        return np.empty(0)
'''
def downside_risk(x, t):
    return np.sqrt(np.power(np.minimum(0.0, x - t), 2.0).sum()/x.size)

if __name__ == '__main__':
    data = pd.read_pickle('data.pickle')
    n = data.shape[1]
    N = 1000
    
    #t = 1.0
    
    # individual returns
    p = data.mean().as_matrix()
    t = np.min(p)
    s = data.apply(lambda x: downside_risk(x, t), axis=0).as_matrix()
    #s = data.std().as_matrix()
    
    # random portfolios
    #x = np.random.random([N, n])
    #x = np.divide(x, np.sum(x, axis=1).reshape(N, 1))
    x = np.random.dirichlet(np.ones(n)/2.5, N)
    
    # portfolio returns
    r = np.zeros(N)
    v = np.zeros(N)
    for j in range(N):
        d = data.dot(x[j]).as_matrix()
        r[j] = np.mean(d)
        v[j] = downside_risk(d, t)
        #v[j] = np.std(d)
        
    # optimal portfolios
    hull = ConvexHull(np.vstack((v, r)).transpose())
    vm = v[hull.vertices]
    rm = r[hull.vertices]
    im0 = np.argmin(vm)
    im1 = np.argmax(rm)
    xm = x[hull.vertices][im0]
    
    # tangent portfolio
    sr = (rm - 1.0)/vm
    it = np.argmax(sr)
    vt = v[hull.vertices][it]
    rt = r[hull.vertices][it]
    xt = x[hull.vertices][it]
        
    colors = ['b', 'g', 'r', 'm']
    plt.figure(0, figsize=(8, 6))
    plt.axis([0.0, 2.5, 0, 13])
    plt.plot(v, r, '.', color='k', alpha=0.05)
    plt.plot([0, vt], [1.0, rt], 'y-', label='tangency')
    plt.plot(vm[im1:im0+1], rm[im1:im0+1], 'c-', label='optimal')
    plt.plot(vm[im0], rm[im0], 'ko', label='mvp')
    for j in range(n):
        plt.plot(s[j], p[j], 'o', label=data.columns[j], color=colors[j])
    
    plt.legend(loc='lower right', ncol=3, numpoints=1)
    plt.title('GiveWell charity portfolios')
    plt.xlabel('Variability')
    plt.ylabel('X as cost effective as Cash')

    
    '''    
    p = data.mean().as_matrix()
    
    S = data.cov().as_matrix()
    #s = data.std().as_matrix()
    s = data.apply(lambda x: downside_risk(x, t), axis=0).as_matrix()
    
    # minimum variance portfolio
    xm = portfolio_solver(S)
    dm = np.multiply(data.as_matrix(), xm.transpose()).sum(axis=1)
    rm = dm.mean()
    vm = downside_risk(dm, t)
    
    # returns and variability
    #rm = np.dot(p, xm)[0]
    #vm = np.sqrt(np.dot(xm.T, np.dot(S, xm))).flatten()[0]
    
    # grid for markowitz curve
    N = 100
    ra = np.linspace(rm, p.max(), N)
    
    # generate curve
    va = np.zeros(ra.shape)
    xa = np.zeros((ra.size, n))
    for j in range(N):
           x = portfolio_solver(S, p, ra[j])
           d = np.multiply(data.as_matrix(), x.transpose()).sum(axis=1)
           if x.size:
               xa[j, :] = x.transpose()
               #va[j] = np.sqrt(np.dot(x.T, np.dot(S, x)))
               va[j] = downside_risk(d, t)
           else:
               xa[j, :] = np.zeros(n)
               va[j] = np.inf
           
    # tangency portfolio
    sr = ra/va
    it = sr.argmax()
    #rt = ra[it]  
    #vt = va[it]
    xt = xa[it, :]
    
    yt = np.linspace(0.0, 1.0, N)
    rt = ra[it]*yt
    vt = va[it]*yt
    
    # plot
    colors = ['b', 'g', 'r', 'm']
    plt.figure(0, figsize=(8, 6))
    #plt.axis([0.0, 1, 1, 10])
    for j in range(n):
        plt.plot(s[j], p[j], 'o', label=data.columns[j], color=colors[j])
    plt.plot(va, ra, '-', label='optimal', color='c')
    #plt.plot([0, vt], np.exp([0, rt]), 'o--', label='tangency', color='y')
    plt.plot(vt, rt, '-', label='tangency', color='y')
    plt.plot(vm, rm, 'o', label='mvp', color='k')

    #plt.grid(b=True, which='minor', linestyle='--')
    
    plt.legend(loc='lower right', ncol=3, numpoints=1)
    plt.title('GiveWell charity portfolios')
    plt.xlabel('Variability')
    plt.ylabel('X as cost effective as Cash')
    '''