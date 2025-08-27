import subprocess
import optparse
import sys
import re
from random import randint as rand


def getUserInput() -> tuple[str, str]:
    parser = optparse.OptionParser("python3 MacChanger.py <interface> -m <MAC Address>")
    parser.add_option("-m", "--mac", dest="mac_address", help="MAC address changer")
    parser.add_option(
        "-r",
        "--random",
        action="store_true",
        dest="random_mac",
        help="Crate Random MAC address and change",
    )
    try:
        (user_input, arguments) = parser.parse_args()
    except Exception as e:
        print(f"[ERROR] {e}")
        print("Invalid argument. Use -h for help.")
        sys.exit(1)
    if len(arguments) > 1:
        print("[ERROR] Please specify an interface.")
        print("Example: python3 MacChanger.py eth0 -m 00:11:22:33:44:55")
        sys.exit(1)
    return parser.parse_args()


def changeMacAddress(interface: str, mac_address: str) -> None:
    try:
        subprocess.call(["ifconfig", interface, "down"])
        subprocess.call(["ifconfig", interface, "hw", "ether", mac_address])
        subprocess.call(["ifconfig", interface, "up"])
    except Exception as e:
        print(f"[ERROR] Invalid interface or MAC: {e}")
        print("Use -h for help.")
        sys.exit(1)


def controlNewMac(interface: str):
    try:
        ifconfig = subprocess.check_output(["ifconfig", interface]).decode("utf-8")
    except Exception as e:
        print(f"[ERROR] Invalid interface or MAC: {e}")
        print("Use -h for help.")
        sys.exit(1)
    mac = re.search(r"([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}", ifconfig)
    if mac:
        return mac.group(0)
    return None


def crateRandomMac() -> str:
    symbols = [
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
    ]
    while True:
        mac_list = [
            f"{symbols[rand(0, len(symbols) - 1)]}{symbols[rand(0, len(symbols) - 1)]}"
            for _ in range(0, 6)
        ]
        mac = ":".join(mac_list)
        if (
            mac.startswith("00")
            or mac.startswith("ff")
            or mac.endswith("00")
            or mac.endswith("ff")
        ):
            continue
        break
    return mac


def main() -> None:

    print(
        r"""
  __  __             _____ _                            
 |  \/  |           / ____| |                           
 | \  / | __ _  ___| |    | |__   __ _ _ __   __ _  ___ 
 | |\/| |/ _` |/ __| |    | '_ \ / _` | '_ \ / _` |/ _ \
 | |  | | (_| | (__| |____| | | | (_| | | | | (_| |  __/
 |_|  |_|\__,_|\___|\_____|_| |_|\__,_|_| |_|\__, |\___|
                                              __/ |     
                                             |___/      
                                     by: PhotoManAi

"""
    )

    (user_input, arguments) = getUserInput()
    print(f"Your Old MAC address: {controlNewMac(arguments[0])}")
    print("MyMacChanger started...")
    if user_input.random_mac:
        random_mac = crateRandomMac()
        changeMacAddress(arguments[0], random_mac)
    else:
        changeMacAddress(arguments[0], user_input.mac_address)
    print(f"Your New MAC address: {controlNewMac(arguments[0])}")


if __name__ == "__main__":
    main()
