from fastapi import FastAPI
from app.controllers import user_controller, entry_controller
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Journal App API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(user_controller.router)
app.include_router(entry_controller.router)

@app.get("/")
def root():
    return {"message": "API running"}