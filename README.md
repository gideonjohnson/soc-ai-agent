# SOC AI Agent

A lightweight AI-assisted log parser and triage tool for cybersecurity monitoring.

##  Features
- Parses raw security logs
- Analyzes entries using LLM (GPT)
- Maps to MITRE ATT&CK framework
- Designed for SOC Level 1 triage automation

##  Current Limitations
- No real-time log watching
- No Wazuh/Splunk/Elastic integration yet
- No syslog/Filebeat/API ingestion

## Coming Soon
- Real-time file monitoring
- SIEM (Wazuh) API support
- Lightweight Flask API for log ingestion

## How to Run

```bash
python src/agent/log_parser.py
