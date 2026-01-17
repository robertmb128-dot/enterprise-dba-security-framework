enterprise-dbre-framework/
├─ README.md
├─ LICENSE
├─ SECURITY.md
├─ CHANGELOG.md
├─ CONTRIBUTING.md
├─ roadmap.md
├─ python-tools/
│   ├─ permission_drift_detector/
│   │   ├─ permission_drift_detector.py
│   │   └─ README.md
│   ├─ incident_snapshot/
│   │   ├─ incident_snapshot.py
│   │   └─ README.md
│   └─ cloud_login_monitor/
│       ├─ cloud_login_monitor.py
│       └─ README.md
├─ sql-scripts/
│   ├─ Deploy-Security.ps1
│   ├─ Rollback-Security.ps1
│   ├─ Deploy-All.ps1
│   └─ Rollback-All.ps1
├─ docs/
│   ├─ architecture.pdf
│   ├─ threat_model.md
│   ├─ interview_questions.md
│   ├─ mentoring.md
│   ├─ failures_lessons.md
│   └─ cloud_walkthrough.md
└─ .gitignore

# Repository Structure

This document explains the layout of the repository and the purpose of each directory/file.

## Root
- README.md: Entry point and framework overview
- LICENSE: MIT license
- SECURITY.md: Vulnerability reporting & scope
- CHANGELOG.md: Version history
- CONTRIBUTING.md: Contribution rules
- roadmap.md: Planned features and improvements

## docs/
Contains high-level documentation:
- architecture.md
- threat-model.md
- interviews.md
- mentoring.md
- failures-lessons.md
- auditor-qna.md

## python-tools/permission_drift_detector/
Contains Python implementation:
- permission_drift_detector.py
- alerting.py
- baseline_example.json
- current_permissions_example.json
- README.md

## sql-scripts/
Contains PowerShell orchestration scripts:
- Deploy-All.ps1
- Rollback-All.ps1
