# Cuentas
Crear Cuentas

## Crear Cuentas

**Request**:

`POST` `/api/v1/accounts/accounts/`

Parametros:

Name            | Type    | Required | Description
----------------|---------|----------|------------
group           | string  | Yes      | El id del grupo
amount          | decimal | Yes      | El monto de la cantidad prestada
balance         | string  | Yes      | El monto que se debe
num_payments    | string  | Yes      | El numero de pagos en la que se dividira el monto a deber


**Response**:

```json
Content-Type application/json
200 OK
```

