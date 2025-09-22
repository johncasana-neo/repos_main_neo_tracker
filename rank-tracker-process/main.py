from fastapi import FastAPI
from routers import proyectos, usuarios, keyword_research
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(docs_url="/documentation", redoc_url="/reference")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"])
app.include_router(proyectos.router)
app.include_router(usuarios.router)
app.include_router(keyword_research.router)
app.mount('/static', StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return {"message": "Hola mundo!"}