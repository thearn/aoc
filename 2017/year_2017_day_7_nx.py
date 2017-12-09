"""
Day 7: 'Recursive Circus' https://adventofcode.com/2017/day/7.

Want to try and learn networkx for the 2nd part instead of rolling my own stuff.
Will save both solutions.
"""

# https://networkx.github.io/documentation/networkx-1.10/reference/algorithms.shortest_paths.html

import pytest
import networkx as nx
from scipy.stats import mode
from year_2017_day_7 import main_inp, test_1

def get_child_weights(G, name):
    """Get list of weights of all children of selected node in G."""
    return [G.nodes[name]['weight'] for name in nx.descendants(G, name)]

def get_weight(G, name):
    """Get weight of selected node in G."""
    return G.nodes[name]['weight'] + sum(get_child_weights(G, name))

def get_level_weights(G, name):
    """Get the weights of direct neighbor nodes."""
    level_weights = []
    neighbors = [i for i in nx.neighbors(G, name)]
    for sub_node in neighbors:
        level_weights.append(get_weight(G, sub_node))
    return level_weights

def has_matching_child_weights(G, name):
    """Returns True if weight of all child nodes match."""
    level_weights = get_level_weights(G, name)
    if len(level_weights) and len(set(level_weights)) > 1:
        return False
    return True

def get_faulty(G, name):
    """Returns the name of any child node whose weight does not match its siblings."""
    neighbors = [i for i in nx.neighbors(G, name)]
    level_weights = get_level_weights(G, name)
    target_weight = mode(level_weights)[0]
    for w in level_weights:
        if w != target_weight:
            faulty_idx = level_weights.index(w)
            return neighbors[faulty_idx]

def day_7_2017_part_2(seq):
    """Solve the problem with networkx help."""
    # build the graph
    seq_list = seq.split('\n')
    G = nx.DiGraph()
    for step in seq_list:
        name = step.split()[0]
        weight = int(step.split('(')[1].split(')')[0])

        if name not in G:
            G.add_node(name, weight=weight)
        else:
            G.nodes[name]['weight'] = weight

        step = step.split("->")
        if len(step) > 1:
            connections = [i.strip() for i in step[1].split(",")]
            for sub_name in connections:

                if sub_name not in G:
                    G.add_node(sub_name, weight=0)
                G.add_edge(name, sub_name)

    # traverse graph to find the faulty one
    for node in G:
        if not has_matching_child_weights(G, node):
            faulty_node = get_faulty(G, node)
            if has_matching_child_weights(G, faulty_node):
                target_weight = mode(get_level_weights(G, node))[0]
                sub_weights = sum(get_level_weights(G, faulty_node))
                return target_weight - sub_weights

@pytest.mark.parametrize('method, inp, expected', [

    (day_7_2017_part_2, test_1, 60),
    (day_7_2017_part_2, main_inp, 1864),
])
def test_day_7_2017_cases(method, inp, expected):
    """Test both parts."""
    assert method(inp) == expected


if __name__ == '__main__':
    # show solution
    print('day_7_2017_part_2 solution:', day_7_2017_part_2(main_inp))

    # run verification tests
    pytest.main(['-x', '-l', __file__])
