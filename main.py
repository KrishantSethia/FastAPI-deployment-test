from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def main():
    return {"message": "This is the first time I'm deploying a fast API application on the google Cloud"}
