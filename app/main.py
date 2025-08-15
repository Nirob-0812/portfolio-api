# app/main.py
from pathlib import Path

from fastapi import FastAPI, Request, Depends, Form
from fastapi.responses import RedirectResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from starlette.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from app.config import settings, get_cors_origins
from app.database import engine, Base, get_db
from app.routers import contact as contact_router
from app.routers import projects as projects_router
from app.routers import certificates as certificates_router

# Create tables on startup (safe on Postgres; no-op if already present)
Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.APP_NAME)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=get_cors_origins(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static & templates (mount only if folders actually exist in this build)
BASE_DIR = Path(__file__).parent
TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"

if STATIC_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

templates = Jinja2Templates(directory=str(TEMPLATES_DIR)) if TEMPLATES_DIR.exists() else None

# Routers (API)
app.include_router(contact_router.router)
app.include_router(projects_router.router)
app.include_router(certificates_router.router)

# -------- Web pages (redirect to GitHub Pages in prod if templates are missing) --------
@app.get("/")
async def home(request: Request):
    if templates:
        featured = projects_router.PROJECTS[:6]
        return templates.TemplateResponse("index.html", {"request": request, "projects": featured})
    return RedirectResponse("https://nirob-0812.github.io/", status_code=307)

@app.get("/about")
async def about(request: Request):
    if templates:
        return templates.TemplateResponse("about.html", {"request": request})
    return RedirectResponse("https://nirob-0812.github.io/about.html", status_code=307)

@app.get("/resume")
async def resume(request: Request):
    if templates:
        return templates.TemplateResponse("resume.html", {"request": request})
    return RedirectResponse("https://nirob-0812.github.io/resume.html", status_code=307)

@app.get("/certificates")
async def certificates(request: Request):
    if templates:
        c_items = certificates_router.CERTIFICATES
        return templates.TemplateResponse("certificates.html", {"request": request, "certificates": c_items})
    return RedirectResponse("https://nirob-0812.github.io/certificates.html", status_code=307)

@app.get("/projects")
async def projects(request: Request):
    if templates:
        items = projects_router.PROJECTS
        order = [
            ("Machine Learning", ("ml",)),
            ("Deep Learning / CV", ("dl",)),
            ("Web", ("web",)),
            ("Apps (Flutter)", ("app",)),
            ("Programming & Algorithms", ("algo",)),
            ("Robotics", ("robotics",)),
            ("Notebooks / Study", ("notebook",)),
        ]
        sections = []
        for title, keys in order:
            group = [p for p in items if p.get("category") in keys]
            if group:
                sections.append({"title": title, "projects": group})
        return templates.TemplateResponse("projects.html", {"request": request, "sections": sections})
    return RedirectResponse("https://nirob-0812.github.io/projects.html", status_code=307)

@app.get("/contact")
async def contact_get(request: Request):
    if templates:
        return templates.TemplateResponse("contact.html", {"request": request, "sent": False})
    return RedirectResponse("https://nirob-0812.github.io/contact.html", status_code=307)

# Contact POST keeps saving to DB even when frontend is on GitHub Pages
@app.post("/contact")
async def contact_post(
    request: Request,
    name: str = Form(...),
    email: str = Form(...),
    subject: str = Form(...),
    message: str = Form(...),
    db: Session = Depends(get_db),
):
    from app.routers.contact import create_message
    from app.schemas import ContactCreate

    create_message(
        ContactCreate(name=name, email=email, subject=subject, message=message),
        db,
    )
    # If API rendered locally, reload /contact; otherwise the frontend should POST directly to /api/contact.
    if templates:
        return RedirectResponse(url="/contact?sent=1", status_code=303)
    return PlainTextResponse("Message received", status_code=201)

# Silence favicon noise in logs
@app.get("/favicon.ico")
async def favicon():
    return PlainTextResponse("", status_code=204)
