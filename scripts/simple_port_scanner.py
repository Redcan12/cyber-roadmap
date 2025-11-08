# scripts/simple_port_scanner.py
import socket
import argparse
from datetime import datetime

parser = argparse.ArgumentParser(description="Simple TCP Port Scanner (local use only)")
parser.add_argument("--host", required=True, help="Host to scan (e.g. 127.0.0.1)")
parser.add_argument("--ports", default="1-1024", help="Port range, e.g. 1-1024")
args = parser.parse_args()

start = datetime.now()
host = args.host
port_range = args.ports.split('-')
start_port = int(port_range[0])
end_port = int(port_range[1])

open_ports = []
print(f"Scanning {host} ports {start_port}-{end_port} ...")

for port in range(start_port, end_port+1):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.4)
        try:
            res = s.connect_ex((host, port))
            if res == 0:
                open_ports.append(port)
                print(f"Port {port} OPEN")
        except Exception:
            pass

print("Done. Open ports:", open_ports)
print("Elapsed:", datetime.now() - start)