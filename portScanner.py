import socket
import threading

def scan_port(host, port, results):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    result = sock.connect_ex((host, port))
    if result == 0:
        print(f"Port {port} is open.")
        results.append(port)
    sock.close()

def scan_ports(host, start, end):
    results = []
    threads = []
    for port in range(start, end+1):
        t = threading.Thread(target=scan_port, args=(host, port, results))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    return results

with open("open_ports.txt", "w") as f:
    f.write("")  # Clear the file content if it already exists

host = input("Enter the target host to scan: ")
start_port = int(input("Enter the start port to scan: "))
end_port = int(input("Enter the end port to scan: "))

open_ports = scan_ports(host, start_port, end_port)

with open("open_ports.txt", "a") as f:
    for port in open_ports:
        f.write(f"{port}\n")

print("Scanning complete. Open ports written to open_ports.txt")
