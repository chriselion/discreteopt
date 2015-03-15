from . import Graph

def solve_greedy_sub(g, offset):
    # For each node, get the color of its neighbors. Use the smallest color not in the set.
    colors = [-1] * g.get_num_nodes()
    for _n in xrange(0,  g.get_num_nodes()):
        n = (_n + offset) % g.get_num_nodes()
        node = g.nodes[n]
        neighbor_colors = set( colors[e] for e in node.edges  )
        for c in xrange(0, len(node.edges)+1):
            if c not in neighbor_colors:
                colors[n] = c
                break
        assert colors[n] != -1

    used_colors = set(colors)
    assert -1 not in used_colors
    assert len(used_colors) == max(used_colors)+1

    return len(used_colors), colors

def solve_greedy(node_count, edges):

    g = Graph(node_count, edges)
    best_num_colors = 100000
    best_colors = []

    for k in range(0, g.get_num_nodes()):
        num_colors, colors = solve_greedy_sub(g, k)
        if num_colors < best_num_colors:
            best_num_colors = num_colors
            best_colors = colors

    return best_num_colors, best_colors