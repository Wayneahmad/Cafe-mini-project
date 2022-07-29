import time
import os
from dotenv import load_dotenv
import pandas as pd
from art import *
import pymysql
import os
import csv
ID_PRODUCT = "SELECT ID, Product FROM Products"
order_statuses = ["PREPARING", "OUT FOR DELIVERY", "DELIVERED", "CANCELLED"]
order_keys = ["Orders", "Customer_name", "Address",
              "Tel", "Courier", "order_status", "Cart", "OrderID"]
products_values = ["Products", "Product", "Price", "ID"]
courier_keys = ["Couriers", "Courier", "Tel", "CourierID"]
CUSTOMER_KEYS = ["Customers", "Customer", "Address", "Tel", "CustomerID"]
COURIER_ID = "SELECT Courier FROM Couriers"
ALLTABLES = ["Products", "Couriers", "Customer", "Orders"]

# Load environment variables from .env file


def db_connect():
    load_dotenv()
    host = os.environ.get("mysql_host")
    user = os.environ.get("mysql_user")
    password = os.environ.get("mysql_pass")
    database = os.environ.get("mysql_db")
    # Establish a database connection
    connection = pymysql.connect(
        host,
        user,
        password,
        database
    )

    return connection


# if __name__ == "__main__":
connection = db_connect()

# A cursor is an object that represents a DB cursor, which is used to manage the context of a fetch operation.
cursor = connection.cursor()


def select_table_query(table_name):
    return f"SELECT * FROM {table_name}"

# Saving database to a csv in the root directory


def csv_save(filename, orders_dict):
    orders_keys = orders_dict[0].keys()
    with open((f"{filename[0]}.csv"), "w") as file:
        dict_writer = csv.DictWriter(file, orders_keys)
        dict_writer.writeheader()
        dict_writer.writerows(orders_dict)


# Download selected database to a csv
def download(database):
    print_file(database)
    selection = input("\nSelect table by index you would like to download: ")
    if selection == "1":
        csv_save(products_values, load_dict(
            select_table_query(products_values[0])))
    elif selection == "2":
        csv_save(courier_keys, load_dict(select_table_query(courier_keys[0])))
    elif selection == "3":
        csv_save(CUSTOMER_KEYS, load_dict(
            select_table_query(CUSTOMER_KEYS[0])))
    elif selection == "4":
        csv_save(order_keys, load_dict(select_table_query(order_keys[0])))
    else:
        invalid()

# Loading database and putting each row into a list of dictionaries


def load_dict(dictss):
    cursorQuery = dictss
    cursor.execute(cursorQuery)
    records = cursor.fetchall()
    insertObject = []
    columnNames = [column[0] for column in cursor.description]

    for record in records:
        insertObject.append(dict(zip(columnNames, record)))
    return insertObject


def print_file(list):
    for index, items in enumerate(list):
        print(index + 1, items)
        time.sleep(.1)


def print_panda(data):
    df = pd.DataFrame.from_dict(data)
    # df.index = df.index + 1
    print(df.to_string(index=False))


# Delete entry by ID from selected database

def delete_id(val):
    print_panda(load_dict(select_table_query(val[0])))
    delete = int(input("\nWhat do you want to delete?: "))
    sql = f"DELETE FROM {val[0]} WHERE {val[-1]} = %s"
    cursor.execute(sql, ({delete}))
    connection.commit()

# Inputs function for both Product/couriers


def get_inputs(values):
    name = input(f"\nAdd {values[1]}: ").title()
    value = input(f"Set {values[2]}: ")
    return name, value

# Sort orders by statuses


def sort_by(keys):
    print("")
    print_file(keys)
    try:
        index = int(input("\nFilter orders by: ")) - 1
        test = load_dict(
            (f"SELECT * FROM Orders WHERE order_status = '{keys[index]}' ORDER BY order_status DESC"))
        count = len([e for e in test if isinstance(e, dict)])
        print(f"\nTotal orders {keys[index]} is '{count}'\n")
        print_panda(test)
    except:
        invalid()


# Add entry function used by Products/Couriers/Customers

def add_entry(values, cursor, prod):
    sql = f"INSERT INTO {values[0]} ({values[1]}, {values[2]}) VALUES (%s, %s)"
    cursor.execute(sql, ({prod[0]}, {prod[1]}))
    refresh()
    print(f"\n---UPDATED {values[0].upper()}---\n")
    print_panda(load_dict(select_table_query(values[0])))
    connection.commit()

# Update Prod/Couriers


