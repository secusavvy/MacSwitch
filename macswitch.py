#!/usr/bin/env python

import subprocess
import argparse

def change_mac(interface, new_mac):
    try:
        print(f"[+] Changing MAC Address for {interface} to {new_mac}")
        subprocess.check_call(["ifconfig", interface, "down"])
        subprocess.check_call(["ifconfig", interface, "hw", "ether", new_mac])
        subprocess.check_call(["ifconfig", interface, "up"])
        print(f"[+] MAC Address changed successfully to {new_mac}")

    except subprocess.CalledProcessError:
        print(f"[-] Error occurred while changing MAC address for {interface}.")
        return

def main():
    parser = argparse.ArgumentParser(description="Change the MAC address of a network interface.")
    parser.add_argument("-i", "--interface", dest="interface", required=True, help="Interface to change MAC Address")
    parser.add_argument("-m", "--mac", dest="new_mac", required=True, help="New MAC Address")
    options = parser.parse_args()
    change_mac(options.interface, options.new_mac)

if __name__ == "__main__":
    main()
