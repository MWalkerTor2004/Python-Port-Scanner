import socket
import psutil

def scan_ports(port):
    try:
        s.connect((target_ip, port))
        return True
    except:
        return False

def service(port):
    try:
        for conn in psutil.net_connections():
            if conn.laddr.port == port:
                return conn.pid
        return None
    except Exception as e:
        print(f"Error occurred while checking service for port {port}: {e}")
        return None

def main():
    print(f'Scanning target: {target_ip}')
    for port in range(80, 125):
        if scan_ports(port):
                print(f'Port {port} is open, Service PID: {service(port)}')
        else:
            print(f'Port {port} is closed')
    s.close()
    print('Scanning complete.')

s = socket.socket()
target = input(f'What do you want to scan?: ')
target_ip = socket.gethostbyname(target)

if __name__ == "__main__":
    main()
