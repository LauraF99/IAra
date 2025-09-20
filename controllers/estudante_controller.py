from utils.db import get_connection
from models.estudante_model import Estudante

def adicionar_estudante(nome, data_nascimento):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO estudantes (nome, data_nascimento) VALUES (?,?)", 
                   (nome,data_nascimento))
    conn.commit()
    conn.close()



def listar_estudantes():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, data_nascimento FROM estudantes")
    rows = cursor.fetchall()
    conn.close()
    return [Estudante(*row) for row in rows]
