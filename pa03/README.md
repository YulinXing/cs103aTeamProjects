# PA03
```
Chris Liang 3/25/2023

Tracker is an app that maintains a transactions database.

It also uses an Object Relational Mapping (ORM)
to abstract out the database operations from the
UI/UX code.

The ORM, TodoList, will map SQL rows with the schema
    (rowid,amount,category,date,description)
to Python Dictionaries as follows:

(100, 'food', 2023-10-5, 'beef') <-->

{rowid:1, 
 amount:100, 
 category:'food', 
 date:'2023-10-5', 
 description:'beef'
}

In place of SQL queries, we will have method calls.

This app will store the data in a SQLite database ~/transactions.db
```

## pylint:
```bash
chris-MacBook-Pro-M1-Max:pa03 chrisliang$ pylint transaction.py

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

chris-MacBook-Pro-M1-Max:pa03 chrisliang$ pylint tracker.py

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```

## pytest:
```bash
=================================================================== test session starts ====================================================================
platform darwin -- Python 3.11.1, pytest-7.2.1, pluggy-1.0.0 -- /Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11
cachedir: .pytest_cache
rootdir: /Users/chrisliang/Desktop/Brandeis/CS/COSI_103a/cs103aTeamProjects/pa03
plugins: anyio-3.6.2
collected 7 items                                                                                                                                                         

test_transaction.py::test_show_transactions PASSED                                                                                                   [ 14%]
test_transaction.py::test_add_transaction PASSED                                                                                                     [ 28%]
test_transaction.py::test_delete PASSED                                                                                                              [ 42%]
test_transaction.py::test_summarize_by_date PASSED                                                                                                   [ 57%]
test_transaction.py::test_summarize_by_month PASSED                                                                                                  [ 71%]
test_transaction.py::test_summarize_by_year PASSED                                                                                                   [ 85%]
test_transaction.py::test_summarize_by_category PASSED                                                                                               [100%]

==================================================================== 7 passed in 0.02s =====================================================================
```

## Tracker.py
```bash
command> quit

You have been disconnected

chris-mbp-m1-max:pa03 chrisliang$ 
```

```bash
command> show transactions

item #     amount       category        date               description
---------------------------------------------------------------------------
1          10           aaa             2023-01-01         aaa
2          10           aaa             2019-03-02         aaa
3          20           bbb             2019-03-10         bbb
4          50           ccc             2021-01-23         ccc
---------------------------------------------------------------------------
```

```bash
command> add

Enter amount: 100000
Enter category: test
Enter date (yyyy-mm-dd): 2012-9-7
Enter description: for test

Now the transactions would be like this:

command> show transactions

item #     amount       category        date               description
---------------------------------------------------------------------------
1          10           aaa             2023-01-01         aaa
2          10           aaa             2019-03-02         aaa
3          20           bbb             2019-03-10         bbb
4          50           ccc             2021-01-23         ccc
5          100000       test            2012-09-07         for test
---------------------------------------------------------------------------
```

```bash
command> delete

item #     amount       category        date               description
---------------------------------------------------------------------------
1          10           aaa             2023-01-01         aaa
2          10           aaa             2019-03-02         aaa
3          20           bbb             2019-03-10         bbb
4          50           ccc             2021-01-23         ccc
5          100000       test            2012-09-07         for test
---------------------------------------------------------------------------

Enter transaction id: 5
no tasks to print

Now the transactions would be like this:

command> show transactions

item #     amount       category        date               description
---------------------------------------------------------------------------
1          10           aaa             2023-01-01         aaa
2          10           aaa             2019-03-02         aaa
3          20           bbb             2019-03-10         bbb
4          50           ccc             2021-01-23         ccc
---------------------------------------------------------------------------
```

```bash
command> summarize by date

date               amount
------------------------------
2019-03-02         10
2019-03-10         20
2021-01-23         50
2023-01-01         10
------------------------------
```

```bash
command> summarize by month

month              amount
------------------------------
01                 60
03                 30
------------------------------
```

```bash
command> summarize by year

year               amount
------------------------------
2019               30
2021               50
2023               10
------------------------------
```

```bash
command> summarize by category

category           amount
------------------------------
aaa                20
bbb                20
ccc                50
------------------------------
```

```bash
command> show menu
usage:
            0. quit
            1. show transactions
            2. add transaction
            3. delete transaction
            4. summarize transactions by date
            5. summarize transactions by month
            6. summarize transactions by year
            7. summarize transactions by category
            8. show menu
```

```bash
Here is what will happen if the command is not implemented:

command> category
['category'] is not implemented
usage:
            0. quit
            1. show transactions
            2. add transaction
            3. delete transaction
            4. summarize transactions by date
            5. summarize transactions by month
            6. summarize transactions by year
            7. summarize transactions by category
            8. show menu
```

