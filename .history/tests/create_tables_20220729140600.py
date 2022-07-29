from file_manager import cursor, connection


def create_orders():
    sql = '''CREATE TABLE IF NOT EXISTS Orders (
        OrderID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        Customer_name VARCHAR(255) NOT NULL,
        Address VARCHAR(255) NOT NULL,
        Tel VARCHAR(255) NOT NULL,
        Courier VARCHAR(255) NOT NULL,
        order_status VARCHAR(255) NOT NULL,
        Cart VARCHAR(255) NOT NULL
    )'''
    cursor.execute(sql)
    connection.commit()


create_orders()


def create_products():
    sql = '''CREATE TABLE IF NOT EXISTS Products(
        ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        Product VARCHAR(255) NOT NULL,
        Price VARCHAR(255) NOT NULL
    )'''
    cursor.execute(sql)
    connection.commit()


create_products()


def create_couries():
    sql = '''CREATE TABLE IF NOT EXISTS Couriers (
        CourierID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        Courier VARCHAR(255) NOT NULL,
        Tel VARCHAR(255) NOT NULL
    )'''
    cursor.execute(sql)
    connection.commit()


create_couries(


def create_customers():
    sql='''CREATE TABLE IF NOT EXISTS Customers (
        CustomerID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        Customer VARCHAR(255) NOT NULL,
        Address VARCHAR(255) NOT NULL,
        Tel VARCHAR(255) NOT NULL
    )'''
    cursor.execute(sql)
    connection.commit()


create_customers()

print("tables have been successfully created")
