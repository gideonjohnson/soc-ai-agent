import openai
import os

def analyze_log(log_entry):
    openai.api_key = os.getenv("OPENAI_API_KEY")  # Make sure it's in your .env and loaded

    prompt = f"""
You are a SOC Level 1 Analyst AI. Analyze this security log:

"{log_entry}"

Your job:
1. Determine threat level (low, medium, high)
2. Recommend an action
3. Map it to a MITRE ATT&CK tactic and technique

Respond in this JSON format:
{{
  "threat_level": "...",
  "recommended_action": "...",
  "mitre_tactic": "...",
  "mitre_technique": "...",
  "mitre_technique_id": "..."
}}
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=500
        )
        message = response['choices'][0]['message']['content']
        return eval(message)  # Or better: use json.loads(message) if formatted correctly
    except Exception as e:
        print(f"❌ GPT Error: {e}")
        return {
            "threat_level": "unknown",
            "recommended_action": "Review manually",
            "mitre_tactic": "unknown",
            "mitre_technique": "unknown",
            "mitre_technique_id": "N/A"
        }
