import socket
import sys

def find_subdomains(target_domain, wordlist_file):
    """
    Encontra subdomínios de um domínio alvo usando uma wordlist.
    """
    print(f"[*] Iniciando busca por subdomínios em: {target_domain}\n")
    
    try:
        with open(wordlist_file, 'r') as f:
            subdomains = f.read().splitlines()
    except FileNotFoundError:
        print(f"[!] Erro: Arquivo de wordlist '{wordlist_file}' não encontrado.")
        return

    found_subdomains = []
    for sub in subdomains:
        full_domain = f"{sub}.{target_domain}"
        try:
            # Tenta resolver o nome de domínio para um endereço IP
            ip_address = socket.gethostbyname(full_domain)
            print(f"[+] Subdomínio encontrado: {full_domain} -> {ip_address}")
            found_subdomains.append(full_domain)
        except socket.gaierror:
            # Ignora se não conseguir resolver (o subdomínio provavelmente não existe)
            pass
        except Exception as e:
            print(f"[!] Ocorreu um erro: {e}")

    print(f"\n[*] Busca finalizada. {len(found_subdomains)} subdomínios encontrados.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python subdomain_finder.py <alvo.com>")
        sys.exit(1)
        
    target = sys.argv[1]
    # Você pode criar um arquivo 'wordlist.txt' com nomes como: www, mail, ftp, api, dev, staging, etc.
    wordlist = "wordlist.txt" 

    find_subdomains(target, wordlist)