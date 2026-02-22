```
  _   _ _____ _______        _____  ____  _  __  ____   ____    _    _   _ _   _ _____ ____  
 | \ | | ____|_   _\ \      / / _ \|  _ \| |/ / / ___| / ___|  / \  | \ | | \ | | ____|  _ \ 
 |  \| |  _|   | |  \ \ /\ / / | | | |_) | ' /  \___ \| |     / _ \ |  \| |  \| |  _| | |_) |
 | |\  | |___  | |   \ V  V /| |_| |  _ <| . \   ___) | |___ / ___ \| |\  | |\  | |___|  _ < 
 |_| \_|_____| |_|    \_/\_/  \___/|_| \_\_|\_\ |____/ \____/_/   \_\_| \_|_| \_|_____|_| \_\
```
NETWORK-SCANNER (SCAPY POWERED)
A professional-grade network discovery tool built from scratch using the 
Scapy library. This tool performs ARP broadcasting to discover live hosts 
within a specific IP range, mapping IP addresses to hardware (MAC) addresses 
directly at the Data Link Layer (Layer 2).

**Features**
* **Custom Packet Crafting:** Manually builds Ether/ARP frames for network discovery.
* **Broadcasting:** Uses 'ff:ff:ff:ff:ff:ff' to reach every device in the subnet.
* **Real-time Analysis:** Captures and summarizes responses from active hosts.
* **CLI Arguments:** Integrated with 'optparse' for flexible IP range targeting.

**Prerequisites**
* Python 3.x
* Scapy Library (`pip install scapy`)
* Root/Sudo privileges (Required for raw socket manipulation)

**Installation**

1. Clone the repository:
   * git clone https://github.com/Tde99/Network-Scanner.git

2. Install dependencies:
   * sudo pip3 install scapy

3. Run with sudo:
   * sudo python3 scanner.py -i 10.0.2.1/24

**How it Works:**
1. **ARP Request:** Creates a "Who has this IP?" packet.
2. **Ethernet Layer:** Wraps the request in a broadcast frame so everyone hears it.
3. **Send/Receive:** Dispatches the packet and waits 1 second for replies.
4. **Parsing:** Extracts the sender's IP and MAC address from the 'reel_package'.



**Important Notes:**
* **Accuracy:** Much faster and more reliable than ping-based scanners in local networks.
* **Stealth:** While effective, ARP scanning is visible to network monitoring tools.
* **Educational:** Designed to demonstrate the fundamentals of the Address Resolution Protocol.
