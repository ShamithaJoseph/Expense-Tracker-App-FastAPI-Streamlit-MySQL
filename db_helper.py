import mysql.connector
from contextlib import contextmanager
import logging

logger = logging.getLogger('db_helper')

# configure the custom logger
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('server.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="expense_manager"
        )
    if connection.is_connected():
        print("connection succesful")
    else:
        print("failed in connectiong to a database")

    cursor = connection.cursor(dictionary=True)
    yield cursor

    if commit:
        connection.commit()

    cursor.close()
    connection.close()

def fetch_all_records():
    with get_db_cursor() as cursor:
        cursor.execute("select * from expenses")
        expenses = cursor.fetchall()

        for expense in expenses:
            print(expense)


def fetch_expenses_for_date(expense_date):
    logger.info(f"fetch_expenses_for_date called with date: {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute("select * from expenses where expense_date=%s", (expense_date,))
        expenses = cursor.fetchall()
        return expenses

        # for expense in expenses:
        #     print(expense)



def insert_expense(expense_date, amount, category, notes):
    logger.info(f"Insert_expenses called with date: {expense_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("INSERT INTO expenses(expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)",
                       (expense_date, amount, category, notes)
                       )

def delete_expenses_for_date(expense_date):
    logger.info(f"delete_expenses_for_date called with date: {expense_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("delete  from expenses where expense_date= %s", (expense_date,))


def fetch_expense_summary(start_date, end_date):
    logger.info(f"fetch_expenses_for_date called with start_date:{start_date} and end_data:{end_date}")
    with get_db_cursor() as cursor:
        cursor.execute(
            '''SELECT category, sum(amount) as total 
                        FROM expenses where expense_date between %s and %s
                        group by category;''', (start_date, end_date)
        )
        data = cursor.fetchall()
        return data

def fetch_monthly_expense_summary():
    logger.info(f"fetch_expense_summary_by_months")
    with get_db_cursor() as cursor:
        cursor.execute(
            '''select month(expense_date) as month,
		       monthname(expense_date) as name,
               sum(amount) as total_amount
               from expenses
               group by monthname(expense_date), month(expense_date)
               order by monthname(expense_date), month(expense_date);'''

        )
        data = cursor.fetchall()
        return data

if __name__=="__main__":

    # expenses= fetch_expenses_for_date("2024-08-03")
    # for expense in expenses:
    #     print(expense)
    #summary =fetch_expense_summary("2024-08-01","2024-08-03" )
    summary =fetch_monthly_expense_summary()
    for monthly_summary in summary:
        print(monthly_summary)

    #for record in summary:
    #print(record)
