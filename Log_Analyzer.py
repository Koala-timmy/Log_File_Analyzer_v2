file_path = "login_log.txt"

logins_failed = {}
logins_passed = {}

def read_logs(file_path): # Read file data
    try:
        with open(file_path, "r") as file:
            log_data = file.readlines()
            
            return log_data
    except FileNotFoundError:
        print(f"ERROR: File not found in path {file_path}")

logs = read_logs(file_path)

def analyze_logs(logs, logins_failed, logins_passed): # Process read data
    for raw_log in logs:
        split_log = raw_log.split()

        if split_log[1] == "FAILED": # Failed line: Increment failures by 1
            failed_user = split_log[3]
            
            if failed_user not in logins_failed:
                logins_failed[failed_user] = 1

            else:
                logins_failed[failed_user] += 1
        
        elif split_log[1] == "SUCCESS": # Passed line: Increment successes by 1
            passed_user = split_log.split_log[3]
            
            if passed_user not in logins_passed:
                logins_passed[passed_user] = 1

            else:
                logins_passed[passed_user] += 1

    print(f"LOGINS FAILED: {logins_failed}")   
    print(f"LOGINS PASSED: {logins_passed}")


analyze_logs(logs, logins_failed, logins_passed)

