from fastapi import FastAPI
from routes.calorie_routes import router as calorie_router

app = FastAPI()

app.include_router(calorie_router)
