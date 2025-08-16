
# Portfolio API (FastAPI)

Companion backend for my portfolio. Serves **projects**, **certificates**, and accepts **contact** messages. Designed to power the static frontend hosted on GitHub Pages.

- **Frontend repo:** [`nirob-0812.github.io`](https://github.com/Nirob-0812/nirob-0812.github.io)
- **Production API:** `https://portfolio-api-z616.onrender.com`
- **Interactive docs:** `/docs` (Swagger) and `/redoc`

---

## ✨ What’s inside

- **FastAPI** with Uvicorn
- **CORS** enabled for GitHub Pages
- Simple data layer (JSON or in‑memory) that you can swap for a DB later
- Clean JSON contracts consumed by the frontend
- Minimal logging and error handling

---

## 🧪 Endpoints

### `GET /api/projects/`
Returns a list of projects. Example shape:
```json
[
  {
    "title": "Object Detection using YOLO",
    "category": "dl",
    "summary": "YOLOv8-based object detection with pre-trained weights and sample inference.",
    "url": "https://github.com/Nirob-0812/...",
    "techs": ["Python", "Ultralytics YOLOv8", "OpenCV"]
  }
]
```

### `GET /api/certificates/`
```json
[
  {
    "title": "Handwritten Digit Classification (Keras)",
    "issuer": "Coursera",
    "date": "2024-02",
    "image": "https://…/certificate.png",
    "verify_url": "https://…"
  }
]
```

### `POST /api/contact/`
Accepts a JSON body:
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "subject": "Freelance inquiry",
  "message": "Hi, I’d like to discuss a project…"
}
```
Responds with `{"ok": true}` on success.

---

## ⚙️ Quickstart

```bash
git clone https://github.com/Nirob-0812/portfolio-api.git
cd portfolio-api

# (Recommended) Python 3.10+
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install -r requirements.txt

# Run locally
uvicorn app.main:app --reload
# open http://127.0.0.1:8000/docs
```

> Your module path may differ (`app.main:app` vs `main:app`) depending on the project layout.

---

## 🔒 Enable CORS

The frontend runs at `https://nirob-0812.github.io`. Make sure it’s allowed:

```python
# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "https://nirob-0812.github.io",
    "http://localhost:8080",  # local static server
    "http://127.0.0.1:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## 🔧 Configuration

Environment variables you may want to add (e.g., in `.env`):

| Variable | Purpose | Example |
|---|---|---|
| `PORT` | port for Uvicorn when deployed | `10000` |
| `ALLOWED_ORIGINS` | comma‑separated CORS origins | `https://nirob-0812.github.io,http://localhost:8080` |
| `CONTACT_EMAIL_TO` | address to forward contact messages (if you wire SMTP later) | `mehedi@example.com` |

---

## ☁️ Deploy (Render)

1. Create a **Web Service** on [Render](https://render.com/) from this repo.
2. Environment: **Python 3.10+**
3. Build command:
   ```bash
   pip install -r requirements.txt
   ```
4. Start command:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port $PORT
   ```
5. Add env var `ALLOWED_ORIGINS=https://nirob-0812.github.io`.
6. Deploy and copy the base URL (e.g., `https://portfolio-api-xxxxx.onrender.com`).  
   Update the frontend `<body data-api="…">` accordingly in [`nirob-0812.github.io`](https://github.com/Nirob-0812/nirob-0812.github.io).

---

## 🔗 Related repositories

- Frontend (GitHub Pages): **[`nirob-0812.github.io`](https://github.com/Nirob-0812/nirob-0812.github.io)**
- API (this): **[`portfolio-api`](https://github.com/Nirob-0812/portfolio-api)**

---

## 👤 Author

**Mehedi Hasan Nirob**  
- GitHub: https://github.com/Nirob-0812  
- X (Twitter): https://x.com/mhnirob0812  
- Email: mehedihasannirobcsediu@gmail.com

---

## 📝 License

MIT
