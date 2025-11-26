import socket
import requests
from urllib.parse import urlparse

def enumerate_subdomains(target_url, wordlist_path=None):
    """
    Enumerasi subdomain menggunakan wordlist dan DNS query.
    """
    print(f"\n[*] Subdomain Enumeration for: {target_url}")
    if not wordlist_path:
        print("[-] Wordlist path required!")
        return
    try:
        with open(wordlist_path, 'r') as f:
            subdomains = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"[-] Error reading wordlist: {str(e)}")
        return
    parsed = urlparse(target_url)
    # Ambil domain tanpa port dan www jika ada
    domain = parsed.netloc or parsed.path
    if not domain:
        print("[-] Invalid target URL!")
        return
    domain = domain.split(':')[0]
    if domain.startswith('www.'):
        domain = domain[4:]
    if not domain or '.' not in domain:
        print(f"[-] Invalid domain parsed: {domain}")
        return
    found = []
    for sub in subdomains:
        sub = sub.strip()
        if not sub:
            continue
        subdomain = f"{sub}.{domain}"
        try:
            socket.gethostbyname(subdomain)
            print(f"[FOUND] {subdomain}")
            found.append(subdomain)
        except socket.gaierror:
            pass
        except Exception as e:
            print(f"[!] Error resolving {subdomain}: {e}")
    print(f"\n[+] Total valid subdomains: {len(found)}\n")
