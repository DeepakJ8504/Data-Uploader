from typing import Literal, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="File Processor API", version="1.0.0")

import csv_to_json_converter as csv_to_json

FILE_TYPE: Literal["xml", "csv"] = "csv"

class RequestType(BaseModel):
    file_path: Optional[str] = None

@app.post("/validate")
async def validate_data(data:RequestType):
    """Validate shared data."""
    file_path = data.file_path
    if not file_path:
        raise HTTPException(status_code=404, detail="file path not found")

    response1 = csv_to_json.convert(file_path)

    return response1

@app.post("/upload")
async def upload_data(data:RequestType):
    """Upload shared data"""
    try:
        file_path = data.file_path
        if not file_path:
            raise HTTPException(status_code=404, detail="file path not found")

        response2 = csv_to_json.convert(file_path, "upload")

        return response2
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)