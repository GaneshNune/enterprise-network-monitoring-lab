# INC-003 — High CPU Utilization on Monitoring Server

## 1. Incident Overview

| Field | Details |
|---|---|
| Incident ID | INC-003 |
| Incident Title | High CPU Utilization on Zabbix Server |
| Severity | High |
| Category | Performance / Resource Utilization |
| Monitoring Tool | Zabbix 7.0.32 |
| Affected Host | Zabbix server |
| Status | Resolved |
| Incident Type | Simulated Lab Incident |

## 2. Alert Detection

Zabbix detected sustained high CPU utilization on the Ubuntu monitoring server.

A custom trigger was configured with the following expression:

`min(/Zabbix server/system.cpu.util,5m)>80`

Trigger configuration:
- CPU threshold: 80%
- Evaluation period: 5 minutes
- Severity: High

The built-in Linux monitoring template also detected CPU utilization above 90% for 5 minutes.

## 3. Investigation

The CPU utilization graph showed a significant increase in CPU usage.

Observed maximum CPU utilization: Approximately 99.99%.

The incident was reproduced intentionally using the Linux stress utility:

`stress --cpu 4 --timeout 600`

Four CPU workers were used to generate controlled CPU load.

## 4. Root Cause Analysis

Root cause: Intentional CPU load generation during the monitoring validation exercise.

The stress utility generated high CPU consumption, causing Zabbix to detect sustained CPU utilization above the configured thresholds.

## 5. Response and Recovery

1. Monitored CPU utilization through Zabbix Latest data and Graph.
2. Verified the custom CPU trigger entered PROBLEM state.
3. Confirmed the built-in Linux CPU alert was also generated.
4. Allowed the stress test to complete.
5. Verified that CPU utilization decreased.
6. Confirmed both alerts entered the resolved state.

## 6. Validation

- Custom CPU trigger successfully generated an alert.
- Built-in Linux CPU trigger successfully generated an alert.
- Both alerts displayed recovery timestamps in Zabbix.
- Incident status: Resolved.

## 7. Lessons Learned

- CPU monitoring helps identify resource utilization issues.
- Trigger thresholds and evaluation periods help detect sustained performance problems.
- Zabbix provides visibility into alert generation and recovery.
- Incident documentation supports investigation, root cause analysis and response tracking.

## 8. Final Outcome

Successfully simulated, detected, investigated and resolved a high CPU utilization incident using Zabbix 7.0.32.