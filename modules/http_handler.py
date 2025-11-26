import requests
from requests.exceptions import RequestException


def fetch_headers(target_url):
    """
    Melakukan Banner Grabbing dengan mengambil headers dari target URL.
    Menampilkan status code, header penting, dan deteksi server info.
    """
    try:
        print(f"\n[*] Fetching headers from: {target_url}")
        response = requests.get(target_url, timeout=7, allow_redirects=True, headers={"User-Agent": "IGotU-Scanner/1.0"})
        print(f"[+] Status Code: {response.status_code}")
        print(f"[+] Final URL: {response.url}")
        print()
        important_headers = ['Server', 'X-Powered-By', 'Content-Type', 'Set-Cookie', 'Strict-Transport-Security', 'X-Frame-Options', 'X-XSS-Protection', 'X-Content-Type-Options', 'Content-Security-Policy']
        for header in important_headers:
            value = response.headers.get(header, None)
            if value:
                print(f"[+] {header}: {value}")
        print("\n[+] All Headers:")
        for k, v in response.headers.items():
            print(f"    {k}: {v}")
        print("-" * 60)
        # Deteksi server info
        server = response.headers.get('Server', '')
        powered = response.headers.get('X-Powered-By', '')
        if server or powered:
            print(f"[!] Server Info: {server} {powered}")
        else:
            print("[!] Server Info: Not disclosed")
        print("[+] Banner Grab completed successfully!\n")
    except RequestException as e:
        print(f"[-] Error connecting to {target_url}: {str(e)}\n")
    except Exception as e:
        print(f"[-] An unexpected error occurred: {str(e)}\n")
