# Grupos
Listar, crear y modificar grupos

## Crear grupos

**Request**:

`POST` `/api/v1/groups/group/`

Parametros:

Name       | Type   | Required | Description
-----------|--------|----------|------------
name       | string | Yes      | El nombre del grupo


**Response**:

```json
Content-Type application/json
200 OK

{
    "name": "Nombre Apellido",
    "id": "47C83"
}
```

## Editar grupo

**Request**:

`PUT` `/api/v1/groups/group/:id/`

Parametros:

Name       | Type   | Required | Description
-----------|--------|----------|------------
name       | string | Yes      | El nombre del grupo


**Response**:

```json
Content-Type application/json
200 OK
```


## Lista de todos los grupos (con miembros)

**Request**:

`GET` `/api/v1/groups/members/`



**Response**:

```json
Content-Type application/json
200 OK
{
    "count": 5,
    "next": null,
    "previous": null,
    "results": [
        {
            "nombre": "POWERPUFF GIRLS",
            "miembros": [
                [
                    "GERTRUDIS LOPEZ MARTINEZ"
                ],
                [
                    "FERNANDA JUAREZ LOPEZ"
                ],
                [
                    "IRMA MARQUEZ RUBIO"
                ],
                [
                    "ALEIDA SANCHEZ AMOR"
                ]
            ],
            "id": "XYZW1"
        },
        {
            "nombre": "CHARLIE'S ANGELS",
            "miembros": [
                [
                    "LORENA GARCIA ROCHA"
                ],
                [
                    "ALBA PEREZ TORRES"
                ],
                [
                    "ELISEO CHAVEZ OLVERA"
                ],
                [
                    "SANDRA SANCHEZ GONZALEZ"
                ]
            ],
            "id": "ABCD2"
        },
        {
            "nombre": "KITTIE",
            "miembros": [
                [
                    "ANGELA GOMEZ MONROY"
                ],
                [
                    "KARLA ENRIQUEZ NAVARRETE"
                ],
                [
                    "DANIELA HERNANDEZ GUERRERO"
                ]
            ],
            "id": "GHIJK"
        },
    ]
}
```

## Detalle de grupo

**Request**:

`GET` `/api/v1/groups/detail/:id/`

*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
Content-Type application/json
200 OK

{
    "cuentas": [
        {
            "monto": 120000.0,
            "balance": "0.00",
            "calendario": [
                {
                    "num_pago": 1,
                    "monto": 20000.0,
                    "fecha_pago": "2020-05-18",
                    "estatus": "pen"
                },
                {
                    "num_pago": 2,
                    "monto": 20000.0,
                    "fecha_pago": "2020-05-25",
                    "estatus": "pen"
                },
                {
                    "num_pago": 3,
                    "monto": 20000.0,
                    "fecha_pago": "2020-06-01",
                    "estatus": "pen"
                },
                {
                    "num_pago": 4,
                    "monto": 20000.0,
                    "fecha_pago": "2020-06-08",
                    "estatus": "pen"
                },
                {
                    "num_pago": 5,
                    "monto": 20000.0,
                    "fecha_pago": "2020-06-15",
                    "estatus": "pen"
                },
                {
                    "num_pago": 6,
                    "monto": 20000.0,
                    "fecha_pago": "2020-06-22",
                    "estatus": "pen"
                }
            ],
            "transacciones": [
                {
                    "fecha": "2020-05-11T23:32:07.389241Z",
                    "monto": 2.0
                },
                {
                    "fecha": "2020-05-11T23:32:38.697572Z",
                    "monto": 119998.0
                }
            ],
            "id": "78139A5",
            "estatus": "CERRADA"
        }
    ]
}
```

## Agregar miembros al un grupo

**Request**:

`PUT` `/api/v1/groups/groups/:id`

Parametros:

Name       | Type   | Required | Description
-----------|--------|----------|------------
members    | list   | Yes      | Lista con id de clientes

**Response**:

```json
Content-Type application/json
200 OK
```

## Eliminar miembros de un grupo

**Request**:

`DEL` `/api/v1/groups/groups/:id`

Parametros:

Name       | Type   | Required | Description
-----------|--------|----------|------------
members    | list   | Yes      | Lista con id de clientes

**Response**:

```json
Content-Type application/json
200 OK
```
