from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from src.banco import criar_tabela, get_connection

app = FastAPI()
criar_tabela()

class Tarefa(BaseModel):
    titulo: str
@app.post("/tarefas")
def criar_tarefa(dados: Tarefa):
    conn = get_connection()
    conn.execute("INSERT INTO tarefas (titulo) VALUES (?)", (dados.titulo,))
    conn.commit()
    conn.close()
    return {"titulo": dados.titulo, "concluida": False}

@app.get("/tarefas")
def lista_tarefa():
    conn = get_connection()
    lista = conn.execute("SELECT * FROM tarefas").fetchall()    
    conn.close()
    return [dict(item) for item in lista]

@app.put("/tarefas/{id}")
def concluida(id: int):
    conn = get_connection()
    cursor = conn.execute("UPDATE tarefas SET concluida = 1 WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return {"mensagem": "Tarefa concluida"}

@app.delete("/tarefas/{id}")
def deletar(id: int):
    conn = get_connection()
    cursor = conn.execute("DELETE FROM tarefas WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return {"mensagem": "Tarefa Deletada"}