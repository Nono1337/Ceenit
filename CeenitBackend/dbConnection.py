import pymongo

def DBconnect():
    client = pymongo.MongoClient("mongodb+srv://admin:7SQH8lDQJDwzeY2GfLLS@cluster0.kjvno.mongodb.net/Cluster0?retryWrites=true&w=majority")
    return client.Ceenit

def getUsersIdByUsername(username: str):
    db = DBconnect()
    userCollection = db["users"]
    myquery = {"username": username}
    myresp = userCollection.find(myquery)
    return myresp[0]


# mydb = myclient["Ceenit"]
# myCol = mydb["users"]


