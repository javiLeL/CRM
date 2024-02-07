# CRM 
## Que es este proyecto

Este es un *CRM* el cual esta escrito en python este cuenta con operaciones de tipo **CRUD** de:

- Clientes
- Oportunidades
- Presupuestos
- Producots
- Pedididos

Este tambien cuenta con un login el cual se usara para que cada usuario de la empresa se pueda conectar al *CMR* sin ningun tipo de problema.

Aparte de una representacion basica de las Oportunidades o *PIPELINE* clasica de la mayoria de los *CRMs* *(Esta no se actualiza a tiempo real por desconocimiento de uso de hilos en este lenguaje)*

## Base de datos

La base de datos usada es:

![](https://github.com/javiLeL/CRM/blob/main/diagrama_BBDD.png)

## Guia

### Como instalar el CMR

Pulsando [aqui](https://github.com/javiLeL/CRM/archive/refs/heads/main.zip) para descargar el `.zip`

o usando el siguiente comando para poder descargarlo *(Teniendo git en el dispositivo obiamente)*

```bash
git clone https://github.com/javiLeL/CRM.git
```

### Como iniciar el CRM

Tras tener instalado python ejecutar el archivo llamado `__init__.py` el cual tiene el gestor de arranque del programa. 

Esto se logra con algun tipo de **IDE** o por el contrario usando la terminal de python siempre que se encuentre en el mismo directorio que el programa y posea el programa python

```bash
python __init__.py
```

Desde cualquier terminal menos la de `Windows` con la cual se lanza con el comando

```bash
py __init__.py
```