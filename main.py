from fastapi import FastAPI

app = FastAPI()


@app.get("/md")
async def root():
    return {"message": "Hello World"}
