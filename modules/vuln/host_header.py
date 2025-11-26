def test_host_header_injection(target_url):
    """
    Uji Host Header Injection, deteksi response abnormal atau kerentanan.
    """
    import requests
    from urllib.parse import urlparse
    print(f"\n[*] Host Header Injection Test for: {target_url}")
    try:
        parsed = urlparse(target_url)
        host = parsed.netloc
        evil = 'evil.com'
        r1 = requests.get(target_url, headers={'Host': host}, timeout=7)
        r2 = requests.get(target_url, headers={'Host': evil}, timeout=7)
        if r1.text != r2.text or r2.status_code != r1.status_code:
            print(f"[!] Possible Host Header Injection! Response differs when Host is {evil}.")
        else:
            print("[-] No Host Header Injection detected.")
    except Exception as e:
        print(f"[-] Error: {str(e)}")
