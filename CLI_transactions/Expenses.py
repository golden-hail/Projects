# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 17:20:42 2026

@author: aiaqu
"""

import json

# Load the dataset
with open("expenses.json", "r") as file:
    transactions = json.load(file)

def add_expense(transactions):
    # get last ID from transactions, increment by 1 for new entry
    last_id = max(t['id'] for t in transactions)
    new_id = last_id + 1
    print(new_id)
    
    # import datetime module to check user input date
    while True:
        input_date = input("Enter date in the following format, YYYY-MM-DD: ")
        from datetime import datetime
        
        try:
            # try to parse the string against the ISO format
            datetime.strptime(input_date, "%Y-%m-%d")
            break
        except ValueError:
            # triggered if the format is wrong or the date is invalid
            print("Invalid date or format.\n")

    # enter the expense description
    description = input("Input expense description: ")

    # amount. int or float, else: throw error
    while True:
        amount = input("input amount: ")
        try:
            amount = float(amount)
            break
        except: 
            print('Amount entry must be type int or float. Try again: ')
    
    # ttype income or expense (push 1 for income 2 for expense?)
    while True:
        ex_type = input("Input expense type (income or expense): ")
        
        if ex_type == "income" or "expense":
            break
        elif ex_type == 0:
            ex_type = "expense"
            break
        elif ex_type == 1:
            ex_type = "income"
            break
        else:
            print('Expense type must be "income" or "expense" \n ')
            
    # category
    category = input('input category of expense: ')
        
    # tags
    tags = input("Input expense tags, separated by commas: ")
    tag_list = [tags.strip() for tag in tags.split(",")]
    
    # create a dictionary of values
    # new_entry = {}
    new_entry = {'id' : new_id,
                 'date' : input_date,
                 'description' : description,
                 'amount' : amount,
                 'type' : ex_type,
                 'category' : category,
                 'tags' : tag_list}
    
    new_entry = {'id' : 66,
                 'date' : 66,
                 'description' : 66,
                 'amount' : 66,
                 'type' : 66,
                 'category' : 66,
                 'tags' : 66}
    
    transactions.append(new_entry)
    
    # save to json file
    with open("transaction.json", "w", encoding="utf-8") as file:
        json.dump(transactions, file, indent=4)
    
    # calculate summary
    calculate_total(transactions)
    
def calculate_total(transactions):
    total_expenses = sum(t["amount"] for t in transactions if t["type"] == "expense")
    total_income = sum(t["amount"] for t in transactions if t["type"] == "income")

    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Net Balance: ${total_income - total_expenses:.2f}")
    
    
add_expense(transactions)

listy = [t['tags'] for t in transactions]

tags = [l for l in listy]

tags = []
for l in listy:
    for t in l:
        tags.append(t)
        
set(tags)
        

    