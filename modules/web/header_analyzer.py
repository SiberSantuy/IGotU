import requests

def analyze_http_headers(target_url):
    """
    Analisis header HTTP untuk keamanan, tampilkan rekomendasi.
    """
    import requests
    print(f"\n[*] HTTP Header Security Analyzer for: {target_url}")
    try:
        r = requests.get(target_url, timeout=7)
        headers = r.headers
        checks = {
            'Strict-Transport-Security': 'HSTS (Strict-Transport-Security)',
            'Content-Security-Policy': 'CSP (Content-Security-Policy)',
            'X-Frame-Options': 'Clickjacking Protection (X-Frame-Options)',
            'X-XSS-Protection': 'XSS Protection (X-XSS-Protection)',
            'X-Content-Type-Options': 'MIME Sniffing Protection (X-Content-Type-Options)',
            'Referrer-Policy': 'Referrer Policy',
            'Permissions-Policy': 'Permissions Policy',
        }
        for h, desc in checks.items():
            if h in headers:
                print(f"[+] {desc}: {headers[h]}")
            else:
                print(f"[!] {desc} header missing!")
    except Exception as e:
        print(f"[-] Error: {str(e)}")
