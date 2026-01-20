import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._artisti = []
        self._mappa_artisti = {}
        self._artisti_connessi = []

    def load_artisti(self, num_album):
        self._artisti = DAO.get_artisti__per_n_album(num_album)
        return self._artisti

    def load_artisti_connessi(self):
        self._artisti_connessi = DAO.get_artisti_connessi()
        return self._artisti_connessi

    def load_mappa_artisti(self):
        for a in self._artisti:
            self._mappa_artisti[a.id] = a
        return self._mappa_artisti

    def build_graph(self, num_album):
        self._grafo.clear()

        self._edges = []

        if len(self._artisti) == 0:
            self.load_artisti(num_album)

        self._grafo.add_nodes_from(self._artisti)

        self._mappa_artisti = self.load_mappa_artisti()

        self._artisti_connessi = self.load_artisti_connessi()

        edges = {}
        for a1, a2, peso in self._artisti_connessi:
            # Non riesce ad associare l'id all'oggetto artista
            if (self._mappa_artisti[a1], self._mappa_artisti[a2]) not in edges:
                edges[(self._artisti[a1], self._artisti[a2])] = int(peso)
        for k, v in edges.items():
            self._edges.append((k[0], k[1], v))
        self._grafo.add_weighted_edges_from(self._edges)

    def get_nodi_grafo(self):
        return list(self._grafo.nodes)

    def get_edges(self):
        return list(self._grafo.edges)

    def numero_nodi_grafo(self):
        return self._grafo.number_of_nodes()

    def numero_archi_grafo(self):
        return self._grafo.number_of_edges()


    def analisi_componente(self, artist_id):
        artista = self._mappa_artisti[artist_id]  # a1

        risultati = []
        for vicino in self._grafo.neighbors(artist_id):
            peso = self._grafo[vicino][artist_id]['weight']
            risultati.append((vicino, peso))

        risultati.sort(key=lambda x: x[1])

        return risultati


    def lunghezza_componente(self, artist_id):
        artista = self._mappa_artisti[artist_id]

        componente = nx.node_connected_component(self._grafo, artista)
        return len(componente)




    def calcola_percorso_ottimo(self):
        self.best_solution = []
        self.best_value = 0  # float("inf") se percorso min - oppure float("-inf") se percorso max

        for nodo in self.G.nodes():
            self._ricorsione(
                parziale=[nodo],
                visitati={nodo},
                valore_corrente=0,
                ultimo_peso=-1
            )
        self.stampa_percorso()
        return self.best_solution, self.best_value

    def _ricorsione(self, parziale, visitati, valore_corrente, ultimo_peso):
        # aggiorna sempre il best (> percorso max, < percorso min) oppure (len(parziale) == L)  oppure  (parziale[-1] == nodo_finale)
        if valore_corrente > self.best_value:
            self.best_value = valore_corrente
            self.best_solution = parziale[:]

        nodo_corrente = parziale[-1]

        for vicino in self.G.neighbors(nodo_corrente):

            if vicino in visitati:
                continue

            peso = self.G[nodo_corrente][vicino]["weight"]

            # vincolo: pesi crescenti
            if peso <= ultimo_peso:
                continue

            # vincolo: pesi maggiori soglia
            if peso < self.soglia:
                continue

            parziale.append(vicino)
            visitati.add(vicino)

            self._ricorsione(
                parziale,
                visitati,
                valore_corrente + peso,
                peso
            )

            visitati.remove(vicino)
            parziale.pop()

    def stampa_percorso(self):
        for i in range(len(self.best_solution) - 1):
            u = self.best_solution[i]
            v = self.best_solution[i + 1]

            peso = self.G[u][v]["weight"]
            print(f"{u} -> {v} | peso={peso}")



