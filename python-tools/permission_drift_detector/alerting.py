"""
Alerting module for permission drift detection.
Mocks Email and Microsoft Teams notifications.
No external secrets or APIs required.
"""

from datetime import datetime

def format_alert(drift_items):
    timestamp = datetime.utcnow().isoformat()
    lines = [
        f"[{timestamp}] 🚨 Permission Drift Detected",
        "-" * 50
    ]
    for item in drift_items:
        lines.append(f"- {item}")
    return "\n".join(lines)

def send_email_alert(drift_items, recipient="security@example.com"):
    alert = format_alert(drift_items)
    print(f"[MOCK EMAIL → {recipient}]")
    print(alert)

def send_teams_alert(drift_items, webhook_url="https://example.webhook"):
    alert = format_alert(drift_items)
    print("[MOCK TEAMS MESSAGE]")
    print(alert)
