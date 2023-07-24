#By: Akash Chinta

import sqlite3
import os

def create_table():
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS accounts (account_name TEXT, username TEXT, password TEXT)")
    conn.commit()
    conn.close()

def add_account(account_name, username, password):
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO accounts VALUES (?, ?, ?)", (account_name, username, password))
    conn.commit()
    conn.close()
    print("Account added successfully!")

def get_account(account_name):
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM accounts WHERE account_name=?", (account_name,))
    account_info = cursor.fetchone()
    conn.close()
    if account_info:
        return account_info
    else:
        return None

def delete_account(account_name):
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM accounts WHERE account_name=?", (account_name,))
    conn.commit()
    conn.close()
    print("Account deleted successfully!")

def show_all_accounts():
    conn = sqlite3.connect("passwords.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM accounts")
    all_accounts = cursor.fetchall()
    conn.close()
    if all_accounts:
        for account in all_accounts:
            print(f"Account: {account[0]}, Username: {account[1]}, Password: {account[2]}")
    else:
        print("No accounts found.")

def main():
    create_table()
    while True:
        print("\nPassword Management System")
        print("1. Add Account")
        print("2. Retrieve Account")
        print("3. Delete Account")
        print("4. Show All Accounts")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            account_name = input("Enter the account name: ")
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            add_account(account_name, username, password)
        elif choice == "2":
            account_name = input("Enter the account name: ")
            account_info = get_account(account_name)
            if account_info:
                print(f"Account: {account_info[0]}, Username: {account_info[1]}, Password: {account_info[2]}")
            else:
                print("Account not found.")
        elif choice == "3":
            account_name = input("Enter the account name: ")
            delete_account(account_name)
        elif choice == "4":
            show_all_accounts()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
