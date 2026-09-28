# DNS Configuration

## Objective

Configure DNS so that client devices can access the application server using a hostname instead of its IP address.

## DNS Server

Device: APP-SRV

IP Address: 192.168.10.20

## DNS Record

Hostname: app-server.lab.local

IPv4 Address: 192.168.10.20

Record Type: A

## HTTP Service

HTTP was enabled on APP-SRV to provide a simple application service for testing.

## Verification

IP connectivity was verified using:

ping 192.168.10.20

DNS resolution was verified using:

ping app-server.lab.local

The HTTP service was tested using:

http://app-server.lab.local

## Result

CLIENT-01 successfully resolved app-server.lab.local to 192.168.10.20 and accessed the HTTP service.