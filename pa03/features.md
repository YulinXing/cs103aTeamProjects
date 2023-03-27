# Features
```
each transaction has following properties: item #, amount, category, date, description

functions include
{show all transactions, 
add transactions, 
delete transaction, 
summarize transaction by date, month, year, and category
}
```

# Implementation
- ## show transactions
```bash
when call show transactions, the program will show the table which contains information of each transaction

command> show transactions

item #     amount       category        date               description
---------------------------------------------------------------------------
1          10           aaa             2023-01-01         aaa
2          10           aaa             2019-03-02         aaa
3          20           bbb             2019-03-10         bbb
4          50           ccc             2021-01-23         ccc
---------------------------------------------------------------------------
```
- ## add transaction
```bash
when call add transaction, the program will ask the user to input the information of the transaction and add the transaction to the database

command> add

Enter amount: 100000
Enter category: test
Enter date (yyyy-mm-dd): 2012-9-7
Enter description: for test

Now table will look like this:

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
- ## delete transaction
```bash
when call delete transaction, the program will ask the user to input the item number of the transaction and delete the transaction from the database

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
- ## summarize transactions by date, month, year, or category
```bash
when call summarize by date, month, year, or category, the program will show the total amount of transactions according to the conditions

command> summarize by date

date               amount
------------------------------
2019-03-02         10
2019-03-10         20
2021-01-23         50
2023-01-01         10
------------------------------

command> summarize by month

month              amount
------------------------------
01                 60
03                 30
------------------------------

command> summarize by year

year               amount
------------------------------
2019               30
2021               50
2023               10
------------------------------

command> summarize by category

category           amount
------------------------------
aaa                20
bbb                20
ccc                50
------------------------------
```
