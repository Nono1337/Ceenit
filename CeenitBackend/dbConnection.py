import logging
from fastapi import HTTPException
import pymongo
import BaseModel.ModelUser

def DBconnect():
    client = pymongo.MongoClient("mongodb+srv://ceenit_admin:KHPta9S8dAIbSOe9@ceenit.kjvno.mongodb.net/Ceenit?retryWrites=true&w=majority")
    return client.Ceenit

def loginUser(username: str, password: str):
    db = DBconnect()
    userCollection = db["users"]
    myquery = {"username": username, "password": password}
    myresp = userCollection.find_one(myquery)

    if myresp is not None :
        return str(myresp.get("_id"))
    else:
        #logging.WARN(f' Falsche Anmeldung von Benuzter: {username}')
        raise HTTPException(status_code=401, detail="Gültige Authentifizierung")


def createUser(user: BaseModel.ModelUser.CreateUser):
    db = DBconnect()
    userCollection = db["users"]
    result =userCollection.insert_one(user)
    return result