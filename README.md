# portScanner

The portScanner scans ports under a prompted IPv4 address using the socket program. The socket program builds a connection between two nodes. The parameters in the socket program uses two arguments: use an IPv4 format and send a ping to port. 

The program prompts the user for an IPv4 written in octet form. Then, the program prompts for the specific port to scan if open or closed. For ease of interpretation, a closed port will be displayed in red text while an open port will be displayed in green.

The code can be adjusted to scan a range of ports. This is a necessary step to use the flash program framework to build a more advanced port scanner.