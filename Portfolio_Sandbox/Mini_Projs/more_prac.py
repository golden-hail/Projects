# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 13:12:29 2026

@author: aiaqu
"""

score = 10000

'''Functions and conditionals: Write risk_label(score) that returns "low" for scores under 40, 
"medium" for 40-69, "high" for 70 and above, and "invalid" if the score is outside 0-100.'''
    
def risk_label(score):
    if not isinstance(score, (int, float)) or score < 0 or score > 100:
        return "invalid"
    elif score < 40:
        return "low"
    elif score <= 69:
        return "medium"
    else:
        return "high"
    
risk_label(score)
    

'''Loops and lists: Given a list of claim amounts, 
write summarize(amounts) that returns a tuple (total, average, max). 
Return (0, 0, None) for an empty list.'''
amounts = [0, 1, 2, 3, 4, 5]

def summarize(amounts):
    # get the total
    total = 0
    
    for i in amounts:
        total = total + i
    
    avg = sum(amounts)/len(amounts)
    
    maxx = max(amounts)
    
    breakpoint()
    tup = (total, avg, maxx)
    return tup
    

summarize(amounts)

'''
Dictionaries: Given a list of words, return a dict of word counts, case-insensitive. 
["Cat", "cat", "dog"] should give {"cat": 2, "dog": 1}.'''

list = ["cat", "cAt", "dog"]
dicty = {}

for i in list:
    # check case sensitivity, make all lowercase
    good_case = i.lower()
    
    if good_case in dicty:
        dicty[good_case] = dicty[good_case] + 1
    else:
        dicty[good_case] = 1
        
print(dicty)
        
    # check if it exists in dict
    # if it does, find the key and update, add number of
    
'''Tuples and unpacking: Given [("A", 10), ("B", 25), ("C", 7)], 
return the name of the item with the highest value without using max() with a key.'''

given = [("A", 10), ("B", 25), ("C", 7)]

highest_num = 0

for i in given: # for each tuple within the list 
    the_num = i[1]
    if the_num > highest_num:
        highest_num = i[1]
        current_ans = i[0]
        
        
        
        
print(current_ans)



        
'''
List filtering: Write flag_outliers(values, threshold) that returns the indices of values more than 
threshold above the mean.'''

values = [0, 1, 2, 3, 4, 5]
threshold = 1

def flag_outliers(values, threshold):
    index = 0
    indices = []
    avg = sum(values)/len(values)
    for i in values:
        if i > avg:
            indices.append(index)
            # APPEND INDICES
        
        index += 1
    return indices 

flag_outliers(values, threshold)
        

'''
Dictionary grouping: Given a list of (customer_id, amount) tuples, return a dict mapping each 
customer to their total. Then return the customer with the highest total.
'''

listy = [('111', 25), ('112', 50), ('113', 70)]

dicty = {}


for customer_id, amount in listy:
    dicty[customer_id] = amount
    

flags = [0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1]

def longest_streak(flags):
    len_true = 0
    comp_true = 0
    max_true = 0
    for flag in flags:
        if flag == True:
            len_true += 1
            comp_true = len_true
        else:
            len_true = 0 
            
        if comp_true > max_true:
            max_true = comp_true

    return max_true

longest_streak(flags)



longest_streak(flags)
    
        
        