import unittest
from graph.graph import Graph

connected_with_cycle = Graph({1, 2, 3}, {(1, 2), (1, 3), (2, 3)}, directed=False)
tree = connected_without_cycle = Graph({1, 2, 3}, {(1, 2), (1, 3)}, directed=False)
unconnected = Graph({1, 2, 3, 4}, {(1, 2), (1, 3)}, directed=False)
dag = Graph({2, 3, 7, 8, 5, 11, 10, 9}, {(7, 11), (7, 8), (5, 11), (3, 8), (3, 10), (11, 2), (11, 9), (11, 10), (8, 9)}, directed=True)

class TestDerivedMethods(unittest.TestCase):
    def test_hascycle(self):
        self.assertTrue(connected_with_cycle.has_cycle())
        self.assertFalse(tree.has_cycle())
        self.assertFalse(unconnected.has_cycle())
        self.assertFalse(dag.has_cycle())
    def test_tree(self):
        self.assertFalse(connected_with_cycle.is_tree())
        self.assertTrue(tree.is_tree())
        self.assertFalse(unconnected.is_tree())
        self.assertTrue(dag.is_tree())
    def test_topological_sorting(self):
        G = dag
        for v in G.topological_sorting():
            self.assertEqual(G.in_degree(v), 0)
            G.remove_vertex(v)

if __name__ == '__main__':
    unittest.main()
