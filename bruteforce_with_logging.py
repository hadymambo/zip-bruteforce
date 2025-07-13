from zipfile import ZipFile
import time
from datetime import datetime

# Function to try extracting with a given password
def attempt_extract(zf_handle, password):
    try:
        zf_handle.extractall(pwd=password)
        return True
    except:
        return False

def main():
    print("[+] Starting brute-force attack...")
    start_time = time.time()
    attempts = 0
    found_password = None
    log_file = "attempt_log.txt"
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Clear the log file before starting
    with open(log_file, 'w') as lf:
        lf.write(f"[{timestamp}] Brute-force attempt started\n\n")

    with ZipFile('enc.zip') as zf:
        with open('rockyou.txt', 'rb') as f:
            for line in f:
                password = line.strip()
                attempts += 1

                # Log each password attempt
                with open(log_file, 'a') as lf:
                    lf.write(f"Attempt #{attempts}: {password.decode('utf-8')}\n")

                if attempt_extract(zf, password):
                    found_password = password.decode('utf-8')
                    break

    end_time = time.time()
    duration = round(end_time - start_time, 2)

    # Final report
    print("\n========== Brute-force Summary ==========")
    print(f"Start Time       : {timestamp}")
    print(f"Total Attempts   : {attempts}")
    print(f"Duration         : {duration} seconds")
    if found_password:
        print(f"[✅] Password Found: {found_password}")
        print(f"Files successfully extracted.")
    else:
        print("[❌] Password not found in wordlist.")
    print(f"Log File Saved   : {log_file}")
    print("=========================================\n")

if __name__ == "__main__":
    main()
