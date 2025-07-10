import nmap
import sys

def scan_ports_stealth(target_host):
    """
    Realiza um scan de portas TCP de forma mais discreta.
    """
    print(f"[*] Iniciando scan DISCRETO de portas em: {target_host}\n")
    nm = nmap.PortScanner()
    
    try:
        # -sS: SYN Scan (mais discreto que o scan TCP connect padrão)
        # -T2: Template "Polite" (educado), muito mais lento e menos propenso a ativar firewalls.
        # --scan-delay 1s: Adiciona um atraso de 1 segundo entre as requisições.
        nm.scan(target_host, '21,22,25,80,443,3306,8080', arguments='-sS -T2 --scan-delay 1s')

        if target_host not in nm.all_hosts():
            print(f"[!] Host {target_host} parece estar offline ou não respondeu.")
            return

        print("--- RESULTADO DO SCAN DISCRETO ---")
        for host in nm.all_hosts():
            print(f"Host: {host} ({nm[host].hostname()})")
            print(f"Estado: {nm[host].state()}")
            
            for proto in nm[host].all_protocols():
                print("----------")
                print(f"Protocolo: {proto}")

                ports = nm[host][proto].keys()
                for port in sorted(ports):
                    port_info = nm[host][proto][port]
                    print(f"  Porta: {port:<5} | Estado: {port_info['state']}")

    except nmap.PortScannerError as e:
        print(f"[!] Erro do Nmap: {e}. Verifique se o Nmap está instalado e se você tem permissões (pode precisar de 'sudo').")
    except Exception as e:
        print(f"[!] Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 port_scanner_stealth.py <ip_ou_dominio>")
        sys.exit(1)
        
    target = sys.argv[1]
    scan_ports_stealth(target)