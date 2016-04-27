"ALG thinking module 2"
import poc_queue
import alg_module2_graphs



def bfs_visited(ugraph, start_node):
    """
    bfs_visited(ugraph, start_node) 
    """
    #bfs_visited(ugraph, start_node) - 
    #Takes the undirected graph ugraph and the 
    #node start_node and returns the set consisting of 
    #all nodes that are visited by a breadth-first search 
    #that starts at start_node.
    visited = set([start_node])
    queue = poc_queue.Queue()
    queue.enqueue(start_node)
    while len(queue):
        node_i = queue.dequeue()
        for neighbor in ugraph[node_i]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.enqueue(neighbor)
    return visited
def cc_visited(ugraph):
    """              
    cc_visited(ugraph) - Takes the undirected graph ugraph and returns a list of sets,
    where each set consists of all the nodes (and nothing else) 
    in a connected component, and there is exactly one set in 
    the list for each connected component in ugraph and nothing else.      
    """
    visited_list = []
    remaining_nodes = [key for key in ugraph.keys()]
    while len(remaining_nodes):
        node = remaining_nodes[0]
        visited = bfs_visited(ugraph,node)
        visited_list.append(visited)
        for visited_node in visited:
            remaining_nodes.remove(visited_node)
    return visited_list
def largest_cc_size(ugraph):
    """
    Takes the undirected graph ugraph and returns the size (an integer)
    of the largest connected component in ugraph.
    """
    visited = cc_visited(ugraph)
    max_size = 0
    for size in visited:
        if max_size < len(size):
            max_size = len(size)
    return max_size
def compute_resilience(ugraph, attack_order):
    """
    compute_resilience(ugraph, attack_order) - Takes the undirected graph ugraph, 
    a list of nodes attack_order and iterates through the nodes in attack_order. 
    For each node in the list, the function removes the given node and its edges
    from the graph and then computes the size of the largest connected component 
    for the resulting graph.
    """
    print ugraph
    resilience_list = [largest_cc_size(ugraph)]
    for attack in attack_order:
        if attack in ugraph.keys():
            for edge in ugraph[attack]:
                ugraph[edge].remove(attack)
            ugraph.pop(attack)
        resilience_list.append(largest_cc_size(ugraph))
    return resilience_list
            
#print compute_resilience(alg_module2_graphs.GRAPH1,[2] )