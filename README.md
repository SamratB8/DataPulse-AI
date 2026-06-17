# DataPulse-AI 📊⚡

A gamified AI/ML study tracker and productivity web application designed for data scientists and developers. DataPulse-AI bridges the gap between structured learning and hands-on coding by tracking domain-specific XP, parsing Jupyter notebooks, and validating mathematical core concepts.

---

## 🚀 Features

* **Gamified XP Tracking:** Earn domain-specific experience points (XP) as you complete data science milestones.
* **Jupyter Notebook Parsing:** Upload and track your progress through local `.ipynb` files directly inside your dashboard.
* **Matrix Algebra Validation:** An integrated feature to test and check complex NumPy multi-dimensional array math matrix logic.
* **Data Processing Pipelines:** Built-in analytics tracking backed by Pandas workflow pipelines.
* **Secure Authentication:** Complete session handling featuring secure registration, login, and protected dashboard routes.

---

## 🛠️ Tech Stack

* **Backend Framework:** Flask (Python)
* **Database:** SQLite (SQLAlchemy ORM)
* **Frontend:** HTML5, CSS3 (Custom Responsive Layouts)
* **Data Science Tools:** Pandas, NumPy

---

## 📦 Directory Structure

```text
DATAPULSE-AI/
│
├── app/
│   ├── static/          # CSS, images, and frontend assets
│   ├── templates/       # HTML layouts (base, dashboard, login, register, etc.)
│   ├── __init__.py      # App factory initialization
│   ├── models.py        # Database schemas and user models
│   └── routes.py        # Application controller and URL endpoints
│
├── datapulse.db         # Local SQLite database instance
├── requirements.txt     # Python project dependencies
└── run.py               # Application entry point
