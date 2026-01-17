# Enterprise DBA Security Framework – Architecture

## Overview
This framework detects and reports permission drift across SQL Server environments using:
- Python-based drift detection
- Baseline JSON definitions
- Read-only queries
- Alert-first operational model

## Components
- Python Drift Detector
- Baseline Permission Store (JSON)
- Alerting Layer (Email / Teams)
- PowerShell Deployment & Rollback

## Execution Flow
1. Read baseline permissions
2. Collect current permissions (read-only)
3. Compare baseline vs current
4. Generate drift report
5. Send alerts (no auto-remediation by default)

## Design Principles
- Least privilege
- No secrets in repo
- Human-in-the-loop remediation
- Rollback-safe automation

