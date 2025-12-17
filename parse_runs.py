import json
import csv
from datetime import datetime

# Cargar ejecuciones
with open("runs.json", "r") as f:
    data = json.load(f)

runs = data.get("workflow_runs", [])

# Cargar JSON extra
with open("extra_data.json", "r") as f:
    extra = json.load(f)

# Nombre de archivo CSV de salida
csv_file = "runs_report.csv"

with open(csv_file, mode="w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "workflow_name", "branch", "status", "conclusion",
        "duration", "owner", "priority", "created_at"
    ])

    for run in runs:
        name = run["name"]
        status = run["status"]
        conclusion = run["conclusion"]
        branch = run["head_branch"]
        created = run["created_at"]
        duration = "N/A"

        if run["updated_at"] and run["created_at"]:
            start = datetime.fromisoformat(run["created_at"].replace("Z", ""))
            end = datetime.fromisoformat(run["updated_at"].replace("Z", ""))
            duration = str(end - start)

        owner = extra.get(name, {}).get("owner", "")
        priority = extra.get(name, {}).get("priority", "")

        writer.writerow([name, branch, status, conclusion, duration, owner, priority, created])

print(f"✅ CSV generado: {csv_file}")
