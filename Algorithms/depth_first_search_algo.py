"""

Depth First Search Algorithm

dfs is same as pre-order traversal in Binary Tree
dfs uses a stack for the traversal

 Step1: Initially marks all the vertices as not visited and create a stack
        Push the source node into it

 Step2: Loop until the stack is not empty
        pop the top the node from the stack and check whether it is visited or not we mark as visited
        Traverse through the entire adjacency list and if we got visited node we push it back to the stack
"""

from collections import defaultdict


def print_dfs_graph_recursion(edge, val):
    visited_edges = [False] * (max(edge) + 1)
    dfs_util_recursion(val, visited_edges, edge)


def dfs_util_recursion(v, visited_edges, edge):
    visited_edges[v] = True
    print v

    for i in edge[v]:
        if not visited_edges[i]:
            dfs_util_recursion(i, visited_edges, edge)


def print_dfs_graph_iterative(nodes, start):
    stack = [start]
    visited = [False] * (max(nodes) + 1)

    while len(stack) != 0:
        pop = stack.pop()

        if not visited[pop]:
            print pop
            visited[pop] = True

        for i in nodes[pop]:
            if not visited[i]:
                stack.append(i)


if __name__ == '__main__':
    edges = defaultdict(list)
    edges[0].append(1)
    edges[0].append(2)
    edges[1].append(2)
    edges[2].append(0)
    edges[2].append(3)
    edges[3].append(3)
    print_dfs_graph_recursion(edges, 2)

    node = defaultdict(list)
    node[0].append(2)
    node[0].append(3)
    node[1].append(0)
    node[2].append(1)
    node[3].append(4)
    node[4].append(0)
    print_dfs_graph_iterative(node, 0)
