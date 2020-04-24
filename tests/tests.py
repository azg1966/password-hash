import unittest
from password_hash import generate_password, check_password

PASSWORD = 'some_password'
WRONG_PASSWORD = 'wrong_password'


class TestPasswordHash(unittest.TestCase):

    def setUp(self):
        self.hashed_password = generate_password(PASSWORD)

    def test_generate_password(self):
        self.assertNotEqual(PASSWORD, self.hashed_password)

    def test_check_password(self):

        self.assertFalse(
            check_password(WRONG_PASSWORD, self.hashed_password))

        self.assertTrue(
            check_password(PASSWORD, self.hashed_password))
