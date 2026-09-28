# DHCP Configuration

## Objective

Configure EDGE-RTR as the DHCP server so that client devices can obtain network configuration automatically.

## Network

Network: 192.168.10.0/24

Default Gateway: 192.168.10.1

DNS Server: 192.168.10.20

## DHCP Design

Addresses 192.168.10.1 through 192.168.10.99 were excluded from dynamic allocation.

Client devices receive addresses beginning from 192.168.10.100.

## DHCP Clients

- CLIENT-01
- CLIENT-02
- CLIENT-03

## Verification

The configuration was verified using:

show ip dhcp binding

Connectivity was tested using ping.

## Result

All three client devices successfully obtained their network configuration through DHCP.