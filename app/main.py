from fastapi import FastAPI, Request, Depends, Form
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from starlette.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from .config import settings, get_cors_origins
from .database import engine, Base, get_db
from .routers import contact as contact_router
from .routers import projects as projects_router
from .routers import certificates as certificates_router

# Create tables on startup
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

# Static files & templates
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# Routers
app.include_router(contact_router.router)
app.include_router(projects_router.router)
app.include_router(certificates_router.router)

# Web pages
@app.get("/")
async def home(request: Request):
    featured=projects_router.PROJECTS[:6]
    return templates.TemplateResponse(
        "index.html", 
        {"request": request,"projects":featured})

@app.get("/about")
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})
@app.get("/resume")
async def resume(request: Request):
    return templates.TemplateResponse("resume.html",{"request":request})

@app.get("/certificates")
async def certificates(request: Request):
    c_items=certificates_router.CERTIFICATES
    return templates.TemplateResponse("certificates.html",{"request": request,"certificates":c_items})

@app.get("/projects")
async def projects(request: Request):
    items = projects_router.PROJECTS

    # Ordered categories -> (title, key or tuple of keys)
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

    return templates.TemplateResponse(
        "projects.html",
        {"request": request, "sections": sections},
    )

@app.get("/contact")
async def contact_get(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request, "sent": False})

@app.post("/contact")
async def contact_post(
    request: Request,
    name: str = Form(...),
    email: str = Form(...),
    subject: str = Form(...),
    message: str = Form(...),
    db: Session = Depends(get_db),
):
    from .routers.contact import create_message
    from .schemas import ContactCreate

    create_message(ContactCreate(name=name, email=email, subject=subject, message=message), db)
    return RedirectResponse(url="/contact?sent=1", status_code=303)
