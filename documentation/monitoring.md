# Monitoring Foundation

## Objective

Prepare a Linux server that will later host the monitoring platform for the lab.

## Monitoring Platform

Zabbix will be used as the monitoring platform for this project.

## Monitoring Server

Hostname:

monitoring-server

Operating System:

Ubuntu Server LTS

## Purpose

The monitoring server will eventually monitor hosts and services in the lab and generate alerts when predefined conditions occur.

## Initial Verification

The following checks were performed:

- Verified hostname
- Verified network interface and IP address
- Tested IP connectivity
- Tested DNS resolution
- Updated the operating system
- Checked disk usage
- Checked memory usage
- Checked running processes

## Architecture

```text
Monitoring Server
       |
       | Monitoring
       ↓
Lab Hosts and Services