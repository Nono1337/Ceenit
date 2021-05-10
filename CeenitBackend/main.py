# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from fastapi import FastAPI, File, UploadFile, status
import logging
import uvicorn
import BaseModel.ModelUser

# globale Varibalen
import dbConnection

VERSION = '1.0'
app = FastAPI()

# Einstellung für das Logging
logging.basicConfig(format='%(asctime)s: %(message)s',
                    level=logging.INFO, datefmt='%H:%M:%S')


@app.get("/versionsinfo")
def version():
    return {'version': VERSION}


@app.post("/CreateUser")
def createUser(user: BaseModel.ModelUser.User):
    pass


@app.post("/LoginUser")
def getLogin(user: BaseModel.ModelUser.User):
    return dbConnection.loginUser(user.username, user.password)

@app.get("/movie/getFiveHottest")
def getFiveHottest():
    pass


@app.get("/movie/search/{title}")
def getMovieSearch(title: str):
    pass


@app.post("/movie/review/{movieid}")
def postReviewToMovie(movieid: int):
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


@app.post("/account/{userid}")
def addTimeLine(userid: int):
    pass


@app.get("/account/reviews/{userid}")
def getReviews(userid: int):
    pass


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=1234)
