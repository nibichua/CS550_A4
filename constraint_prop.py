'''
Constraint propagation
'''
from csp_lib import csp

def AC3(csp, queue=None, removals=None):
    """AC3 constraint propagation
    
    """
    
    # Hints:
    # Remember that:
    #    csp.variables is a list of variables
    #    cps.neighbors[x] is the neighbors of variable x
    if queue != None:
            q = queue
    else:
        q = []
    #populate queue with binary arcs in CSP
    
    csp.support_pruning()
    
    for x in csp.variables:
        for y in csp.neighbors[x]:
            q.append((x,y))
    while q.__len__() != 0:
        (xi,xj) = q.pop() #get binary constraint
        if revise(csp,xi,xj,removals):
            if csp.curr_domains[xi] is None:
                return False
            else:
                for xk in (csp.neighbors[xi] - {xj}):
                    q.append((xk,xi))
    return True

def revise(csp,xi,xj,removals):
    revised = False
    for x in csp.curr_domains[xi]:
        if all(not csp.constraints(xi, x, xj, y) for y in csp.curr_domains[xj]):
            csp.prune(xi,x,removals)
            revised = True
    return revised