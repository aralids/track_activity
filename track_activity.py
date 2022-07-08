from datetime import datetime

def track_activity(sum_dict, log_dict):
    activity = input("Activity of the Last 10 Minutes: ")
    if not (activity in list(sum_dict.keys())):
        sum_dict[activity] = 10
        log_dict[datetime.now().strftime("%d/%m/%Y, %H:%M:%S")] = activity
    else:
        sum_dict[activity] += 10
        log_dict[datetime.now().strftime("%d/%m/%Y, %H:%M:%S")] = activity
    return sum_dict, log_dict

if __name__ == "__main__":
    sum_dict = {}
    log_dict = {}
    while 1:
        sum_dict, log_dict = track_activity(sum_dict, log_dict)
        print("\n------------------------------------")
        for key, value in sum_dict.items():
            print(key, ' : ', value)
        print("------------------------------------\n")
        for key, value in log_dict.items():
            print(key, ' : ', value)
