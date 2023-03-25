'''
This program is written by Tim

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

Recall that sys.argv is a list of strings capturing the
command line invocation of this program
sys.argv[0] is the name of the script invoked from the shell
sys.argv[1:] is the rest of the arguments (after arg expansion!)

Note the actual implementation of the ORM is hidden and so it 
could be replaced with PostgreSQL or Pandas or straight python lists
'''

import sys
import datetime
from transaction import Transaction

def print_usage():
    ''' print the menu options '''
    print('''usage:
            0. quit
            1. show transactions
            2. add transaction
            3. delete transaction
            4. summarize transactions by date
            5. summarize transactions by month
            6. summarize transactions by year
            7. summarize transactions by category
            8. show menu
            '''
          )

def print_transactions(transaction):
    ''' print the todo items '''
    if len(transaction)==0:
        print('no tasks to print')
        return

    for item in transaction:
        values = tuple(item.values())

    if len(values)==5:
        print('\n' + f"{'item #':<10} {'amount':<12} {'category':<15} {'date':<18} {'description'}")
        print('-'*75)
        for item in transaction:
            values = tuple(item.values())
            print(f"{values[0]:<10} {values[1]:<12} {values[2]:<15} {values[3]:<18} {values[4]}")
    else:
        print('\n' + f"{'category':<18} {'amount'}")
        print('-'*30)
        for item in transaction:
            values = tuple(item.values())
            print(f"{values[0]:<18} {values[1]}")

def print_date_summary(transaction):
    ''' print the todo items '''
    if len(transaction)==0:
        print('no tasks to print')
        return
    print('\n' + f"{'date':<18} {'amount'}")
    print('-'*30)
    for item in transaction:
        values = tuple(item.values())
        print(f"{values[0]:<18} {values[1]}")

def print_year_summary(transaction):
    ''' print the todo items '''
    if len(transaction)==0:
        print('no tasks to print')
        return
    print('\n' + f"{'year':<18} {'amount'}")
    print('-'*30)
    for item in transaction:
        values = tuple(item.values())
        print(f"{values[0]:<18} {values[1]}")


def print_month_summary(transaction):
    ''' print the todo items '''
    if len(transaction)==0:
        print('no tasks to print')
        return
    print('\n' + f"{'month':<18} {'amount'}")
    print('-'*30)
    for item in transaction:
        values = tuple(item.values())
        print(f"{values[0]:<18} {values[1]}")

def process_args(arglist):
    ''' examine args and make appropriate calls to TodoList'''
    transaction = Transaction("transactions.db")
    if arglist==[]:
        print_usage()
    elif arglist[0]=='quit':
        print('\n' + "You have been disconnected" + '\n')
        sys.exit()
    elif arglist[0]=='show transactions':
        print_transactions(transaction.show_transactions())
    elif arglist[0]=='add' or arglist[0]=='add transaction':
        amount = int(input('\n' + 'Enter amount: '))
        category = input('Enter category: ')
        date = datetime.datetime.strptime(input('Enter date (yyyy-mm-dd): '), '%Y-%m-%d')
        description = input('Enter description: ')
        info = {'amount':amount, 'category':category, 'date':date.date(), 'description':description}
        transaction.add_transaction(info)
    elif arglist[0]=='delete' or arglist[0]=='delete transaction':
        print_transactions(transaction.show_transactions())
        print('-'*75 + '\n')
        num = input('Enter transaction id: ')
        print_transactions(transaction.delete_transaction(num))
    elif arglist[0]=='summarize by date':
        print_date_summary(transaction.summarize_by_date())
    elif arglist[0]=='summarize by month':
        print_month_summary(transaction.summarize_by_month())
    elif arglist[0]=='summarize by year':
        print_year_summary(transaction.summarize_by_year())
    elif arglist[0]=='summarize by category':
        print_transactions(transaction.summarize_by_category())
    elif arglist[0]=='show menu' or arglist[0]=='menu':
        print_usage()
    else:
        print(arglist,"is not implemented")
        print_usage()

def toplevel():
    ''' read the command args and process them'''
    if len(sys.argv)==1:
        # they didn't pass any arguments,
        # so prompt for them in a loop
        print('\n' + '-'*40)
        print_usage()
        args = []
        while args!=['']:
            args = input("command> ").split(' ')
            curr = args[0]
            args = [' '.join(args[0:])]
            process_args(args)
            if curr=='summarize':
                print('-'*30 + '\n')
            elif args[0]=='show transactions':
                print('-'*75 + '\n')
            else:
                print('-'*40 + '\n')
    else:
        # read the args and process them
        args = sys.argv[1:]
        process_args(args)
        print('-'*40+'\n'*3)

if __name__ == '__main__':
    toplevel()
