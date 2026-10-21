 # INC-002 — Zabbix Agent Unavailable

## Incident Summary

- **Incident ID:** INC-002
- **Category:** Monitoring and Availability
- **Affected host:** Zabbix server
- **Severity:** Average
- **Status:** Resolved
- **Detection platform:** Zabbix 7.0.32

## Objective

Validate that Zabbix detects an unavailable monitoring agent, generates a problem event, and records recovery after the agent service is restored.

## Test Procedure

1. Confirmed that the Zabbix server host was enabled and available.
2. Verified that the trigger `Linux: Zabbix agent is not available` was enabled and initially in the OK state.
3. Intentionally stopped the Zabbix Agent 2 service to simulate an availability incident.
4. Observed the problem event in **Monitoring → Problems**.
5. Restarted Zabbix Agent 2.
6. Verified that the event changed to RESOLVED.

## Detection Evidence

Zabbix generated a problem for the trigger:

`Linux: Zabbix agent is not available`

The event appeared with Average severity and a PROBLEM status.

## Resolution

Restarted the Zabbix Agent 2 service and allowed monitoring checks to resume.

## Verification

The Zabbix Problems page subsequently showed the event as RESOLVED, with a recorded duration of approximately three minutes.

## Result

**PASS** — The controlled test demonstrated detection of agent unavailability and subsequent recovery.

## Lessons Learned

- Monitoring triggers can detect failures in the monitoring agent.
- An alert must be verified against the affected host and trigger.
- Recovery verification is an essential part of incident handling.
- Incident evidence should include the problem state, recovery state, and corrective action.

## Evidence

Capture and retain screenshots showing:
- The trigger in the OK state before testing.
- The PROBLEM event during the test.
- The RESOLVED event after recovery.
