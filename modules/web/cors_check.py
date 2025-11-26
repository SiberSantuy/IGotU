import requests

def check_cors(target_url):
    """
    Cek misconfiguration CORS pada target.
    """
    import requests
    print(f"\n[*] CORS Misconfiguration Checker for: {target_url}")
    try:
        headers = {"Origin": "https://evil.com"}
        r = requests.get(target_url, headers=headers, timeout=7)
        acao = r.headers.get('Access-Control-Allow-Origin', '')
        acac = r.headers.get('Access-Control-Allow-Credentials', '')
        if acao == '*':
            print("[!] Insecure: Access-Control-Allow-Origin is wildcard (*)!")
        elif 'evil.com' in acao:
            print(f"[!] Insecure: Reflection of Origin header: {acao}")
        elif acao:
            print(f"[+] Access-Control-Allow-Origin: {acao}")
        else:
            print("[-] No Access-Control-Allow-Origin header.")
        if acac.lower() == 'true':
            print("[!] Access-Control-Allow-Credentials: true (potential risk)")
    except Exception as e:
        print(f"[-] Error: {str(e)}")
