import re

def limpar_resposta(text:str)-> str:
    return re.sub(r"<think>.*?</think", "", text, flags=re.DOTALL).strip()