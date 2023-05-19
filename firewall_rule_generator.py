import ipaddress
import sys
import platform

def generate_firewall_rule(source_ip, destination_ip, port, action):
    # Validate source IP
    try:
        source_ip = ipaddress.ip_network(source_ip)
    except ValueError:
        return None

    # Validate destination IP
    try:
        destination_ip = ipaddress.ip_network(destination_ip)
    except ValueError:
        return None

    # Generate firewall rule syntax based on the platform
    if platform.system() == 'Windows':
        rule = f"netsh advfirewall firewall add rule name=\"Custom Rule\" dir=in action={action} localport={port} protocol=TCP remoteip={source_ip}"
    else:
        rule = f"iptables -A INPUT -s {source_ip} -d {destination_ip} -p tcp --dport {port} -j {action}"

    return rule

# Example usage
source_ip = input("Enter the source IP (in CIDR notation): ")
destination_ip = input("Enter the destination IP (in CIDR notation): ")
port = input("Enter the port: ")
action = input("Enter the action (ACCEPT or DROP): ")

firewall_rule = generate_firewall_rule(source_ip, destination_ip, port, action)
if firewall_rule:
    print(f"Generated Firewall Rule: {firewall_rule}")
else:
    print("Invalid input. Please check the provided IP addresses.")
