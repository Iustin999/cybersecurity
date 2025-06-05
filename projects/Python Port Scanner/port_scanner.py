import socket
import sys
from datetime import datetime

# Get user input
target = input("Enter IP address or hostname to scan: ").strip()
try:
    start_port = int(input("Enter start port (e.g., 1): "))
    end_port = int(input("Enter end port (e.g., 1024): "))
except ValueError:
    print("[!] Invalid port number.")
    sys.exit()

print(f"\n🔍 Scanning target {target} from port {start_port} to {end_port}...\n")
start_time = datetime.now()

try:
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        result = sock.connect_ex((target, port))

        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown"
            print(f"[+] Port {port} is OPEN ({service})")

        sock.close()

except KeyboardInterrupt:
    print("\n[!] Scan interrupted by user.")
    sys.exit()
except socket.gaierror:
    print("[!] Hostname could not be resolved.")
    sys.exit()
except socket.error:
    print("[!] Couldn't connect to server.")
    sys.exit()

end_time = datetime.now()
total_time = end_time - start_time
print(f"\n✅ Scan completed in: {total_time}")
