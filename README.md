# Mehedi Hasan Nirob — Portfolio (FastAPI + HTML/CSS)

A complete, professional, responsive portfolio you can deploy for **free** via GitHub → Render.
Root directory: **`mhn_portfolio/`**.

## Project Structure

```
mhn_portfolio/
├─ app/
│  ├─ __init__.py
│  ├─ main.py
│  ├─ config.py
│  ├─ database.py
│  ├─ models.py
│  ├─ schemas.py
│  ├─ routers/
│  │   ├─ __init__.py
│  │   ├─ contact.py
│  │   └─ projects.py
│  ├─ templates/
│  │   ├─ base.html
│  │   ├─ index.html
│  │   ├─ about.html
│  │   ├─ projects.html
│  │   ├─ contact.html
│  │   └─ resume.html
│  └─ static/
│      ├─ css/
│      │   └─ style.css
│      ├─ js/
│      │   └─ main.js
│      ├─ img/
│      │   └─ avatar.png
│      └─ files/
│          └─ Mehedi_Hasan_Nirob_Resume.pdf
├─ tests/
│  └─ test_api.py
├─ .gitignore
├─ LICENSE
├─ Procfile
├─ README.md
├─ render.yaml
├─ requirements.txt
└─ .env.example
```

## Local Setup

```bash
git clone https://github.com/<your-username>/mhn_portfolio.git
cd mhn_portfolio
python -m venv .venv
# Windows: .venv\Scripts\activate
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env    # optional
uvicorn app.main:app --reload
# open http://127.0.0.1:8000
```

## Free Deploy (GitHub → Render)

1. Push this folder to a **public GitHub repo** named `mhn_portfolio` (name optional).
2. On **Render.com**, create a **Web Service** from your repo. `render.yaml` is auto-detected.
3. Confirm **Free plan**, and set env vars if needed (e.g. `ADMIN_TOKEN`).

## Admin: Read Contact Messages

```bash
curl -H "X-Admin-Token: <your-admin-token>" https://<your-app>.onrender.com/api/contact/
```

## Customize

- Replace `app/static/img/avatar.png` (220×220).
- Replace `app/static/files/Mehedi_Hasan_Nirob_Resume.pdf` with your real CV.
- Edit `app/templates/*.html` and `app/routers/projects.py` for your info.
