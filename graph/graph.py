# Graph implementation as per:
# http://www.inf.ufsc.br/grafos/represen/algoritmos/grafo.html
from copy import deepcopy

class Graph:
    def __init__(self, V=set(), E=set(), directed=True):
        self.Vertices = set()
        self.Edges = set()
        self._successors = {}
        self._antecessors = {}
        self._directed = directed

        for v in V:
            self.add_vertex(v)

        for (a, b) in E:
            self.connect(a, b)

    def __str__(self):
        return "V={0} | E={1}".format(self.Vertices, self.Edges)

    # Basic methods
    def add_vertex(self, v): # O(1)
        self.Vertices.add(v)
        self._successors[v] = set()
        self._antecessors[v] = set()

    def add_vertices(self, *V):
        for v in V:
            self.add_vertex(v)

    def remove_vertex(self, v): # O(m/n)
        self.Vertices.remove(v)                # O(1)
        for n in self.successors(v).copy():    # O(m/n)
            self.disconnect(v, n)              # O(1)
        for n in self.antecessors(v).copy():   # O(m/n)
            self.disconnect(n, v)              # O(1)

    def remove_vertices(self, *V):
        for v in V:
            self.remove_vertex(v)

    def connect(self, v1, v2): # O(1)
        self.Edges.add((v1, v2))
        self._successors[v1].add(v2)
        self._antecessors[v2].add(v1)
        if not self._directed:
            self.Edges.add((v2, v1))
            self._successors[v2].add(v1)
            self._antecessors[v1].add(v2)

    def disconnect(self, v1, v2): # O(1)
        self.Edges.remove((v1, v2))
        self._successors[v1].remove(v2)
        self._antecessors[v2].remove(v1)
        if not self._directed:
            self.Edges.remove((v2, v1))
            self._successors[v2].remove(v1)
            self._antecessors[v1].remove(v2)
    
    def order(self): # O(1)
        return len(self.Vertices)

    def vertices(self): # O(1)
        return self.Vertices
    
    def any_vertex(self): # probably O(1) :P
        return iter(self.Vertices).next()

    def successors(self, v): # O(1)
        return self._successors[v]

    def antecessors(self, v): # O(1)
        return self._antecessors[v]

    def adjacents(self, v): # O(1)
        return self.successors(v).union(self.antecessors(v))
    
    def in_degree(self, v): # O(1)
        return len(self.antecessors(v))

    def out_degree(self, v): # O(1)
        return len(self.successors(v))

    def degree(self, v): # O(1)
        return self.in_degree(v) + self.out_degree(v)

    def sources(self): # O(n)
        return {v for v in self.Vertices if self.in_degree(v) == 0}

    def sinks(self): # O(n)
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
        graph = deepcopy(self)
        Marked = set()
        while graph.Vertices != set():
            v = graph.any_vertex()
            Marked.add(v)
            for u in graph.successors(v):
                if u not in Marked and graph.has_cycle_util(v, u, Marked):
                    return True
            to_remove = Marked.intersection(graph.Vertices)
            graph.remove_vertices(*to_remove)
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
            for n in G.successors(v).copy():
                G.disconnect(v, n)
                if G.in_degree(n) == 0:
                    s.add(n)
        if len(G.Edges) > 0:
            raise TypeError("Graph is not DAG, has at least one cycle")
        else:
            return l
