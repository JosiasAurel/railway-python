from fastapi import FastAPI
import trim
import subprocess
import uvicorn
import os

app = FastAPI()


@app.get("/")
def _root():
    return "Hello World from Railway"


@app.get("/nice")
def _nice():
    trim.trim_stuff()
    dir_content = subprocess.check_output("ls").splitlines()
    print(dir_content)
    return f"Directory currently contains {dir_content}"


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=int(
        os.getenv("PORT")), log_level="info")
