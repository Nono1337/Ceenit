import unittest

import main


class TestWebservice(unittest.TestCase):
    def test_SearchMovie(self):
        movie = main.getMovieSearch("Joker")


if __name__ == '__main__':
    unittest.main()
