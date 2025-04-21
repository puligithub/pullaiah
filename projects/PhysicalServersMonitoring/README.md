# Physical Servers Monitoring

**Title:** Physical Servers (DELL, HP & LENOVO) Monitoring  
**Objective:** End‑to‑end, agentless monitoring of physical servers with a centralized Splunk dashboard and automated ServiceNow incident creation.  
**Business Impact:** Reduced Mean Time to Repair (MTTR) by **80%**, enabling proactive hardware fault remediation and improved customer satisfaction.

---

**> IBM ESA Container runs in GKE, collects hardware metrics via SNMP.

> Splunk Dashboard visualizes health and triggers alerts.

> Python Script ingests alerts and auto‑creates ServiceNow incidents.

> Multi‑Zone GKE for high availability and region‑spanning coverage.**

---
 **Tools & Technologies** 

> IBM ESA (beta container image)

> Google Kubernetes Engine (GKE) – multi‑zone clusters

> SNMP – agentless polling across platforms

> Splunk Infrastructure Monitoring – centralized dashboard & alerting

> ServiceNow API – incident creation via Python scripts

> Jenkins – CI/CD for image scanning & deployment

> SRE Practices – SLO tracking, MTTR metrics, retrospectives

---
  
## 📋 Agile Process

We followed a **Scrum‑style Agile** approach over a **12‑month** engagement, delivering in two‑week sprints:

1. **Sprint Planning & Backlog Grooming**  
   - Refined user stories for SNMP integration, dashboarding, and incident workflows.  
2. **Daily Stand‑ups**  
   - Coordinated Unix, Windows, and VMware platform teams; addressed blockers in real time.  
3. **Sprint Reviews & Demos**  
   - Showcased incremental capabilities to stakeholders; collected feedback for the next iteration.  
4. **Retrospectives**  
   - Improved CI/CD pipelines, vendor collaboration, and alert‑tuning processes.

---

## 🗓️ Project Timeline

| Sprint  | Dates    | Key Deliverables                              |
|:-------:|----------|-----------------------------------------------|
| 1–2     |NA      | GKE cluster provisioning; IBM ESA beta deploy |
| 3–6     | JNA    | SNMP polling; Splunk dashboard MVP            |
| 7–10    | NA     | ServiceNow API scripts; incident routing      |
| 11–12   | NA     | Multi‑region rollout; performance hardening   |

> _Each sprint spanned two weeks, enabling rapid feedback and continuous improvement._

---

## 🛠️ Tools & Technologies

We list only the core tools to keep the README concise and recruiter‑friendly—per recommended “Prerequisites” and “Tools” sections :contentReference[oaicite:1]{index=1}:  
- **IBM ESA** (beta container image)  
- **Google Kubernetes Engine (GKE)** – multi‑zone clusters  
- **SNMP** – agentless polling across platforms  
- **Splunk Infrastructure Monitoring** – centralized dashboard & alerting  
- **ServiceNow API** – incident creation via Python scripts  
- **Jenkins** – CI/CD pipelines for image scanning & deployment  
- **Languages & Scripting:** Python, Shell, YAML  
- **SRE Practices:** SLO tracking, MTTR metrics, retrospectives :contentReference[oaicite:2]{index=2}

---

## 📁 File Structure

A clear, top‑level layout guides contributors—mirroring industry conventions :contentReference[oaicite:3]{index=3}:

├── README.md ← Project overview (this file) ├── docs/ ← Architecture & Agile process details │ ├── architecture.md │ └── agile_process.md ├── k8s/ ← Kubernetes manifests & configs │ └── deployment.yaml ├── scripts/ ← Automation & incident logic │ └── create_incident.py └── LICENSE ←

---

## 🔥 Highlights & Importance

> **IMPORTANT**  
> - **MTTR ↓ 80%:** Automated alerting & incident creation cut hardware repair times from 10 hrs to < 2 hrs.  
> - **Agentless SNMP:** Supported Dell, HP, and Lenovo servers without installing host agents.  
> - **Multi‑Region HA:** GKE multi‑zone clusters ensure failover and resilience.  
> - **Vendor Collaboration:** Partnered with IBM ESA beta team for product hardening and feature stabilization.

---

## ⚙️ Implementation

This section describes **how we built** the system—following “write your README before your code” to clarify scope :contentReference[oaicite:4]{index=4}:  
1. **Provision GKE cluster** with multi‑zone nodes and network policies.  
2. **Deploy IBM ESA** container via Helm chart; configure SNMP targets for Dell, HP, Lenovo servers.  
3. **Integrate with Splunk** using HTTP Event Collector for real‑time dashboards and alerts.  
4. **Automate ServiceNow incidents** by triggering Python scripts on Splunk alerts, ensuring correct assignment & logging.  
5. **Harden container images** in CI/CD (Jenkins) with vulnerability scanning and automated rollbacks.  
6. **Extend cross‑region** coverage by replicating Helm releases and maintaining a unified config repository. :contentReference[oaicite:5]{index=5}

---

## 🚀 Usage

Quickstart commands—modeled after “Getting Started” examples—to get you up and running in minutes :contentReference[oaicite:6]{index=6}:

```bash
# 1. Deploy IBM ESA on GKE
kubectl apply -f k8s/deployment.yaml

# 2. Configure Splunk HEC
#    - Set `SPLUNK_HEC_TOKEN` & `SPLUNK_HEC_URL` in ESA config

# 3. Run incident creation script
python3 scripts/create_incident.py --alert-id <ALERT_ID>

# 4. View dashboards
#    - Login to Splunk → Dashboards → “Physical Servers Health”
```
---

## 🏗️ Architecture & Design

```mermaid
flowchart LR
  subgraph "GKE Cluster"
    ESA["IBM ESA Container"]
    SNMP["SNMP Polling"]
    ESAdash["Splunk Dashboard"]
    ESASNOW["ServiceNow API Script"]
    ESA -->|SNMP Polling| SNMP
    ESA --> ESAdash
    ESA --> ESASNOW
  end

  subgraph "Physical Servers"
    DELL["DELL Server"]
    HP["HP Server"]
    LENOVO["LENOVO Server"]
  end

  DELL <--->|SSH, SNMP, Logs via HTTPS| ESA
  HP   <--->|SSH, SNMP, Logs via HTTPS| ESA
  LENOVO <--->|SSH, SNMP, logs via HTTPS| ESA

  subgraph "On‑Estate Proxy"
    InternalProxy["Internal Proxy Server"]
  end

  ESA -->|Incident events Forwarding| ESAdash
  ESA -->| Logs | InternalProxy
  ESASNOW <-->|API Calls| ESA
  SNMP -->|HW events & Alerts Forwarding| InternalProxy

  subgraph "IBM Proxy & Portal"

    IBMProxy["IBM Proxy"]
    IBMPortal["IBM Vendor Portal"]
    IBMProxy --> IBMPortal
  end

  InternalProxy -->|HTTPS| IBMProxy
