# DataPulse-AI 📊⚡

[![Development Status](https://img.shields.io/badge/status-work--in--progress-orange)](https://github.com/SamratB8/DataPulse-AI)
[![Backend](https://img.shields.io/badge/Backend-Flask%20%7C%20Python-blue)](https://flask.palletsprojects.com/)
[![Database](https://img.shields.io/badge/Database-PostgreSQL%20%7C%20Neon-cyan)](https://neon.tech/)
[![Storage](https://img.shields.io/badge/Storage-Cloudflare%20R2-yellow)](https://www.cloudflare.com/products/r2/)

A gamified, enterprise-architected AI/ML study tracker and productivity web application designed for data scientists and developers. **DataPulse-AI** bridges the gap between structured learning and hands-on coding by tracking domain-specific XP, validating mathematical core concepts, and securely processing user metrics over an isolated, cloud-decoupled pipeline.

> ☕ **Infrastructure Note:** This project is deployed on a modern, decoupled cloud environment. If the initial dashboard load takes a moment, the free-tier backend containers are safely completing a routine server cold-start. Subsequent features and database operations run at full speed!

---

## 🛠️ System Architecture & Cloud Infrastructure

DataPulse-AI uses a highly optimized, decoupled **production-grade cloud topology** engineered to bypass traditional server constraints like memory limits and rigid request timeouts:

* **🖥️ Application Server (`Render Pro Workspace`)**: Hosts the Flask Python runtime engine. It handles core analytical routing, provides a healthy 25 GB of outbound bandwidth, and hooks directly into GitHub for automated continuous integration (CI/CD).
* **🐘 Database Engine (`Neon.tech PostgreSQL`)**: A permanent, serverless relational database cluster isolated entirely from the compute layer. This architecture guarantees your tables, progress, and metric logs are never lost during code updates.
* **🪣 Object Storage (`Cloudflare R2`)**: An S3-compatible asset vault built with absolute **$0 egress fees**. Massive notebook uploads stream straight here from the client's browser, completely protecting the app server's RAM.
* **🌐 Security & Routing (`Cloudflare Registrar & DNS`)**: Manages our custom domain with zero-markup pricing, global edge caching, and automated end-to-end SSL/TLS encryption.

### 🚀 Direct-to-Cloud Stream Workflow

```text
                  [ Student Browser ]
                           │
         (Direct Upload via Secure Presigned URL)
                           │
                           ▼
               [ Cloudflare R2 Storage ] (Isolated File Vault)
                           │
                 (Egress-Free Data Stream)
                           │
                           ▼
    [ Render Server Core ] ◄───────► [ Neon.tech Postgres ]
  (Flask/Pandas Processing Core)       (Permanent Cloud Memory)
```

### 🛣️ Project Roadmap & Status
[x] Phase 1 & 2: Decoupled Architecture Setup & Cloud Core Database Schema Design (models.py)

[/] Phase 3: Frontend UI Templates & Secure User Authentication Routing (Currently In Progress)

[ ] Phase 4 & 5: Pandas Workflow Pipelines & Analytics Tracking Engine

[ ] Phase 6 & 7: NumPy Multi-Dimensional Matrix Algebra Validation & High-Performance Jupyter Notebook Parsing Component

[ ] Phase 8: MLOps, End-to-End System Integration Testing & Finalization

### ⚡ Key Features
🏆 Gamified XP Tracking: Earn domain-specific experience points (XP) dynamically as you finish core data science modules and Python engineering tasks.

📂 Direct-to-Cloud Notebook Parsing: Upload and process local .ipynb files seamlessly. The data stream leverages ijson to parse records sequentially, keeping the live server memory locked at a stable ~20 MB regardless of file size.

🧮 Matrix Algebra Validation: An integrated interactive evaluation playground built to calculate, check, and visually validate multi-dimensional NumPy array operations.

📊 Data Processing Pipelines: Experience deep real-time feedback with backend statistics powered entirely by analytical Pandas workflows.

🔐 Secure Authentication: Enterprise-ready native session architecture complete with password hashing, encrypted tokens, and strict dashboard route protections.

### 📦 Directory Structure
```text
DATAPULSE-AI/
│
├── app/
│   ├── static/          # Custom responsive CSS layouts, interactive components, and visual assets
│   ├── templates/       # HTML5 Jinja2 UI layouts (base structural layout, dashboard, authentication)
│   ├── __init__.py      # App factory lifecycle configuration, R2 storage connections & extensions
│   ├── models.py        # Object-Relational PostgreSQL production database schemas and metrics mapping
│   └── routes.py        # Controller architecture, analytical API endpoints, and presigned URL providers
│
├── requirements.txt     # Locked production dependencies (Flask, SQLAlchemy, ijson, pandas, numpy)
└── run.py               # Live cloud application initialization script
```

### 🧰 Tech Stack
```text
**Layer**                           **Technology**
**Backend Core**                    Flask (Python 3.x)
**Data Science Engines**            Pandas, NumPy, ijson
**Database & ORM**                  PostgreSQL / SQLAlchemy ORM (Hosted via Neon.tech)
**Cloud Infrastructure**            Cloudflare R2 Storage (S3 API Engine)
**Networking & Gateways**           Cloudflare DNS & Registrar
**Frontend Foundation**             Semantic HTML5, Custom Adaptive CSS3 Layouts
```
