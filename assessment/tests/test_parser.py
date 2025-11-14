from app.services.parser import extract_text_from_docx
from docx import Document
import tempfile
import os

def test_extract_text_from_docx():
    """Ensure text extraction from DOCX works correctly."""
    doc = Document()
    doc.add_paragraph("This is a test document.")
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".docx")
    doc.save(tmp.name)

    text = extract_text_from_docx(tmp.name)
    os.remove(tmp.name)

    assert "test document" in text.lower()
