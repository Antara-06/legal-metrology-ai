# Legal Metrology AI

An AI-powered system that analyzes packaged product labels using OCR and rule-based validation to identify missing or potentially non-compliant declarations under Indian Legal Metrology requirements.

## Project Overview

The system follows this pipeline:

Image Upload
→ OCR
→ Field Extraction
→ Rule Validation
→ Compliance Report

### Current Features

- Upload a product/package image
- Extract text using EasyOCR
- Detect important product declarations
- Extract structured fields from OCR output
- Backend API using FastAPI
- React frontend using Vite
- Rule-based compliance checking (to be implemented)

### Currently Extracted Fields

- MRP
- Batch Number
- Manufacturing Date
- Expiry Date
- Manufacturer
- Customer Care Number
- Customer Email

---

# Project Structure

```text
legal-metrology-ai/
│
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── ocr.py
│   │   ├── extractor.py
│   │   ├── rules.py
│   │   └── validator.py
│   │
│   ├── requirements.txt
│   └── venv/              # Created locally, NOT included in Git
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── ...
│
├── .gitignore
└── README.md

Setup Instructions
1. Clone the Repository
git clone https://github.com/Antara-06/legal-metrology-ai.git
cd legal-metrology-ai

Backend Setup
Open a terminal in the project folder.
Go to backend
cd backend
Create virtual environment
python -m venv venv
Activate virtual environment
Windows PowerShell
.\venv\Scripts\Activate.ps1

You should see:

(venv)

at the beginning of your terminal.

Install dependencies
pip install -r requirements.txt
Start the backend
python -m uvicorn app.main:app --reload --port 8010

Backend will run at:

http://127.0.0.1:8010

API documentation:
http://127.0.0.1:8010/docs

Frontend Setup
Open a new terminal.

From the project root:
cd frontend

Install dependencies:
npm install

Start the development server:
npm run dev

The frontend will normally run at:
http://localhost:5173

Important

You need two terminals running at the same time:

Terminal 1 — Backend
cd backend
.\venv\Scripts\Activate.ps1
python -m uvicorn app.main:app --reload --port 8010
Terminal 2 — Frontend
cd frontend
npm run dev
API
POST /inspect

Accepts a product/package image and performs OCR + field extraction.

Input

Multipart form-data:

file: <image>
Example Response
{
  "filename": "product.jpg",
  "ocr_results": [],
  "extracted_fields": {
    "mrp": "250.00",
    "batch_no": "MLB-04",
    "manufacturing_date": "04-2026",
    "expiry_date": "03-2029",
    "manufacturer": "Mediwin Laboratories",
    "customer_care": "09255666660",
    "customer_email": "Info@mediwinlabs.com"
  }
}

Development Notes
Use clear, straight product-label images for testing.
OCR accuracy depends on image quality.
venv/ should not be committed to Git.
node_modules/ should not be committed to Git.
Do not commit API keys or .env files.
The compliance rules are still under development.

Team Workflow

Before starting work:

git pull origin main

After making changes:

git status
git add .
git commit -m "Describe your changes"
git push
Before pushing

Always check:

git status

Make sure you are not accidentally committing:

venv/
node_modules/
.env
API keys
temporary images/files

Current Development Status
Completed
 React/Vite frontend setup
 FastAPI backend setup
 EasyOCR integration
 OCR JSON response
 Field extraction
 MRP extraction
 Batch number extraction
 Manufacturing date extraction
 Expiry date extraction
 Manufacturer extraction
 Customer care extraction
 Customer email extraction
 
To Do
 Improve manufacturer extraction
 Implement Legal Metrology rule engine
 Connect frontend to backend
 Display extracted fields in UI
 Display PASS / VIOLATION / MANUAL REVIEW results
 Add evidence/highlighting
 Generate compliance report
 Test with multiple product images
