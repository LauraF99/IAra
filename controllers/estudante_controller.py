from utils.db import get_connection
from models.estudante_model import Estudante

def adicionar_estudante(nome):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO estudantes (nome) VALUES (?)", 
                   (nome,))
    conn.commit()
    conn.close()

def listar_estudantes():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome FROM estudantes")
    rows = cursor.fetchall()
    conn.close()
    return [Estudante(*row) for row in rows]
