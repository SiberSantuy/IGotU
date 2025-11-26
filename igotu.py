import sys
from modules.network.ip_resolver import get_ip_from_url
import time
import threading
import itertools

from modules.http_handler import fetch_headers
from modules.brute_force import scan_directories
from modules.discovery.subdomain_enum import enumerate_subdomains
from modules.network.port_scan import scan_ports
from modules.web.http_methods import discover_http_methods
from modules.web.cms_detect import detect_cms
from modules.vuln.sql_injection import test_sql_injection
from modules.vuln.xss_test import test_xss
from modules.discovery.admin_finder import find_admin_pages
from modules.web.robots_fetch import fetch_robots_txt
from modules.web.sitemap_fetch import fetch_sitemap_xml
from modules.web.cors_check import check_cors
from modules.vuln.open_redirect import test_open_redirect
from modules.web.clickjacking import test_clickjacking
from modules.discovery.sensitive_file import find_sensitive_files
from modules.web.ua_spoof import test_user_agent_spoofing
from modules.web.cookie_check import check_cookie_security
from modules.web.header_analyzer import analyze_http_headers
from modules.vuln.host_header import test_host_header_injection



def spinner(text, duration=2):
    done = False
    def animate():
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if done:
                break
            print(f'\r{text} {c}', end='', flush=True)
            time.sleep(0.1)
        print('\r' + ' ' * (len(text) + 2) + '\r', end='', flush=True)
    t = threading.Thread(target=animate)
    t.start()
    time.sleep(duration)
    done = True
    t.join()

def loading_bar():
    for i in range(1, 101):
        print(f'\rLoading... {i}%', end='', flush=True)
        time.sleep(0.02)
    print('\rLogin success!         ')

def login():
    print("\nWelcome to IGotU Security Scanner!")
    for _ in range(3):
        pwd = input("Enter password to continue: ")
        if pwd == "whattheheck":
            loading_bar()
            return True
        else:
            print("Incorrect password! Try again.")
    print("Too many failed attempts. Exiting.")
    sys.exit(1)

