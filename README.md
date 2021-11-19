# Reserva de Habitaciones

Reserva de habitaciones utilizando Django Rest Framework

## Setup

```
$ python3 -m venv .env
$ source .env/bin/activate
(.env) $ pip install -r requirements
(.env) $ ./manage runserver
```

## Indicaciones

El flujo de procesos para realizar la reserva a una habitación es la siguiente:

1. Registro de cliente
2. Inicio de sesión del cliente
3. Registrar habitaciones
4. Registrar reservación de habitaciones de clientes
5. Registrar de facturas

### **Registro de cliente**

[![Generic badge](https://img.shields.io/static/v1?label=status&message=<POST>&color=green)](https://shields.io/)

`/clients/signup`

Payload:

```
{
    "first_name": "<Tu-Nombre>:String",
    "last_name": "<Tu-Apellido>: String",
    "email": "<Tu-Email>: String",
    "password": "<Tu-Password>: String",
    "pass_confirmation": "<Confirmación-Password>: String",
}
```

### **Inicio de sesión del cliente**

[![Generic badge](https://img.shields.io/static/v1?label=status&message=<POST>&color=green)](https://shields.io/)

`/clients/singin`

Payload:

```
{
    "email": "<Tu-Email>: String",
    "password": "<Tu-Password>: String",
}
```

Ésto retornará el token de autenticación

```
{
    "token": "<El-Token-Obtenido>"
}
```

### **Registrar habitaciones _(Requiere Autenticación)_**

Es importante de ahora en adelante usar el token de autorización ya que todos los endpoints a continuación requerirán que el cliente esté autenticado.
_Agregar en el header con el siguiente formato_

```
Authorization: "Token <El-Token-Obtenido>"
```

[![Generic badge](https://img.shields.io/static/v1?label=status&message=<POST>&color=green)](https://shields.io/)

`/rooms/`

Tipos de Habitación:
`["IND", "DOUB", "TRIP", "QUAD", "ROOM"]`

Payload:

```
{
    "type": <Tipo-Habitación>: String,
    "price": <Precio-Habitación>: Float,
    "details": <Detalle-Habitación>: Text
}
```

### **Listar habitaciones _(Requiere Autenticación)_**

Tambien pueden listarse todas las habitaciones o filtrando por el tipo de habitación.

**Sin filtro**

[![Generic badge](https://img.shields.io/static/v1?label=status&message=<GET>&color=blue)](https://shields.io/)

`/rooms/`

**Con filtro**

[![Generic badge](https://img.shields.io/static/v1?label=status&message=<GET>&color=blue)](https://shields.io/)

`/rooms?type=<Tipo-Habitación>`

### **Registrar reservación _(Requiere Autenticación)_**

[![Generic badge](https://img.shields.io/static/v1?label=status&message=<POST>&color=green)](https://shields.io/)

`/booking/?room=<ID-HABITACIÓN>`

Payload:

```
{
    "stay_days": <Estancia-Días>: Int,
    "reserved_for": <Fecha-Reservado-Para>: Date,
    "payment_ammount": <Monto-Pago>: Float
}
```

### **Registrar Factura _(Requiere Autenticación)_**

[![Generic badge](https://img.shields.io/static/v1?label=status&message=<POST>&color=green)](https://shields.io/)

`/invoices/?booking_ids=<Ids-Rerservas-Separada-Por-Comas>`

Payload:

```
{
    "nit": <Nit-Client>: String
}
```
