from fastapi import FastAPI, File, UploadFile, status
from fastapi.responses import FileResponse
import logging
import json
from time import sleep
from datetime import datetime
from threading import Thread
from xml.dom import minidom
import yaml

# globale Varibalen
VERSION = '1.0'
app = FastAPI()

# Einstellung für das Logging
logging.basicConfig(format='%(asctime)s: %(message)s',
                    level=logging.INFO, datefmt='%H:%M:%S')

#Logging einlesen
with open('logging.yaml', 'r') as f:
    config_log = yaml.safe_load(f.read())
    logging.config.dictConfig(config_log)

@app.get("/versionsinfo",  status_code=status.HTTP_200_OK)
def version():
    return {'version': VERSION}


@app.post("/CreateUser", status_code=status.HTTP_200_OK)
def createUser( file: UploadFile = File(...)):
    pass

@app.post("/LoginUser", status_code=status.HTTP_200_OK)
def getSession(file: UploadFile = File(...)):
    pass

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


