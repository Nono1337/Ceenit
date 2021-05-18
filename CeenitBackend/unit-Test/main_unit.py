import unittest

import main


class TestWebservice(unittest.TestCase):
    def test_SearchMovie(self):
        movie = main.getMovieSearch("'Batman Beyond: Return of the Joker'")
        assert(movie[0].movieId == "16234")


if __name__ == '__main__':
    unittest.main()
