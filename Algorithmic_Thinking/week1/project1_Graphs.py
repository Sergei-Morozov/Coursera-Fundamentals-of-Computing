"""
Distrubed Graph
"""

EX_GRAPH0 ={0: set([1, 2]),
             1: set([]),
             2: set([])}

EX_GRAPH1 ={0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3]),
             3:set([0]),
             4: set([1]),
             5:set([2]),           
             6: set([])}
EX_GRAPH2 ={0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3,7]),
             3:set([7]),
             4: set([1]),
             5:set([2]),           
             6: set([]),
             7: set([3]),
             8:set([1,2]),           
             9: set([0,4,5,6,7,3])}

def make_complete_graph(num_nodes):
    """
    returns a dictionary corresponding to a complete directed 
    graph with the specified number of nodes.
    """
    result = {0: set([])}
    for node in range(num_nodes):
        result[node] = set([num for num in range(num_nodes) if num != node])
        
    return result
def compute_in_degrees(digraph):
    """
    Takes a directed graph digraph (represented as a dictionary) 
    and computes the in-degrees for the nodes in the graph.
    """
    result =  dict([(key, 0) for key in digraph])
    
    for key in digraph:
        for num in digraph[key]:
            result[num] =  1 + result[num]
    return result

def in_degree_distribution(digraph):
    """
    Takes a directed graph digraph (represented as a dictionary)
    and computes the unnormalized distribution of the in-degrees of the graph.
    """
    digraph = compute_in_degrees(digraph)
    result = {}
    for indegree in digraph.values():
        result[indegree] = 1 + result.get(indegree,0) 
    return result

print in_degree_distribution(EX_GRAPH0)


    
    
    
    
    
    
    
    
    
    
    
    
    
    