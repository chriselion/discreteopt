from dsatur import solve_dsatur
from collections import defaultdict
import random

class ReorderableNode(object):
    def __init__(self, orginal_index = -1):
        self.original_index = orginal_index
        self.edges = set()

    def get_degree(self):
        return len(self.edges)

class ReorderableGraph(object):
    def __init__(self, num_nodes, edge_list):
        self.nodes = []
        """:type : list of ReorderableNode"""
        for n in xrange(0, num_nodes):
            self.nodes.append(ReorderableNode(n))

        for node_a, node_b in edge_list:
            self.nodes[node_a].edges.add(self.nodes[node_b])
            self.nodes[node_b].edges.add(self.nodes[node_a])

    def get_num_nodes(self):
        return len(self.nodes)

class Coloring(object):
    def __init__(self):
        self.colors = {}
        self.colored_nodes = set()
        """:type : dict[ReorderableNode, int] """

    def realize(self, g):
        colors = [-1]*len(g.nodes)
        for node in g.nodes:
            colors[node.original_index] = self.colors[node]
        return colors

    def color_node(self, node, c):
        self.colors[node] = c
        self.colored_nodes.add(node)

    def get_neighbor_colors(self, node):
        return set( self.colors.get(e) for e in node.edges & self.colored_nodes )

def solve_iter_greedy(node_count, edges):
    random.seed(node_count)
    num_colors, colors = solve_dsatur(node_count, edges)

    num_iter = 5000
    g = ReorderableGraph(node_count, edges)
    coloring = Coloring()
    for node, c in zip(g.nodes, colors):
        coloring.colors[node] = c
    for i in xrange(0, num_iter):
        # Group by assigned color
        color_class = defaultdict(set)
        for node, c in coloring.colors.viewitems():
            color_class[c].add(node)

        grouped_by_color = list(color_class.values())
        random.shuffle(grouped_by_color)
        # flatten the list of sets
        new_nodes = [item for group in grouped_by_color for item in group]
        g.nodes = new_nodes
        #print [colors[n.original_index] for n in new_nodes]

        # Now do a greedy pass with this ordering
        coloring = Coloring()
        for node in g.nodes:
            neighbor_colors = coloring.get_neighbor_colors(node)
            for c in xrange(0, len(node.edges)+1):
                if c not in neighbor_colors:
                    coloring.color_node(node, c)
                    break

            #assert node in coloring.colors

    colors = coloring.realize(g)
    num_colors = len(set(colors))
    return num_colors, colors
