import subprocess
import optparse
import re


def get_arguements():
    parse = optparse.OptionParser()
    parse.add_option("-i","--interface",dest="interface",help="Interface to change its mac address")
    parse.add_option("-m","--mac",dest="new_mac",help="New MAC address")
    (options,arguements)= parse.parse_args()
    if not options.interface:
        parse.error("[-] Hey! You have forgot to specify interface name,please use --help for more info")
    elif not options.new_mac:
        parse.error("[-] Hey! You have forgot to specify new mac address,please use --help for more info")
    return options


def change_mac_address(interface,new_mac):
    print("[+] Changing mac address for interface",interface)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up",])
    print("Mac address changed successfully")


def get_current_mac(interface):
    ifconfig_result=subprocess.check_output("ifconfig",interface)
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig_result))
    if(mac_address_search_result):
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read Mac address")


options=get_arguements()
current_mac=get_current_mac(options.interface)
print("Current MAC = "+str(current_mac))
change_mac_address(options.interface,options.new_mac)
current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] Mac address was changed successfully to "+current_mac)
else:
    print("[-] Mac address did not changed")