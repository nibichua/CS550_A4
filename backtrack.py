

from csp_lib.backtrack_util import (first_unassigned_variable, 
                                    unordered_domain_values,
                                    no_inference)
from csp_lib import csp
from csp_lib.csp import CSP
from _ast import Assign

def backtracking_search(csp,
                        select_unassigned_variable=first_unassigned_variable,
                        order_domain_values=unordered_domain_values,
                        inference=no_inference):
    """backtracking_search
    Given a constraint satisfaction problem (CSP),
    a function handle for selecting variables, 
    a function handle for selecting elements of a domain,
    and a set of inferences, solve the CSP using backtrack search
    """
    
    # See Figure 6.5] of your book for details

    def backtrack(assignment):
        """Attempt to backtrack search with current assignment
        Returns None if there is no solution.  Otherwise, the
        csp should be in a goal state.
        """
        if assignment.__len__() == csp.variables.__len__():
            return assignment #every variable has been assigned
        #decide which variable to work on
        var = select_unassigned_variable(assignment,csp)
        #pick value within variable
        for value in order_domain_values(var, assignment, csp):
            #does a conflict occur?
            if 0 == csp.nconflicts(var,value,assignment):
                #no conflict can assign
                csp.assign(var,value,assignment)
                #get removed values
                removals = csp.suppose(var,value)
                #if successfull inference, backtrack and print result
                if inference(csp, var, value, assignment, removals):
                    result = backtrack(assignment)
                    if result is not None: #successful backtrack
                        return result
                csp.restore(removals) #undo suppose
        csp.unassign(var,assignment)
        return None
        

    # Call with empty assignments, variables accessed
    # through dynamic scoping (variables in outer
    # scope can be accessed in Python)
    result = backtrack({})
    assert result is None or csp.goal_test(result)
    return result
