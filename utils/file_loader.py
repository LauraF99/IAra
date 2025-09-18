import pandas as pd
from PyPDF2 import PdfReader
from langchain.schema import Document

def load_pdf(file) -> list:
    reader = PdfReader(file)
    texts = [page.extract_text() for page in reader.pages if page.extract_text()]
    return [Document(page_content=t, metadata={"source": file.name}) for t in texts]

def load_excel(file) -> list:
    df = pd.read_excel(file)
    text = df.to_string(index=False)
    return [Document(page_content=text, metadata={"source": file.name})]


