import logging

import uvicorn
from fastapi import FastAPI

# Custom logger configuration
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)


app = FastAPI(
    title="DB-updater",
)


@app.get("/health", tags=["health_check"])
async def root():
    return {"message": "app is running"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)