def update_entry(database):
    try:
        # Prints database, Chooses what to update

        print_panda(load_dict(select_table_query(database[0])))
        update_select = int(input(f"\nSelect {database[1]} by ID?: "))
        print_file(database[1:-1])
        key = int(input("What would you like to update?: "))

        if key == 1:
            update = input(f"Update {database[1]} name: ").title()
        elif key == 2:
            update = input(f"Update {database[1]} {database[2]}: ")
        elif key == 3 and database[0] == "Customers":
            update = input(f"Update {database[1]} {database[3]}: ")

        cursor.execute(
            f"UPDATE {database[0]} SET {database[key]} = '{update}' WHERE {database[-1]} = {update_select}")
        connection.commit()
        refresh()
        print(f"\n---UPDATED {database[0].upper()}---\n")
        print_panda(load_dict(select_table_query(database[0])))

    except:
        invalid()


def print_id(data):
    cursor.execute(f"SELECT {data[-1]}, {data[1]} FROM {data[0]}")
    rows = cursor.fetchall()
    print("")
    for row in rows:
        print(f"{str(row[0])} {row[1]}")
        time.sleep(.1)


# Function that handles getting customers info

def customer_info():
    name = input("Enter your name: ")
    address = input("Enter your current address: ")
    tel = input("Enter Tel: ")
    cursor.execute(
        f"INSERT INTO Customers (Customer, Address, Tel) VALUES (\'{name}\', \'{address}\', '{tel}')")
    return name, address, tel

# Function that gets orders inputs


def order_inputs():
    customers = customer_info()
    product_index = update_Oproducts()
    print_id(courier_keys)
    selected_courier = input("Choose your courier: ")
    return customers[0], customers[1], customers[2],  product_index, selected_courier


# Add a new order
def add_order():
    prod_inputs = order_inputs()  # Gets orders inputs
    # Runs SQL query
    sql = f"INSERT INTO Orders (Customer_name, Address, Tel, couriers, order_status, Cart) VALUES (\'{prod_inputs[0]}\', \'{prod_inputs[1]}\', \'{prod_inputs[2]}\', \'{prod_inputs[4]}\', 'PREPARING', \'{prod_inputs[3]}\')"
    refresh()
    cursor.execute(sql)
    connection.commit()


def update_order(order_keys):
    try:
        # Prints orders and gets key of what to update

        print_panda(load_dict(select_table_query(order_keys[0])))
        order_select = int(input("\nSelect order by ID: "))
        print_file(order_keys[1:-1])
        key_update = int(input("What would you like to update?: "))
    # If user selects 4, 5 or 6 Run the selected update functions.

        if key_update == 5:
            update_status(order_select)
        elif key_update == 4:
            update_Ocourier(order_select)  # Updates the orders Courier
        elif key_update == 6:
            product_index = update_Oproducts()  # Updates the orders Products
            sql = f"UPDATE Orders SET Cart = '{product_index}' WHERE OrderID = {order_select}"
            cursor.execute(sql)
            connection.commit()
        else:
            # Updates the order at chosen key
            update_with = input("Update with?: ").title()
            cursor.execute(
                f"UPDATE Orders SET {order_keys[key_update]} = %s WHERE OrderID = %s", (update_with, order_select))
            connection.commit()

    except:
        invalid()


def view_one_order():
    # Allows you to view one order at a time
    try:
        while True:
            # refresh()
            order_select = (
                input("\nTo view order, select ID or hit <ENTER> to exit: "))
            if order_select == "":
                break
            else:
                test = load_dict(
                    f"SELECT * FROM Orders WHERE OrderID = {int(order_select)}")
                print("\n --Selected Order--\n")
                print_panda(test)
    except:
        invalid()


# Updates just the orders status which is called in update_order func
def update_status(order_select):
    print_file(order_statuses)
    status_index = int(input("\nSelect status: ")) - 1
    sql = f"UPDATE Orders SET order_status = %s WHERE OrderID = {order_select}"
    cursor.execute(sql, (order_statuses[status_index]))
    connection.commit()


# Updates just the orders Courier which is called in update_order func
def update_Ocourier(order_select):
    print_panda(load_dict(select_table_query(courier_keys[0])))
    status_index = int(input("\nSelect courierID: "))
    sql = f"UPDATE Orders SET couriers = %s WHERE OrderID = {order_select}"
    cursor.execute(sql, (status_index))
    connection.commit()


def update_Oproducts():  # Updates just the orders Products which is called in update_order func
    print("")
    print_panda(load_dict(ID_PRODUCT))
    product_index = input(
        "\nEnter index seperated by a ',' Example 1, 3, 4: ").split(',')
    product_index = [int(i) for i in product_index]
    return product_index


def ani():
    os.system("clear")
    print("\nLoading.")
    time.sleep(.2)
    os.system("clear")
    print("\nLoading..")
    time.sleep(.2)
    os.system("clear")
    print("\nLoading...")
    time.sleep(.2)


def refresh():
    ani()
    ani()
    os.system("clear")


def save_exit():
    os.system("clear")
    print(logo)
    print("Saving changes...")
    time.sleep(2)
    print("Goodbye!")


def to_continue():
    return input("\n----Press <ENTER> to return to menu----")


def invalid():
    print("Please select a valid input")
    time.sleep(1)
