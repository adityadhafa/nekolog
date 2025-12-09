import pytest
import sqlite3
from unittest.mock import patch
from models.cat import Cat
from models.expense import Expense

class ZombieConnection:
    def __init__(self, real_connection):
        self._connection = real_connection
    
    def close(self):
        pass
    
    def __getattr__(self, name):
        return getattr(self._connection, name)
        
    def __setattr__(self, name, value):
        if name == "_connection":
            super().__setattr__(name, value)
        else:
            setattr(self._connection, name, value)

@pytest.fixture(scope="function", autouse=True)
def test_db():
    real_conn = sqlite3.connect(":memory:")
    real_conn.row_factory = sqlite3.Row

    zombie_conn = ZombieConnection(real_conn)

    with patch("database.db.sqlite3.connect", return_value=zombie_conn):

        Cat.create_table()
        Expense.create_table()
        
        yield zombie_conn

        real_conn.close()