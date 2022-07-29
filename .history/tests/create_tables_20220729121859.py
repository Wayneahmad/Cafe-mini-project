def create_orders():
    sql = '''CREATE TABLE Orders(
        OrderID INT NOT NULL AUTO_INCREMENT,
        Customer_name VARCHAR(255) NOT NULL,
        last_name VARCHAR(255) NOT NULL,
        age INT,
        PRIMARY KEY(person_id
    )'''
