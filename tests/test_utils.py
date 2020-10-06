
from contextlib import closing
import unittest
from pgutils.context import tempPg

class TestUtils(unittest.TestCase):
    def test_temp_db(self):
        with tempPg(port = 5454) as con:
            c = con.cursor()
            c.execute("SELECT version()")
            ret = c.fetchall()
        self.assertIsNotNone(ret)
