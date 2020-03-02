import math,time
import numpy as np

def great_circle_numpy(mat):
    """numpys great circle"""
    radius = 3956
    x = np.pi/180.0
    lon1 = mat[:,0]
    lat1 = mat[:,1]
    lon2 = mat[:,2]
    lat2 = mat[:,3]

    a = (90.0-lat1)*(x)
    b = (90.0-lat2)*(x)
    theta = (lon2-lon1)*(x)
    c = np.arccos((np.cos(a)*np.cos(b)) +
                  (np.sin(a)*np.sin(b)*np.cos(theta)))
    return radius*c

## create the matrix
lon1,lat1,lon2,lat2 = 42,0.5,-13,-32
n = int(1e06)
mat = np.zeros((n,4),)
mat = mat + [lon1,lat1,lon2,lat2]

for i in range(mat.shape[0]):
    x = great_circle_numpy(*mat[i,:])
