import socket
import concurrent.futures

def scan_ports(target_host, ports=None):
    """
    TCP port scan multi-threaded, banner grab jika memungkinkan.
    """
    print(f"\n[*] Port Scanning: {target_host}")
    if not ports:
        ports = list(range(1, 1025))  # default: 1-1024
    elif isinstance(ports, str):
        ports = [int(p) for p in ports.split(',') if p.isdigit()]
    open_ports = []
    banners = {}
    def scan(port):
        try:
            s = socket.socket()
            s.settimeout(1)
            s.connect((target_host, port))
            try:
                s.send(b'\r\n')
                banner = s.recv(1024).decode(errors='ignore').strip()
            except Exception:
                banner = ''
            s.close()
            return (port, banner)
        except Exception:
            return None
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        results = executor.map(scan, ports)
    for res in results:
        if res:
            port, banner = res
            open_ports.append(port)
            banners[port] = banner
    for port in open_ports:
        print(f"[OPEN] Port {port}/tcp", end='')
        if banners[port]:
            print(f" | Banner: {banners[port]}")
        else:
            print()
    print(f"\n[+] Total open ports: {len(open_ports)}\n")
