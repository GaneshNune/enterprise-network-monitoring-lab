# INC-001 — CLIENT-02 DNS Resolution Failure

## Incident Summary

CLIENT-02 was unable to access the application server using its hostname.

## Symptom

The application server was reachable using its IP address:

192.168.10.20

However, the hostname:

app-server.lab.local

could not be resolved.

## Investigation

The following checks were performed:

1. Verified CLIENT-02 IP configuration.
2. Tested connectivity to APP-SRV using its IP address.
3. Tested connectivity using the application server hostname.
4. Checked DNS configuration using `ipconfig /all`.
5. Compared CLIENT-02 DNS configuration with CLIENT-01.

## Findings

IP connectivity to APP-SRV was successful.

Hostname resolution failed because CLIENT-02 was configured with an incorrect DNS server:

192.168.10.250

The correct DNS server was:

192.168.10.20

## Root Cause

Incorrect DNS server configuration on CLIENT-02.

## Resolution

CLIENT-02 was returned to DHCP configuration so that it received the correct DNS server address.

## Validation

The following tests were successful after remediation:

- Ping to APP-SRV IP address
- DNS hostname resolution
- HTTP access using `app-server.lab.local`

## Lessons Learned

Successful IP connectivity does not necessarily mean DNS is functioning correctly. Testing both IP-based and hostname-based access helps isolate DNS-related issues.