# DOM App


## 1. Instalación

Para descargar la aplicación del repo, se debe escribir el siguiente comando:

```
$ git clone https://github.com/FragmentosTemporales/email_sender.git
```

### Servidor de correo electrónico

```
app.fastmail.com
```

### Variables de entorno

Al interior de la carpeta debes crear un documento .env el cual debe contener las siguiente variables, puedes guiarte con el documento example.env :

```
EMAIL_PASSWORD = 
EMAIL_USER = 
EMAIL_RECEIVER = 
```

### Instalación

Para instalar la aplicación debes ejecutar el siguiente código, es necesario que las variables de entorno estén definidas para este punto:

```
$ pip install virtualenv
```

Posteriormente debes crear el entorno:

```
$ python -m venv venv
```

Activa el entorno de trabajo ejecutando el siguiente comando:

```
$ venv\scripts\activate
```

Una vez creado el entorno de trabajo, puedes instalar las librerías requeridas:

```
$ pip install -r requirements.txt
```

## 2. Ejecución

Para ejecutar la aplicación debes ingresar (desde la consola) el siguiente comando:

```
$ python main.py
```

Saludos!