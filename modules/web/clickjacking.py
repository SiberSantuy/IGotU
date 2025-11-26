import requests

def test_clickjacking(target_url):
    """
    Uji clickjacking pada target, cek header X-Frame-Options dan CSP.
    """
    import requests
    print(f"\n[*] Clickjacking Test for: {target_url}")
    try:
        r = requests.get(target_url, timeout=7)
        xfo = r.headers.get('X-Frame-Options', '')
        csp = r.headers.get('Content-Security-Policy', '')
        if xfo:
            print(f"[+] X-Frame-Options: {xfo}")
        else:
            print("[!] X-Frame-Options header missing! (Vulnerable)")
        if 'frame-ancestors' in csp:
            print(f"[+] CSP frame-ancestors: {csp}")
        else:
            print("[!] CSP frame-ancestors missing or not set!")
    except Exception as e:
        print(f"[-] Error: {str(e)}")
