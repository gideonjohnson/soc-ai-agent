# SOC AI Agent  

A lightweight AI-assisted log parser and triage tool for cybersecurity monitoring.  

## Features (Current)  
- Parses raw security logs (`.json` format)  
- Analyzes entries using a **simulated GPT engine** (no live API key required)  
- Maps events to **MITRE ATT&CK tactics and techniques**  
- Outputs triage decisions in an analyst-friendly format  
- Designed for **SOC Level 1 triage automation**  

## Current Limitations  
- No real-time log watching yet (works on saved log files only)  
- No Wazuh/Splunk/Elastic SIEM integration  
- No syslog/Filebeat/API ingestion yet  

## In the works  
- Real-time file monitoring  
- SIEM (Wazuh) API support  
- Lightweight Flask API for remote log ingestion  
- Direct GPT integration (when API keys are configured)  

## How to Run  
```bash
python main.py
