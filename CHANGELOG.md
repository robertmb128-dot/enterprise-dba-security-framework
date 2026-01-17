# Changelog

All notable changes to this project are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
and adheres to Semantic Versioning.

---

## [1.0.1] – Automation Safety & AG Awareness
### Fixed
- Drift detection scripts now return structured objects
- Deterministic drift evaluation in Deploy-All.ps1
- Parameterized hardcoded script paths

### Added
- Availability Group primary replica detection helper
- Azure SQL platform capability clarifications
- Timestamped drift result objects

### Changed
- Improved automation safety and execution predictability

### Removed
- Implicit pipeline output assumptions

---

## [1.0.0] – Initial Public Release
### Added
- Permission drift detection
- Login drift detection
- Optional auto-remediation
- AG-aware execution logic
- Azure SQL / Managed Instance support
- Deploy-All.ps1 and Rollback-All.ps1 orchestration
- Sentinel / Defender integration hooks
- NIST / ISO control mapping
