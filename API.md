# Documentação da API

## POST /tarefas

Descrição: Cria uma nova tarefa

Request:
{
  "titulo": "Estudar Python"
}

Response (200):
{
  "titulo": "Estudar Python",
  "concluida": false
}

---

## GET /tarefas

Descrição: Lista todas as tarefas

Response (200):
[
  {
    "ID": 1,
    "TITULO": "Estudar Python",
    "CONCLUIDA": 0
  }
]

---

## PUT /tarefas/{id}

Descrição: Marca uma tarefa como concluída

Response (200):
{
  "mensagem": "Tarefa concluida"
}

---

## DELETE /tarefas/{id}

Descrição: Deleta uma tarefa

Response (200):
{
  "mensagem": "Tarefa Deletada"
}

---

## Códigos de status

- 200: Sucesso  
- 400: Erro de requisição  
- 500: Erro interno