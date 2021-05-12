import dbConnection
import unittest
from fastapi import HTTPException
import BaseModel.ModelUser
from faker import Faker

class TestDB(unittest.TestCase):
    def test_connection(self):
        db= dbConnection.DBconnect()
        myCol = db["users"]
        for x in myCol.find():
            self.assertEqual(str(x), "{'_id': ObjectId('60814dab36edb0a032855243'), 'username': 'TestuserStark', 'email': 'sean_bean@asd.com', 'lastname': 'Bean', 'password': 'testpassword', 'firstname': 'Sean'}")

    def test_loginUser(self):
        id = dbConnection.loginUser("TestuserStark", "testpassword")
        self.assertEqual(id, "60814dab36edb0a032855243")
        with self.assertRaises(HTTPException) as context:
            dbConnection.loginUser("failUser", "failPassword")
        self.assertTrue('Gültige Authentifizierung' in context.exception.detail)

    def test_CreateUser(self):
        user = BaseModel.ModelUser.CreateUser()
        fake = Faker()
        setattr(user, "firstname", fake.name())
        user.firstname = fake.name()
        user.lastname = fake.last_name()
        user.username = user.firstname + user.lastname
        user.password = "start123"
        user.email = user.firstname + "."+ user.lastname +"@mail.de"
        id = dbConnection.createUser(user)


        #self.assertEqual(id)



if __name__ == '__main__':
    unittest.main()