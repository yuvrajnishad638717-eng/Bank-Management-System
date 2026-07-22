import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import mysql.connector 

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "PASSWORD",
    database = "bank_db"
)
cursor = conn.cursor()

def create_account():
    account_number = int(input("Enter your account number: "))
    customer_name= input("Enter customer name: ")
    age = int(input("Enter your age: "))
    gender = input("Enter your gender: ")
    phone = int(input("Enter your phone number: "))
    email = input("Enter your emails: ")
    account_type = input("Enter account type: ")
    balance = int(input("Enter your balance: "))
    city = input("Enter your city: ")
    state = input("Enter your state: ")
    created_at = datetime.now()
    
    query = """ INSERT INTO customeres(account_number, customer_name, age, gender, phone, email, account_type, balance, city, state, created_at)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        account_number,
        customer_name,
        age,
        gender,
        phone,
        email,
        account_type,
        balance,
        city,
        state,
        created_at
    )
    
    print(created_at)
    print(type(created_at))
    print(values)

    print("---------ACCOUNT_CREATE_SUCCESSFULLY----------")
    cursor.execute(query, values)
    conn.commit()

def view_all_account():
    query = "SELECT * FROM customeres"
    
    df = pd.read_sql(query, conn)
    
    print(df)
    
def update_account():
    account_type = input("Enter your account_type: ")
    gender = input("Enter your gender: ")
    customer_name = input("Enter new customer_name: ")
    account_number = int(input("Enter your new account_number: "))
    customer_id = int(input("Enter your customer_id: "))
    
    query = """ UPDATE customeres
    SET account_type = %s, gender = %s, customer_name = %s, account_number = %s WHERE customer_id = %s
    """
    values = (
        account_type,
        gender,
        customer_name,
        account_number,
        customer_id
    )
    
    cursor.execute(query, values)
    conn.commit()
    print("\n .........UPDATED_SUCCESSFULLY........")
    
def delete_account():
    customer_id = int(input("Enter your customer_id: "))
    
    query = """
    DELETE FROM customeres WHERE customer_id = %s
    """
    values = (
        customer_id,
    )
    
    print("--------ACCOUNT_DELETED SUCCESSFULLY---------")
    cursor.execute(query, values)
    conn.commit()
    
def deposit_amount():
    customer_id = int(input("Enter your customer_id: "))
    deposit = int(input("deposit amount: "))
    query = """
    SELECT balance
    FROM customeres WHERE customer_id = %s
    """
    cursor.execute(query, (customer_id,))
    result = cursor.fetchone()
    
    current_balance = result[0] 
    new_balance = current_balance + deposit
    
    query = """
    UPDATE customeres
    SET balance = %s WHERE customer_id = %s
    """
    cursor.execute(query, (new_balance, customer_id))
    conn.commit()
    
def withdraw_amount():
   customer_id = int(input("Enter customer_id: "))
   withdraw = int(input("Enter withdraw amount: "))
   
   query = """
   SELECT balance
   FROM customeres WHERE customer_id = %s
   """
   cursor.execute(query, (customer_id,))
   result = cursor.fetchone()
   
   current_balance = result[0]
   new_balance = current_balance - withdraw
   
   query = """
   UPDATE customeres
   SET balance = %s WHERE customer_id = %s
   """
   cursor.execute(query, (new_balance, customer_id))
   conn.commit()
   
    
def main():
    while True:
        print("\n -------------BANK_MANAGEMENT_SYSTEM--------------")
        print(" 1 create account")
        print(" 2 view account")
        print(" 3 update account")
        print(" 4 delete account")
        print(" 5 deposit_amount")
        print(" 6 withdraw amount")
        print(" 7 exits")
        
        choice  =  int(input("Enter your choice: "))
        
        if choice == 1:
            create_account()
            
        elif choice == 2:
            view_all_account()
            
        elif choice == 3:
            update_account()
            
        elif choice == 4:
            delete_account()
            
        elif choice == 5:
            deposit_amount()
            
        elif choice == 6:
            withdraw_amount()
            
        elif choice == 7:
            print("----GOOD_BYE---")
            break
        else:
            print("INVALID_CHOICE.....")
            

conn.commit()
if __name__ == "__main__":
    main()
    
