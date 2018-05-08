import unittest
from graph.graph import Graph

connected_with_cycle = Graph({1, 2, 3}, {(1, 2), (1, 3), (2, 3)})
tree = connected_without_cycle = Graph({1, 2, 3}, {(1, 2), (1, 3)})
unconnected = Graph({1, 2, 3, 4}, {(1, 2), (1, 3)})

class TestDerivedMethods(unittest.TestCase):
    def test_hascycle(self):
        self.assertTrue(connected_with_cycle.has_cycle())
        self.assertFalse(tree.has_cycle())
        self.assertFalse(unconnected.has_cycle())
    def test_tree(self):
        self.assertFalse(connected_with_cycle.is_tree())
        self.assertTrue(tree.is_tree())
        self.assertFalse(unconnected.is_tree())

if __name__ == '__main__':
    unittest.main()
