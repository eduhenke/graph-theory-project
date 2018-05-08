# Graph implementation as per:
# http://www.inf.ufsc.br/grafos/represen/algoritmos/grafo.html
class Graph:
    def __init__(self, V, E):
        self.Vertices = V
        self.Edges = E
        
    def __str__(self):
        return "V={0} | E={1}".format(self.Vertices, self.Edges)

    # Basic methods
    def add_vertex(self, v):
        self.Vertices.add(v)

    def remove_vertex(self, v):
        self.Vertices.remove(v)

    def connect(self, v1, v2):
        self.Edges.add((v1, v2))

    def disconnect(self, v1, v2):
        self.Edges.remove((v1, v2))
    
    def order(self):
        return len(self.Vertices)

    def vertices(self):
        return self.Vertices
    
    def any_vertex(self):
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
    def is_regular(self):
        degree = self.degree(self.any_vertex())
        for v in self.Vertices:
            if self.degree(v) != degree:
                return False
        return True

    def is_complete(self):
        for v in self.Vertices:
            if self.adjacents(v) != self.Vertices:
                return False
        return True

    def transitive_closure_util(self, v, reachable):
        reachable.add(v)
        for u in self.adjacents(v):
            if u not in reachable:
                reachable.union(self.transitive_closure_util(u, reachable))
        return reachable

    def transitive_closure(self, v):
        return self.transitive_closure_util(v, set())

    def is_connected(self):
        for v in self.Vertices:
            if self.transitive_closure(v) != self.Vertices:
                return False
        return True
    
    def has_cycle_util(self, came_from, v, C):
        C.add(v)
        for u in self.adjacents(v) - {came_from}:
            if u in C:
                return True
            elif self.has_cycle_util(v, u, C):
                return True
        return False

    def has_cycle(self):
        graph = self
        Marked = set()
        while graph.Vertices != set():
            v = graph.any_vertex()
            Marked.add(v)
            for u in graph.adjacents(v):
                if self.has_cycle_util(v, u, Marked):
                    return True
            remaining_vertices = self.Vertices - Marked
            graph = Graph(remaining_vertices, self.Edges)
        return False

    def is_tree(self):
        if not self.is_connected():
            return False
        return not self.has_cycle()
