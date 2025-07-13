from zipfile import ZipFile

# Function to try extracting with a given password
def attempt_extract(zf_handle, password):
    try:
        zf_handle.extractall(pwd=password)
        return True
    except:
        return False

def main():
    print("[+] Beginning bruteforce...")
    
    with ZipFile('enc.zip') as zf:
        with open('rockyou.txt', 'rb') as f:
            for line in f:
                password = line.strip()
                if attempt_extract(zf, password):
                    print(f"[+] Password found: {password.decode('utf-8')}")
                    return
                else:
                    print(f"[-] Attempt failed: {password.decode('utf-8')}")

    print("[!] Password not found in list.")

if __name__ == "__main__":
    main()