from subprocess import check_output, CalledProcessError
from platform import system


def get_SSIDS() -> list:
    """Returns a list of SSIDs"""
    try:
        if system() != "Windows":
            print("This script only works on Windows")
            raise OSError

        networks = check_output(['netsh', 'wlan', 'show', 'network'], shell=True, text=True).strip().split('\n')

        # list of SSID - do not take the hidden networks
        SSIDs = [line.split(":")[1].strip() for line in networks if "SSID" in line and line.split(":")[1].strip()]

        return SSIDs
    
    except CalledProcessError as e:
        print("Error: Unable to retrieve Wi-Fi network information.")
        print(f"The error message is: {e}")