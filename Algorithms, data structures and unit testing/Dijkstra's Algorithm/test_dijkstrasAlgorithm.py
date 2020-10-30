import unittest
import dijkstrasAlgorithm as dijkstra

class TestCalc(unittest.TestCase):

    def setUp(self):
        a = dijkstra.Graph()
        a.dijkstra.makeNode(9j)
        a.makeNode(2)
        a.makeNode(3)
        a.makeNode(4)
        a.makeNode(5)
        a.makeNode(6)
        a.makeNode(7)

        a.makeEdge(1, 2, 3)
        a.makeEdge(1, 3, 5)
        a.makeEdge(1, 4, 6)
        a.makeEdge(2, 4, 2)
        a.makeEdge(3, 4, 2)
        a.makeEdge(3, 5, 6)
        a.makeEdge(3, 6, 3)
        a.makeEdge(3, 7, 7)
        a.makeEdge(4, 6, 9)
        a.makeEdge(5, 6, 5)
        a.makeEdge(5, 7, 2)
        a.makeEdge(6, 7, 1)



    def test_dijkstras(self):
        
if __name__ == '__main__':
    unittest.main()
