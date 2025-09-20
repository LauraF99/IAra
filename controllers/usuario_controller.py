from utils.db import get_connection
from models.usuario_models import Usuario
import hashlib
import sqlite3

def criar_usuario(email, senha):
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        senha_hash = hashlib.sha256(senha.encode()).hexdigest()

        cursor.execute("""
            INSERT INTO usuarios (email, senha)
            VALUES (?, ?)
        """, (email, senha_hash))

        conn.commit()
        return True, "Usuário criado com sucesso!"
        
    except sqlite3.IntegrityError:
        return False, "Este e-mail já está cadastrado."
        
    except Exception as e:
        return False, f"Erro ao criar usuário: {str(e)}"
        
    finally:
        conn.close()

def validar_login(email, senha):
    conn = get_connection()
    cursor = conn.cursor()

   
    cursor.execute("""
        SELECT senha FROM usuarios WHERE email = ?
    """, (email,))
    resultado = cursor.fetchone()
    conn.close()

    if resultado:
        senha_hash = resultado[0]
        return hashlib.sha256(senha.encode()).hexdigest() == senha_hash
    else:
        return False  
