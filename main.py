from fastapi import FastAPI, UploadFile, File
import fitz  # PyMuPDF
import os
import uvicorn

app = FastAPI()

@app.post("/extract-text/")
async def extract_text(file: UploadFile = File(...)):
    contents = await file.read()
    doc = fitz.open(stream=contents, filetype="pdf")
    text = "\n".join([page.get_text() for page in doc])
    return {"text": text}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
