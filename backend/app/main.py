from fastapi import FastAPI
from app.controllers import user_controller, entry_controller
app = FastAPI()
app.include_router(user_controller.router)
app.include_router(entry_controller.router)
