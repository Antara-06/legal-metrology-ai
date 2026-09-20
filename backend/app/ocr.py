import easyocr
import cv2
import numpy as np
from PIL import Image, ImageOps

reader = easyocr.Reader(["en"])


def extract_text(image_path):

    # Read image while respecting phone EXIF orientation
    pil_image = Image.open(image_path)
    pil_image = ImageOps.exif_transpose(pil_image)
    pil_image = pil_image.convert("RGB")

    # Convert PIL image to OpenCV format
    image = np.array(pil_image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Resize large images
    max_width = 1600

    height, width = image.shape[:2]

    if width > max_width:
        scale = max_width / width
        new_width = int(width * scale)
        new_height = int(height * scale)

        image = cv2.resize(
            image,
            (new_width, new_height)
        )

    results = reader.readtext(
        image,
        detail=1,
        paragraph=False
    )

    extracted = []

    for bbox, text, confidence in results:

        if confidence < 0.5:
            continue

        clean_bbox = [
            [int(point[0]), int(point[1])]
            for point in bbox
        ]

        extracted.append({
            "text": text,
            "confidence": float(confidence),
            "bbox": clean_bbox
        })

    return extracted