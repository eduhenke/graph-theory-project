class Graph:
    def __init__(self, V, E):
        self.Vertices = V
        self.Edges = E
        
    def __str__(self):
        return "V={0} | E={1}".format(self.Vertices, self.Edges)

    def addVertex(self, v):
        self.Vertices.add(v)

    def removeVertex(self, v):
        self.Vertices.remove(v)

    def connect(self, v1, v2):
        self.Edges.add((v1, v2))

    def disconnect(self, v1, v2):
        self.Edges.remove((v1, v2))
    
    def order(self):
        return len(self.Vertices)

    def vertices(self):
        return self.Vertices
    
    def anyVertex(self):
        return iter(self.Vertices).next()

    def adjacents(self, v):
        return {(u, w) for (u, w) in self.Edges if w == v or u == v}
    
    def degree(self, v):
        return len(self.adjacents(v))

if __name__ == "__main__":
    g = Graph(set(), set())
    g.addVertex(1)
    g.addVertex(2)
    g.addVertex(3)
    g.addVertex(4)
    g.connect(2, 3)
    g.connect(1, 2)
    g.connect(4, 3)
    print(g)
    print(g.anyVertex())
    print(g.adjacents(2))
    g.removeVertex(2)
    g.removeVertex(3)
    g.disconnect(2, 3)
    print(g)