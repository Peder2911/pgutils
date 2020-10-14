
from contextlib import closing
import unittest
from pgutils.testing import PgTest 

class TestTest(PgTest):
    initialization = """
        CREATE TABLE testtable (x int, y int);
    """

    def test_db(self):
        with self.getcursor() as curs:
            curs.execute("""
                INSERT INTO testtable VALUES (1,2);
            """)
            curs.execute("SELECT * FROM testtable;")
            x,y = curs.fetchone()

            self.assertEqual(x,1)
            self.assertEqual(y,2)

