#
# Created by 14chanwa on 2017.02.25
#

# Project Euler - Problem 107
# Minimal network

import math
import numpy as np


f = open('p107_network.txt', 'r')
network_file = f.read()

# Create graph matrix
network_tmp = list(map(str, network_file.split("\n")))
network_list = []
for line in network_tmp:
    if line != "":
        network_list += [0 if s == '-' else int(s) for s in list(map(str, line.split(",")))]

network = np.array(network_list)
network.shape = (int(math.sqrt(len(network_list))), -1)

# print(network)


def recursive_search(graph_network, current_node, reached_nodes, ignore_node=(0, 0)):
    """
    Reach all possible nodes
    :param graph_network:
    :param current_node:
    :param reached_nodes:
    :param ignore_node: Ignore this node in the process
    :return:
    """
    # print(reached_nodes)
    graph_line = graph_network[current_node]
    for index in range(len(graph_line)):
        if index not in reached_nodes \
                and graph_network[current_node, index] != 0 \
                and (index, current_node) != ignore_node\
                and (current_node, index) != ignore_node:
            reached_nodes.append(index)
            recursive_search(graph_network, index, reached_nodes)


def is_connected(graph_network, ignore_node=(0, 0)):
    """
    Checks if the provided graph is connected using a depth graph search.
    :param graph_network:
    :param ignore_node: Ignore this node in the process
    :return:
    """
    # For each point checks the reachable points.
    # If one point is missing, then the graph is not connected.
    # TODO: could be optimized excluding some nodes from previous searches, eg if 1 is linked to 2 then 2 is linked to 1
    for i in range(0, graph_network.shape[0]):
        reached_nodes = [i]
        recursive_search(graph_network, i, reached_nodes, ignore_node)
        if len(reached_nodes) < graph_network.shape[0]:
            return False
    return True

# print(is_connected(network))


def problem107(graph_network):

    initial_sum = graph_network.sum()

    # Store the available links along with the corresponding weights
    weights_links = {}
    for i in range(0, graph_network.shape[0]):
        for j in range(i + 1, graph_network.shape[0]):
            weight = graph_network[i, j]
            if weight > 0:
                if weight in weights_links.keys():
                    weights_links[weight].append((i, j))
                else:
                    weights_links[weight] = [(i, j)]

    available_weights = sorted(list(weights_links.keys()), reverse=True)

    # For each weight, lookup nodes
    # For each node, try to remove the link and check if the graph is still connected
    for weight in available_weights:
        for node in weights_links[weight]:
            if is_connected(graph_network, node):
                graph_network[node[0], node[1]] = 0
                graph_network[node[1], node[0]] = 0

    # print(graph_network)

    return (initial_sum - graph_network.sum()) // 2

print(problem107(network))
