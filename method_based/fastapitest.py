from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

class ReadFile(BaseModel):
    path : str

app = FastAPI()



@app.post("/read-file")
async def readfile(readfile : ReadFile):
    path = readfile.path
    s = ""
    with open(path,"r") as f:

        s = f.readlines()
        f.close()

    return s

if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1", port = 8000)




def test():
    yield 1
    