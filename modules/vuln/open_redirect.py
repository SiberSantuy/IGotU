def test_open_redirect(target_url):
    """
    Uji open redirect otomatis dengan payload redirect eksternal.
    """
    import requests
    from urllib.parse import urlparse, urlencode
    print(f"\n[*] Open Redirect Test for: {target_url}")
    payloads = [
        'https://evil.com',
        '//evil.com',
        '/\\evil.com',
        '///evil.com',
        'http://evil.com',
    ]
    params = ['url', 'redirect', 'next', 'target', 'dest', 'destination', 'redir', 'continue', 'return', 'returnTo']
    vulnerable = False
    for param in params:
        for payload in payloads:
            try:
                url = f"{target_url}?{urlencode({param: payload})}"
                r = requests.get(url, allow_redirects=False, timeout=7)
                if r.is_redirect or r.status_code in [301, 302, 303, 307, 308]:
                    loc = r.headers.get('Location', '')
                    if 'evil.com' in loc:
                        print(f"[!] Open Redirect detected: {url} -> {loc}")
                        vulnerable = True
            except Exception:
                continue
    if not vulnerable:
        print("[-] No open redirect detected.")
