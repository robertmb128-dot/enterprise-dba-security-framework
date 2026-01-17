# Permissions Module

This directory contains the **permission modeling and analysis layer** of the framework.

It supports two data sources:
1. Static JSON files (demo / testing)
2. Read-only SQL Server permission snapshots (enterprise usage)

## Purpose

- Normalize SQL Server permissions into a reviewable format
- Detect drift, over-privilege, and policy violations
- Enable approval-based remediation workflows

## Contents

- `schemas/` — JSON schema definitions
- `samples/` — Example permission snapshots
- `policies/` — Policy rules and validation logic

## Design Notes

- No live database connections
- No mutation of permissions
- All outputs are human-reviewable artifacts

This module is intentionally decoupled from remediation.
