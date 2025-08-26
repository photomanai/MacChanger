# MAC Address Changer

A Python-based command-line tool for changing MAC addresses on network interfaces in Linux systems.

## Repository

🔗 **GitHub**: [https://github.com/photomanai/MacChanger](https://github.com/photomanai/MacChanger)

## Features

- Change MAC address to a specific value
- Generate and apply random MAC addresses
- Validate network interfaces
- Display old and new MAC addresses
- Error handling and user-friendly messages

## Requirements

- Python 3.6+
- Linux operating system
- Root/sudo privileges
- `ifconfig` command available on the system

## Installation

### Method 1: Clone from GitHub
```bash
git clone https://github.com/photomanai/MacChanger.git
cd MacChanger
```

### Method 2: Download ZIP
1. Download the ZIP file from [GitHub repository](https://github.com/photomanai/MacChanger)
2. Extract the files
3. Navigate to the extracted folder

### Prerequisites
- Python 3.6+
- Git (for cloning method)
- No additional Python dependencies required (uses only standard library)

## Usage

### Basic Syntax

```bash
python3 MacChanger.py <interface> [options]
```

### Options

- `-m, --mac`: Specify a custom MAC address
- `-r, --random`: Generate and apply a random MAC address
- `-h, --help`: Show help message

### Examples

#### Change to a specific MAC address:
```bash
sudo python3 MacChanger.py eth0 -m 00:11:22:33:44:55
```

#### Generate and apply a random MAC address:
```bash
sudo python3 MacChanger.py wlan0 -r
```

#### Show help:
```bash
python3 MacChanger.py -h
```

## How It Works

1. **Interface Validation**: Checks if the specified network interface exists
2. **Current MAC Display**: Shows the current MAC address before making changes
3. **MAC Address Change**: 
   - Brings the interface down
   - Changes the hardware (MAC) address
   - Brings the interface back up
4. **Verification**: Displays the new MAC address after the change

## Important Notes

⚠️ **Root Privileges Required**: This script requires sudo/root access to modify network interface settings.

⚠️ **Network Disruption**: Changing MAC address will temporarily disconnect the network interface.

⚠️ **Interface Names**: Common interface names include:
- `eth0`, `eth1` - Ethernet interfaces
- `wlan0`, `wlan1` - Wireless interfaces
- `enp0s3`, `wlp2s0` - Modern systemd naming

## Random MAC Generation

The random MAC generator:
- Creates valid hexadecimal MAC addresses
- Avoids problematic addresses (starting/ending with 00 or FF)
- Ensures proper MAC address format (XX:XX:XX:XX:XX:XX)

## Error Handling

The script handles various error scenarios:
- Invalid interface names
- Malformed MAC addresses
- Permission issues
- Command execution failures

## Example Output

```
Your Old MAC address: aa:bb:cc:dd:ee:ff
MyMacChanger started...
Your New MAC address: 12:34:56:78:9a:bc
```

## Troubleshooting

### Permission Denied
```bash
sudo python3 MacChanger.py eth0 -r
```

### Interface Not Found
Check available interfaces:
```bash
ifconfig -a
```
or
```bash
ip link show
```

### Command Not Found (ifconfig)
Install net-tools:
```bash
sudo apt install net-tools  # Ubuntu/Debian
sudo yum install net-tools   # CentOS/RHEL
```

## Security Considerations

- MAC address changes are temporary and reset after reboot
- Some networks use MAC address filtering
- This tool is for legitimate network administration and privacy purposes
- Be aware of local laws and network policies

## Legal Disclaimer

This tool is intended for educational purposes and legitimate network administration. Users are responsible for complying with applicable laws and network policies when using this software.

## License

This project is open source. Use responsibly and at your own risk.
