# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json

from fastapi import FastAPI, File, UploadFile, status
import logging
import uvicorn
import BaseModel.ModelUser
import requests
# globale Varibalen
import dbConnection
from Response.Movie import MovieList

VERSION = '1.0'
app = FastAPI()

# Einstellung für das Logging
logging.basicConfig(format='%(asctime)s: %(message)s',
                    level=logging.INFO, datefmt='%H:%M:%S')


@app.get("/versionsinfo")
def version():
    return {'version': VERSION}


@app.post("/CreateUser")
def createUser(user: BaseModel.ModelUser.CreateUser):
    return dbConnection.CreateUser(user);


@app.post("/LoginUser")
def getLogin(user: BaseModel.ModelUser.LoginUser):
    return dbConnection.loginUser(user.username, user.password)

@app.get("/movie/getFiveHottest")
def getFiveHottest():

    pass


@app.get("/movie/search/{title}")
def getMovieSearch(title: str):
    url = "https://api.themoviedb.org/3/search/movie?api_key=4b2ecb935b35b20429859a891b9941a8&query="+ title

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    data =json.loads(response.text)

    myReturn= []

    for item in data["results"]:
        try:
            movie_list = MovieList()
            movie_list.movieId = str(item["id"])
            movie_list.title = item["title"]

            if item["poster_path"] is not None:
                movie_list.poster_path = f'https://image.tmdb.org/t/p/w500/{item["poster_path"]}'

            if "release_date" in item:
                movie_list.releaseDate = item["release_date"]

            myReturn.append(movie_list)
        except Exception as err:
            print('Handling run-time error: '+ err)
    return myReturn
    #https://api.themoviedb.org/3/search/movie?api_key=4b2ecb935b35b20429859a891b9941a8&query=Joker
    #https://image.tmdb.org/t/p/w500/9yBVqNruk6Ykrwc32qrK2TIE5xw.jpg Bild für die Suche


@app.get("/movie/detail/{movieid}")
def getReviewToMovie(movieid: int):
    pass

@app.post("/movie/review/{movieid}")
def postReviewToMovie(movieid: int):
    pass

@app.post("/movie/rating/{movieid}")
def postMovieRating(movieid : int):
    pass

# localhost:1234/account/watchlist?userid=1221234
@app.get("/account/watchlist/{userid}")
def getWatchlist(userid: int):
    pass


@app.post("/account/watchlist/{userid}")
def addWatchlist(userid: int):
    pass


@app.get("/account/timeline/{userid}")
def getTimeLine(userid: int):
    pass


@app.post("/account/timeline/{userid}")
def getTimeLine(userid: int):
    pass

@app.get("/account/reviews/{userid}")
def getReviews(userid: int):
    pass


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=1234)
