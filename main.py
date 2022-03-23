from fastapi import FastAPI
from loguru import logger
from uvicorn import run
from fastapi.middleware.cors import CORSMiddleware
from routes.all_routes import router


app = FastAPI(
    title="BreakPoint Backend API"
)


app.include_router(router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)


if __name__ == '__main__':
    logger.info("Started main")
    run("main:app", host="0.0.0.0", port=5055, reload=True)
