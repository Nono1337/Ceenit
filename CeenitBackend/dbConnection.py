import logging
from fastapi import HTTPException
import pymongo
import BaseModel.ModelUser
import BaseModel.List
from bson.objectid import ObjectId
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


def findUsername(username: str, dbConnect):#sad
    userCollection = dbConnect["users"]
    myquery = {"username": username}
    myresp = userCollection.find_one(myquery)
    return myresp is not None


def createUser(user: BaseModel.ModelUser.CreateUser):
    db = DBconnect()
    if findUsername(user["username"], db) == True:
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
    myquery = {"name": + "*"+list_name + "*"}
    return list(listCollection.find(myquery))


def createMovielist(movieColletction : BaseModel.List.CreateList):
    db = DBconnect()
    listCollection = db["movieLists"]
    myquery = {"name": "*" + movieColletction["name"] + "*"}
    if listCollection.find_one(myquery) is None:

        return str(listCollection.insert_one(movieColletction).inserted_id)
    else:
        # logging.WARN(f' Falsche Anmeldung von Benuzter: {username}')
        raise HTTPException(status_code=400, detail="Liste kann nicht erstellt, da bereits eine Liste mit gleichen vorhanden ist")

