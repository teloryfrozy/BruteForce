from subprocess import check_output, CalledProcessError
from platform import system
from colorama import Fore, Style


try:
    if system() != "Windows":
        print("This script only works on Windows")
        raise OSError
    
    # Run the 'netsh' command to list Wi-Fi networks
    networks = check_output(['netsh', 'wlan', 'show', 'network'], shell=True, text=True)
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
    num_networks = len(wifi_networks.keys())
    
    if num_networks == 0:
        print(Fore.RED + "No networks available" + Style.RESET_ALL)
    elif num_networks == 1:
        print(Fore.CYAN + "There is 1 network available" + Style.RESET_ALL)
    else:
        print(Fore.CYAN + f"There are {num_networks} networks available" + Style.RESET_ALL)
    
    list_ssid = []
    for ssid, details in wifi_networks.items():
        list_ssid.append(ssid)
        print(Fore.GREEN + f"SSID: {ssid}" + Style.RESET_ALL)
        
        # Authentication color based on value
        auth = details.get('Authentication', 'N/A')
        auth_color = Fore.YELLOW if auth != 'N/A' else Fore.RED
        print(f"Authentication: {auth_color + auth + Style.RESET_ALL}")
        
        # Encryption color based on value
        encr = details.get('Encryption', 'N/A')
        encr_color = Fore.YELLOW if encr != 'N/A' else Fore.RED
        print(f"Encryption: {encr_color + encr + Style.RESET_ALL}")
        
        print()

except CalledProcessError as e:
    print("Error: Unable to retrieve Wi-Fi network information.")
    print(f"The error message is: {e}")