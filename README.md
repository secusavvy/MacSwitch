# MacSwitch

**MacSwitch** is a Python script that allows you to easily change the MAC address of a network interface on Linux systems. This tool can be useful for privacy enhancement, network management, or testing purposes.

### Features
- Change the MAC address of a specified network interface.
- Simple and intuitive command-line interface.
- Validates the MAC address format to ensure correctness.

### Technologies Used
- Python 3
- `ifconfig` command for changing the MAC address

### Usage
1. Clone the repository:
    ```bash
    git clone https://github.com/secusavvy/MacSwitch.git
    cd MacSwitch
    ```

2. Run the script:
    ```bash
    python macswitch.py -i <interface> -m <new_mac>
    ```

3. Configuration:
    - Replace `<interface>` with the network interface you want to modify (e.g., `eth0`, `wlan0`).
    - Replace `<new_mac>` with the new MAC address in the format `XX:XX:XX:XX:XX:XX`.

4. Example:
    ```bash
    python macswitch.py -i wlan0 -m 00:11:22:33:44:55
    ```

### How It Works
- The script takes the network interface and new MAC address as inputs.
- It uses the `ifconfig` command to bring the interface down, change the MAC address, and bring the interface back up.
- Provides immediate feedback on the status of the MAC address change.

### Disclaimer!

**The author of this script is not responsible for any misuse or damages caused by using this script. Use it at your own risk.**

*Happy hacking responsibly!*
