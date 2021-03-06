from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListView, QVBoxLayout, QPushButton

from listaservizi.controller.ControlloreListaServizi import ControlloreListaServizi


class VistaListaServizi(QWidget):
    def __init__(self, parent=None):
        super(VistaListaServizi, self).__init__(parent)

        self.controller= ControlloreListaServizi()

        h_layout= QHBoxLayout()
        self.lista_view= QListView()
        self.listview_model= QStandardItemModel(self.lista_view)
        for servizio in self.controller.get_lista_dei_servizi():
            item= QStandardItem()
            item.setText(servizio.nome)
            item.setEditable(False)
            font= item.font()
            font.setPointSize(18)
            item.setFont(font)
            self.listview_model.appendRow(item)
        self.lista_view.setModel(self.listview_model)
        h_layout.addWidget(self.lista_view)

        buttons_layout= QVBoxLayout()
        open_button= QPushButton("Apri")
        buttons_layout.addWidget(open_button)
        buttons_layout.addStretch()
        h_layout.addLayout(buttons_layout)
        self.setLayout(h_layout)
        self.resize(600,300)
        self.setWindowTitle('Lista Servizi')

    def closeEvent(self, event):
        self.controller.save_data()
        event.accept()