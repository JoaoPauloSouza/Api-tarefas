import sqlite3

def get_connection():
    conn = sqlite3.connect("tarefas.db")
    conn.row_factory = sqlite3.Row 
    return conn

def criar_tabela():
    conn = get_connection()
    conn.execute("""
                 CREATE TABLE IF NOT EXISTS Tarefas(
                 ID INTEGER PRIMARY KEY AUTOINCREMENT,
                 TITULO TEXT NOT NULL,
                 CONCLUIDA INTEGER DEFAULT 0)
                 """)

    conn.commit()
    conn.close()