# Auto-Remediation Framework

This directory documents the **philosophy, guardrails, and decision logic**
behind safe database auto-remediation.

⚠️ No scripts in this directory perform automatic changes.

## Philosophy

- Detection does not imply correction
- Automation proposes, humans approve
- Rollback must always be possible

## What This Is

- Decision matrices
- Safety constraints
- Approval workflows

## What This Is Not

- Blind self-healing
- Autonomous permission changes
- Write-enabled automation

This framework is intentionally conservative by design.
