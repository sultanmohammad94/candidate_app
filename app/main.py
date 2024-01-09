from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()


@app.get("/health", status_code=200)
async def server_health():
    return {"message": "Server is running"}
