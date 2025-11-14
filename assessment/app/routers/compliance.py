from fastapi import APIRouter, UploadFile, File, HTTPException
import tempfile
from app.services import parser, analyzer, modifier

router = APIRouter(prefix="/api")
@router.post("/upload")
async def upload_and_analyze(file: UploadFile = File(...)):
    if not file.filename.endswith((".pdf", ".docx")):
        raise HTTPException(status_code=400, detail="Only PDF or DOCX allowed")

    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(await file.read())
        file_path = tmp.name

    # Extract text
    text = parser.extract_text(file_path, file.filename)

    # Analyze
    report = analyzer.check_compliance(text)

    return {"file_name": file.filename, "report": report}


@router.post("/modify")
async def modify_to_compliance(file: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(await file.read())
        file_path = tmp.name

    text = parser.extract_text(file_path, file.filename)
    modified_text = modifier.correct_text(text)
    return {"modified_text": modified_text}
