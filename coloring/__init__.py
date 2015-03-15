class Node(object):
    def __init__(self, orginal_index = -1):
        self.original_index = orginal_index
        self.edges = set()

    def get_degree(self):
        return len(self.edges)

class Graph(object):
    def __init__(self, num_nodes, edge_list):
        self.nodes = []
        for n in xrange(0, num_nodes):
            self.nodes.append(Node(n))

        for node_a, node_b in edge_list:
            self.nodes[node_a].edges.add(node_b)
            self.nodes[node_b].edges.add(node_a)

    def get_num_nodes(self):
        return len(self.nodes)
