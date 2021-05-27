import dbConnection
import unittest
from fastapi import HTTPException
from BaseModel.ModelUser import CreateUser
from faker import Faker
from bson.objectid import ObjectId

class TestDB(unittest.TestCase):
       def test_loginUser(self):
        id = dbConnection.loginUser("TestuserStark", "testpassword")
        self.assertEqual(id, "60814dab36edb0a032855243")
        with self.assertRaises(HTTPException) as context:
            dbConnection.loginUser("failUser", "failPassword")
        self.assertTrue('Gültige Authentifizierung' in context.exception.detail)

    def test_CreateUser(self):
        fake = Faker()
        firstname = fake.first_name()
        lastname = fake.last_name()
        user = {
            "firstname": firstname,
            "lastname": lastname,
            "username": firstname + lastname,
            "password": "start123",
            "email": firstname + "." + lastname + "@mail.de"
        }
        id = dbConnection.createUser(user)

        self.assertEqual(id, dbConnection.loginUser(user["username"], user["password"]))

    def test_getMovieListById(self):
        resp=dbConnection.getMovieListById("60a667979c7e383c848b2cd5")
        self.assertEqual( resp["name"] ,"Erste Liste")

    def test_getMovieListsByName(self):
        resp = dbConnection.getMovieListsByName("Erste Liste")
        self.assertEqual(resp[0]["_id"], ObjectId("60a667979c7e383c848b2cd5"))

    def test_CreateMovieList(self):
        fake = Faker()
        randomName = fake.pystr()
        resp = dbConnection.createMovielist({"name":randomName, "description": ""})
        self.assertEqual(dbConnection.getMovieListById(resp)["name"],randomName)

    def test_deleteMovieList(self):
        fake = Faker()
        randomName = fake.pystr()
        createdID=dbConnection.createMovielist({"name": randomName, "description": ""})
        resp = dbConnection.deleteMovieList(createdID)
        self.assertEqual(1, resp.deleted_count)


    def test_CreateAandFindMovieReview(self):
        fake = Faker()
        movieID= 76341
        countReviews=len(dbConnection.getMovieReviewById(movieID))
        resp=dbConnection.createMovieReview(movieID, {"userID": "60814dab36edb0a032855243", "content" : fake.text()})
        self.assertEqual(countReviews +1 , len(dbConnection.getMovieReviewById(movieID)))
    def test_getAllLists():
        resp =dbConnection.getMovieLists()
        print(resp)

if __name__ == '__main__':
    unittest.main()
