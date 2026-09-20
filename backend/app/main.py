from fastapi import FastAPI, UploadFile, File
from app.ocr import extract_text
from app.extractor import extract_fields

app = FastAPI()


@app.get("/")
def home():
    return {"message": "NEW SERVER TEST 123"}


@app.post("/inspect")
async def inspect(file: UploadFile = File(...)):
    image_data = await file.read()

    with open("temp_image.jpg", "wb") as f:
        f.write(image_data)

    ocr_results = extract_text("temp_image.jpg")

    extracted_fields = extract_fields(ocr_results)

    return {
        "filename": file.filename,
        "ocr_results": ocr_results,
        "extracted_fields": extracted_fields,
        "TEST": "NEW CODE IS RUNNING"
    }