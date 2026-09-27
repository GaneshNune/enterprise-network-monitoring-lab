# IP Addressing Documentation

## Network Information

| Parameter | Value |
|---|---|
| Network | 192.168.10.0/24 |
| Subnet Mask | 255.255.255.0 |
| Default Gateway | 192.168.10.1 |
| Broadcast Address | 192.168.10.255 |
| Usable Host Range | 192.168.10.1 - 192.168.10.254 |

## Device IP Addressing

| Device | IP Address | Subnet Mask | Default Gateway |
|---|---|---|---|
| EDGE-RTR | 192.168.10.1 | 255.255.255.0 | N/A |
| CLIENT-01 | 192.168.10.11 | 255.255.255.0 | 192.168.10.1 |
| CLIENT-02 | 192.168.10.12 | 255.255.255.0 | 192.168.10.1 |
| CLIENT-03 | 192.168.10.13 | 255.255.255.0 | 192.168.10.1 |
| APP-SRV | 192.168.10.20 | 255.255.255.0 | 192.168.10.1 |

## Why /24 Was Selected

The lab uses the 192.168.10.0/24 network.

The /24 CIDR prefix means that 24 of the 32 IPv4
bits represent the network portion.

The corresponding subnet mask is:

255.255.255.0

A /24 network provides 256 total IP addresses,
including the network and broadcast addresses,
resulting in 254 usable host addresses.

A /24 network was selected because this lab currently
contains a small number of devices while leaving
sufficient address space for future expansion.

### Address Details

- Network Address: 192.168.10.0
- Broadcast Address: 192.168.10.255
- Usable Range: 192.168.10.1 - 192.168.10.254
- Total Addresses: 256
- Usable Host Addresses: 254