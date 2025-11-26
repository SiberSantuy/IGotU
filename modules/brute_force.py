import requests
from urllib.parse import urljoin
from requests.exceptions import RequestException


import requests
from urllib.parse import urljoin
from requests.exceptions import RequestException
import concurrent.futures

def scan_directories(target_url, wordlist_path):
    """
    Directory Brute-Forcing dengan multi-threading, hasil valid, forbidden, redirect, error handling optimal.
    """
    print(f"\n[*] Starting directory scan on: {target_url}")
    print(f"[*] Using wordlist: {wordlist_path}")
    print("-" * 60)
    found = []
    forbidden = []
    redirect = []
    notfound = 0
    try:
        with open(wordlist_path, 'r') as wordlist_file:
            paths = [p.strip() for p in wordlist_file if p.strip()]
    except Exception as e:
        print(f"[-] Error reading wordlist: {str(e)}\n")
        return

    def check_path(path):
        url = urljoin(target_url, path)
        try:
            resp = requests.head(url, timeout=5, allow_redirects=True, headers={"User-Agent": "IGotU-Scanner/1.0"})
            code = resp.status_code
            if code in [200, 201]:
                return ("FOUND", url, code)
            elif code in [301, 302, 307, 308]:
                return ("REDIRECT", url, code)
            elif code == 403:
                return ("FORBIDDEN", url, code)
            else:
                return ("NOTFOUND", url, code)
        except Exception:
            return ("ERROR", url, None)

    import threading
    lock = threading.Lock()
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        results = list(executor.map(check_path, paths))
    for status, url, code in results:
        if status == "FOUND":
            print(f"[FOUND]     {url}  (Status: {code})")
            found.append(url)
        elif status == "FORBIDDEN":
            print(f"[FORBIDDEN] {url}  (Status: {code})")
            forbidden.append(url)
        elif status == "REDIRECT":
            print(f"[REDIRECT]  {url}  (Status: {code})")
            redirect.append(url)
        elif status == "NOTFOUND":
            notfound += 1
    print("-" * 60)
    print(f"[+] Directory scan completed!")
    print(f"[+] Found: {len(found)} | Forbidden: {len(forbidden)} | Redirect: {len(redirect)} | Not Found: {notfound}\n")
