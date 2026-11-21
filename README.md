# Enterprise Network Monitoring & Incident Response Lab

## Overview

This project is a hands-on enterprise network lab designed to demonstrate practical skills in:

- Network design
- IP addressing
- Routing and switching
- Network monitoring
- Network troubleshooting
- Packet analysis
- Incident response
- Root cause analysis
- Basic network automation

## Objectives

- Build a simulated enterprise network
- Configure network devices and endpoints
- Implement basic network services
- Monitor network availability and performance
- Simulate network incidents
- Troubleshoot incidents using a structured methodology
- Analyze network traffic using Wireshark
- Document incidents and root causes
- Develop basic automation using Python

## Technologies

- Cisco Packet Tracer
- Wireshark
- Linux
- Windows
- Zabbix
- Python
- Git
- GitHub

## Project Status

The project is being developed in multiple phases, covering network infrastructure, monitoring, troubleshooting, incident response and automation.

### Completed Activities

| Day | Activity | Status |
|---|---|---|
| Day 1 | Git and GitHub project setup | Completed |
| Day 2 | Enterprise network topology using Packet Tracer | Completed |
| Day 3 | IP addressing and network planning | Completed |
| Day 4 | DHCP configuration | Completed |
| Day 5 | DNS and HTTP configuration | Completed |
| Day 6 | Network traffic analysis using Wireshark | Completed |
| Day 7 | DNS resolution failure incident simulation | Completed |
| Day 8 | Ubuntu monitoring server setup | Completed |
| Day 9 | Zabbix installation and agent monitoring | Completed |
| Day 10 | Zabbix monitoring and filesystem discovery | Completed |
| Day 11 | Network interface monitoring and dashboard configuration | Completed |

### Current Monitoring Capabilities

- CPU utilization monitoring
- Memory utilization monitoring
- Server availability monitoring
- Network interface discovery
- Incoming and outgoing network traffic monitoring
- Network packet errors and discards monitoring
- Zabbix dashboard visualization

### Monitoring Environment

- Monitoring Platform: Zabbix 7.0.32
- Operating System: Ubuntu Server 26.04.1 LTS
- Monitoring Agent: Zabbix Agent 2
- Network Interface: ens33
- Virtualization: VMware


## Initial Network Topology

The initial lab consists of:

- 1 Cisco 2911 router
- 1 Cisco 2960 switch
- 3 client PCs
- 1 server

### Network

Network: 192.168.10.0/24

Gateway: 192.168.10.1

### Devices

| Device | IP Address |
|--------|------------|
| EDGE-RTR| 192.168.10.1 |
| CLIENT-01| 192.168.10.11 |
| CLIENT-02| 192.168.10.12 |
| CLIENT-03| 192.168.10.13 |
| APP-SRV| 192.168.10.20 |

## Author

Ganesh