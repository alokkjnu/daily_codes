"""
write a api using FASTAPI to return revese of string in response.
"""

from fastapi import  FastAPI,Request
import uvicorn
from pydantic import BaseModel

app = FastAPI()

class Data(BaseModel):
    name:str

@app.post("/")
def test(name:Data):
    name = name.name
    res = ""
    for i in name:
        res = i+res

    return {"response":res}


if __name__=="__main__":
    
    uvicorn.run(app,host="127.0.0.1",port=8000)