from statistics import mode

logs = []
valid_logs = []
skipped_logs = []
error_count = 0
warning_count = 0
info_count = 0
error_messages = []
IPS = []

def get_logs(logs_list): #get logs from sample.log
    with open("sample.log", "r", encoding="utf-8") as file: 
        for line in file:
            log = []
            fields = line.strip().split("|")
            fields = [field.strip() for field in fields]
            log.extend(fields)
            logs_list.append(log)

    return logs_list

def verify_logs(logs_list, valid_logs_list, skipped_logs_list): # Remove any invalid logs
    for log in logs_list:
        if len(log) != 4 or log[1] not in ["INFO", "WARNING", "ERROR"] or log[0] == "" or log[2] == "" or log[3] == "":
            skipped_logs_list.append(log)
        else:
            valid_logs_list.append(log)

    return valid_logs_list, skipped_logs_list

def count_logs(error, warning, info, logs_list):# Count the number of errors, warnings, and info messages
    for log in logs_list:
        if log[1] == "ERROR":
            error += 1
        elif log[1] == "WARNING":
            warning += 1
        elif log[1] == "INFO":
            info += 1

    return error, warning, info

def get_most_frequent_error(logs_list, error_messages_list): # Print most frequent error message
    for log in logs_list:
        if log[1] == "ERROR":
            message = log[3]
            error_messages_list.append(message)

    if len(error_messages_list) == 0:
        return "No error messages found"

    return mode(error_messages_list)

def get_most_frequent_ip(logs_list, IPS_list): # Print most frequent IP address
    for log in logs_list:
        IPS_list.append(log[2])

    if len(IPS_list) == 0:
        return "No IP addresses found"
    return mode(IPS_list)

# DEFINE ALL VARIABLES
logs, skipped_logs = verify_logs(get_logs(logs), valid_logs, skipped_logs)
error_count, warning_count, info_count = count_logs(error_count, warning_count, info_count, logs)
most_frequent_error = get_most_frequent_error(logs, error_messages)
most_frequent_ip = get_most_frequent_ip(logs, IPS)

# PRINT RESULTS
print(f"Total logs: {len(logs)}")
print(f"Error count: {error_count}")
print(f"Warning count: {warning_count}")
print(f"Info count: {info_count}")
print(f"Skipped logs: {len(skipped_logs)}")
print(f"Most frequent error message: {most_frequent_error} (Count: {error_messages.count(most_frequent_error)})")
print(f"Most frequent IP address: {most_frequent_ip}")