import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QFileDialog, QComboBox, \
    QHBoxLayout, QTabWidget, QListWidget, QListWidgetItem
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from client.control.image import apply_filter, get_images, view_image


class ImageClient(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cliente de Filtros de Imagem")
        self.setGeometry(100, 100, 800, 500)

        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()

        # Criar abas
        self.tabs = QTabWidget()

        # Aba de carregar e aplicar filtros
        self.filter_tab = QWidget()
        self.tabs.addTab(self.filter_tab, "Aplicar Filtro")

        # Aba para listar e visualizar imagens processadas
        self.view_tab = QWidget()
        self.tabs.addTab(self.view_tab, "Imagens Processadas")

        self.layout.addWidget(self.tabs)

        self.init_filter_tab()
        self.init_view_tab()

        self.setLayout(self.layout)

    def init_filter_tab(self):
        # Layout para aplicar filtros
        layout = QVBoxLayout()

        # Imagem original
        self.original_label = QLabel("Imagem Original")
        self.original_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.original_label)

        # Imagem processada
        self.processed_label = QLabel("Imagem Processada")
        self.processed_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.processed_label)

        # Botão para carregar imagem
        self.load_button = QPushButton("Carregar Imagem")
        self.load_button.clicked.connect(self.load_image)
        layout.addWidget(self.load_button)

        # ComboBox para escolher filtro
        self.filter_combobox = QComboBox()
        self.filter_combobox.addItem("Invert")
        self.filter_combobox.addItem("Grayscale")
        self.filter_combobox.addItem("Pixelate")
        layout.addWidget(self.filter_combobox)

        # Botão para aplicar filtro
        self.apply_button = QPushButton("Aplicar Filtro")
        self.apply_button.clicked.connect(self.apply_filter)
        layout.addWidget(self.apply_button)

        self.filter_tab.setLayout(layout)

    def init_view_tab(self):
        # Layout para listar imagens
        layout = QVBoxLayout()

        self.image_list = QListWidget()
        self.image_list.itemClicked.connect(self.view_image)
        layout.addWidget(self.image_list)

        # Botão para carregar lista de imagens
        self.load_images_button = QPushButton("Carregar Imagens Processadas")
        self.load_images_button.clicked.connect(self.load_processed_images)
        layout.addWidget(self.load_images_button)

        self.view_tab.setLayout(layout)

    def load_image(self):
        # Abrir caixa de diálogo para selecionar imagem
        options = QFileDialog.Options()
        file, _ = QFileDialog.getOpenFileName(self, "Escolha uma imagem", "", "Imagens (*.png *.jpg *.jpeg)",
                                              options=options)
        if file:
            self.original_pixmap = QPixmap(file)
            self.original_label.setPixmap(self.original_pixmap.scaled(300, 300, Qt.KeepAspectRatio))
            self.original_image_path = file

    def apply_filter(self):
        if hasattr(self, 'original_image_path'):
            filter_type = self.filter_combobox.currentText().lower()
            files = {'image': open(self.original_image_path, 'rb')}
            data = {'filter': filter_type}
            response = apply_filter(files, data)
            pixmap = QPixmap()
            pixmap.loadFromData(response.content)
            self.processed_label.setPixmap(pixmap.scaled(300, 300, Qt.KeepAspectRatio))

    def load_processed_images(self):
            list_images = get_images()
            if list_images:
                self.image_list.clear()
                for image in list_images:
                    item = QListWidgetItem(image[1])
                    item.setData(Qt.UserRole, (image[0], image[-1]))
                    self.image_list.addItem(item)

    def view_image(self, item):
        image_id, image_path = item.data(Qt.UserRole)
        response = view_image(image_id)
        if response:
            pixmap = QPixmap()
            pixmap.loadFromData(response.content)
            self.processed_label.setPixmap(pixmap.scaled(300, 300, Qt.KeepAspectRatio))


def run_client():
    """Inicia o cliente PyQt."""
    app = QApplication(sys.argv)
    client = ImageClient()
    client.show()
    sys.exit(app.exec_())
