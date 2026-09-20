import re


def extract_fields(ocr_results):
    # Combine OCR text in reading order
    texts = [item["text"] for item in ocr_results]
    full_text = " ".join(texts)

    fields = {
        "mrp": None,
        "batch_no": None,
        "manufacturing_date": None,
        "expiry_date": None,
        "manufacturer": None,
        "customer_care": None,
        "customer_email": None
    }

    # ---------------- MRP ----------------
    mrp_match = re.search(
        r"MRP\s*:?\s*(?:Rs\.?|₹)?\s*(\d+(?:\.\d{1,2})?)",
        full_text,
        re.IGNORECASE
    )

    if mrp_match:
        fields["mrp"] = mrp_match.group(1)

    # ---------------- Batch Number ----------------
    batch_match = re.search(
        r"Batch\s*(?:No\.?|Number)?\s*:?\s*([A-Za-z0-9-]+)",
        full_text,
        re.IGNORECASE
    )

    if batch_match:
        fields["batch_no"] = batch_match.group(1)

    # ---------------- Manufacturing Date ----------------
    mfg_match = re.search(
        r"Mfg\.?\s*Date\.?\s*[:_]?\s*([0-9]{1,2}[-/][0-9]{4})",
        full_text,
        re.IGNORECASE
    )

    if mfg_match:
        fields["manufacturing_date"] = mfg_match.group(1)

    # ---------------- Expiry Date ----------------
    exp_match = re.search(
        r"Exp\.?\s*Date\.?\s*[:_]?\s*([0-9]{1,2}[-/][0-9]{4})",
        full_text,
        re.IGNORECASE
    )

    if exp_match:
        fields["expiry_date"] = exp_match.group(1)

    # ---------------- Customer Care Number ----------------
    phone_match = re.search(
        r"Customer\s*Care\s*(?:No\.?|Number)?\s*:?\s*(\d{10,12})",
        full_text,
        re.IGNORECASE
    )

    if phone_match:
        fields["customer_care"] = phone_match.group(1)

    # ---------------- Email ----------------
    email_match = re.search(
        r"[\w.-]+@[\w.-]+\s+\w+",
        full_text
    )

    if email_match:
        email = email_match.group(0)
        email = re.sub(r"\s+", ".", email, count=1)
        fields["customer_email"] = email

    # ---------------- Manufacturer ----------------
    manufacturer_match = re.search(
        r"Manufactured\s+in\s+India\s+for\s*:?\s*(.*?)(?=\s+New\s+|\s+Customer\s+|\s+Registered\s+|$)",
        full_text,
        re.IGNORECASE
    )

    if manufacturer_match:
        fields["manufacturer"] = manufacturer_match.group(1).strip()

    return fields