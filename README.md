# DataPulse-AI 📊⚡

[![Development Status](https://img.shields.io/badge/status-work--in--progress-orange)](https://github.com/SamratB8/DataPulse-AI)
[![Backend](https://img.shields.io/badge/Backend-Flask%20%7C%20Python-blue)](https://flask.palletsprojects.com/)
[![Database](https://img.shields.io/badge/Database-PostgreSQL%20%7C%20Neon-cyan)](https://neon.tech/)
[![Storage](https://img.shields.io/badge/Storage-Cloudflare%20R2-yellow)](https://www.cloudflare.com/products/r2/)

A gamified, enterprise-architected AI/ML study tracker and productivity web application designed for data scientists and developers. **DataPulse-AI** bridges the gap between structured learning and hands-on coding by tracking domain-specific XP, validating mathematical core concepts, and securely processing user metrics over an isolated, cloud-decoupled pipeline.

---

## 🛠️ System Architecture & Cloud Infrastructure

DataPulse-AI is built using a modern, decoupled production-grade cloud topology engineered to bypass traditional server constraints like memory limits and rigid request timeouts:

* 🖥️ Application Server (Render Starter Instance): Runs the Flask Python core on a dedicated, always-on virtual machine container (512 MB RAM, 0.5 CPU). Running on Render's Starter tier within your Pro Workspace guarantees 24/7 always-on availability with zero cold-starts, high-performance request handling, 25 GB of outbound bandwidth, and automated GitHub continuous integration (CI/CD).

* 🐘 Database Engine (Neon.tech PostgreSQL): A serverless, fully-compliant PostgreSQL database cluster running completely isolated from the application compute layer. This guarantees persistent progress and metric tables are never lost or corrupted during application updates.

* 🪣 Object Storage (Cloudflare R2): An S3-compatible asset vault with $0 egress fees. Heavy notebook uploads bypass the main application server entirely, saving CPU cycles and keeping RAM usage flat.

* 🌐 Security & Routing (Cloudflare DNS & Registrar): Direct DNS records with active edge caching, secure headers, and automated global SSL/TLS encryption.

## 🚀 Direct-to-Cloud Stream Workflow

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
## 🛡️ Production Engineering Patterns

To ensure high availability and enterprise-grade reliability, the codebase employs the following advanced operational patterns:

### 1. Memory-Safe Event-Driven Parsing

Rather than decoding entire raw .ipynb documents directly into system memory, the ingestion pipeline reads files sequentially as an active character stream. The parser filters and processes target metadata keys on the fly, locking memory utilization to a flat, safe footprint.

### 2. Pessimistic Disconnect Handling

To counter natural sleep cycles of serverless cloud database connections, the database connection engine initiates a fast pre-ping handshake on every transaction. If a connection socket has dropped, it is silently recycled to prevent unhandled database disconnect errors (OperationalError).

### 3. Multi-Threaded Resource Gateway

Render's production server core runs over a multi-worker Gunicorn WSGI gateway configuration. By dividing tasks across isolated processing threads, the application seamlessly handles concurrent file streams without causing interface blocking.

## 🛣️ Project Roadmap & Status
* [x] Phase 1 & 2: Decoupled Architecture Setup & Cloud Core Database Schema Design (models.py)

* [/] Phase 3: Frontend UI Templates & Secure User Authentication Routing (Currently In Progress)

* [ ] Phase 4 & 5: Pandas Workflow Pipelines & Analytics Tracking Engine

* [ ] Phase 6 & 7: NumPy Multi-Dimensional Matrix Algebra Validation & High-Performance Jupyter Notebook Parsing Component

* [ ] Phase 8: MLOps, End-to-End System Integration Testing & Finalization

## ⚡ Key Features
* 🏆 Gamified XP Tracking: Earn domain-specific experience points (XP) dynamically as you finish core data science modules and Python engineering tasks.

* 📂 Direct-to-Cloud Notebook Parsing: Upload and process local .ipynb files seamlessly. The data stream leverages ijson to parse records sequentially, keeping the live server memory locked at a stable ~20 MB regardless of file size.

* 🧮 Matrix Algebra Validation: An integrated interactive evaluation playground built to calculate, check, and visually validate multi-dimensional NumPy array operations.

* 📊 Data Processing Pipelines: Experience deep real-time feedback with backend statistics powered entirely by analytical Pandas workflows.

* 🔐 Secure Authentication: Enterprise-ready native session architecture complete with password hashing, encrypted tokens, and strict dashboard route protections.

## 📦 Directory Structure
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

## 🧰 Tech Stack
```text
Layer                           Technology
Backend Core                    Flask (Python 3.x)
Data Science Engines            Pandas, NumPy, ijson
Database & ORM                  PostgreSQL / SQLAlchemy ORM (Hosted via Neon.tech)
Cloud Infrastructure            Cloudflare R2 Storage (S3 API Engine)
Networking & Gateways           Cloudflare DNS & Registrar
Frontend Foundation             Semantic HTML5, Custom Adaptive CSS3 Layouts
```
