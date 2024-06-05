# Network Port Scanner

This project is a simple Python tool that detects open ports on a given IP address.

## Usage

1. Make sure Python 3.x is installed.
2. Download the `port_scanner.py` file.
3. In the terminal, navigate to the folder where the `port_scanner.py` file is located.
4. Run the following command:
    ```bash
    python port_scanner.py
    ```
5. Enter the IP address and port range to scan.
6. Open ports will be listed.

## Requirements

- Python 3.x

## Sample Usage

```bash
Enter the IP address to scan: 127.0.0.1
Enter start port: 22
Enter end port: 33
Scanning is performed between 20-30 ports at the address 127.0.0.1...
Open ports: [24, 80]
