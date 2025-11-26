def test_xss(target_url):
    """
    Uji XSS otomatis: reflected XSS pada parameter GET.
    """
    import requests
    print(f"\n[*] XSS Test for: {target_url}")
    payloads = [
        '<script>alert(1)</script>',
        '"<svg/onload=alert(1)>',
        "'><img src=x onerror=alert(1)>"
    ]
    vulnerable = False
    for p in payloads:
        try:
            r = requests.get(target_url, params={'q': p}, timeout=7)
            if p in r.text:
                print(f"[!] Reflected XSS detected with payload: {p}")
                vulnerable = True
        except Exception:
            continue
    if not vulnerable:
        print("[-] No reflected XSS detected.")
