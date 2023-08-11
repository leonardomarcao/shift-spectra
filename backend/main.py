from app.core.logger import logger
from app.setup_app import create_app, settings
from fastapi.middleware.cors import CORSMiddleware

app = create_app()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn

    logger.info("Starting uvicorn")
    uvicorn.run(
        "main:app",
        host=settings.UVICORN_HOST,
        reload=settings.is_dev(),
        port=settings.UVICORN_PORT,
    )
