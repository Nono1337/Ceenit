import logging
from fastapi import HTTPException
import pymongo
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
    if findUsername(user["username"], db) == True:
        # logging.WARN(f' Falsche Anmeldung von Benuzter: {username}')
        raise HTTPException(status_code=400, detail="Benutzer ist bereits vorhanden")
    userCollection = db["users"]
    result = userCollection.insert_one(user)
    return str(result.inserted_id)

