from . import Graph

# Start with the node that has the maximum degree.
# Color the current node with the lowest available color.
# Select the next node by selecting the node with the maximum degree of saturation. This means that you have to select
#   the node that has the most number of unique neighboring colors. In case of a tie, use the node with the largest
#   degree.
# Goto step 2. until all nodes are colored.

def get_node_max_degree(g):
    max_deg = -1
    max_node = -1
    for i in xrange(0, g.get_num_nodes()):
        deg = len(g.nodes[i].edges)
        if deg > max_deg:
            max_deg = deg
            max_node = i
    return max_node

def get_node_max_satur(g, colors):
    max_node = -1
    max_satur = -1
    max_deg = -1
    for n, node in enumerate(g.nodes):
        if colors[n] != -1:
            continue
        neighbor_colors = set( colors[e] for e in node.edges ) - set([-1])
        satur = len(neighbor_colors)
        deg = len(node.edges)

        if (satur > max_satur) or (satur == max_satur and deg > max_deg):
            max_satur = satur
            max_deg = deg
            max_node = n

    return max_node

def get_lowest_color(g, colors, n):
    node = g.nodes[n]
    neighbor_colors = set( colors[e] for e in node.edges  )
    for c in xrange(0, len(node.edges)+1):
        if c not in neighbor_colors:
            return c
    raise Exception()

def solve_dsatur(node_count, edges):

    g = Graph(node_count, edges)
    colors = [-1] * g.get_num_nodes()
    cur = get_node_max_degree(g)

    while cur != -1:
        assert colors[cur] == -1
        colors[cur] = get_lowest_color(g, colors, cur)
        cur = get_node_max_satur(g, colors)

    num_colors = len(set(colors))
    return num_colors, colors