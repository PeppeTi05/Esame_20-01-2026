import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_create_graph(self, e):
        try:
            alb_min = int(self._view.txtNumAlbumMin.value)
            if alb_min == 0:
                return
        except Exception:
            self._view.show_alert("Numero album non valido.")
            return
        self._model.build_graph(alb_min)

        self.popola_dd_artisti()

        n_nodi = self._model.numero_nodi_grafo()
        n_archi = self._model.numero_archi_grafo()

        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f'Grafo creato: {n_nodi} nodi, {n_archi} archi.'))
        self._view.update_page()

    def popola_dd_artisti(self):
        all_nodes = self._model.get_nodi_grafo()
        self._view.ddArtist.options = [ft.dropdown.Option(key=c.id, text=c.name, data=c) for c in all_nodes]

    def scegli_artista(self, e):
        selected_key = e.control.value
        for opt in e.control.options:
            if opt.key == selected_key:
                self._view.ddArtist = opt.data
                break


    def handle_connected_artists(self, e):
        risultato = self._model.analisi_componente(self._view.ddArtist.id)
        n_artisti_connessi = self._model.lunghezza_componente(self._view.ddArtist.id)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f'Artisti connessi: {n_artisti_connessi}'))
        for v, p in risultato:
            self._view.txt_result.controls.append(ft.Text(f'{v.id}, {v.name} - Numero di generi trovati: {p})'))




