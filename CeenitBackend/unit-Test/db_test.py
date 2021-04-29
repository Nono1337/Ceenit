import dbConnection
import unittest

class TestDB(unittest.TestCase):
    def test_connection(self):
        db= dbConnection.DBconnect()
        myCol = db["users"]
        for x in myCol.find():
            self.assertEqual(str(x), "{'_id': ObjectId('60814dab36edb0a032855243'), 'username': 'Testuser Stark', 'email': 'sean_bean@asd.com', 'fristname': 'Sean', 'lastname': 'Bean', 'password': '$2b$12$UREFwsRUoyF0CRqGNK0LzO0HM/jLhgUCNNIJ9RJAqMUQ74crlJ1Vu'}")
    def test_getUserIDByUsername(self):
        id = dbConnection.getUsersIdByUsername("Testuser_Stark")
        self.assertEqual(id, "60814dab36edb0a032855243")
        
if __name__ == '__main__':
    unittest.main()