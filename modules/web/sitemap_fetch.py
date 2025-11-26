import requests

def fetch_sitemap_xml(target_url):
    """
    Mengambil sitemap.xml dari target, parsing dan tampilkan URL penting.
    """
    import requests
    from urllib.parse import urljoin
    import re
    print(f"\n[*] Fetching sitemap.xml for: {target_url}")
    url = urljoin(target_url, '/sitemap.xml')
    try:
        r = requests.get(url, timeout=7)
        if r.status_code == 200:
            urls = re.findall(r'<loc>(.*?)</loc>', r.text)
            print(f"[+] Found {len(urls)} URLs in sitemap.xml:")
            for u in urls:
                print(f"    {u}")
        else:
            print(f"[-] sitemap.xml not found (Status: {r.status_code})")
    except Exception as e:
        print(f"[-] Error: {str(e)}")
