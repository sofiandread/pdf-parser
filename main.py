from fastapi import FastAPI, File, UploadFile
import pdfplumber

app = FastAPI()

@app.post("/extract-text/")
async def extract_text(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        with pdfplumber.open(file.file) as pdf:
            text = "\n".join(page.extract_text() or "" for page in pdf.pages)
        return {"text": text}
    except Exception as e:
        return {"error": str(e)}
