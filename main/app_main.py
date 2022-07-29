
from art import logo
import os
from file_manager import *
from data_visual import show_status

# Menu functions

def main_menu():
    print(loadinglogo)
    print("Vending Machine")
    print("""
   0 - Exit
   1 - Product
   2 - Couriers
   3 - Orders
   4 - Customers
   5 - Download tables
    """)
    return input("Chose your option: ").lower()


def submenu():
    refresh()
    print(logo2)
    print("Product Menu")
    print("""
   0 - Return to the main menu
   1 - List products
   2 - Add product
   3 - Update product
   4 - Delete product
    """)
    return input("Chose your option: ").lower()


def couriers_menu():
    refresh()
    print(delivery)
    print("Couriers Machine")
    print("""
   0 - Return to the main menu
   1 - List Couriers
   2 - Add Couriers
   3 - Update Couriers
   4 - Delete Couriers
    """)
    return input("Chose your option: ").lower()


def orders_menu():
    refresh()
    print(orders_logo)
    print("Orders")
    print("""
   0 - Return to the main menu
   1 - List orders
   2 - Create order
   3 - Update order
   4 - Show orders by status
   5 - Status visualization 
   6 - Delete order
  """)
    return input("Chose your option: ").lower()


def customer_menu():
    refresh()
    print(office)
    print("Customer")
    print("""
   0 - Return to the main menu
   1 - List customers
   2 - Add new customer
   3 - Update customer
   4 - Delete csutomer
  """)
    return input("Chose your option: ").lower()

if __name__ == "__main__":
    while True:
        os.system("clear")
        main_settings = main_menu()

        if main_settings == "0": 
            connection.commit()
            cursor.close()
            connection.close()
            save_exit()
            break
        elif main_settings == "1":
            # Product Menu

            while True:
                settings = submenu()
                if settings == "0":
                    refresh()
                    break
                elif settings == "1":
                    print(f"\n---LISTING {products_values[0].upper()}---\n")
                    print_panda(load_dict(select_table_query(products_values[0])))
                    to_continue()
                elif settings == "2":
                    add_entry(products_values, cursor, get_inputs(products_values))
                    to_continue()
                elif settings == "3":
                    print(f"\n---LISTING {products_values[0].upper()}---\n")
                    update_entry(products_values)
                    to_continue()
                elif settings == "4":
                    print(f"\n---LISTING {products_values[0].upper()}---\n")
                    delete_id(products_values)
                    to_continue()
                elif settings == "5":
                    download(ALLTABLES)
                else:
                    invalid()
    # Courier Menu

        elif main_settings == "2":
            while True:
                settings = couriers_menu()
                if settings == "0":                 
                    refresh()
                    break
                elif settings == "1":               
                    print(f"\n---LISTING {courier_keys[0].upper()}---\n")
                    print_panda(load_dict(select_table_query(courier_keys[0])))
                    to_continue()
                elif settings == "2":               
                    add_entry(courier_keys, cursor, get_inputs(courier_keys))
                    to_continue()
                elif settings == "3":
                    print(f"\n---LISTING {courier_keys[0].upper()}---\n") 
                    update_entry(courier_keys)                
                    to_continue()
                elif settings == "4":
                    print(f"\n---LISTING {courier_keys[0].upper()}---\n")               
                    delete_id(courier_keys)
                    to_continue()
                else:
                    invalid()
    # Orders Menu

        elif main_settings == "3":
            while True:
                settings = orders_menu()
                if settings == "0":                 
                    refresh()
                    break
                elif settings == "1":
                    print(f"\n---LISTING {order_keys[0].upper()}---\n") 
                    print_panda(load_dict(select_table_query(order_keys[0]))) 
                    view_one_order()                               
                elif settings == "2":
                    add_order()
                    print(f"\n---UPDATED {order_keys[0].upper()}---\n")
                    print_panda(load_dict(select_table_query(order_keys[0])))
                    view_one_order()
                elif settings == "3": 
                    update_order(order_keys)
                    refresh()
                    print_panda(load_dict(select_table_query(order_keys[0])))   
                elif settings == "4":
                    sort_by(order_statuses)
                    to_continue()
                elif settings == "5":    
                    show_status()           
                    to_continue()
                elif settings == "6":    
                    delete_id(order_keys)           
                    to_continue()
                else:
                    invalid()
    #Customers Menu

        elif main_settings == "4":
            while True:
                settings = customer_menu()
                if settings == "0":                 
                    refresh()
                    break
                elif settings == "1":               
                    print(f"\n---LISTING {CUSTOMER_KEYS[0].upper()}---\n")
                    print_panda(load_dict(select_table_query(CUSTOMER_KEYS[0])))
                    to_continue()
                elif settings == "2":               
                    customer_info()
                    print(f"\n---LISTING {CUSTOMER_KEYS[0].upper()}---\n")
                    print_panda(load_dict(select_table_query(CUSTOMER_KEYS[0])))
                    to_continue()
                elif settings == "3":
                    print(f"\n---LISTING {CUSTOMER_KEYS[0].upper()}---\n") 
                    update_entry(CUSTOMER_KEYS)                
                    to_continue()
                elif settings == "4":
                    print(f"\n---LISTING {CUSTOMER_KEYS[0].upper()}---\n")               
                    delete_id(CUSTOMER_KEYS)
                    to_continue()
                else:
                    invalid()
        elif main_settings == "5":
            download(ALLTABLES)
        else:
            invalid()

