import os
import json
import logging

#chemin fichier json
Cur_Dir = os.path.dirname(__file__)
Data_File = os.path.join(Cur_Dir, "data", "movies.json")

#config logg
logging.basicConfig(filename="app.log",
                    filemode="a",
                    format ='%(asctime)s - %(levelname)s - %(message)s')

#recuperer chaque film de la liste sous forme d'instance
def get_movies():
    
    with open(Data_File, 'r') as f:
        movies_title = json.load(f)

    movies = [Movie(movie_title) for movie_title in movies_title]
    return movies



#creation de la class Movie
class Movie:
    def __init__(self, titre):
        self.titre = titre.title()

    def __str__(self):
        return f"C'est le film {self.titre}"

    def _get_movies(self):
        with open(Data_File, "r") as f:
            return json.load(f)
        

    def _write_movies(self, movies):
        with open(Data_File, "w") as f:
            json.dump(movies, f, indent=4)

    def add_movies(self):
        movies = self._get_movies() 
        
        if self.titre not in movies:
            movies.append(self.titre)
            self._write_movies(movies)
            return True
        else:
            logging.warning(f"Le film {self.titre} est déjà enregistré.")
            return False

    def remove_movies(self):
        movies = self._get_movies()

        if self.titre in movies:
            movies.remove(self.titre)
            self._write_movies(movies)
        else:
            pass


#test de la class
if __name__ == "__main__":
    m = Movie("harry potter")
    m._write_movies(["pepe le putuois", "germaine "])
    print(m._get_movies())
    m.add_movies()
    print(m._get_movies())
    #m.remove_movies()

#structure conditionnel de verif
if __name__ == "__main__":
        print(Data_File)