# Monitoring Foundation

## Objective

Prepare a Linux server that will host the monitoring platform for the Enterprise Network Monitoring & Incident Response Lab.

## Monitoring Platform

**Zabbix** is the monitoring platform selected for this project.

## Monitoring Server

- **Operating System:** Ubuntu Server 26.04.1 LTS
- **Architecture:** x86_64
- **Network Interface:** `ens33`
- **Network Mode:** VMware NAT
- **IP Address:** `192.168.196.129/24`

## Purpose

The monitoring server will monitor hosts and services in the lab, collect operational metrics, identify predefined problem conditions, and generate alerts when configured triggers are activated.

## Initial Verification

The following checks were performed:

- Verified the operating system and architecture.
- Verified the hostname and network interface.
- Verified the assigned IPv4 address.
- Tested IP connectivity using `ping -c 4 8.8.8.8`.
- Tested DNS resolution.
- Updated the operating system.
- Checked disk usage using `df -h`.
- Checked memory usage using `free -h`.
- Inspected running processes using `top`.

## Zabbix Installation Progress

- Investigated the Zabbix 8.0 repository package availability on Ubuntu 26.04.
- Disabled the unstable Zabbix repository during troubleshooting.
- Configured the official Zabbix 7.0 repository.
- Verified the available `zabbix-server-mysql` package candidate.
- Installed the Zabbix server, web frontend, SQL scripts, Agent 2, and MariaDB packages.
- Confirmed that MariaDB and Apache were running.
- Created the Zabbix database and database user.

**Remaining tasks:** Import the Zabbix database schema, configure the server database connection, start and verify Zabbix services, complete the web setup, and test host monitoring and alerts.

## Architecture

```text
              Monitoring Server
              Ubuntu Server
              ├── Zabbix Server
              ├── MariaDB
              ├── Apache / Web Frontend
              └── Zabbix Agent 2
                       |
                       | Monitoring
                       v
              Lab Hosts and Services
              ├── Client Systems
              ├── Application Server
              └── Network Devices
```

## Next Steps

1. Complete the Zabbix database schema import.
2. Configure and start the Zabbix server.
3. Access the web frontend.
4. Configure monitored hosts and triggers.
5. Simulate an incident and verify alert generation and recovery.
6. Document the results and publish project evidence to GitHub.
