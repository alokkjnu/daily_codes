"""
write a api using FASTAPI to return revese of string in response.
input:"Alok"
output:"kolA"
"""

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

class Data(BaseModel):

    name : str


app = FastAPI()

@app.post("/")
async def post_name(data:Data):

    try:

        name = data.name
        res= ""
        for i in name:
            res= i+res
        
        return {"response":res}

    except Exception as e:
        return {"error":e}

if __name__ == "__main__":

    uvicorn.run(app,host="127.0.0.1",port=8003)