# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json

from fastapi import FastAPI, File, UploadFile, status
import logging
import uvicorn
import BaseModel.ModelUser
import BaseModel.ModelList
import requests
# globale Varibalen
import dbConnection
from BaseModel import ModelMovie
from Response.Movie import MovieList, MovieDetail

VERSION = '1.0'
app = FastAPI()

# Einstellung für das Logging
logging.basicConfig(format='%(asctime)s: %(message)s',
                    level=logging.INFO, datefmt='%H:%M:%S')

@app.get("/")
def home():
    return "Welcome to Ceenit Backend API"

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
    url = "https://api.themoviedb.org/3/movie/popular?api_key=4b2ecb935b35b20429859a891b9941a8"
    resultMovieDataBase =  callMovieDataBaseApi(url)
    return changeMovieDataResponseToMovieList(resultMovieDataBase)[:5]

@app.get("/movie/search/{title}")
def getMovieSearch(title: str):
    url = "https://api.themoviedb.org/3/search/movie?api_key=4b2ecb935b35b20429859a891b9941a8&query="+ title
    resultMovieDataBase = callMovieDataBaseApi(url)
    return changeMovieDataResponseToMovieList(resultMovieDataBase)
    #https://api.themoviedb.org/3/search/movie?api_key=4b2ecb935b35b20429859a891b9941a8&query=Joker
    #https://image.tmdb.org/t/p/w500/9yBVqNruk6Ykrwc32qrK2TIE5xw.jpg Bild für die Suche

@app.get("/movie/detail/{movieid}")
def getDetails(movieid: int):
    url = "https://api.themoviedb.org/3/movie/"+str(movieid)+"?api_key=4b2ecb935b35b20429859a891b9941a8"
    resultMovieDataBase = callMovieDataBaseApi(url)
    return changeMovieDataResponseToMovie(resultMovieDataBase)

@app.get("/lists/")
def getAllLists():
    return  dbConnection.getMovieLists()

@app.get("/list/{list_id}")
def getListById(list_id: str):
    return dbConnection.getMovieListById(list_id)

@app.get("/lists/{list_name}")
def getListsByName(list_name: str):
    return dbConnection.getMovieListByName(list_name)

@app.post("/list")
def addMovieCollection(movieColletction: BaseModel.ModelList.CreateList):
    return dbConnection.createMovielist(movieColletction)

@app.delete("/list")
def delete(list_id):
    return dbConnection.deleteMovieList(list_id)

@app.post("/movie/{movieid}/review")
def postReviewToMovie(movieid: int,review: BaseModel.ModelMovie.CreateReview):
    return dbConnection.createMovieReview(movieid, review)

@app.get("/movie/{movieid}/reviews")
def getReviews(movieId: int):
    return dbConnection.getMovieReviewById(movieId)

@app.post("/movie/rating/{movieid}")
def postMovieRating(movieid : int, movieRating: BaseModel.ModelMovie.MovieRating):
    return dbConnection.addRating(movieid, movieRating)

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

def callMovieDataBaseApi(url: str):
    payload = {}
    headers = {}
    url += "&language=de"
    response = requests.request("GET", url, headers=headers, data=payload)
    data =json.loads(response.text)

    return data

def changeMovieDataResponseToMovie(item):
    movieDetail = MovieDetail()

    try:
            movieDetail.movieId = str(item["id"])
            movieDetail.title = item["title"]

            if item["poster_path"] is not None:
                movieDetail.poster_path = f'https://image.tmdb.org/t/p/w500/{item["poster_path"]}'

            if "release_date" in item:
                movieDetail.releaseDate = item["release_date"]
            if "overview" in item:
                movieDetail.overview = item["overview"]
            if "backdrop_path" in item:
                movieDetail.backdrop_path = f'https://image.tmdb.org/t/p/w500/{item["backdrop_path"]}'
            if "adult" in item:
                movieDetail.adult = item["adult"]
            if "vote_average" in item:
                movieDetail.rating = item["vote_average"]

    except Exception as err:
            print('Handling run-time error: ' + err)
    return movieDetail

def changeMovieDataResponseToMovieList(results):
    myReturn = []
    for item in results["results"]:
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



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=1234)
