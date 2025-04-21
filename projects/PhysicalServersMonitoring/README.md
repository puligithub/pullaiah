# Physical Servers Monitoring

**Title:** Physical Servers (DELL, HP & LENOVO) Monitoring  
**Objective:** End‑to‑end, agentless monitoring of physical servers with a centralized Splunk dashboard and automated ServiceNow incident creation.  
**Business Impact:** Reduced Mean Time to Repair (MTTR) by **80%**, enabling proactive hardware fault remediation and improved customer satisfaction.

---

> IBM ESA Container runs in GKE, collects hardware metrics via SNMP.

> Splunk Dashboard visualizes health and triggers alerts.

> Python Script ingests alerts and auto‑creates ServiceNow incidents.

> Multi‑Zone GKE for high availability and region‑spanning coverage.

 **Tools & Technologies** 

> IBM ESA (beta container image)

> Google Kubernetes Engine (GKE) – multi‑zone clusters

> SNMP – agentless polling across platforms

> Splunk Infrastructure Monitoring – centralized dashboard & alerting

> ServiceNow API – incident creation via Python scripts

> Jenkins – CI/CD for image scanning & deployment

> SRE Practices – SLO tracking, MTTR metrics, retrospectives

**File structure**

README.md               ← This file
docs/
  architecture.md       ← Detailed architecture diagrams
  agile_process.md      ← Sprint backlogs & retrospectives
scripts/
  create_incident.py    ← ServiceNow integration logic
k8s/
  deployment.yaml       ← GKE manifests & configs
  
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

## 🔥 Highlights & Importance

> **IMPORTANT**  
> - **MTTR ↓ 80%:** Automated alerting & incident creation cut hardware repair times from 10 hrs to < 2 hrs.  
> - **Agentless SNMP:** Supported Dell, HP, and Lenovo servers without installing host agents.  
> - **Multi‑Region HA:** GKE multi‑zone clusters ensure failover and resilience.  
> - **Vendor Collaboration:** Partnered with IBM ESA beta team for product hardening and feature stabilization.

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
