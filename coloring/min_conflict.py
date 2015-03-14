from . import Graph

def get_conflict_for_node(n, graph, colors):
    num_conflicts = 0
    cur_color = colors[n]
    edges = graph.nodes[n].edges
    for e in edges:
        num_conflicts += (1 if colors[e] == cur_color else 0)
    return num_conflicts

def get_all_conflicts(graph, colors):
    conflicts = []
    for n in xrange(0, graph.get_num_nodes()):
        conflicts.append(get_conflict_for_node(n, graph, colors))
    return conflicts

def solve_min_conflict(node_count, edges):

    g = Graph(node_count, edges)
    # Start the same color. This will cause a lot of conflicts.
    colors = [0] * node_count

    conflicts = get_all_conflicts(g, colors)
    num_item = 0
    num_colors = 1
    while sum(conflicts) > 0:
        #print "Colors:   %s" % colors
        #print "Conflicts %s" % conflicts

        # Get the most conflicting node
        worst_node = -1
        max_conflicts = -1
        for i, c in enumerate(conflicts):
            if c > max_conflicts:
                max_conflicts = c
                worst_node = i

        #print "Worst: %d conflicts for node %d" % (max_conflicts, worst_node)

        node_to_change = worst_node
        # Decide what color to change to
        best_new_conflicts = max_conflicts
        best_new_color = -1
        new_colors = list(colors)
        new_color_conflicts = []
        for new_color in xrange(0, num_colors):
            new_colors[node_to_change] = new_color
            new_conflicts = get_conflict_for_node(node_to_change, g, new_colors)
            if new_conflicts < best_new_conflicts:
                best_new_conflicts = new_conflicts
                best_new_color = new_color
            new_color_conflicts.append(new_conflicts)

        #print "New conflicts: %s" % new_color_conflicts

        if best_new_conflicts < max_conflicts:
            # Reduced conflicts. That's good.
            #print "Changing color"
            new_colors[node_to_change] = best_new_color
            colors = new_colors
        else:
            # Couldn't reduce conflict. Add a new color so we eventually converge
            #print "Adding color"
            colors[node_to_change] = num_colors
            num_colors += 1

        # Recompute conflicts. Can probably do this faster.
        conflicts = get_all_conflicts(g, colors)

        #print

    return num_colors, colors