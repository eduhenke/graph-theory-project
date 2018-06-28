# obter uma ordenação topológica das disciplinas do currículo
# considerando as disciplinas obrigatórias que ainda lhe resta cursar, distribuir
# estas disciplinas ao longo de semestres subsequentes (montar um plano para cursá-las),
# respeitando os pré-requisitos e o limite de carga horária que pode ser cursada num período.

import sys
sys.path.append(sys.path[0] + "/..")
from graph.graph import Graph

class Course:
    def __init__(self, name, workload, requisite):
        self.name = name
        self.workload = workload
        self.requisite = requisite
    def depends(self, other):
        return self.requisite == other.name

CCO_COURSES = [
  Course("Formais", 72, ''),
  Course("Compiladores", 72, "Formais"),
  Course("Sistemas Operacionais", 72, ''),
  Course("Sistemas Operacionais II", 72, "Sistemas Operacionais"),
  Course("Computação Gráfica", 72, "Cálculo II"),
  Course("Cálculo II", 72, ""),
  Course("Computação Distribuida", 72, "Sistemas Operacionais"),
  Course("Cálculo Numérico", 72, "Cálculo II"),
]

MAX_WORKLOAD = 216

V = set(COMPUTER_SCIENCE_COURSES)
E = {(v, w) for v in V for w in V if v.requisite == w.name }

g = Graph(V, E)
sorting = g.topological_sorting() # <---------------------------------------------------------------------------
print(g)
