import socket
from urllib.parse import urlparse

def get_ip_from_url(target_url):
    """
    Mendapatkan IP address dari target URL.
    """
    print(f"\n[*] Resolving IP for: {target_url}")
    try:
        parsed = urlparse(target_url)
        domain = parsed.netloc or parsed.path
        if not domain:
            print("[-] Invalid URL!")
            return
        domain = domain.split(':')[0]
        if domain.startswith('www.'):
            domain = domain[4:]

        # IPv4 addresses (A records)

        try:
            ipv4s = [str(ai[4][0]) for ai in socket.getaddrinfo(domain, None, socket.AF_INET)]
            ipv4s = list(set(ipv4s))
        except Exception:
            ipv4s = []
        try:
            ipv6s = [str(ai[4][0]) for ai in socket.getaddrinfo(domain, None, socket.AF_INET6)]
            ipv6s = list(set(ipv6s))
        except Exception:
            ipv6s = []


        if ipv4s:
            print(f"[+] Server IP Address (A record utama): {ipv4s[0]}")
        else:
            print(f"[+] Server IP Address (A record utama): -")
        print(f"[+] IPv4 addresses (A): {', '.join(ipv4s) if ipv4s else '-'}")
        print(f"[+] IPv6 addresses (AAAA): {', '.join(ipv6s) if ipv6s else '-'}")

        # All resolved IPs (A, AAAA, CNAME, etc)
        try:
            all_info = socket.gethostbyname_ex(domain)
            print(f"[+] All resolved IPs: {', '.join(all_info[2]) if all_info[2] else '-'}")
            print(f"[+] Canonical name: {all_info[0]}")
        except Exception:
            pass

        # Server info via reverse DNS (PTR)
        try:
            for ip in ipv4s:
                try:
                    host, _, _ = socket.gethostbyaddr(str(ip))
                    print(f"[+] PTR (reverse DNS) for {ip}: {host}")
                except Exception:
                    pass
            for ip in ipv6s:
                try:
                    host, _, _ = socket.gethostbyaddr(str(ip))
                    print(f"[+] PTR (reverse DNS) for {ip}: {host}")
                except Exception:
                    pass
        except Exception:
            pass
    except Exception as e:
        print(f"[-] Error resolving IP: {e}")
