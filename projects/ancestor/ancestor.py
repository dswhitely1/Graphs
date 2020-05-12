graph = {

}

"""
 10
 /
1   2   4  11
 \ /   / \ /
  3   5   8
   \ / \   \
    6   7   9
"""


class Graph:
    def __init__(self):
        self.node = {}

    def add_node(self, value):
        if value not in self.node:
            self.node[value] = set()

    def add_edge(self, v1, v2):
        self.node[v1].add(v2)

    def get_neighbor(self, value):
        return self.node[value]

    def dfs(self, start, visited=None, path=None, result=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []
        if result is None:
            result = []
        path = path + [start]
        if len(self.get_neighbor(start)) == 0 and len(visited) == 0:
            return -1
        elif len(self.get_neighbor(start)) == 0:
            result.append((start, len(path)))
        for parent in self.get_neighbor(start):
            visited.add(start)
            self.dfs(parent, visited, path, result)
        return result


def earliest_ancestor(ancestors, starting_node):
    """
    Gets the Top Level most node
    :param ancestors: List of Tuples Describing the Path
    :param starting_node: The starting point in the graph
    :return: Returning the highest ancestor, -1 if at highest
    """
    g = Graph()
    # Load the Graph
    for ancestor in ancestors:
        g.add_node(ancestor[0])
        g.add_node(ancestor[1])
        g.add_edge(ancestor[1], ancestor[0])

    result = g.dfs(starting_node)
    max_value = 0
    new_result = None
    if result == -1:
        return result
    for data in result:
        if data[1] == max_value:
            if new_result is not None:
                if new_result[0] > data[0]:
                    new_result = data
            else:
                new_result = data
        elif data[1] > max_value:
            max_value = data[1]
            new_result = data

    return new_result[0]


ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(ancestors, 1))
print(earliest_ancestor(ancestors, 2))
print(earliest_ancestor(ancestors, 3))
print(earliest_ancestor(ancestors, 4))
print(earliest_ancestor(ancestors, 5))
print(earliest_ancestor(ancestors, 6))
print(earliest_ancestor(ancestors, 7))
print(earliest_ancestor(ancestors, 8))
print(earliest_ancestor(ancestors, 9))
print(earliest_ancestor(ancestors, 10))
print(earliest_ancestor(ancestors, 11))
