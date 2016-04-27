"""
Student template code for Project 3
Student will implement five functions:

slow_closest_pair(cluster_list)
fast_closest_pair(cluster_list)
closest_pair_strip(cluster_list, horiz_center, half_width)
hierarchical_clustering(cluster_list, num_clusters)
kmeans_clustering(cluster_list, num_clusters, num_iterations)

where cluster_list is a 2D list of clusters in the plane
"""

import math
import alg_cluster



######################################################
# Code for closest pairs of clusters

def pair_distance(cluster_list, idx1, idx2):
    """
    Helper function that computes Euclidean distance between two clusters in a list

    Input: cluster_list is list of clusters, idx1 and idx2 are integer indices for two clusters
    
    Output: tuple (dist, idx1, idx2) where dist is distance between
    cluster_list[idx1] and cluster_list[idx2]
    """
    return (cluster_list[idx1].distance(cluster_list[idx2]), min(idx1, idx2), max(idx1, idx2))


def slow_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (slow)

    Input: cluster_list is the list of clusters
    
    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.       
    """
    distance = (float("inf"), -1 ,-1 )
    for idx1 in range(len(cluster_list)):
        for idx2 in range(len(cluster_list)):
            if idx1 != idx2:
                calc_distance = pair_distance(cluster_list,idx1,idx2)
                if distance[0] > calc_distance[0]:
                    distance = calc_distance
    return distance



def fast_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (fast)

    Input: cluster_list is list of clusters SORTED such that horizontal positions of their
    centers are in ascending order
    
    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.       
    """
    distance = (float("inf"), -1 ,-1 )
    cluster_len = len(cluster_list)
    if  cluster_len <= 3:
        distance = slow_closest_pair(cluster_list)
    else:
        m_ind = int(cluster_len//2)
        p_left = cluster_list[:m_ind]
        p_right = cluster_list[m_ind:]
        distance_left = fast_closest_pair(p_left)
        distance_right = fast_closest_pair(p_right)
        if distance_left[0] > distance_right[0] :
            distance = (distance_right[0],distance_right[1] + m_ind,distance_right[2] + m_ind)
        else:
            distance = distance_left
        mid = (cluster_list[m_ind].horiz_center() + cluster_list[m_ind-1].horiz_center() )/2
        strip_distance = closest_pair_strip(cluster_list,mid,distance[0])
        if strip_distance[0] < distance[0] :
            distance = strip_distance
    return distance


def closest_pair_strip(cluster_list, horiz_center, half_width):
    """
    Helper function to compute the closest pair of clusters in a vertical strip
    
    Input: cluster_list is a list of clusters produced by fast_closest_pair
    horiz_center is the horizontal position of the strip's vertical center line
    half_width is the half the width of the strip (i.e; the maximum horizontal distance
    that a cluster can lie from the center line)

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] lie in the strip and have minimum distance dist.       
    """
    distance = (float("inf"), -1 ,-1 )
    strip_list = [  idx for idx in range(len(cluster_list)) 
                  if  math.fabs(cluster_list[idx].horiz_center() - horiz_center) < half_width]
    strip_list.sort(key = lambda idx: cluster_list[idx].vert_center())
    k_len = len(strip_list)
    for u_ind  in range(k_len-1):
        for v_ind in range(u_ind + 1 , min(u_ind+4,k_len)):
            strip_distance = pair_distance(cluster_list,strip_list[u_ind],strip_list[v_ind])
            if strip_distance[0] < distance[0]:
                distance = strip_distance
    return distance
######################################################################
# Code for hierarchical clustering


def hierarchical_clustering(cluster_list, num_clusters):
    """
    Compute a hierarchical clustering of a set of clusters
    Note: the function may mutate cluster_list
    
    Input: List of clusters, integer number of clusters
    Output: List of clusters whose length is num_clusters
    """
    while len(cluster_list) > num_clusters:
        cluster_list.sort(key = lambda cluster: cluster.horiz_center())
        distance = fast_closest_pair(cluster_list)
        cluster_list[distance[1]].merge_clusters(cluster_list[distance[2]])
        cluster_list.pop(distance[2])
    return cluster_list


######################################################################
# Code for k-means clustering

    
def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    """
    Compute the k-means clustering of a set of clusters
    Note: the function may not mutate cluster_list
    
    Input: List of clusters, integers number of clusters and number of iterations
    Output: List of clusters whose length is num_clusters
    """    
    def nearest_cluster(point, clusters):
        """Nearest cluster for point"""
        nearist_idx = -1
        min_distance = float('inf')
        for idx, cluster in enumerate(clusters):
            if point.distance(cluster) < min_distance:
                min_distance = point.distance(cluster)
                nearist_idx = idx
        return nearist_idx
    
    num_n = len(cluster_list)
    centers = [idx.copy() for idx in cluster_list]
    centers.sort(key = lambda idx: idx.total_population(),reverse=True)
    centers = centers[:num_clusters]

    for dummy_iteration in range(num_iterations):
        set_k = [alg_cluster.Cluster(set(), 0, 0, 0, 0) for dummy_cluster in range(num_clusters)]
        for idx_j in range(num_n):
            nearest = nearest_cluster(cluster_list[idx_j], centers)
            set_k[nearest].merge_clusters(cluster_list[idx_j])

        for idx_j,cluster_k in enumerate(set_k):
            centers[idx_j] = cluster_k.copy()

    return centers 

