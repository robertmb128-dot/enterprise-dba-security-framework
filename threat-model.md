# Threat Model (STRIDE-lite)

This document provides a lightweight threat assessment for the
Enterprise DBA Security Framework.

---

## Assets
- Permission baselines
- Audit logs and evidence
- Execution context (SQL Server / Azure SQL)
- Automation scripts

---

## STRIDE Analysis

### Spoofing
**Threat:** Unauthorized execution context  
**Mitigation:**
- No embedded credentials
- Execution identity provided externally
- Supports Managed Identity patterns

---

### Tampering
**Threat:** Modification of baselines or scripts  
**Mitigation:**
- Baselines treated as trusted inputs
- Git version control
- Optional hash validation recommended

---

### Repudiation
**Threat:** Changes without accountability  
**Mitigation:**
- Pre-change audit capture
- Timestamped drift results
- Explicit remediation logging

---

### Information Disclosure
**Threat:** Leakage of sensitive data  
**Mitigation:**
- No secrets stored
- Placeholders only
- No outbound data exfiltration

---

### Denial of Service
**Threat:** Over-aggressive remediation  
**Mitigation:**
- Auto-remediation disabled by default
- No recursive or continuous enforcement loops
- Manual approval model assumed

---

### Elevation of Privilege
**Threat:** Automation granting excessive rights  
**Mitigation:**
- Framework only enforces approved policies
- No privilege escalation logic
- Explicit scope boundaries

---

## Residual Risk
Residual risk is low and primarily operational.
This framework prioritizes **safety and auditability** over autonomy.
