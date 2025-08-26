import subprocess
import optparse
import re

def getUserInput() -> tuple[str, str]:
    parse_object = optparse.OptionParser()
    # parse_object.add_option("-i", "--interface", dest="interface", help="interface to change!")
    parse_object.add_option("-m", "--mac", dest="mac_address", help="mac address to change!", )
    return parse_object.parse_args()

def changeMacAddress(interface: str,mac_address: str) -> None:
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_address])
    subprocess.call(["ifconfig", interface, "up"])

def controlNewMac(user_interface: str):
    ifconfig = subprocess.check_output(["ifconfig", user_interface]).decode("utf-8")
    mac = re.search(r"([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}", ifconfig)
    if mac:
        return mac.group(0)
    return None

(user_input, arguments) = getUserInput()
print("MyMacChanger started...")
changeMacAddress(arguments[0],user_input.mac_address)
print(controlNewMac(arguments[0]))
