# Clientes
Crear y modificar clientes

## Crear clientes

**Request**:

`POST` `/api/v1/users/client/`

Parametros:

Name       | Type   | Required | Description
-----------|--------|----------|------------
name       | string | Yes      | El nombre completo del cliente


**Response**:

```json
Content-Type application/json
200 OK

{
    "id": "5936B71"
}
```

## Editar clientes

**Request**:

`PUT` `api/v1/users/client/:id/`

Parametros:

Name       | Type   | Required | Description
-----------|--------|----------|------------
name       | string | Yes      | El nombre completo del cliente


**Response**:

```json
Content-Type application/json
200 OK
```
