import requests

def test_user_agent_spoofing(target_url):
    """
    Uji User-Agent spoofing pada target, deteksi perbedaan response.
    """
    import requests
    print(f"\n[*] User-Agent Spoofing Test for: {target_url}")
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'curl/7.68.0',
        'sqlmap/1.5.2',
        'Googlebot/2.1 (+http://www.google.com/bot.html)',
        'IGotU-Scanner/1.0'
    ]
    responses = {}
    for ua in user_agents:
        try:
            r = requests.get(target_url, headers={'User-Agent': ua}, timeout=7)
            responses[ua] = r.text[:200]
        except Exception:
            responses[ua] = 'ERROR'
    for ua, resp in responses.items():
        print(f"[UA: {ua}] -> {('DIFFERENT' if list(responses.values()).count(resp)==1 else 'SIMILAR')}")
