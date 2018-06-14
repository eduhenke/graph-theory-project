# Graph implementation as per:
# http://www.inf.ufsc.br/grafos/represen/algoritmos/grafo.html
class Graph:
    def __init__(self, V, E, directed=True):
        self.Vertices = V
        if not directed: # duplicate
            E = {(b, a) for (a, b) in E}.union(E)
        self.Edges = E
        
    def __str__(self):
        return "V={0} | E={1}".format(self.Vertices, self.Edges)

    # Basic methods
    def add_vertex(self, v): # O(1)
        self.Vertices.add(v)

    def remove_vertex(self, v): # O(m)
        self.Vertices.remove(v)         # O(1)
        for n in self.successors(v):    # O(m)
            self.disconnect(v, n)       # O(1)
        for n in self.antecessors(v):   # O(m)
            self.disconnect(n, v)       # O(1)

    def add_edge(self, a, b):
        self.Edges.add((a, b))

    def remove_edge(self, a, b):
        self.Edges.remove((a, b))

    def connect(self, v1, v2): # O(1)
        self.Edges.add((v1, v2))

    def disconnect(self, v1, v2): # O(1)
        self.Edges.remove((v1, v2))
    
    def order(self): # O(1)
        return len(self.Vertices)

    def vertices(self): # O(1)
        return self.Vertices
    
    def any_vertex(self): # probably O(1) :P
        return iter(self.Vertices).next()

    def successors(self, v): # O(m)
        return {w for (u, w) in self.Edges if u == v}

    def antecessors(self, v): # O(m)
        return {u for (u, w) in self.Edges if w == v}

    def adjacents(self, v): # O(m)
        return self.successors(v).union(self.antecessors(v))
    
    def in_degree(self, v): # O(m)
        return len(self.antecessors(v))

    def out_degree(self, v): # O(m)
        return len(self.successors(v))

    def degree(self, v): # O(m)
        return len(self.adjacents(v))

    def sources(self): # O(n*m)
        return {v for v in self.Vertices if self.in_degree(v) == 0}

    def sinks(self): # O(n*m)
        return {v for v in self.Vertices if self.out_degree(v) == 0}

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
        for u in self.successors(v) - {came_from}:
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
            for u in graph.successors(v):
                if u not in Marked and graph.has_cycle_util(v, u, Marked):
                    return True
            remaining_vertices = graph.Vertices - Marked
            graph = Graph(remaining_vertices, graph.Edges)
        return False

    def is_tree(self):
        if not self.is_connected():
            return False
        return not self.has_cycle()

    def topological_sorting(self):
        G = self
        l = []
        s = G.sources()
        while s != set():
            v = s.pop()
            l.append(v)
            for n in G.successors(v):
                G.remove_edge(v, n)
                if G.in_degree(n) == 0:
                    s.add(n)
        if len(G.Edges) > 0:
            raise TypeError("Graph is not DAG, has at least one cycle")
        else:
            return l
