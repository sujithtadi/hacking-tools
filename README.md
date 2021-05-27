# Hacking-Tools
Ethical Hacking tools programmed in python3.
These tools can only be used in linux/unix based systems and penetrations distributions like kali linux and parrotos. 
Use it for educational purpose and to learn 

HACKING TOOLS LIST

1.MAC ADDRESS SPOOFER

MAC(Media Access Control) address is the physical address, which uniquely identifies each device on a given network. 
To make communication between two networked devices, we need two addresses: IP address and MAC address. It is assigned to the 
NIC (Network Interface card) of each device that can be connected to the internet.

WHY DO WE NEED IT?

Some Routers and Firewalls uses a list called access control list which have list of blacklisted mac addresses added by network 
administrators so whenever those blacklisted mac addresses tries to access the network the router or firewall will block those 
devices from accessing
This program will change your mac address thereby evading firewall or routers access control lists and also bringing
anonymity to you when you are in a network

USAGE

    python3 macchanger.py [options]
    options:
    -h ,--help            help to list the options
    -i ,--interface       set the interface
    -m ,--mac             set the new mac address

