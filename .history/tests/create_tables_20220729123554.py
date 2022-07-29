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
    sql = '''CREATE TABLE IF NOT EXISTS Product(
        ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        Products VARCHAR(255) NOT NULL,
        Price VARCHAR(255) NOT NULL
    )'''
    cursor.execute(sql)
    connection.commit()


create_products()


def create_couries():
    sql = '''CREATE TABLE IF NOT EXISTS Couriers (
        CourierID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        Customer_name VARCHAR(255) NOT NULL,
        Address VARCHAR(255) NOT NULL,
        Tel VARCHAR(255) NOT NULL,
        Courier VARCHAR(255) NOT NULL,
        order_status VARCHAR(255) NOT NULL,
        Cart VARCHAR(255) NOT NULL
    )'''
    cursor.execute(sql)
    connection.commit()
