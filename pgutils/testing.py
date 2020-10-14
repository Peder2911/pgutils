
import unittest

from pgutils.context import TempPg

class PgTest(unittest.TestCase):
    con = None
    initialization = None

    def _callSetUp(self):
        self._tpg = TempPg(self.initialization)
        self.con = self._tpg.con
        super()._callSetUp()

    def _callTearDown(self):
        self._tpg.__exit__(None,None,None)
        self.con = None
        super()._callTearDown()

    def getcursor(self):
        return self.con.cursor()

