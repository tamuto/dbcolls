import unittest
import os
import sqlite3

from dbcolls.sqlite3.Row import DictRow


class TestRow(unittest.TestCase):
    def test_get_attr(self):
        if os.path.exists('./dist/test.sqlite'):
            os.remove('./dist/test.sqlite')

        with sqlite3.connect('./dist/test.sqlite') as conn:
            conn.row_factory = DictRow

            conn.execute('CREATE TABLE TEST ( aaa char(3), bbb int )')
            conn.execute("INSERT INTO TEST VALUES ('test1', 10)")
            conn.execute("INSERT INTO TEST VALUES ('test2', 20)")
            conn.execute("INSERT INTO TEST VALUES ('test3', 30)")

            result = conn.execute('SELECT * FROM TEST')
            for r in result:
                print(r.aaa, r.bbb)
