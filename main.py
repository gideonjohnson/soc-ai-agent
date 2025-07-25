import json
import openai
from openai import OpenAI
from rich import print

# === Step 1: Load config ===
with open("config.json", "r") as cfg:
    config = json.load(cfg)

client = OpenAI(api_key=config["openai_api_key"])
gpt_model = config.get("gpt_model", "gpt-3.5-turbo")

# === Step 2: Load logs ===
log_file_path = "logs/test_logs.json"
try:
    with open(log_file_path, "r") as file:
        logs = json.load(file)
except FileNotFoundError:
    print("[bold red]Log file not found. Check the path.[/bold red]")
    exit()

# === Step 3: Load prompt template ===
with open("prompts/triage_prompt.txt", "r") as file:
    base_prompt = file.read()

# === Step 4: Define function to send to GPT ===
def analyze_log_with_gpt(log_entry):
    # Mock GPT analysis for now
    simulated_response = {
        "threat_level": "medium",
        "recommended_action": "Block the IP address temporarily and monitor traffic.",
        "notes": f"Simulated analysis based on log message: {log_entry.get('message', '')}"
    }
    return simulated_response

# === MITRE ATT&CK Mapping (very simple) ===
mitre_map = {
    "failed login": {"tactic": "Credential Access", "technique": "T1110 – Brute Force"},
    "port scan": {"tactic": "Discovery", "technique": "T1046 – Network Service Scanning"},
    "malware": {"tactic": "Execution", "technique": "T1204 – User Execution"}
}

# === Step 5: Process each log ===
for i, log in enumerate(logs, start=1):
    print(f"\n[bold blue]🔍 Analyzing Log #{i}[/bold blue]")
    print("[bold yellow]Log Summary:[/bold yellow]", log.get("message", "No message field."))

    result = analyze_log_with_gpt(log)

    # MITRE ATT&CK matching (inside the loop)
    message = log.get("message", "").lower()
    for keyword, mapping in mitre_map.items():
        if keyword in message:
            print(f"🎯 MITRE ATT&CK: {mapping['tactic']} → {mapping['technique']}")
            break

    if result:
        print("[bold green]✅ GPT Decision:[/bold green]")
        print(json.dumps(result, indent=2))
    else:
        print("[bold red]❌ Failed to analyze log.[/bold red]")
