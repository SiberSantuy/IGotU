import requests

def check_cookie_security(target_url):
    """
    Cek keamanan cookie pada target, cek flag Secure, HttpOnly, SameSite.
    """
    import requests
    print(f"\n[*] Cookie Security Checker for: {target_url}")
    try:
        r = requests.get(target_url, timeout=7)
        cookies = r.cookies
        set_cookie = r.headers.get('Set-Cookie', '')
        if not set_cookie:
            print("[-] No Set-Cookie header found.")
            return
        for c in set_cookie.split(','):
            c = c.strip()
            print(f"[Cookie] {c}")
            if 'secure' not in c.lower():
                print("  [!] Missing Secure flag!")
            if 'httponly' not in c.lower():
                print("  [!] Missing HttpOnly flag!")
            if 'samesite' not in c.lower():
                print("  [!] Missing SameSite flag!")
    except Exception as e:
        print(f"[-] Error: {str(e)}")
