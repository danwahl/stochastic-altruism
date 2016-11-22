# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 20:16:53 2016

@author: dan
"""

import numpy as np

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
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
    ea_data = pd.read_pickle('data.pickle')
    ace_data = pd.read_pickle('ace_data.pickle')
    
    #data = pd.concat([ea_data, ace_data], axis=1)
    data = ea_data
    n = data.shape[1]
    N = 1000
    
    #t = data['bednets'].mean()
    t = 1.5
    
    # individual returns
    p = data.mean().as_matrix()
    #t = np.min(p)
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
    sr = (rm - 0.0)/vm
    it = np.argmax(sr)
    vt = v[hull.vertices][it]
    rt = r[hull.vertices][it]
    xt = x[hull.vertices][it]
        
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
    plt.figure(0, figsize=(8, 6))
    plt.axis([0.0, np.max(s)*1.1, 0.0, np.max(p)*1.1])
    plt.plot(v, r, '.', color='k', alpha=0.1)
    plt.plot([0, vt], [0.0, rt], 'k-', label='tangency')
    plt.plot(vm[im1:im0+1], rm[im1:im0+1], 'c-', label='optimal')
    plt.plot(vm[im0], rm[im0], 'yo', label='mvp')
    for j in range(n):
        plt.plot(s[j], p[j], 'o', label=data.columns[j], color=colors[j])
    
    plt.legend(loc='lower left', ncol=3, numpoints=1)
    plt.title('GiveWell charity portfolios')
    plt.xlabel('x')
    plt.ylabel('y')
    
    plt.figure(1, figsize=(8, 6))
    plt.axis('equal')
    patches, texts = plt.pie(xm, colors=colors, startangle=90)
    plt.legend(patches, labels=['{} ({:2.1%})'.format(data.columns[i], xm[i]) for i in range(n)], loc='best')
    #plt.title('Minimum variance portfolio')
    
    '''
    nf = 5
    tf = np.linspace(0.0, 1.0, nf)    
    fig, ax = plt.subplots(1, nf, figsize=(8, 2))
    fig.suptitle("Tangency portfolios, varying Cash", fontsize="x-large")
    for j in range(nf):
        xtf = np.append((xm*tf[j]), (1.0 - tf[j]))
        patches = ax[j].pie(xtf, colors=colors, startangle=90)  
        ax[j].axis('equal')
        ax[j].set_xlabel('{:2.1%}'.format(1.0 - tf[j]))
    
    '''
    plt.show()