# Framework Overview

This framework provides a structured approach to detecting permission drift
in SQL Server environments without introducing operational risk.

## What It Does
- Captures permission snapshots
- Compares against known-good baselines
- Surfaces drift for human review

## What It Does NOT Do
- Automatically change permissions
- Store credentials
- Execute unapproved remediation
