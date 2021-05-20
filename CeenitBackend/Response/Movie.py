class MovieList(object):
    movieId: str
    title: str
    releaseDate: str
    poster_path: str

    def __init__(self):
        pass
    # def __init__(self, movieId: str = None, title: str = None, releaseDate: str = None, posterpath: str = None):
    #     """
    #
    #     :param movieId:
    #     :param title:
    #     :param releaseDate:
    #     :param posterpath:
    #     """
    #     self.title = title
    #     self.movieId = movieId
    #     self.releaseDate = releaseDate
    #     self.poster_path = posterpath


class MovieDetail(object):
    movieId: int
    title: str
    releaseDate: str
    overview: str
    poster_path: str
    backdrop_path: str
    adult: bool
    rating: float


class Review(object):
    movieId: int
    userId: str
    rating: int
    text: str
