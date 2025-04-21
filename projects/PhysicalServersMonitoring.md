This README documents the Physical Servers Monitoring project, executed over a 12‑month Agile initiative with iterative two‑week sprints for backlog‑driven development and continuous improvement 
Atlassian
Atlassian
. It follows GitHub README best practices, leveraging Markdown extended syntax for clear organization, highlights, and “important” callouts 
Informa TechTarget
Markdown Guide
.

Overview
Title: Physical Servers (DELL, HP & LENOVO) Monitoring

Objective: End‑to‑end, agentless monitoring of physical servers with a centralized Splunk dashboard and automated ServiceNow incident creation 
GitHub
.

Business Impact: Reduced mean time to repair (MTTR) by 80%, enabling proactive hardware fault remediation and improved customer satisfaction.

Agile Process
This project adhered to Scrum‑style Agile methodologies, featuring:

Sprint Planning & Backlog Grooming every two weeks to refine user stories and prioritize hardware‑monitoring features 
Atlassian
.

Daily Stand‑ups to synchronize cross‑functional teams (Unix, Windows, VMware) and address blockers immediately 
Atlassian
.

Sprint Reviews & Demos to showcase incremental monitoring capabilities, gather stakeholder feedback, and adjust the roadmap 
Atlassian
.

Retrospectives to continuously improve processes, including CI/CD pipeline tuning and vendor collaboration 
Reddit
.

Project Timeline

Sprint #	Dates	Deliverables
1–2	Apr – May 2023	GKE cluster setup, IBM ESA beta deployment
3–6	Jun – Aug 2023	SNMP integration, Splunk dashboard creation
7–10	Sep – Nov 2023	ServiceNow API scripting, incident flows
11–12	Dec 2023 – Mar 2024	Multi‑region rollout, performance hardening
Each sprint lasted two weeks, aligned with Agile best practices for rapid feedback and iteration 
Atlassian
.		
Highlights & Importance
[!IMPORTANT]

MTTR Reduced by 80% through automated alerting and case creation 
Hatica
.

Agentless SNMP Monitoring enabled cross‑platform support without host‑OS dependencies 
Enterprise Modernization Firm
.

Multi‑Region High Availability using GKE multi‑zone clusters for resilience 
Codecademy
.

Continuous Vendor Collaboration in beta testing IBM ESA to stabilize critical features 
WIRED
.

Architecture & Design
mermaid
Copy
Edit
flowchart LR
    Subgraph GKE Cluster
      ESA[IBM ESA Container] --> SNMP[SNMP Polling]
      ESA --> Dashboard[Splunk Dashboard]
      ESA --> ServiceNow[Python Script ➔ ServiceNow]
    end
    User[IT Ops Team] --> Dashboard
    Vendor[Hardware Vendor] --> ServiceNow
The agentless IBM ESA container runs within a GKE multi‑zone cluster, collecting hardware health via SNMP and pushing alerts to Splunk, which triggers Python‑based ServiceNow incidents 
Atlassian
GitHub Docs
.

Tools & Technologies
IBM ESA (beta container image)

Google Kubernetes Engine (GKE) – multi‑zone clusters 
Codecademy

SNMP – agentless hardware polling 
Atlassian

Splunk Infrastructure Monitoring – centralized dashboard 
Reddit

ServiceNow API – incident creation via Python scripts 
GitHub

Jenkins – CI/CD for image scanning and deployments

SRE Practices – SLO tracking, MTTR metrics, retrospectives 
Atlassian

File Structure
text
Copy
Edit
README.md               ← This file  
docs/
  architecture.md       ← Detailed design  
  agile_process.md      ← Sprint details & retrospectives  
scripts/
  create_incident.py    ← ServiceNow integration  
k8s/
  deployment.yaml       ← GKE manifests  
A lightweight root README for onboarding; extended docs live in /docs 
GitHub Docs
.

Usage
bash
Copy
Edit
# Deploy IBM ESA on GKE
kubectl apply -f k8s/deployment.yaml

# Configure Splunk HTTP Event Collector
# ...

# Run incident creation script
python3 scripts/create_incident.py --alert-id <ALERT_ID>
Replace placeholders with your cluster and Splunk settings.

Contributing
We follow “write your README before your code” to maintain clarity on user needs 
WIRED
.

Fork the repo and create a feature branch.

Write tests and update docs (docs/).

Submit a pull request and link it to the relevant sprint in the backlog.

Contact

For questions, reach out to Pullaiah Gavvala at puli.gavvala@gmail.com
