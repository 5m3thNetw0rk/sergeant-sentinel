import requests
import sys

# Sergeant-Sentinel: Automated Web Security Scanner
# Focus: SQLi, RCE, and XSS detection

def check_sqli(url):
    payload = "'"
    print(f"[*] Testing for SQLi: {url}")
    try:
        r = requests.get(url + payload)
        if "SQL syntax" in r.text or "mysql_fetch" in r.text:
            print("[!] Potential SQL Injection found!")
        else:
            print("[+] SQLi: No immediate error detected.")
    except Exception as e:
        print(f"[-] Error: {e}")

def check_rce(url):
    payload = "; ls -la"
    print(f"[*] Testing for RCE: {url}")
    try:
        r = requests.get(url + "?cmd=" + payload)
        if "total" in r.text or "bin" in r.text:
            print("[!] Potential Remote Code Execution found!")
        else:
            print("[+] RCE: No immediate shell output detected.")
    except Exception as e:
        print(f"[-] Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 sentinel_scanner.py <target_url>")
    else:
        target = sys.argv[1]
        check_sqli(target)
        check_rce(target)
