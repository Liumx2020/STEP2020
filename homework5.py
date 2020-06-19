import numpy as np
import random
import matplotlib.pyplot as plt
import copy



xlist = [214.9827906,1222.03939,792.6961393,1042.548756,150.1753388]
ylist = [762.6903632,229.5621232,404.5419583,709.851016,25.51272887]

def tsp(xlist,ylist,loop_N):
    length = len(xlist)
    path_order = np.arange(0,length,1)
    old_order = copy.deepcopy(path_order)

    for i in range(loop_N):
        new_order = Mutation_order(path_order)

        ans = Accept_Reject_Function(old_order,new_order)
        if ans == 1:
            old_order = copy.deepcopy(new_order)
    
    return old_order
        





# comparing MCMC (M-H), Simulated Annealingh(SA) have a extra parameter T to address the Accept_Rate
# However, MCMC (M-H) has the guarantee of convergence. SA seems not to gurantee convergence.(not sure)
def Accept_Reject_Function(old_order,new_order):
    dist0 = DistanceSum(xlist,ylist,old_order)
    dist1 = DistanceSum(xlist,ylist,new_order)
    E0 = -1*dist0/1000000
    E1 = -1*dist1/1000000

    # probalility function: P = 1/z*exp(E), r = P_new / P_old
    r = np.exp(E1) / np.exp(E0)

    # accept rare = min(1,r)
    if (r < np.random.rand()):
        # stand in old
        return 0
    else:
        # move to new
        return 1



# sum(distance**2)
def DistanceSum(xlist,ylist,order):
    length = len(xlist)
    sum0 = 0
    path_order = order
    for i in range(length-1):
        sum0 += (xlist[path_order[i]]-xlist[path_order[i+1]])**2 + (ylist[path_order[i]]-ylist[path_order[i+1]])**2
    return sum0

#  exchange 2 node's order once
def Mutation_order(order):
    length = len(order)
    a,b = 0,0
    path_order = order
    while (a == b):
        a = int(np.random.uniform(1,length))
        b = int(np.random.uniform(1,length))
    temp = copy.deepcopy(path_order[a])
    path_order[a] = copy.deepcopy(path_order[b])
    path_order[b] = copy.deepcopy(temp)
    return path_order






