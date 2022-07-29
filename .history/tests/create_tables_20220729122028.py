def create_orders():
    sql = '''CREATE TABLE Orders(
        OrderID INT NOT NULL AUTO_INCREMENT,
        Customer_name VARCHAR(255) NOT NULL,
        Address VARCHAR(255) NOT NULL,
        Tel VARCHAR(255) NOT NULL,
        Courier VARCHAR(255) NOT NULL,
        Order_status VARCHAR(255) NOT NULL,
        Cart VARCHAR(255) NOT NULL,
        PRIMARY KEY(person_id
    )'''
