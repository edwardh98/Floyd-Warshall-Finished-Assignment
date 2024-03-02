import unittest
from src.floyd_warshall import floyd_warshall_recursive

class TestFloydWarshall(unittest.TestCase):

    def test_combined_scenarios(self):
        graph = [
            [0, 3, float('inf'), -2],    # Positive and negative weights
            [float('inf'), 0, 1, float('inf')], 
            [4, float('inf'), 0, 5],     # Some missing edges
            [float('inf'), float('inf'), float('inf'), 0]  
        ]
        expected_distances = [
            [0, 3, 2, -2], 
            [float('inf'), 0, 1, 6],
            [4, 7, 0, 5],
            [float('inf'), float('inf'), float('inf'), 0]
        ]
        result = floyd_warshall_recursive(graph, len(graph))
        self.assertEqual(result, expected_distances)

if __name__ == '__main__':
    unittest.main() 
