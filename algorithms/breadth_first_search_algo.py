"""

Breadth First Search Algorithm

BFS is same as 'level-search' in Binary Tree
BFS uses a queue for the traversal

 Basically the idea here is to traverse the nodes in layers
 Step1: Initially marks all the vertices as not visited and create a queue
        Push the source node into queue and marked visited = True

 Step2: Loop until the queue is not empty
        pop the top the node from the stack and check whether it is visited or not we mark as visited
        Traverse through the entire adjacency list and if we got non visited node we push it back to the queue and
        marked them as visited at the same time
"""

from collections import defaultdict


def print_bfs_graph_recursion(edge, val):
    visited_edges = [False] * (max(edge) + 1)
    queue = [val]
    bfs_util_recursion(queue, visited_edges, edge)


def bfs_util_recursion(queue, visited_edges, edge):
    while len(queue) != 0:
        top = queue[-1]
        visited_edges[top] = True
        print(top)

        pop = queue.pop()

        for i in edge[pop]:
            if not visited_edges[i]:
                queue.append(i)
                visited_edges[i] = True
        bfs_util_recursion(queue, visited_edges, edge)


def print_bfs_graph_iterative(edge, val):
    queue = [val]
    visited = [False] * (max(edge) + 1)

    visited[val] = True

    while queue:
        pop = queue.pop()
        print(pop)

        for i in edge[pop]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


if __name__ == '__main__':
    edges = defaultdict(list)
    edges[0].append(1)
    edges[0].append(2)
    edges[1].append(2)
    edges[2].append(0)
    edges[2].append(3)
    edges[3].append(3)
    print_bfs_graph_recursion(edges, 2)

    edges = defaultdict(list)
    edges[0].append(1)
    edges[0].append(2)
    edges[1].append(2)
    edges[2].append(0)
    edges[2].append(3)
    edges[3].append(3)
    print_bfs_graph_iterative(edges, 2)


