#Network Port Scanner
# This tool is used to detect open ports at a specified IP address.



import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port):
    """
    Scans the port at the specified IP address and checks if it is open.
    """
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)
    try:
        scanner.connect((ip, port))
        return port, True
    except:
        return port, False
    finally:
        scanner.close()

def scan_ports(ip, ports):
    """
    Scans a range of ports at the specified IP address.
    """
    open_ports = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        results = executor.map(lambda port: scan_port(ip, port), ports)
        for port, is_open in results:
            if is_open:
                open_ports.append(port)
    return open_ports

if __name__ == "__main__":
    target_ip = input("Enter the IP address to scan: ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))
    
    print(f"Scanning {target_ip} in the port range {start_port}-{end_port}...")

    ports = range(start_port, end_port + 1)
    open_ports = scan_ports(target_ip, ports)
    
    if open_ports:
        print(f"Open ports: {open_ports}")
    else:
        print("No open port found.")
