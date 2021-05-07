import dbConnection
import unittest
from  fastapi import HTTPException

class TestDB(unittest.TestCase):
    def test_connection(self):
        db= dbConnection.DBconnect()
        myCol = db["users"]
        for x in myCol.find():
            self.assertEqual(str(x), "{'_id': ObjectId('60814dab36edb0a032855243'), 'username': 'TestuserStark', 'email': 'sean_bean@asd.com', 'fristname': 'Sean', 'lastname': 'Bean', 'password': 'testpassword'}")

    def test_loginUser(self):
        id = dbConnection.loginUser("TestuserStark", "testpassword")
        self.assertEqual(id, "60814dab36edb0a032855243")
        with self.assertRaises(HTTPException) as context:
            dbConnection.loginUser("failUser", "failPassword")
        self.assertTrue('Gültige Authentifizierung' in context.exception.detail)

if __name__ == '__main__':
    unittest.main()