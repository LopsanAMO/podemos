# Transacciones
Crear transacciones

## Crear transacciones

**Request**:

`POST` `/api/v1/transactions/transaction/`

Parametros:

Name       | Type    | Required | Description
-----------|---------|----------|------------
date       | string  | Yes      | La fecha del pago efectuado
amount     | decimal | Yes      | El monto de la cantidad pagada
account    | string  | Yes      | El id de la cuenta a la cual se le hara el pago


**Response**:

```json
Content-Type application/json
200 OK
```

