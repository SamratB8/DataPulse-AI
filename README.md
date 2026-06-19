DataPulse-AI 📊⚡

[![Development Status](https://img.shields.io/badge/status-work--in--progress-orange)](https://github.com/SamratB8/DataPulse-AI)

> **⚠️ Notice:** This project is currently a **Work in Progress (WIP)**. I am actively developing the core data pipelines, analytical modules, and frontend tracking systems.

A gamified, enterprise-architected AI/ML study tracker and productivity web application designed for data scientists and developers. DataPulse-AI bridges the gap between structured learning and hands-on coding by tracking domain-specific XP, validating mathematical core concepts, and securely processing user metrics over an isolated, cloud-decoupled pipeline.

☕ Notice: This project is deployed on a decoupled cloud environment. If the initial dashboard load takes a moment, the backend containers are safely completing a server cold-start. Subsequent features are blazingly fast!

🛠️ System Architecture & Cloud Infrastructure

DataPulse-AI is built using a modern, decoupled production-grade cloud layout engineered to bypass traditional server constraints (such as RAM bottlenecks and request timeouts):

Application Server: Render Pro — Hosts the Flask Python runtime core, guaranteeing 24/7 high-performance availability, 25 GB of outbound bandwidth, and automated GitHub continuous integration (CI/CD).

Database Engine: Neon.tech (PostgreSQL) — A permanent, serverless, relational database cluster running completely separated from the application web service, ensuring zero data loss during code updates.

Object Storage: Cloudflare R2 (S3-Compatible) — Acts as an isolated file vault with $0 egress fees. Large uploads completely skip Render's infrastructure via a programmatic secure handshake.

Networking & Domain Security: Cloudflare Registrar & DNS — Enforces zero-markup wholesale domain management, automated global edge caching, and end-to-end SSL/TLS encryption.

🚀 Direct-to-Cloud Stream Workflow

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
    [ Render Pro Server ] ◄───────► [ Neon.tech Postgres ]
  (Flask/Pandas Processing Core)       (Permanent Cloud Memory)


🛠️ Project Roadmap & Status

[x] Phase 1 & 2: Decoupled Architecture Setup & Cloud Core Database Schema Design (models.py)

[/] Phase 3: Frontend UI Templates & Secure User Authentication Routing (Currently In Progress)

[ ] Phase 4 & 5: Pandas Workflow Pipelines & Analytics Tracking Engine

[ ] Phase 6 & 7: NumPy Multi-Dimensional Matrix Algebra Validation & High-Performance Jupyter Notebook Parsing Component

[ ] Phase 8: MLOps, System Testing & Finalization

🚀 Key Features

Gamified XP Tracking: Earn domain-specific experience points (XP) as you complete data science and Python engineering milestones.

Direct-to-Cloud Jupyter Notebook Parsing: Upload and process local .ipynb files effortlessly. Uses ijson and stream looping to keep the server's RAM footprint down to a fixed ~20 MB, regardless of the notebook size.

Matrix Algebra Validation: Integrated interactive canvas to evaluate and check complex NumPy multi-dimensional array math matrix logic.

Data Processing Pipelines: Built-in dashboard analytics tracking backed by custom Pandas workflow calculation pipelines.

Secure Authentication: Native Python session management featuring secure cryptography registration, login, and protected tracking dashboard routes.

📦 Directory Structure

DATAPULSE-AI/
│
├── app/
│   ├── static/          # Custom responsive CSS layouts and frontend assets
│   ├── templates/       # HTML5 Jinja layouts (base, dashboard, login, register, etc.)
│   ├── __init__.py      # App factory initialization, R2 storage connections & extensions
│   ├── models.py        # PostgreSQL production database schemas and ORM relationships
│   └── routes.py        # Controller routes, API endpoints, and presigned URL generators
│
├── requirements.txt     # Production dependencies (Flask, SQLAlchemy, ijson, pandas, numpy)
└── run.py               # Application cloud entry point


🛠️ Tech Stack

Backend Framework: Flask (Python 3.x)

Database ORM: SQLAlchemy / PostgreSQL (Neon.tech)

Cloud Storage: Cloudflare R2 Core (S3 API Client)

Data Science Engine: Pandas, NumPy, ijson

Frontend UI: HTML5, CSS3 (Pure Responsive Flexbox Layouts)
