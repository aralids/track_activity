from datetime import datetime

def track_activity(log_dict):
    activity = input("Activity of the Last 10 Minutes: ")
    if not (activity in list(log_dict.keys())):
        log_dict[activity] = 10
    else:
        log_dict[activity] += 10
    return log_dict

if __name__ == "__main__":
    log_dict = {}
    while 1:
        log_dict = track_activity(log_dict)
        print("\n------------------------------------")
        for key, value in log_dict.items():
            print(key, ' : ', value)
        print("------------------------------------\n")
