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

Response (422):
{
  "detail": "campo titulo é obrigatório"
}

---

## GET /tarefas

Descrição: Lista todas as tarefas

Response (200):
[
  {
    "id": 1,
    "titulo": "Estudar Python",
    "concluida": 0
  }
]

---

## PUT /tarefas/{id}

Descrição: Marca uma tarefa como concluída

Response (200):
{
  "mensagem": "Tarefa concluida"
}

Response (404):
{ 
  "detail": "Tarefa não encontrada"
}

---

## DELETE /tarefas/{id}

Descrição: Deleta uma tarefa

Response (200):
{
  "mensagem": "Tarefa Deletada"
}

Response (404):
{ 
  "detail": "Tarefa não encontrada"
}

---

## Códigos de status

- 200: Sucesso  
- 400: Erro de requisição 
- 404: Recurso não encontrado
- 422: Erro de validação  
- 500: Erro interno