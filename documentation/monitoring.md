# Enterprise Network Monitoring & Incident Response Lab

## Project Overview

This project is a hands-on network monitoring and incident response lab designed to demonstrate practical skills in network configuration, Linux administration, infrastructure monitoring, troubleshooting, and incident documentation.

The lab combines a simulated enterprise network built in Cisco Packet Tracer with a Linux-based monitoring server running Zabbix. It includes network services, traffic analysis, incident simulation, monitoring configuration, and alert validation.

## Objectives

- Design and configure a small enterprise network.
- Implement IP addressing, DHCP, DNS, and application-server connectivity.
- Understand network traffic analysis using Wireshark.
- Document incidents using a structured troubleshooting workflow.
- Set up an Ubuntu Server monitoring environment.
- Install and configure Zabbix for infrastructure monitoring.
- Monitor CPU, memory, and filesystem resources.
- Simulate monitoring failures and validate alert recovery.
- Maintain technical documentation and version control using Git and GitHub.

## Technologies and Tools

- Cisco Packet Tracer
- Ubuntu Server 26.04.1 LTS
- Zabbix 7.0.32
- Zabbix Agent 2
- MariaDB
- Apache
- Wireshark
- Git and GitHub
- VMware virtualization

---

## Day 1 — Git and GitHub Project Setup

### Objective
Establish the project repository and organize the documentation structure.

### Work Completed
- Created the GitHub repository for the Enterprise Network Monitoring & Incident Response Lab.
- Initialized the local Git project.
- Organized project folders for architecture, configurations, incidents, monitoring, Wireshark analysis, scripts, and documentation.
- Practiced staging, committing, and pushing project files to GitHub.

### Outcome
Established the version-controlled foundation for the project and its technical documentation.

---

## Day 2 — Enterprise Network Topology

### Objective
Design a small enterprise network in Cisco Packet Tracer.

### Work Completed
- Created a simulated network topology.
- Added a router, switch, client devices, and an application server.
- Connected the devices to form a basic LAN.
- Established the initial network layout for subsequent configuration and testing.

### Outcome
Created the foundation for testing network connectivity and infrastructure services.

---

## Day 3 — IP Addressing and Connectivity

### Objective
Configure IP addressing and verify connectivity between network devices.

### Network Addressing Plan

| Device | IP address |
|---|---|
| Router / default gateway | 192.168.10.1 |
| Client 1 | 192.168.10.11 |
| Client 2 | 192.168.10.12 |
| Client 3 | 192.168.10.13 |
| Application server | 192.168.10.20 |
| Network | 192.168.10.0/24 |

### Work Completed
- Defined the `192.168.10.0/24` network.
- Assigned IP addresses to the router, clients, and application server.
- Configured the default gateway.
- Performed basic connectivity checks.

### Outcome
Established the addressing plan for the simulated enterprise LAN.

---

## Day 4 — DHCP Configuration

### Objective
Configure automatic IP address assignment for client devices.

### Work Completed
- Configured DHCP on the simulated router.
- Defined the network scope and default gateway.
- Tested DHCP address assignment on client devices.
- Verified that clients could obtain network configuration automatically.

### Outcome
Implemented automatic IP configuration, reducing the need for manual client addressing.

---

## Day 5 — DNS and Application Server

### Objective
Configure local name resolution and test application-server access.

### Work Completed
- Configured DNS for the lab environment.
- Created the hostname `app-server.lab.local`.
- Mapped the hostname to `192.168.10.20`.
- Enabled HTTP on the application server.
- Tested access to the server using its hostname and IP address.

### Outcome
Established local DNS resolution and application-server connectivity in the simulated network.

---

## Day 6 — Wireshark and Network Traffic Analysis

### Objective
Understand how network traffic can be inspected and analyzed during troubleshooting.

### Work Completed
- Documented network traffic analysis concepts and relevant protocol information.
- Reviewed how packet captures can help identify DNS queries, responses, and connectivity issues.
- Documented the role of Wireshark in network troubleshooting.

### Technical Note
The Cisco Packet Tracer simulation and Wireshark packet capture are separate activities. Packet Tracer simulation traffic should not be described as a real Wireshark capture unless an actual capture was performed.

### Outcome
Established a documented workflow for using packet analysis during network troubleshooting.

---

## Day 7 — Incident Response: DNS Resolution Failure

### Incident Reference
`INC-001-DNS-Resolution-Failure.md`

### Objective
Simulate and document a DNS resolution problem using a structured troubleshooting workflow.

### Incident Scenario
A client was unable to resolve an application-server hostname because of an incorrect DNS configuration.

### Investigation
- Checked hostname resolution.
- Compared hostname-based access with direct IP connectivity.
- Identified the incorrect DNS configuration on CLIENT-02.
- Corrected the DNS setting and retested resolution.

### Resolution
DNS resolution was restored after correcting the client configuration.

### Outcome
Practiced fault isolation, root-cause identification, remediation, and incident documentation.

---

## Day 8 — Ubuntu Monitoring Server Foundation

### Objective
Prepare a Linux server to support infrastructure monitoring.

