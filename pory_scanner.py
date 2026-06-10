import socket
import sys

def scan_ports(target_host):
    # Common ports jo hum check karna chahte hain
    ports_to_scan = [21, 22, 23, 25, 80, 443, 8080]
    
    print(f"[*] Starting scan on host: {target_host}")
    print("-" * 40)
    
    try:
        # IP address check karna
        target_ip = socket.gethostbyname(target_host)
        print(f"[+] Target IP resolved: {target_ip}\n")
    except socket.gaierror:
        print("[-] Error: Could not resolve hostname.")
        sys.exit()

    # Har ek port ko check karne ka loop
    for port in ports_to_scan:
        # AF_INET = IPv4, SOCK_STREAM = TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # 1 second ka timeout taaki script fance na rahe
        s.settimeout(1.0)
        
        # Connection try karna
        result = s.connect_ex((target_ip, port))
        
        if result == 0:
            print(f"[+] Port {port}: OPEN")
        else:
            print(f"[-] Port {port}: CLOSED")
            
        # Socket connection band karna
        s.close()

if __name__ == "__main__":
    # Localhost (apne hi system) par test karne ke liye
    target = "127.0.0.1"
    scan_ports(target)
