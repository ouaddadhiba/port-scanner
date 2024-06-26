import socket
import threading
import argparse
import ipaddress

#lists: result TCP
open_tcp = []
closed_tcp = []
filtered_tcp = []

 #list: result UDP
open_udp= []
closed_udp = []
filtered_udp = []


start_point = 1
end_point = 1024

#input (ip address)

def valid_ip(address):
    try:
        ipaddress.ip_address(address)
        return address
    except ValueError:
        raise argparse.ArgumentTypeError(f"{address} in invalid")

parser = argparse.ArgumentParser()
parser.add_argument('ip_address', type=valid_ip, help='Enter the address you want to scan')
arg = parser.parse_args()

host = arg.ip_address

# To create all the sockets from the port 1 to 1024 (common ports)
ports_list = list(range(start_point, end_point + 1))
 #to append to the list once at a time
lock = threading.Lock()
    
def tcp_scanner(host, port):   
    
        tcp_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_s.settimeout(6)

        try:
            tcp_s.connect((host, port))
            with lock:
                open_tcp.append(port)

        except socket.timeout:
            with lock:
                filtered_tcp.append(port)
                 
        except socket.error:
            with lock:
                closed_tcp.append(port)
        finally:
             tcp_s.close()



def udp_scanner(host, port):
    udp_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_s.settimeout(6)

    try:
        udp_s.sendto(b'', (host, port))
        udp_s.recvfrom(1024)

        with lock:
            open_udp.append(port)

    except socket.timeout:
        with lock:
            filtered_udp.append(port)
                 
    except socket.error:
        with lock:
            closed_udp.append(port)
    finally:
        udp_s.close()
     

def thread_processor():
    threads = []

    for port in ports_list:
        thread1 = threading.Thread(target=tcp_scanner, daemon=False, args=(host, port))
        thread2 = threading.Thread(target=udp_scanner, daemon=False, args=(host, port))
        
        threads.append(thread1)
        threads.append(thread2)

        thread1.start()
        thread2.start()

    for thread1 in threads:
        thread1.join()

    for thread2 in threads:
        thread2.join()


thread_processor()

#Output results: open ports
print("Open")
for port in open_tcp:
    print(f"{port}/tcp")

for port in open_udp:
    print(f"{port}/udp")
