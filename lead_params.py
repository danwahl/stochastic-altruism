# -*- coding: utf-8 -*-
"""

"""

import json
import numpy as np

if __name__ == '__main__':
    # animals
    water = {'Water lead (mg/L)': {'dist': 'array', 'val': [0.001, 0.002, 0.003, 0.005, 0.01, 0.015, 0.03, 0.05, 0.1]}, \
        'Increase in BPb ug/dl': {'dist': 'array', 'val': [0.3, 0.6, 0.8, 1, 1.3, 1.5, 1.9, 2.2, 2.6]}, \
        '95% CI low': {'dist': 'array', 'val': [0.1, 0.3, 0.4, 0.5, 0.7, 0.8, 1, 1.1, 1.3]}, \
        '95% CI High': {'dist': 'array', 'val': [0.4, 0.9, 1.2, 1.5, 2, 2.3, 2.8, 3.3, 3.8]}
    }
    
    iq = {'Concurrent blood lead (ug/dL)': {'dist': 'array', 'val': [1, 5, 10, 15, 20, 25, 30, 35]}, \
        'IQ': {'dist': 'array', 'val': [100.90, 96.67, 94.83, 93.81, 93.10, 92.57, 92.14, 91.71]}, \
        '95% CI Low': {'dist': 'array', 'val': [97.28, 93.78, 91.90, 90.78, 89.90, 89.22, 88.69, 88.22]}, \
        '95% CI Low': {'dist': 'array', 'val': [104.11, 99.67, 97.86, 96.84, 96.17, 95.71, 95.35, 95.05]}
    }
    
    weight = {'IQ low': {'dist': 'array', 'val': [70, 50, 35, 20, 5]}, \
        'IQ high': {'dist': 'array', 'val': [84, 69, 49, 34, 20]}, \
        'Weight': {'dist': 'array', 'val': [0.090, 0.286, 0.430, 0.820, 0.760]}, \
        'CI low': {'dist': 'array', 'val': [0.137, 0.496, 0.518, 0.967, 0.980]}, \
        'CI high': {'dist': 'array', 'val': [0.040, 0.091, 0.353, 0.673, 0.534]}
    }
    
    chicago = {'Year': {'dist': 'array', 'val': [1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015]}, \
        'BLL > 5 ug/dL': {'dist': 'array', 'val': [0.6748, 0.6090, 0.5629, 0.5026, 0.4284, 0.4048, 0.3685, 0.3055, 0.2706, 0.2315, 0.1784, 0.1364, 0.1044, 0.0822, 0.0699, 0.0646, 0.0537, 0.0512, 0.0446]}, \
        'BLL > 10 ug/dL': {'dist': 'array', 'val': [0.2426, 0.1990, 0.1701, 0.1412, 0.1109, 0.0882, 0.0625, 0.0501, 0.0344, 0.0237, 0.0193, 0.0128, 0.0106, 0.0076, 0.0084, 0.0075, 0.0053, 0.0051, 0.0044]}, \
    }
    
    lsls = {'Year Disturbed': {'dist': 'array', 'val': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 2010, 2010, 2011, 2011, 2008, 2008, 2005, 2005, 2008, 2008, 2009, 2009, 2008, 2008, 2010, 2010, 2009, 2010, 2010, 2000, 2010, 2010, 2011, 2011]}, \
        '1': {'dist': 'array', 'val': [5.8, 8.3, 3.6, 2.5, 2.3, 2.2, 3.0, 1.9, 4.6, 4.8, 2.9, 3.0, 2.1, 2.3, 8.3, 7.0, 4.6, 6.6, 4.3, 3.5, 4.9, 3.1, 2.9, 1.5, 5.0, 4.6, 1.9, 7.0, 9.2, 2.6, 2.8, 4.9, 4.0, 11.1, 9.2, 10.4, 8.3, 3.7, 3.5, 2.4, 2.7, 8.1, 12.6, 3.9, 13.7, 17.6, 7.9, 4.0, 6.0, 2.9, 3.4]}, \
        '2': {'dist': 'array', 'val': [8.9, 5.6, 5.6, 2.2, 2.2, 2.6, 4.1, 7.7, 5.7, 5.1, 2.6, 3.1, 2.8, 2.9, 9.1, 8.0, 6.1, 8.8, 4.3, 3.8, 4.6, 2.3, 2.2, 1.7, 6.9, 5.0, 3.0, 10.5, 12.8, 6.7, 10.8, 5.5, 4.3, 12.8, 9.0, 18.0, 20.0, 5.2, 6.3, 8.5, 2.4, 9.1, 12.4, 5.6, 35.7, 36.7, 7.5, 5.0, 5.8, 7.9, 7.4]}, \
        '3': {'dist': 'array', 'val': [9.2, 5.2, np.nan, 2.3, 3.4, 2.8, 3.9, 9.0, 5.1, 4.9, 2.4, 2.8, 5.1, 5.6, 11.1, 9.0, 6.4, 7.3, 4.2, 4.0, 4.5, 2.1, 2.0, 1.7, 7.7, 5.5, 3.1, 24.8, 21.4, 14.0, 12.2, 6.3, 5.7, 21.6, 9.5, 20.8, 18.8, 5.4, 6.2, 7.1, 5.5, 9.8, 12.2, 5.4, 18.8, 18.3, 8.7, 5.1, 5.2, 12.9, 14.6]}, \
        '4': {'dist': 'array', 'val': [10.2, 6.4, 7.2, 2.6, 2.4, 3.0, 3.9, 3.6, 6.4, 5.5, 8.2, 3.8, 5.4, 5.4, 13.5, 11.0, 5.2, 6.4, 4.2, 3.9, 4.5, 2.3, 2.2, 1.6, 8.5, 6.1, 3.0, 27.8, 22.3, 17.3, 10.9, 6.7, 5.8, 19.7, 11.8, 20.0, 21.3, 6.5, 5.1, 7.2, 4.4, 10.3, 12.5, 5.3, 17.7, 17.3, 9.5, 6.2, 6.7, 11.9, 18.9]}, \
        '5': {'dist': 'array', 'val': [13.1, 8.5, 8.9, 2.4, 2.3, 3.4, 4.3, 2.5, 5.4, 4.8, 4.6, 3.3, 6.9, 6.3, 13.2, 12.5, 5.1, 6.5, 6.8, 3.9, 4.5, 7.0, 5.5, 1.7, 9.9, 13.0, 2.9, 27.5, 22.0, 16.5, 12.3, 7.0, 9.9, 32.0, 18.3, 17.9, 20.0, 14.9, 14.8, 7.3, 4.1, 10.4, 12.5, 5.4, 16.8, 16.6, 9.1, 13.1, 15.6, 9.9, 16.0]}, \
        '6': {'dist': 'array', 'val': [14.6, 14.9, 9.4, 2.8, 2.3, 3.6, 4.4, 3.9, 5.6, 8.2, 3.2, 3.4, 12.6, 8.5, 12.4, 12.1, 4.9, 6.6, 10.9, 4.0, 4.3, 15.5, 17.3, 2.7, 9.8, 11.6, 3.0, 24.3, 19.6, 9.9, 7.2, 22.9, 15.1, 33.5, 25.0, 17.0, 17.6, 23.6, 21.4, 10.5, 4.1, 11.4, 13.1, 5.1, 16.5, 15.9, 11.0, 15.4, 13.4, 8.6, 12.5]}, \
        '7': {'dist': 'array', 'val': [14.4, 19.6, 8.8, 2.7, 2.8, 3.7, 4.4, 3.0, 5.5, 8.6, 4.0, 5.8, 7.8, 7.4, 11.7, 12.8, 5.0, 6.8, 11.3, 4.0, 5.2, 9.9, 9.4, 2.9, 9.5, 10.3, 3.1, 22.6, 16.5, 6.7, 5.5, 23.6, 15.3, 32.2, 22.7, 15.8, 16.3, 22.4, 33.1, 9.9, 3.7, 13.1, 16.3, 5.7, 16.6, 15.9, 12.9, 15.6, 17.3, 7.3, 10.1]}, \
        '8': {'dist': 'array', 'val': [12.9, 16.4, 8.3, 2.6, 2.3, 3.8, 4.7, 2.2, 9.4, 8.7, 5.1, 6.0, 7.1, 7.2, 11.0, 11.8, 8.2, 10.6, 10.9, 4.0, 5.4, 9.3, 9.1, 2.9, 9.3, 10.4, 3.1, 17.8, 15.6, 6.3, 5.2, 19.7, 15.2, 28.9, 22.3, 14.7, 15.7, 21.9, 29.8, 9.6, 3.4, 13.9, 18.0, 5.7, 15.7, 14.3, 22.9, 16.3, 18.5, 6.8, 9.6]}, \
        '9': {'dist': 'array', 'val': [12.1, 15.4, 5.1, 3.6, 2.2, 4.3, 5.0, 2.9, 14.0, 11.6, 4.6, 6.2, 6.5, 6.6, 9.6, 10.5, 11.9, 14.5, 10.1, 4.1, 5.9, 8.3, 8.6, 3.2, 9.2, 10.9, 3.4, 19.5, 14.5, 6.0, 4.7, 16.3, 12.1, 32.1, 22.9, 14.3, 14.6, 23.9, 32.4, 22.6, 3.4, 14.2, 18.9, 5.3, 14.4, 16.2, 31.3, 20.8, 23.9, 6.2, 7.6]}, \
        '10': {'dist': 'array', 'val': [11.6, 14.3, 3.6, 5.3, 4.2, 4.1, 4.8, 7.6, 12.1, 11.6, 4.1, 5.2, 6.6, 7.1, 7.2, 12.1, 12.6, 13.2, 9.7, 4.4, 5.7, 6.1, 7.6, 2.1, 8.9, 10.3, 3.2, 20.0, 14.2, 5.7, 5.3, 16.2, 14.8, 29.7, 19.1, 12.9, 14.8, 20.2, 28.1, 23.3, 3.4, 13.3, 19.6, 5.5, 14.1, 12.8, 31.8, 18.8, 16.3, 5.3, 8.2]}, \
        '11': {'dist': 'array', 'val': [10.7, 17.1, 3.1, 4.7, 5.0, 4.1, 4.5, 5.7, 11.3, 11.4, 3.3, 3.8, 7.6, 7.4, 5.7, 10.1, 11.9, 12.8, 9.2, 4.3, 5.8, 2.6, 3.5, 1.9, 9.2, 9.9, 3.0, 21.1, 13.8, 5.7, 5.4, 16.7, 13.9, 24.2, 15.8, 11.5, 16.1, 20.7, 27.7, 24.7, 3.2, 12.2, 17.3, 5.6, 13.7, 13.2, 33.1, 7.9, 5.7, 5.0, 7.2]}, \
        '12': {'dist': 'array', 'val': [9.3, np.nan, 3.0, 4.8, np.nan, 4.4, np.nan, np.nan, 11.6, np.nan, 2.8, np.nan,7.5, np.nan, 5.4, np.nan, 12.2, 12.8, 8.8, 4.2, np.nan, 1.7, np.nan, np.nan, 9.2, np.nan, 3.8, 19.6, 13.9, 5.6, np.nan, 14.6, 12.7, 18.7, 12.8, 9.5, np.nan, 20.9, np.nan, 6.3, 2.8, 10.1, 16.0, np.nan, 13.4, 11.1, np.nan, 4.5, 4.2, 4.8, np.nan]}, \
        '13': {'dist': 'array', 'val': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 15.3, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 14.1, np.nan, np.nan, np.nan, 9.3, np.nan, 9.3, np.nan, np.nan, np.nan, 27.1, np.nan, 2.6, np.nan, 12.8, np.nan, np.nan, 10.1, np.nan, np.nan, np.nan, np.nan, np.nan]}, \
        '14': {'dist': 'array', 'val': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 15.4, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 11.7, np.nan, np.nan, np.nan, 6.5, np.nan, 7.9, np.nan, np.nan, np.nan, 21.1, np.nan, 2.6, np.nan, 9.2, np.nan, np.nan, 9.2, np.nan, np.nan, np.nan, np.nan, np.nan]}, \
        '15': {'dist': 'array', 'val': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 6.0, np.nan, 6.3, np.nan, np.nan, np.nan, 10.7, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 9.0, np.nan, np.nan, np.nan, np.nan, np.nan]}, \
        '16': {'dist': 'array', 'val': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 9.3, np.nan, np.nan, np.nan, np.nan, np.nan]}, \
        '17': {'dist': 'array', 'val': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 9.0, np.nan, np.nan, np.nan, np.nan, np.nan]}, \
        '18': {'dist': 'array', 'val': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 8.8, np.nan, np.nan, np.nan, np.nan, np.nan]}, \
        '19': {'dist': 'array', 'val': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 8.7, np.nan, np.nan, np.nan, np.nan, np.nan]}, \
        '20': {'dist': 'array', 'val': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 8.4, np.nan, np.nan, np.nan, np.nan, np.nan]}     
    }
    
    actuarial = {'Exact Age': {'dist': 'array', 'val': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119]}, \
        'Male Life expectancy': {'dist': 'array', 'val': [76.28, 75.78, 74.82, 73.84, 72.85, 71.87, 70.88, 69.89, 68.9, 67.9, 66.91, 65.92, 64.92, 63.93, 62.94, 61.96, 60.99, 60.02, 59.05, 58.09, 57.14, 56.2, 55.27, 54.33, 53.4, 52.47, 51.54, 50.61, 49.68, 48.75, 47.82, 46.89, 45.96, 45.03, 44.1, 43.17, 42.24, 41.31, 40.38, 39.46, 38.53, 37.61, 36.7, 35.78, 34.88, 33.98, 33.08, 32.19, 31.32, 30.44, 29.58, 28.73, 27.89, 27.05, 26.23, 25.41, 24.61, 23.82, 23.03, 22.25, 21.48, 20.72, 19.97, 19.22, 18.48, 17.75, 17.03, 16.32, 15.61, 14.92, 14.24, 13.57, 12.92, 12.27, 11.65, 11.03, 10.43, 9.85, 9.28, 8.73, 8.2, 7.68, 7.19, 6.72, 6.27, 5.84, 5.43, 5.04, 4.68, 4.34, 4.03, 3.74, 3.47, 3.23, 3.01, 2.82, 2.64, 2.49, 2.36, 2.24, 2.12, 2.01, 1.9, 1.8, 1.7, 1.6, 1.51, 1.42, 1.34, 1.26, 1.18, 1.11, 1.04, 0.97, 0.9, 0.84, 0.78, 0.72, 0.67, 0.61]}, \
        'Female Life expectancy': {'dist': 'array', 'val': [81.05, 80.49, 79.52, 78.54, 77.55, 76.56, 75.57, 74.58, 73.58, 72.59, 71.6, 70.6, 69.61, 68.62, 67.63, 66.64, 65.65, 64.67, 63.68, 62.7, 61.72, 60.75, 59.77, 58.8, 57.82, 56.85, 55.88, 54.91, 53.94, 52.97, 52.01, 51.04, 50.08, 49.11, 48.15, 47.19, 46.23, 45.28, 44.33, 43.37, 42.43, 41.48, 40.54, 39.6, 38.66, 37.73, 36.81, 35.89, 34.97, 34.06, 33.16, 32.27, 31.38, 30.49, 29.62, 28.74, 27.88, 27.01, 26.16, 25.31, 24.46, 23.62, 22.78, 21.95, 21.13, 20.32, 19.52, 18.73, 17.95, 17.18, 16.43, 15.68, 14.95, 14.23, 13.53, 12.83, 12.16, 11.5, 10.86, 10.24, 9.64, 9.05, 8.48, 7.94, 7.42, 6.92, 6.44, 5.99, 5.57, 5.17, 4.8, 4.45, 4.13, 3.84, 3.57, 3.34, 3.12, 2.93, 2.76, 2.6, 2.45, 2.3, 2.17, 2.03, 1.91, 1.78, 1.67, 1.56, 1.45, 1.35, 1.26, 1.17, 1.08, 1, 0.92, 0.85, 0.78, 0.72, 0.67, 0.61]}
    }
    
    filters = {'TDS': {'dist': 'array', 'val': [50, 200, 300, 400]}, \
        'Gallons': {'dist': 'array', 'val': [40, 25, 15, 8]}, \
        'Chicago TDS': {'dist': 'const', 'val': 175}, \
        'Gallons/child/day': {'dist': 'const', 'val': 1}, \
        'Children/house': {'dist': 'const', 'val': 2.5}, \
        'Days/intervention': {'dist': 'const', 'val': 60}, \
        'Filter cost': {'dist': 'const', 'val': 100.99/12}, \
        'Pitcher cost': {'dist': 'const', 'val': 30}, \
        'Filters/pitcher': {'dist': 'const', 'val': 1}
    }
    
    # parameters
    params = {'water': water, 'iq': iq, 'weight': weight, 'chicago': chicago, \
        'lsls': lsls, 'actuarial': actuarial, 'filters': filters
    }
    
    with open('lead_params.json', 'w') as fp:
        json.dump(params, fp, indent=4)