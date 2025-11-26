def find_admin_pages(target_url, wordlist_path=None):
    """
    Cari halaman admin menggunakan wordlist, tampilkan yang valid dan statusnya.
    """
    import requests
    from urllib.parse import urljoin
    print(f"\n[*] Admin Page Finder for: {target_url}")
    if not wordlist_path:
        print("[-] Wordlist path required!")
        return
    try:
        with open(wordlist_path, 'r') as f:
            paths = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"[-] Error reading wordlist: {str(e)}")
        return
    for path in paths:
        url = urljoin(target_url, path)
        try:
            r = requests.get(url, timeout=7)
            if r.status_code in [200, 301, 302]:
                print(f"[FOUND] {url} (Status: {r.status_code})")
        except Exception:
            continue
