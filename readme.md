# Proyecto E-commerce con Django

## Descripción
Este es un proyecto de e-commerce desarrollado con Django, que incluye funcionalidades de autenticación, gestión de productos, carrito de compras y pagos con Stripe.

## Requisitos Previos
- Anaconda
- Git
- Stripe CLI (opcional para webhooks)

## Configuración del Entorno de Desarrollo

### 1. Clonar el Repositorio
```bash
git https://github.com/EliazarNoaLlas/e_commerce_RestAPI-.git
cd e_commerce_RestAPI-
```

### 2.1 Crear Entorno Virtual con Anaconda
```bash
conda create -n django_ecommerce python=3.7.6 -y
conda activate django_ecommerce
```

### 2.2 Crear Entorno Virtual con PIP

1. Instalar virtualenv (si aún no lo tienes instalado):
```bash
pip install virtualenv
```

2. Crear el entorno virtual:
```bash
virtualenv django_ecommerce
```
3. Activar el entorno virtual:
```bash
.\django_ecommerce\Scripts\activate
```

### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 4. Configuración de Variables de Entorno
1. Crea un archivo `.env` en el directorio raíz del proyecto
2. Copia el contenido de `.env.copy` y completa las variables

Ejemplo de configuración de `.env`:
```
SECRET_KEY=kVMp1O3zzdAB4g0ZIOHOgNevSz9HUZ0w0QUfDuKRGMXHfenToNDjg41vjzXDNePG5bQ
DEBUG=True
STRIPE_TEST_PUBLIC_KEY=pk_test_51QP5rLDalEHjdVHvAyVJ9txZWLFwXq2xMCDSI1IZkkMDjoQzXm6vG7zgzUohQUbUUtZxpGSHxpmuZdKcSsUlF1Hj00WfipNhxY
STRIPE_TEST_SECRET_KEY=sk_test_51QP5rLDalEHjdVHvwF9PDfoW3ZfWo1i6cl1OPl7jeYjgNAY1pCaAmZS0ARHSwVYlAEQjXQRRg0CAwIJ8siNGftft007lzPPXoC
STRIPE_WEBHOOK_SECRET_KEY=
DB_NAME=my_ecommerce_db
DB_USER=
DB_PASSWORD=
DB_HOST=
```

#### Rellenar las variables

Completa cada clave con los valores apropiados. Aquí hay una descripción de lo que representa cada variable y cómo obtener su valor:

- **SECRET_KEY**  
  Esta es una clave secreta utilizada por Django para seguridad interna (como la protección CSRF).  
  Si no tienes una, puedes generar una ejecutando este comando en Python:
  
  ```python
  import secrets
  print(secrets.token_urlsafe(50))
   ```
  
- **DEBUG**
Indica si el servidor está en modo de desarrollo (True) o producción (False).
Durante el desarrollo, deja DEBUG=True.
- **STRIPE_SECRET_KEY** y **STRIPE_PUBLIC_KEY**
- https://dashboard.stripe.com/
Estas son claves de API para integrar Stripe en tu proyecto.
Ve a tu cuenta de Stripe y obtén las claves desde la sección API Keys.
Copia la clave secreta en STRIPE_SECRET_KEY y la clave pública en STRIPE_PUBLIC_KEY.
- **GOOGLE_CLIENT_ID y GOOGLE_CLIENT_SECRET**
Estas claves son necesarias para la autenticación con Google OAuth 2.0.
Ve a la Google API Console:
Crea un nuevo proyecto.
Habilita la API de OAuth 2.0.
Crea credenciales de cliente OAuth 2.0.
Configura el URI de redirección, por ejemplo:
```bash
http://127.0.0.1:8000/accounts/google/login/callback/
```
Obtén las claves generadas y copia los valores en las variables GOOGLE_CLIENT_ID y GOOGLE_CLIENT_SECRET.




### 5. Configurar Base de Datos
```bash
python manage.py migrate
```

### 6. Crear Superusuario
```bash
python manage.py createsuperuser
```

### 7. Ejecutar Servidor de Desarrollo
```bash
python manage.py runserver
```

Accede a la aplicación en: `http://127.0.0.1:8000`

## Configuraciones Adicionales

### Stripe Webhook (Opcional)
1. Instalar Stripe CLI
2. Configurar webhook:
```bash
stripe listen --forward-to localhost:8000/webhooks/stripe/
```

### Google OAuth 2.0 (Opcional)
1. Ir a Google API Console
2. Crear proyecto y habilitar OAuth 2.0
3. Configurar cliente OAuth con redirect URI:
   `http://127.0.0.1:8000/accounts/google/login/callback/`

## Notas Importantes
- Base de datos por defecto: SQLite
- Para producción:
  - Deshabilitar `DEBUG`
  - Configurar correctamente valores sensibles en `.env`

## Solución de Problemas
- Verificar que todas las variables de entorno estén configuradas correctamente
- Asegurarse de que todas las dependencias están instaladas
- Comprobar conexiones de API (Stripe, Google)

## Contribuciones
Las contribuciones son bienvenidas. Por favor, lee las pautas de contribución antes de enviar un pull request.

## Licencia


## Stripe webhook

To test and complete the order, stripe webhook must be working.

First, install [Stripe CLI]
Then run this command
```bash
stripe listen --forward-to localhost:8000/webhooks/stripe/
```


### ENLACES PARA LA INSTLACION DE LAS LIBRERIAS

Python: https://www.python.org/downloads/release/python-376/

 Django: https://www.djangoproject.com/download/
Template: https://mdbootstrap.com/freebies/jquery/e-commerce/

Stripe CLI: https://stripe.com/docs/stripe-cli#install
   
Stripe: https://stripe.com/
   
Google API: https://developers.google.com/identity/protocols/oauth2

### ENLACE DE LA DEMOSTRACION DEL REST API
https://user-images.githubusercontent.com/57330864/127233277-4d24491b-aec0-4d94-86e5-f7883843eafa.mp4