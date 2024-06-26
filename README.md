Port Scanner
Welcome to my first Python project! This script is a simple port scanner that checks the status of TCP and UDP ports on a given IP address. It scans ports in the range from 1 to 1024, categorizing them as open, closed, or filtered.

Features
Scans both TCP and UDP ports.
Categorizes ports as open, closed, or filtered.
Utilizes threading for efficient scanning.
Requirements
Python 3.x

Installation
Clone the repository:

```bash
git clone https://github.com/ouaddadhiba/port-scanner.git
cd port-scanner

Usage
To run the port scanner, use the following command:

python port_scanner.py <IP_ADDRESS>
Replace <IP_ADDRESS> with the IP address you want to scan.

Example
python port_scanner.py 192.168.1.1

Code Overview
The script consists of the following parts:

Imports: Necessary libraries for creating sockets, threading, parsing command-line arguments, and validating IP addresses.
Result Lists: Lists to store the results of the port scan.
Input Validation: Function to validate the input IP address.
Argument Parsing: Handling command-line arguments and validating the IP address.
Port List and Lock: Initializing the range of ports to scan and a lock to manage threading.
TCP and UDP Scanners: Functions to scan TCP and UDP ports and categorize them based on their status.
Thread Processor: Managing threading for the port scanning functions.
Output Results: Printing the results of the port scan.

Example Output

Open
80/tcp
443/tcp
53/udp

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Contributing
Since this is my first project, I am open to any feedback or contributions. Feel free to open an issue or submit a pull request.

Contact
For any questions or feedback, please contact me at [houaddad@gmail.com].