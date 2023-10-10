import re
import subprocess


try:
    # Run the 'netsh' command to list Wi-Fi networks
    networks = subprocess.check_output(['netsh', 'wlan', 'show', 'network'], shell=True, text=True)
    decoded_networks = networks.strip()

    wifi_networks = {}

    # Split the decoded network information into lines
    network_lines = decoded_networks.split('\n')

    # Iterate through each line and parse network details
    for line in network_lines:
        if "SSID" in line:
            ssid = line.split(":")[1].strip()  # Extract SSID
            wifi_networks[ssid] = {}  # Create a dictionary for the SSID
        elif "Authentication" in line:
            authentication = line.split(":")[1].strip()  # Extract Authentication
            wifi_networks[ssid]["Authentication"] = authentication
        elif "Encryption" in line:
            encryption = line.split(":")[1].strip()  # Extract Encryption
            wifi_networks[ssid]["Encryption"] = encryption

    # Print the dictionary with network information
    print(f"There are {len(wifi_networks.keys())} networks available")
    for ssid, details in wifi_networks.items():
        print(f"SSID: {ssid}")
        print(f"Authentication: {details.get('Authentication', 'N/A')}")
        print(f"Encryption: {details.get('Encryption', 'N/A')}")
        print()  # Add a blank line for separation

except subprocess.CalledProcessError as e:
    print("Error: Unable to retrieve Wi-Fi network information.")