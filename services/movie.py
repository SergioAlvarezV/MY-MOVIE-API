from models.movie import Movies as MoviesModel
from schemas.movie import Movie

class MovieService():

    def __init__(self, db) -> None:
        self.db = db

    def get_movies(self):
        resul = self.db.query(MoviesModel).all()
        return resul

    def get_movie(self, id):
        resul = self.db.query(MoviesModel).filter(MoviesModel.id == id).first()
        return resul

    def get_movieCTG(self, category):
        resul = self.db.query(MoviesModel).filter(MoviesModel.category == category).all()
        return resul
    
    def create_movie(self, movie: Movie):
        new_movi = MoviesModel(**movie.model_dump())
        self.db.add(new_movi)
        self.db.commit()
        return
    
    def update_movie(self, id: int, data: Movie):
        movie = self.db.query(MoviesModel).filter(MoviesModel.id == id).first()
        movie.title = data.title
        movie.overview = data.overview
        movie.year = data.year
        movie.rating = data.rating
        movie.category = data.category
        self.db.commit()
        return
    
    def dele_movie(self,id: int):
        self.db.query(MoviesModel).filter(MoviesModel.id == id).delete()
        self.db.commit()
        return