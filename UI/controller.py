import flet as ft
from UI.view import View
from database.dao import DAO
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model
        self.lista_squadre = []
        self.dizionario_squadre={}

    def handle_crea_grafo(self, e):
        """ Handler per gestire creazione del grafo """""
        # TODO
        self.crea_dizionario_squadre()
        self._model.crea_grafo(self.lista_squadre, self.dizionario_squadre)

    def handle_dettagli(self, e):
        """ Handler per gestire i dettagli """""
        # TODO
        code=self._view.dd_squadra.value

        if code in self._model.grafo:
            self._view.txt_risultato.controls.clear()
            for a, b, data in self._model.grafo.edges(code, data=True):
                peso=data['weight']
                vicino = b if a == code else a
                self._view.txt_risultato.controls.append(ft.Text(f"{code} --> {vicino} | peso={peso}"))
        self._view.update()

    def handle_percorso(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del percorso """""
        # TODO

    """ Altri possibili metodi per gestire di dd_anno """""
    # TODO
    def crea_dizionario_squadre(self):
        anno=int(self._view.dd_anno.value)
        lista_squadre = DAO.read_salario_squadre(anno)
        for team_code, salario_tot in lista_squadre:
            self.dizionario_squadre[team_code] = salario_tot



    def populate_dd(self, dd):
        lista_anni= DAO.read_anni()
        for a in lista_anni:
            dd.options.append(ft.dropdown.Option(a))

    def handle_cambio_anni(self, e):
        anno=int(self._view.dd_anno.value)
        self.lista_squadre.clear()
        self.lista_squadre=DAO.read_squadre_per_anno(anno)
        self._view.txt_out_squadre.controls.clear()
        self._view.txt_out_squadre.controls.append(ft.Text(f"Numero di Squadre:{len(self.lista_squadre)}"))
        self._view.dd_squadra.options.clear()
        self._view.dd_squadra.value = None
        for s in self.lista_squadre:
            self._view.dd_squadra.options.append(ft.dropdown.Option(s))
        for s in self.lista_squadre:
            self._view.txt_out_squadre.controls.append(ft.Text(f"{s}"))
        self._view.update()
