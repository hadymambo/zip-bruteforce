# 🔐 ZIP Password Brute-Force Tool (AIG Shields Up Project)

This repository contains a Python script used to ethically brute-force the password of an encrypted ZIP archive as part of a cybersecurity incident response exercise.

> 💼 **Completed as part of the AIG Shields Up: Cybersecurity Virtual Experience Program on Forage – July 2025**

---

## 📌 Project Overview

This project simulates a real-world incident where a ransomware attack encrypts a ZIP file using a password. Instead of paying the ransom, a brute-force approach was used to recover the password and decrypt the file — demonstrating the importance of incident response, ethical hacking, and forensic logging.

---

## 🛠️ Features

- Brute-forces password-protected `.zip` files using Python.
- Uses a common wordlist (`rockyou.txt`) for password attempts.
- Logs every password attempt to `attempt_log.txt`.
- Generates a summary report after each run.
- Successfully avoids ransom payment through ethical recovery methods.

---

## 📂 Files Included

- `bruteforce_with_logging.py` – The main brute-force script.
- `attempt_log.txt` – Log of all password attempts (optional).
- `Incident_Report.pdf` – A professional summary of the incident and response.
- `README.md` – Project description and usage.

---

## 🚀 How to Use

### Prerequisites:
- Python 3.6 or higher installed
- `enc.zip` – The encrypted ZIP file
- `rockyou.txt` – A wordlist of possible passwords

### Run the script:

```bash
python bruteforce_with_logging.py
