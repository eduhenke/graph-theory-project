# Knight's tour model
# https://en.wikipedia.org/wiki/Knight%27s_tour

import sys
sys.path.append(sys.path[0] + "/..")
from graph.graph import Graph

# logic from http://www.inf.ufsc.br/grafos/temas/hamiltoniano/cavalo.htm
def horse_movement(l_a, c_a, l_b, c_b):
    return all([
        (abs(l_a - l_b) + abs(c_a - c_b)) == 3,
        l_a != l_b,
        c_a != c_b
    ])

V = {(l,c) for l in range(8) for c in range(8)}
E = {((l_a, c_a), (l_b, c_b)) for (l_a, c_a) in V for (l_b, c_b) in V if horse_movement(l_a, c_a, l_b, c_b)}

g = Graph(V, E)
print(g)