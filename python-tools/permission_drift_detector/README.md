[README.md](https://github.com/user-attachments/files/24689453/README.md)
## Permission Source Options

This module supports two permission sources:

1. Static JSON files (public demo / testing)
2. Read-only SQL Server snapshots (enterprise usage)

The included T-SQL script generates a permission snapshot
that can be exported and reviewed without granting this
repository direct database access.

## Safety Guarantees

- No write operations
- No direct database connections by default
- No secrets or credentials stored
- Designed for human review and approval

## Auto-Remediation Philosophy

This framework intentionally disables automatic remediation by default.

Remediation actions (permission revocation, login disablement)
must be:
- Explicitly enabled
- Logged
- Reviewed
- Reversible

This reflects real enterprise security controls and change management.

### Optional Remediation (Disabled by Default)

This tool includes commented remediation logic for revoking unauthorized permissions.
Remediation must be explicitly enabled and tested in non-production environments first.
