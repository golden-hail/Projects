# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 15:38:07 2026

@author: aiaqu
"""

raw_logs = [
    {"username": "Alice", "status": "SUCCESS", "duration": 120, "feature": "export"},
    {"username": "BOB", "status": "FAILED", "duration": 45, "feature": "login"},
    {"username": "alice", "status": "SUCCESS", "duration": 80, "feature": "dashboard"},
    {"username": "Charlie", "status": "SUCCESS", "duration": 200, "feature": "export"},
    {"username": "ALICE", "status": "SUCCESS", "duration": 150, "feature": "export"},
]

def process_logs(logs):
    output_log = {}
    for log in raw_logs:
        # check if log is valid ("SUCCESS" status)
        if log["status"].upper() != "SUCCESS":
            continue ### go to the next log
        
        # check username if in output as record
        uname = log["username"]
        # breakpoint()
        if uname.lower() in output_log:
            # we're going to update counts from the existing record
            output_log[uname.lower()]['request_count'] += 1
            output_log[uname.lower()]['total_duration'] += log["duration"]
            if log["feature"] in output_log[uname.lower()]['features_accessed']:
                pass
            else:
                # add the feature to the list in the output
                output_log[uname.lower()]['features_accessed'].append(log["feature"])
                
            if len(output_log[uname.lower()]['features_accessed']) > 1:
                # sort alphabetically
                output_log[uname.lower()]['features_accessed'].sort()
        else:
            output_log[uname.lower()] = {"request_count" : 1,
                                         "total_duration": log["duration"],
                                         "features_accessed" : [log["feature"]]}
            
    return output_log

process_logs(raw_logs)
# Expected output format:
# {
#     "alice": {"request_count": 3, "total_duration": 350, "features_accessed": ["dashboard", "export"]},
#     "charlie": {"request_count": 1, "total_duration": 200, "features_accessed": ["export"]}
# }