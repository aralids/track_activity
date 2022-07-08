import time
import schedule
from datetime import datetime

def track_activity(sum_dict, log_dict):
    activity = input("Activity of the Last 10 Minutes: ")
    current_time = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    if not (activity in list(sum_dict.keys())):
        sum_dict[activity] = 10
        log_dict[current_time] = activity
    else:
        sum_dict[activity] += 10
        log_dict[current_time] = activity
    record_activity(current_time, activity)
    return sum_dict, log_dict

def record_activity(current_time, activity):
    log_file = open("log.txt", "a")
    log_file.write(current_time + " : " + activity + "\n")
    log_file.close()

def summarize(sum_dict):
    lines = ["\n"]
    for key, value in sum_dict.items():
        value = str(value)
        lines.append(key + " : " + value + "\n")
    lines.append("------------------------------------\n\n")
    with open("log.txt", "a") as log_file:
        log_file.writelines(lines)

if __name__ == "__main__":
    sum_dict = {}
    log_dict = {}
    schedule.every().day.at("11:43").do(summarize, sum_dict)
    while 1:
        schedule.run_pending()
        sum_dict, log_dict = track_activity(sum_dict, log_dict)
        print("\n------------------------------------")
        for key, value in sum_dict.items():
            print(key, ' : ', value)
        print("------------------------------------\n")
