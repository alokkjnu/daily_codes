from fastapi.testclient import TestClient
from app.main import app
from docx import Document
import tempfile

client = TestClient(app)

def create_temp_docx(content="This is a sample document."):
    doc = Document()
    doc.add_paragraph(content)
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".docx")
    doc.save(tmp.name)
    return tmp.name

def test_upload_endpoint():
    file_path = create_temp_docx("This is a test file for compliance checking.")
    with open(file_path, "rb") as f:
        response = client.post("/api/upload", files={"file": ("test.docx", f, "application/vnd.openxmlformats-officedocument.wordprocessingml.document")})
    assert response.status_code == 200
    data = response.json()
    assert "report" in data
    assert "score" in data["report"]

def test_modify_endpoint():
    file_path = create_temp_docx("It was written by the author and is very interesting.")
    with open(file_path, "rb") as f:
        response = client.post("/api/modify", files={"file": ("test.docx", f, "application/vnd.openxmlformats-officedocument.wordprocessingml.document")})
    assert response.status_code == 200
    data = response.json()
    assert "modified_text" in data
