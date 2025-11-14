import fitz  # PyMuPDF
from docx import Document

def extract_text_from_pdf(path: str) -> str:
    doc = fitz.open(path)
    text = " ".join([page.get_text() for page in doc])
    return text.strip()

def extract_text_from_docx(path: str) -> str:
    doc = Document(path)
    text = "\n".join([p.text for p in doc.paragraphs])
    return text.strip()

def extract_text(file_path: str, filename: str) -> str:
    if filename.endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    elif filename.endswith(".docx"):
        return extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file format")
