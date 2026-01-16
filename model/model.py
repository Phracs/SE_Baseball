import networkx as nx


class Model:
    def __init__(self):
        self.grafo=nx.Graph()

    def crea_grafo(self, lista_squadre: list, dict_squadre: dict):
        self.grafo = nx.Graph()
        for code in lista_squadre:
            self.grafo.add_node(code, salario_tot=dict_squadre[code])
        for i in range(len(lista_squadre)):
            for j in range(i + 1, len(lista_squadre)):
                u=lista_squadre[i]
                v=lista_squadre[j]
                peso=self.grafo.nodes[u]["salario_tot"]+self.grafo.nodes[v]["salario_tot"]
                self.grafo.add_edge(u, v, weight=peso)

    def dettagli(self, code: str):
        if code in self.grafo:
            for a, b, data in self.grafo.edges(code, data=True):
                peso=data['weight']