### Environment
- Operating system: Ubuntu Server 26.04.1 LTS
- Virtualization platform: VMware
- Network interface: `ens33`
- Lab VM address: `192.168.196.129/24`

### Work Completed
- Prepared the Ubuntu Server virtual machine.
- Verified network configuration and internet connectivity.
- Checked available memory and disk capacity.
- Documented the monitoring-server foundation in this file.

### Outcome
Prepared the Linux environment for installing and configuring Zabbix.

---

## Day 9 — Zabbix Installation and Agent Failure Testing

### Objective
Install Zabbix and verify that it can monitor the Linux server and detect an agent failure.

### Environment
- Zabbix server: 7.0.32
- Zabbix Agent 2
- Database: MariaDB
- Web server: Apache
- Frontend access: local Zabbix web interface

### Work Completed
- Configured the official Zabbix 7.0 package repository.
- Installed Zabbix server, frontend, agent, database, and required supporting packages.
- Created and configured the Zabbix database.
- Completed the web frontend setup.
- Signed in to the Zabbix dashboard and changed the default administrator password.
- Verified communication between the Zabbix server and its agent.
- Checked the host's Latest data and monitoring items.

### Controlled Incident Test

**Incident:** Zabbix agent unavailable.

1. Stopped the Zabbix Agent 2 service.
2. Waited for Zabbix to detect the agent outage.
3. Verified that the agent-availability trigger entered the PROBLEM state.
4. Restarted the agent.
5. Verified that the problem recovered and the event was marked RESOLVED.

### Incident Documentation
`incidents/INC-002-zabbix-agent-unavailable.md`

### Outcome
Successfully demonstrated monitoring of a Linux host, detection of an agent failure, and recovery after restoring the service.

---

## Day 10 — CPU, Memory, and Filesystem Monitoring

### Objective
Verify resource monitoring in Zabbix and investigate filesystem discovery.

### Environment
- Zabbix server: 7.0.32
- Host: `Zabbix server`
- Linux template: `Linux by Zabbix agent`
- Monitoring agent: Zabbix Agent 2

### 1. CPU Monitoring

Verified the CPU utilization graph in Zabbix.

Example observations from the displayed one-hour graph:

- Average CPU utilization: approximately 2.88%.
- Maximum CPU utilization: approximately 19.66%.
- Minimum CPU utilization: approximately 0.52%.

These values represent the displayed graph at the time of observation, not permanent server performance measurements.

### 2. Memory Monitoring

Verified the Available memory graph and historical data.

Example observations from the displayed one-hour graph:

- Latest available memory: approximately 1000.07 MB.
- Average available memory: approximately 1005.44 MB.
- Minimum available memory: approximately 961.41 MB.
- Maximum available memory: approximately 1023.85 MB.

### 3. Filesystem Discovery Investigation

Investigated why individual filesystem disk-space metrics were not appearing in Latest data.

Work completed:
- Confirmed that the `Linux by Zabbix agent` template was linked to the host.
- Confirmed that the `Mounted filesystem discovery` rule was enabled.
- Inspected the seven filesystem item prototypes.
- Reviewed prototypes for available space, total space, used space, utilization, and inode monitoring.
- Manually tested the `Get filesystems` master item using the Zabbix frontend.
- Confirmed that the manual test returned filesystem JSON data.

### Outstanding Issue

Individual filesystem monitoring items were not visible when searching Latest data for `vfs.fs`. The routine collection status and discovery processing still need investigation.

### Next Steps
- Check the master item's normal collection status and latest value.
- Investigate the filesystem discovery results and dependent-item processing.
- Verify that disk-space metrics are created for the root filesystem (`/`).
- Confirm that free space and space utilization can be monitored.
- Build a practical Zabbix dashboard for CPU, memory, disk, and host availability.

### Outcome

CPU and memory graphs have been verified, and the filesystem discovery configuration and prototypes have been inspected. Filesystem monitoring remains in progress and is not yet considered complete.

---

## Current Project Status

| Component | Status |
|---|---|
| Git/GitHub project setup | Completed |
| Packet Tracer network topology | Completed |
| IP addressing and connectivity configuration | Completed |
| DHCP configuration | Completed |
| DNS and application-server setup | Completed |
| Network traffic analysis documentation | Completed |
| DNS incident report | Completed |
| Ubuntu monitoring server foundation | Completed |
| Zabbix installation and frontend setup | Completed |
| Zabbix agent failure and recovery test | Completed |
| CPU graph verification | Completed |
| Memory graph verification | Completed |
| Filesystem discovery troubleshooting | In progress |
| NOC-style monitoring dashboard | Planned |

## Future Enhancements

- Complete filesystem monitoring and validate disk-space metrics.
- Configure a consolidated Zabbix dashboard.
- Capture screenshots as evidence of monitoring and incident testing.
- Add additional monitored hosts when resources permit.
- Explore additional triggers and alerting scenarios.
- Improve the README with architecture diagrams, test evidence, and project results.
- Continue documenting changes using Git commits.

## Project Documentation Principles

- Record only tests and results that were actually observed.
- Keep incident reports in the `incidents/` directory.
- Keep monitoring setup and progress in this file.
- Store network configuration and architecture material in their existing directories.
- Use Git commits to preserve the project's development history.