def main():
    # Login terlebih dahulu
    login()

    # Menu interaktif loop
    while True:
        # ASCII art warna (coklat terang dan kuning)
        ascii_art = (
            "\033[38;5;220m"  # kuning terang
                " █████      █████████            █████       █████  █████   \n"
                "▒▒███      ███▒▒▒▒▒███          ▒▒███       ▒▒███  ▒▒███    \n"
                " ▒███     ███     ▒▒▒   ██████  ███████      ▒███   ▒███   \n"
                " ▒███    ▒███          ███▒▒███▒▒▒███▒       ▒███   ▒███   \n"
                " ▒███    ▒███    █████▒███ ▒███  ▒███        ▒███   ▒███   \n"
                " ▒███    ▒▒███  ▒▒███ ▒███ ▒███  ▒███ ███    ▒███   ▒███   \n"
                " █████    ▒▒█████████ ▒▒██████   ▒▒█████     ▒▒████████  \n"
                "▒▒▒▒▒      ▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒     ▒▒▒▒▒       ▒▒▒▒▒▒▒▒   \n"
            "\033[0m"                                      
            "\033[38;5;136m"  # coklat terang
            "   IGotU - Web Security Scanner CLI v1.0\n"
            "\033[0m"
            "\033[38;5;136m"  # coklat terang
            "   Author: Peju3ncer\n"
            "\033[0m"
        )
        print("\n" + "=" * 60)
        print(ascii_art)
        print("╔════════════════════════════════════════════════════════╗")
        print("║  1: IP Resolver                                        ║")
        print("║  2: Banner Grab                                        ║")
        print("║  3: Directory Scan                                     ║")
        print("║  4: Subdomain Enumeration                              ║")
        print("║  5: Port Scanning                                      ║")
        print("║  6: HTTP Method Discovery                              ║")
        print("║  7: CMS Detection                                      ║")
        print("║  8: SQL Injection Testing                              ║")
        print("║  9: XSS Testing                                        ║")
        print("║ 10: Admin Page Finder                                  ║")
        print("║ 11: Robots.txt Fetcher                                 ║")
        print("║ 12: Sitemap.xml Fetcher                                ║")
        print("║ 13: CORS Misconfiguration Checker                      ║")
        print("║ 14: Open Redirect Tester                               ║")
        print("║ 15: Clickjacking Tester                                ║")
        print("║ 16: Sensitive File Finder                              ║")
        print("║ 17: User-Agent Spoofing Tester                         ║")
        print("║ 18: Cookie Security Checker                            ║")
        print("║ 19: HTTP Header Security Analyzer                      ║")
        print("║ 20: Host Header Injection Tester                       ║")
        print("║  q: Quit                                               ║")
        print("╚════════════════════════════════════════════════════════╝")
        print("=" * 60)

        choice = input("\n[?] Select an option (1-20/q): ").strip().lower()

        if choice == '1':
            url = input("Target URL: ").strip()
            spinner("Resolving IP...")
            get_ip_from_url(url)
        elif choice == '2':
            url = input("Target URL: ").strip()
            spinner("Fetching headers...")
            fetch_headers(url)
        elif choice == '3':
            url = input("Target URL: ").strip()
            wordlist = input("Wordlist path [wordlist.txt]: ").strip() or 'wordlist.txt'
            spinner("Scanning directories...")
            scan_directories(url, wordlist)
        elif choice == '4':
            url = input("Target URL: ").strip()
            wordlist = input("Wordlist path [wordlist.txt]: ").strip() or 'wordlist.txt'
            spinner("Enumerating subdomains...")
            enumerate_subdomains(url, wordlist)
        elif choice == '5':
            host = input("Target Host (domain/IP): ").strip()
            spinner("Scanning ports...")
            scan_ports(host)
        elif choice == '6':
            url = input("Target URL: ").strip()
            spinner("Discovering HTTP methods...")
            discover_http_methods(url)
        elif choice == '7':
            url = input("Target URL: ").strip()
            spinner("Detecting CMS...")
            detect_cms(url)
        elif choice == '8':
            url = input("Target URL: ").strip()
            spinner("Testing SQL Injection...")
            test_sql_injection(url)
        elif choice == '9':
            url = input("Target URL: ").strip()
            spinner("Testing XSS...")
            test_xss(url)
        elif choice == '10':
            url = input("Target URL: ").strip()
            wordlist = input("Wordlist path [wordlist.txt]: ").strip() or 'wordlist.txt'
            spinner("Finding admin pages...")
            find_admin_pages(url, wordlist)
        elif choice == '11':
            url = input("Target URL: ").strip()
            spinner("Fetching robots.txt...")
            fetch_robots_txt(url)
        elif choice == '12':
            url = input("Target URL: ").strip()
            spinner("Fetching sitemap.xml...")
            fetch_sitemap_xml(url)
        elif choice == '13':
            url = input("Target URL: ").strip()
            spinner("Checking CORS...")
            check_cors(url)
        elif choice == '14':
            url = input("Target URL: ").strip()
            spinner("Testing open redirect...")
            test_open_redirect(url)
        elif choice == '15':
            url = input("Target URL: ").strip()
            spinner("Testing clickjacking...")
            test_clickjacking(url)
        elif choice == '16':
            url = input("Target URL: ").strip()
            wordlist = input("Wordlist path [wordlist.txt]: ").strip() or 'wordlist.txt'
            spinner("Finding sensitive files...")
            find_sensitive_files(url, wordlist)
        elif choice == '17':
            url = input("Target URL: ").strip()
            spinner("Testing User-Agent spoofing...")
            test_user_agent_spoofing(url)
        elif choice == '18':
            url = input("Target URL: ").strip()
            spinner("Checking cookie security...")
            check_cookie_security(url)
        elif choice == '19':
            url = input("Target URL: ").strip()
            spinner("Analyzing HTTP headers...")
            analyze_http_headers(url)
        elif choice == '20':
            url = input("Target URL: ").strip()
            spinner("Testing Host Header Injection...")
            test_host_header_injection(url)
        elif choice == 'q':
            print("\n[*] Thank you for using IGotU. Goodbye!")
            break
        else:
            print("\n[-] Invalid option! Please enter 1-20 or q.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n[*] Scan interrupted by user. Exiting...")
        sys.exit(0)
    except Exception as e:
        print(f"\n[-] Fatal error: {str(e)}")
        sys.exit(1)
