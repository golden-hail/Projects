'''Gemini practive problems'''

def rolling_average(data: list[float], window_size: int) -> list[float]:

    if window_size > len(data) | window_size < 1:
        pass
    else:
        pass
    
    avgs = []
    
    # window size == 3
    for elem in data:
        avgs.append(elem/window_size)
        
    for i in range(len(data) - window_size): # why + 1?
        window = data[i : i + window_size]
        window_average = sum(window) / window_size
        avgs.append(window_average)
    
    return avgs


data = [10.0, 20.0, 30.0, 40.0, 50.0]
window_size = 3
rolling_average(data, window_size)

# Output: [20.0, 30.0, 40.0]
# Explanation: [(10+20+30)/3, (20+30+40)/3, (30+40+50)/3]\\\
    
# Problem 2: having issues referencing output 
def aggregate_transactions(records: list[tuple[str, str, float]]) -> dict[str, dict[str, float]]:
    summary = {}
    for category, subcategory, amount in records:
        if category not in summary:
            summary[category] = {}
        summary[category][subcategory] = summary[category].get(subcategory, 0.0) + amount
    return summary

records = [
    ("Electronics", "Phones", 500.0),
    ("Electronics", "Accessories", 50.0),
    ("Electronics", "Phones", 300.0),
    ("Clothing", "Shirts", 40.0),
    ("Clothing", "Shirts", 25.0)
]

aggregate_transactions(records)


# Expected Output:
# {
#     "Electronics": {
#         "Phones": 800.0,
#         "Accessories": 50.0
#     },
#     "Clothing": {
#         "Shirts": 65.0
#     }
# }
