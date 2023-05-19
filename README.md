# Firewall Rule Generator

This repository contains a Python script for generating firewall rules based on user inputs. The script supports both Windows and Linux platforms, allowing users to generate platform-specific firewall rules using `netsh` for Windows and `iptables` for Linux. With this tool, users can easily generate custom firewall rules by specifying the source IP, destination IP, port, and action (ACCEPT or DROP). This script simplifies the process of generating firewall rules and can be used in real-world scenarios to enhance network security.

## Features

- Generates firewall rules for Windows and Linux platforms
- Supports both `netsh` command for Windows and `iptables` command for Linux
- User-friendly interface for specifying source IP, destination IP, port, and action (ACCEPT or DROP)

## Prerequisites

- Python 3.6 or higher

## Usage

1. Clone or download this repository to your local machine.

2. Open a terminal or command prompt and navigate to the repository directory.

3. Run the script using the following command:

    ```
    python firewall_rule_generator.py
    ```

4. Follow the prompts to enter the required information:
   - Source IP (in CIDR notation)
   - Destination IP (in CIDR notation)
   - Port
   - Action (ACCEPT or DROP)

5. Once you provide the required inputs, the script will generate the corresponding firewall rule.

## Examples

### Example 1: Generate a firewall rule to allow incoming traffic from a specific IP to port 80

```
Enter the source IP (in CIDR notation): 192.168.0.10/32
Enter the destination IP (in CIDR notation): 0.0.0.0/0
Enter the port: 80
Enter the action (ACCEPT or DROP): ACCEPT

Generated Firewall Rule:
- Windows: netsh advfirewall firewall add rule name="Custom Rule" dir=in action=ACCEPT localport=80 protocol=TCP remoteip=192.168.0.10/32
- Linux: iptables -A INPUT -s 192.168.0.10/32 -d 0.0.0.0/0 -p tcp --dport 80 -j ACCEPT
```

### Example 2: Generate a firewall rule to block all incoming traffic from a specific IP

```
Enter the source IP (in CIDR notation): 10.0.0.5/32
Enter the destination IP (in CIDR notation): 0.0.0.0/0
Enter the port: 0
Enter the action (ACCEPT or DROP): DROP

Generated Firewall Rule:
- Windows: netsh advfirewall firewall add rule name="Custom Rule" dir=in action=DROP remoteip=10.0.0.5/32
- Linux: iptables -A INPUT -s 10.0.0.5/32 -d 0.0.0.0/0 -j DROP
```

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

e-mail     : ajithchandranr@protonmail.com 

linkedin  : https://www.linkedin.com/in/ajithchandranr/

