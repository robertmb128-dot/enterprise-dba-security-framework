import json
import logging
from datetime import datetime
from pathlib import Path

OUTPUT_DIR = "output"

FILES = {
    "permission_baseline": "baseline_example.json",
    "permission_current": "current_permissions_example.json",
    "login_baseline": "login_baseline_example.json",
    "login_current": "current_logins_example.json"
}

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def load_json(path):
    with open(path, "r") as f:
        return json.load(f)

def normalize(obj):
    return json.dumps(obj, sort_keys=True)

def diff_sets(baseline, current):
    base = {normalize(x) for x in baseline}
    curr = {normalize(x) for x in current}
    return {
        "added": [json.loads(x) for x in curr - base],
        "removed": [json.loads(x) for x in base - curr]
    }

def write_report(name, drift):
    Path(OUTPUT_DIR).mkdir(exist_ok=True)
    ts = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    out = Path(OUTPUT_DIR) / f"{name}_drift_{ts}.json"
    with open(out, "w") as f:
        json.dump(drift, f, indent=2)
    logging.info(f"{name} drift report written: {out}")

def main():
    logging.info("Starting security drift detection")

    # --- Permission Drift ---
    perm_base = load_json(FILES["permission_baseline"])
    perm_curr = load_json(FILES["permission_current"])
    perm_drift = diff_sets(perm_base, perm_curr)

    if any(perm_drift.values()):
        logging.warning("Permission drift detected")
        write_report("permission", perm_drift)
    else:
        logging.info("No permission drift detected")

    # --- Login Drift ---
    login_base = load_json(FILES["login_baseline"])
    login_curr = load_json(FILES["login_current"])
    login_drift = diff_sets(login_base, login_curr)

    if any(login_drift.values()):
        logging.warning("Login drift detected")
        write_report("login", login_drift)
    else:
        logging.info("No login drift detected")

    # --- OPTIONAL AUTO-REMEDIATION (INTENTIONALLY DISABLED) ---
    """
    if AUTO_REMEDIATE:
        remediate_permissions(perm_drift)
        remediate_logins(login_drift)
    """

if __name__ == "__main__":
    main()
