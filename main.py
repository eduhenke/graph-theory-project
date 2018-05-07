# Graph implementation as per:
# http://www.inf.ufsc.br/grafos/represen/algoritmos/grafo.html
class Graph:
    def __init__(self, V, E):
        self.Vertices = V
        self.Edges = E
        
    def __str__(self):
        return "V={0} | E={1}".format(self.Vertices, self.Edges)

    # Basic methods
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

    def successors(self, v):
        return {w for (u, w) in self.Edges if u == v}

    def antecessors(self, v):
        return {u for (u, w) in self.Edges if w == v}

    def adjacents(self, v):
        return self.successors(v).union(self.antecessors(v))
    
    def degree(self, v):
        return len(self.adjacents(v))

    # Derived methods
    def isRegular(self):
        degree = self.degree(self.anyVertex())
        for v in self.Vertices:
            if self.degree(v) != degree:
                return False
        return True

    def isComplete(self):
        for v in self.Vertices:
            if self.adjacents(v) != self.Vertices:
                return False
        return True

    def transitiveClosure(self, v, reachable):
        reachable.add(v)
        for u in self.adjacents(v):
            if u not in reachable:
                reachable.union(self.transitiveClosure(u, reachable))
        return reachable

    def isConnected(self):
        for v in self.Vertices:
            if len(self.adjacents(v)) == 0:
                return False
        return True

if __name__ == "__main__":
    g = Graph(set(), set())
    g.addVertex(1)
    g.addVertex(2)
    g.addVertex(3)
    g.addVertex(4)
    g.addVertex(5)
    g.connect(1, 2)
    g.connect(2, 3)
    g.connect(4, 3)
    print(g)
    print(g.successors(2), g.antecessors(2), g.adjacents(2))
    print(g.transitiveClosure(2, set()))
    print(g.isConnected())
    g.removeVertex(2)
    g.removeVertex(3)
    g.disconnect(2, 3)
    print(g)