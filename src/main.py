from fastapi import FastAPI

from pydantic import BaseModel

from src.banco import criar_tabela, get_connection

app = FastAPI()
criar_tabela()

class Tarefa(BaseModel):
    titulo: str
@app.post("/tarefas")
def criar_tarefa(dados: Tarefa):
    conn = get_connection()
    conn.execute("INSERT INTO Tarefas (titulo) VALUES (?)", (dados.titulo,))
    conn.commit()
    conn.close()
    return {"titulo": dados.titulo, "concluida": False}

@app.get("/tarefas")
def lista_tarefa():
    conn = get_connection()
    lista = conn.execute("SELECT * FROM Tarefas").fetchall()    
    conn.close()
    return [dict(item) for item in lista]

@app.put("/tarefas/{id}")
def concluida(id: int):
    conn = get_connection()
    conn.execute("UPDATE Tarefas SET CONCLUIDA = 1 WHERE ID = ?", (id,))
    conn.commit()
    conn.close()
    return {"mensagem": "Tarefa concluida"}

@app.delete("/tarefas/{id}")
def deletar(id: int):
    conn = get_connection()
    conn.execute("DELETE FROM Tarefas WHERE ID = ?", (id,))
    conn.commit()
    conn.close()
    return {"mensagem": "Tarefa Deletada"}