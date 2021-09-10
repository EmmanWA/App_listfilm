from PySide2 import QtWidgets, QtCore
import movie

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CineClub")
        self.setup_ui()
        self.populate_movies()
        self.setup_connections()

    def setup_ui(self):
        self.layout = QtWidgets.QVBoxLayout(self)

        self.le_movieTitle = QtWidgets.QLineEdit()
        self.btn_addMovie = QtWidgets.QPushButton("Ajouter un film")
        self.lw_movies = QtWidgets.QListWidget()
        self.lw_movies.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection) #permet une selection multiple
        self.btn_delMovies = QtWidgets.QPushButton("Supprimer le(s) film(s)")

        #ajout au layout
        self.layout.addWidget(self.le_movieTitle)
        self.layout.addWidget(self.btn_addMovie)
        self.layout.addWidget(self.lw_movies)
        self.layout.addWidget(self.btn_delMovies)

    def setup_connections(self):
        self.btn_addMovie.clicked.connect(self.add_movie)
        self.btn_delMovies.clicked.connect(self.remove_movie)
        self.le_movieTitle.returnPressed.connect(self.add_movie)

    def populate_movies(self):
        contenu = movie.get_movies()
        
        for f in contenu:
            lw_item = QtWidgets.QListWidgetItem(f.titre)
            lw_item.setData(QtCore.Qt.UserRole, f)
            self.lw_movies.addItem(lw_item)

    def add_movie(self):
        contenu = self.le_movieTitle.text()
        #si le line edit est vide returné faux
        if not contenu:
            return False
        
        m = movie.Movie(contenu)
        resultat = m.add_movies() #assigner a une variable car n'aura lieu que si la fonction retourne true
        if resultat: #si resultat = true
            lw_item = QtWidgets.QListWidgetItem(m.titre)
            lw_item.setData(QtCore.Qt.UserRole, m)
            self.lw_movies.addItem(lw_item)
            
        self.le_movieTitle.setText("")

    def remove_movie(self):
        for selected_item in self.lw_movies.selectedItems():
            movie = selected_item.data(QtCore.Qt.UserRole)
            movie.remove_movies()
            self.lw_movies.takeItem(self.lw_movies.row(selected_item))

        
        

app = QtWidgets.QApplication([])
win = App()
win.show()

app.exec_()