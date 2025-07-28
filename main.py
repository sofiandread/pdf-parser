from fastapi import FastAPI, UploadFile, File
import fitz  # PyMuPDF

app = FastAPI()

@app.post("/extract-text/")
async def extract_text(file: UploadFile = File(...)):
    contents = await file.read()
    doc = fitz.open(stream=contents, filetype="pdf")
    text = "\n".join([page.get_text() for page in doc])
    return {"text": text}
