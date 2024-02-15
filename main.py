#!/usr/bin/python
# Input host IPv4 to scan if specified ports are open or closed
# By koriol on Wednesday February 14, 2024

import socket
from termcolor import colored

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#variable defined by two parameters
#AF_INET the address (and protocol) families, used for the first argument to socket(). IPv4 format
#SOCK_STREAM represent the socket types, used for the second argument to socket(). Ping

#socket.settimeout(5)

host = input("[+] Enter a host to scan: ") #"192.168.1.7" format
port = int(input("[+] Enter a port to scan: ")) #445

def portScan(port):
    if socket.connect_ex((host, port)):
        # Like connect(address), but return an error indicator instead of raising an exception for 
        # errors returned by the C-level connect() call (other problems, such as “host not found,” 
        # can still raise exceptions). The error indicator is 0 if the operation succeeded, otherwise 
        # the value of the errno variable. This is useful to support, for example, asynchronous connects.
        print(colored(f"[!!] Port {port} on {host} is closed", 'red'))
    else:
        print(colored(f"[+] Port {port} on Host {host} is open", 'green'))


# if we want to scan a whole range of ports then let's change a few lines in the code!
# port = 22 assign a variable for port to scan a single port
# for port in (22):
# for port in range (1, 10): to scan a range of ports within said ip
portScan(port)
    #this will allow the scanning to take place in the assigned ip addr and a range of 
    # ports between 1-10