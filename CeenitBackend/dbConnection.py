import datetime

import pymongo
from bson.objectid import ObjectId
from fastapi import HTTPException

import BaseModel.ModelList
import BaseModel.ModelUser


def DBconnect():
    client = pymongo.MongoClient(
        "mongodb+srv://ceenit_admin:KHPta9S8dAIbSOe9@ceenit.kjvno.mongodb.net/Ceenit?retryWrites=true&w=majority")
    return client.Ceenit


def loginUser(username: str, password: str):
    db = DBconnect()
    userCollection = db["users"]
    myquery = {"username": username, "password": password}
    myresp = userCollection.find_one(myquery)

    if myresp is not None:
        return str(myresp.get("_id"))
    else:
        # logging.WARN(f' Falsche Anmeldung von Benuzter: {username}')
        raise HTTPException(status_code=401, detail="Gültige Authentifizierung")


def findUsername(username: str, dbConnect):
    userCollection = dbConnect["users"]
    myquery = {"username": username}
    myresp = userCollection.find_one(myquery)
    return myresp is not None


def createUser(user: BaseModel.ModelUser.CreateUser):
    db = DBconnect()
    if findUsername(user["username"], db):
        # logging.WARN(f' Falsche Anmeldung von Benuzter: {username}')
        raise HTTPException(status_code=400, detail="Benutzer ist bereits vorhanden")
    userCollection = db["users"]
    result = userCollection.insert_one(user)
    return str(result.inserted_id)


def getMovieListById(list_id):
    db = DBconnect()
    listCollection = db["movieLists"]
    myquery = {"_id": ObjectId(list_id)}
    myresp = listCollection.find_one(myquery)
    if myresp is not None:
        return myresp
    else:
        # logging.WARN(f' Falsche Anmeldung von Benuzter: {username}')
        raise HTTPException(status_code=401, detail="Keine Liste gefunden")


def getMovieListsByName(list_name):
    db = DBconnect()
    listCollection = db["movieLists"]
    myquery = {"name": {'$regex': list_name, '$options': 'i'}}
    return list(listCollection.find(myquery))


def getMovieLists():
    db = DBconnect()
    listCollection = db["movieLists"]
    return list(listCollection.find())


def createMovielist(movieColletction: BaseModel.ModelList.CreateList):
    db = DBconnect()
    listCollection = db["movieLists"]
    myquery = {"name": "*" + movieColletction["name"] + "*"}
    if listCollection.find_one(myquery) is None:

        return str(listCollection.insert_one(movieColletction).inserted_id)
    else:
        # logging.WARN(f' Falsche Anmeldung von Benuzter: {username}')
        raise HTTPException(status_code=400,
                            detail="Liste kann nicht erstellt, da bereits eine Liste mit gleichen vorhanden ist")


def deleteMovieList(list_id):
    db = DBconnect()
    myQuery = {"_id": ObjectId(list_id)}
    return db["movieLists"].delete_one(myQuery)


def createMovieReview(movieid, review):
    db = DBconnect()
    review["movieID"] = movieid
    review["created"] = datetime.datetime.now()
    return str(db["reviews"].insert_one(review))


def getMovieReviewById(movieId):
    db = DBconnect()
    myQuery = {"movieID": movieId}
    return list(db["reviews"].find(myQuery))


def getRatingByMovieUserId(movieID, userID):
    db = DBconnect()
    myQuery = {"movieID": movieID, "userID": ObjectId(userID)}
    return db["rating"].find_one(myQuery)


def addRating(movieid, movieRating):
    ratingCollection = DBconnect()["rating"]
    movieRating["movieID"] = movieid
    findID = getRatingByMovieUserId(movieid, movieRating["userID"])["_id"]
    if findID is None:
        return ratingCollection.insert(movieRating)


def getWatchlist(userid):
    db = DBconnect()
    myquery = {"userID": ObjectId(userid)}
    return list(db["watchlist"].find(myquery))


def isMovieInWatchlist(watchListCollect, myQuery):
    if watchListCollect.find_one(myQuery) is None:
        return False
    else:
        return True


def addMovieToWatchlist(userid, movieID):
    watchlistCollection = DBconnect()["watchlist"]
    myQuery = {"userID": ObjectId(userid), "movieID": movieID}
    myInsert = myQuery | {"watchtime": datetime.datetime.now()}
    if not (isMovieInWatchlist(watchlistCollection, myQuery)):
        return watchlistCollection.insert(myInsert)
    return watchlistCollection.update(myQuery, myInsert)


def getMovieReviewByUserID(userid):
    reviewCollect = DBconnect()["reviews"]
    myQuery = {"userID": ObjectId(userid)}
    return list(reviewCollect.find(myQuery))