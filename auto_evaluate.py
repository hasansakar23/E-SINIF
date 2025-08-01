import google.generativeai as genai
from fastapi import UploadFile
import json
import tempfile
from PyPDF2 import PdfReader

GENAI_API_KEY = "....."

genai.configure(api_key=GENAI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

def extract_text_from_pdf(file: UploadFile) -> str:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(file.file.read())
        tmp_path = tmp.name

    reader = PdfReader(tmp_path)
    text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    return text

def evaluate_homework_with_gemini(text: str) -> dict:
    prompt = f"""
    Aşağıdaki metni değerlendir:

    METİN:
    {text}

    Değerlendirme Kriterleri:
    - Anlatım Bütünlüğü (1–5)
    - Kaynak Kullanımı (1–5)
    - Yorum Gücü (1–5)
    - Dil ve Anlatım (1–5)
    - Geri Bildirim

    Cevabını şu JSON formatında döndür:
    {{
      "coherence": int,
      "sources": int,
      "reasoning": int,
      "language": int,
      "feedback": string,
      "total_score": int
    }}
    """

    response = model.generate_content(prompt)
    try:
        result = json.loads(response.text)
        return result
    except Exception as e:
        return {"error": str(e), "raw": response.text}