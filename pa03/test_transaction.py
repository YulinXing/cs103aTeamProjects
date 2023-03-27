# chris liang 3/25/2023
# test 
import sqlite3
import pytest
import datetime
from transaction import Transaction, to_dict, tuples_to_dicts

@pytest.fixture
def tuples():
    " create some tuples to put in the database "
    return [(10, "category0", datetime.date(2023, 1, 1).strftime('%Y-%m-%d'), "test0"), 
            (10, "category1", datetime.date(2023, 1, 2).strftime('%Y-%m-%d'), "test1")
           ]

@pytest.fixture
def returned_tuples(tuples):
    " add a rowid to the beginning of each tuple "
    return [(i+1,)+tuples[i] for i in range(len(tuples))]

@pytest.fixture
def returned_dicts(tuples):
    " add a rowid to the beginning of each tuple "
    return tuples_to_dicts([(i+1,)+tuples[i] for i in range(len(tuples))])

@pytest.fixture
def transactions_path(tmp_path):
    yield tmp_path / 'transactions.db'

@pytest.fixture(autouse=True)
def transactions(transactions_path,tuples):
    "create and initialize the transactions.db database in /tmp "
    con= sqlite3.connect(transactions_path)
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS transactions (amount int, category text, date date, description text)''')
    cur = con.cursor()
    for i in range(len(tuples)):
        cur.execute('''insert into transactions values(?,?,?,?)''',tuples[i])
    con.commit()
    # create the todolist database
    con.commit()
    t = Transaction(transactions_path)
    yield t
    cur.execute('''drop table transactions''')
    con.commit()

def test_show_transactions(transactions, returned_dicts):
    t = transactions
    result = t.show_transactions()
    expected = returned_dicts
    assert expected == result


def test_add_transaction(transactions, returned_dicts):
    t = transactions
    tuple = (len(returned_dicts)+1, 100, 'food', datetime.date(2023, 10, 5).strftime('%Y-%m-%d'), 'beef')
    transactions.add_transaction(to_dict(tuple))
    results = t.show_transactions()
    assert results[-1] == to_dict(tuple)

def test_delete(transactions,returned_dicts):
    t = transactions
    t.delete_transaction(1)
    results = t.show_transactions()
    expected = returned_dicts
    assert results == expected[1:]

def test_summarize_by_date(transactions):
    t = transactions
    tuple = ('2023-01-02', 10)
    results = t.summarize_by_date()
    assert results[-1] == to_dict(tuple)

def test_summarize_by_month(transactions):
    t = transactions
    tuple = ('01', 20)
    results = t.summarize_by_month()
    assert results[-1] == to_dict(tuple)

def test_summarize_by_year(transactions):
    t = transactions
    tuple = ('2023', 20)
    results = t.summarize_by_year()
    assert results[-1] == to_dict(tuple)

def test_summarize_by_category(transactions):
    t = transactions
    tuple = ('category1', 10)
    results = t.summarize_by_category()
    assert results[-1] == to_dict(tuple)