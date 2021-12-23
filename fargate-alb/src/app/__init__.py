from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_root():
    print("test")
    return {"message": "FastAPI running in a Docker container"}
