import sqlite3

def get_connection():
    return sqlite3.connect("data/escola.db", check_same_thread=False)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Estudantes
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS estudantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT
        )                   
    """)
     # Verifica se a coluna 'data_nascimento' já existe
    cursor.execute("PRAGMA table_info(estudantes)")
    colunas = [coluna[1] for coluna in cursor.fetchall()]

    if "data_nascimento" not in colunas:
        cursor.execute("""
            ALTER TABLE estudantes ADD COLUMN data_nascimento TEXT
        """)


    # Documentos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS documentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            data_upload TEXT
        )
    """)    
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE,
            senha TEXT
        )
    """)   
    
    conn.commit()
    conn.close()
