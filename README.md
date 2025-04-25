📚 Projeto Django - Generic Routes

Este projeto implementa uma engine de rotas dinâmicas utilizando Django + Django REST Framework + drf-spectacular para documentação via Swagger UI.

Chamadas via terminal (curl)

GET sem parâmetro:

curl -X GET http://127.0.0.1:8000/routes/
--

POST sem parâmetro:

curl -X POST http://127.0.0.1:8000/routes/
--

PUT sem parâmetro:

curl -X PUT http://127.0.0.1:8000/routes/
--

DELETE sem parâmetro:

curl -X DELETE http://127.0.0.1:8000/routes/
--

GET com parâmetro:

curl -X GET http://127.0.0.1:8000/routes/seu_parametro/
--

POST com parâmetro:

curl -X POST http://127.0.0.1:8000/routes/seu_parametro/
--

PUT com parâmetro:

curl -X PUT http://127.0.0.1:8000/routes/seu_parametro/
--

DELETE com parâmetro:

curl -X DELETE http://127.0.0.1:8000/routes/seu_parametro/
--

Acessar documentação Swagger UI:

http://127.0.0.1:8000/api/schema/swagger-ui/
