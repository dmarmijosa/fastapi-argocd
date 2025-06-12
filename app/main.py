from fastapi import FastAPI

app = FastAPI(title="FastAPI ArgoCD demo")

@app.get("/ping")
async def ping():
    return {"message": "pong"}