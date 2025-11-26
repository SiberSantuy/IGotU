import requests

def fetch_robots_txt(target_url):
    """
    Mengambil robots.txt dari target, parsing dan tampilkan disallow/allow path.
    """
    import requests
    from urllib.parse import urljoin
    print(f"\n[*] Fetching robots.txt for: {target_url}")
    url = urljoin(target_url, '/robots.txt')
    try:
        r = requests.get(url, timeout=7)
        if r.status_code == 200:
            print("[+] robots.txt content:")
            for line in r.text.splitlines():
                if line.strip().lower().startswith('disallow') or line.strip().lower().startswith('allow'):
                    print(f"    {line.strip()}")
        else:
            print(f"[-] robots.txt not found (Status: {r.status_code})")
    except Exception as e:
        print(f"[-] Error: {str(e)}")
