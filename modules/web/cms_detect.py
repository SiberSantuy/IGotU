import requests
import re

def detect_cms(target_url):
    """
    Fingerprinting CMS populer via header, path, dan konten.
    """
    print(f"\n[*] CMS Detection for: {target_url}")
    try:
        resp = requests.get(target_url, timeout=7)
        headers = resp.headers
        text = resp.text
        # WordPress
        if 'wp-content' in text or 'wordpress' in text.lower() or 'wp-' in text:
            print("[+] Detected: WordPress")
        elif 'Joomla!' in text or 'joomla' in text.lower():
            print("[+] Detected: Joomla!")
        elif 'Drupal.settings' in text or 'drupal' in text.lower():
            print("[+] Detected: Drupal")
        elif 'prestashop' in text.lower():
            print("[+] Detected: PrestaShop")
        elif 'shopify' in text.lower():
            print("[+] Detected: Shopify")
        elif 'magento' in text.lower():
            print("[+] Detected: Magento")
        elif 'opencart' in text.lower():
            print("[+] Detected: OpenCart")
        else:
            print("[-] CMS tidak terdeteksi secara otomatis.")
    except Exception as e:
        print(f"[-] Error: {str(e)}")
