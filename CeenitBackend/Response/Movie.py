class MovieList():
    movieId:int
    title: str
    releaseDate: str
    poster_path: str

class MovieDetail():
    movieId:int
    title: str
    releaseDate: str
    overview: str
    poster_path: str
    backdrop_path: str
    adult: bool
    rating: float

class Review():
    movieId: int
    userId: str
    rating: int
    text: str
