import json
import openai
from openai import OpenAI
from rich import print
from rich.table import Table

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
    prompt = base_prompt.replace("{{log_entry}}", json.dumps(log_entry, indent=2))
    
    try:
        response = client.chat.completions.create(
            model=gpt_model,
            messages=[
                {"role": "system", "content": "You are a SOC Level 1 Analyst AI assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )
        result_text = response.choices[0].message.content.strip()
        return json.loads(result_text)
    
    except Exception as e:
        print(f"[bold red]❌ GPT Error:[/bold red] {e}")
        return None



# === Step 5: Process each log ===
for i, log in enumerate(logs, start=1):
    print(f"\n[bold blue]🔍 Analyzing Log #{i}[/bold blue]")
    print("[bold yellow]Log Summary:[/bold yellow]", log.get("message", "No message field."))

    result = analyze_log_with_gpt(log)

    if result:
        print("[bold green]✅ GPT Decision:[/bold green]")
        print(json.dumps(result, indent=2))
    else:
        print("[bold red]❌ Failed to analyze log.[/bold red]")
