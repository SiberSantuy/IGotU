import requests

def discover_http_methods(target_url):
    """
    Menemukan HTTP methods yang diizinkan pada target.
    """
    print(f"\n[*] HTTP Method Discovery for: {target_url}")
    try:
        resp = requests.options(target_url, timeout=7)
        allow = resp.headers.get('Allow', '')
        if allow:
            print(f"[+] Allow header: {allow}")
        else:
            print("[!] No Allow header, testing common methods...")
            methods = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'HEAD', 'TRACE', 'PATCH', 'CONNECT']
            for m in methods:
                r = requests.request(m, target_url, timeout=5)
                if r.status_code < 400:
                    print(f"[+] {m} allowed (Status: {r.status_code})")
    except Exception as e:
        print(f"[-] Error: {str(e)}")
