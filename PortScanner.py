import socket

def scan_ports(ports):
    try:
        s.connect((target_ip, port))
        return True
    except:
        return False

s = socket.socket()
target = input(f'What do you want to scan?: ')
target_ip = socket.gethostbyname(target)
print(f'Scanning target: {target_ip}')
for port in range(80, 125):
    if scan_ports(port):
            print(f'Port {port} is open')
    else:
        print(f'Port {port} is closed')