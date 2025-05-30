# src/app/main.py

# Imported Libraries
from fastapi import FastAPI

# Imported Utils
from src.utils.logger import setup_logger, get_logger

# Configure Logging
setup_logger(name="fastapi")
logger = get_logger("fastapi")

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    logger.info("FastAPI application starting...")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("FastAPI application shutting down...")

@app.get("/")
async def read_root():
    logger.debug("Handling GET '/'")
    return {
        "message": "Hello, World!"
    }