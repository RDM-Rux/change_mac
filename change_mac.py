#!/usr/bin/env python

import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please input interface, use --help for more info")
    elif not options.new_mac:
        parser.error("[-] Please input new MAC address, use --help for more info")
    return options

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_mac(interface):
    result_ifconfig = subprocess.check_output(["ifconfig", interface])
    print(result_ifconfig)
    # regex
    # \w\w:\w\w:\w\w:\w\w:\w\w:\w\w
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", result_ifconfig)
    if mac_address_search_result:
        return (mac_address_search_result.group(0))
    else:
        print("[-] Could not get MAC address!")

options = get_arguments()
mac_address = get_mac(options.interface)
print("Current MAC address is: " + mac_address)

change_mac(options.interface, options.new_mac)




