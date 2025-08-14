# Introducción práctica a Git

## Prerrequisitos

- Tener Visual Studio Code instalado en la computadora.

## Indice de contenidos

- [1. Crear cuenta de GitHub](#1-crear-cuenta-de-github)
- [2. Instalar Git](#2-instalar-git)
- [3. Crear un repositorio local](#3-crear-un-repositorio-local)
- [4. Crear un nuevo repositorio remoto](#4-crear-un-nuevo-repositorio-remoto)
- [5. Clonar un repositorio remoto existente](#5-clonar-un-repositorio-remoto-existente)

## 1. Crear cuenta de GitHub

Entramos en [GitHub](https://github.com/) e ingresamos nuestro email institucional, al lado del botón *Sign up for GitHub*.

![Screenshot 6.png](../.img/instructivo-git/Screenshot%206.png)

Hacemos clic sobre el botón *Sign up for GitHub* y llenamos el formulario. Al finalizar, hacemos clic sobre *Continue*.

![Screenshot 7.png](../.img/instructivo-git/Screenshot%207.png)

Verificamos que somos un humano...

![Screenshot 8.png](../.img/instructivo-git/Screenshot%208.png)

Ingresamos el OTP que nos enviaron a la casilla de email:

![Screenshot 9.png](../.img/instructivo-git/Screenshot%209.png)

Y finalmente nos logueamos con mail y contraseña:

![Screenshot 10.png](../.img/instructivo-git/Screenshot%2010.png)

Con estos pasos completados, ya tenemos una cuenta en GitHub para subir y descargar nuestros repositorios de código.

## 2. Instalar Git

Para descargar Git, podemos abrir Visual Studio Code y dirigirnos al botón de *`Source Control`* en la barra lateral izquierda.

![Screenshot 1.png](../.img/instructivo-git/Screenshot%201.png)

Hacemos clic sobre el botón *`Download Git for Windows`* que nos llevará a la página oficial de descargas de Git.

![Screenshot 2.png](../.img/instructivo-git/Screenshot%202.png)

Hacemos clic sobre el link *`Click here to download`* y ejecutamos el archivo .exe que se descarga.

![Screenshot 3.png](../.img/instructivo-git/Screenshot%203.png)

Instalamos el programa (dejando todas las opciones por default) y destildamos las dos opciones del paso final.

![Screenshot 4.png](../.img/instructivo-git/Screenshot%204.png)

Volvemos a Visual Studio Code y hacemos clic sobre *`reload`*.

![Screenshot 5.png](../.img/instructivo-git/Screenshot%205.png)

Por último, vamos a identificarnos en Git con un nombre y un email (no necesariamente los mismos que usamos al crear la cuenta de GitHub).

Para hacer esto, vamos a abrir el Menú Inicio y buscar `Terminal` (o `Windows PowerShell`) y la vamos a abrir.

![Screenshot 11.png](../.img/instructivo-git/Screenshot%2011.png)

Vamos a correr dos comandos (por única vez):

```bash
git config --global user.name "Nombre Apellido"
```
(luego apretamos `Enter`)

```bash
git config --global user.email "ejemplo@mail.com"
```

(luego apretamos `Enter`)

En mi caso se ve así:

![Screenshot 12.png](../.img/instructivo-git/Screenshot%2012.png)

Con estos pasos completados, ya tenemos Git instalado, configurado y listo para usar en conjunto con Visual Studio Code.

## 3. Crear un repositorio local

Para crear un repositorio local, vamos a abrir una nueva instancia de Visual Studio Code y luego crear una carpeta nueva, haciendo clic en *`add a folder`*.

![Screenshot 13.png](../.img/instructivo-git/Screenshot%2013.png)

Vamos a guardar la carpeta, por ejemplo, dentro de Documentos, y la vamos a llamar `EDP`.

![Screenshot 14.png](../.img/instructivo-git/Screenshot%2014.png)

Hacemos clic sobre el botón *`Yes, I trust the authors`*.

![Screenshot 15.png](../.img/instructivo-git/Screenshot%2015.png)

Creamos un nuevo archivo de ejemplo haciendo clic en el botón *`New file...`*, y lo llamamos `script.py`:

![Screenshot 16.png](../.img/instructivo-git/Screenshot%2016.png)

Escribimos nuestro script con algún contenido (yo voy a escribir el típico `Hola mundo`):

![Screenshot 17.png](../.img/instructivo-git/Screenshot%2017.png)

Algo **muy** importante en Visual Studio Code es que nos marca en la pestaña que está al lado del nombre del archivo que estamos editando **con un círculo relleno** aquellos editores en donde **aún no guardamos los cambios**.

Luego de hacer `Ctrl + S`, el archivo se guarda en el disco duro y el círculo relleno se reemplaza por una cruz.

![Screenshot 18.png](../.img/instructivo-git/Screenshot%2018.png)

Volvemos a abrir el botón de *`Source Control`* en la barra lateral izquierda. En este punto estamos listos para inicializar nuestro repositorio, haciendo clic en el botón *`Initialize Repository`*.

![Screenshot 19.png](../.img/instructivo-git/Screenshot%2019.png)

Luego de inicializar el repositorio, veremos que la barra de *`Source Control`* se modifica para mostrarnos el control de cambios de nuestra carpeta.

![Screenshot 20.png](../.img/instructivo-git/Screenshot%2020.png)

Como podemos ver, Git detecta como cambio al archivo `script.py` con una letra `U`. La misma representa que el archivo no está siendo "seguido" por Git (untracked).

Para añadir este archivo al control de cambios, se puede hacer clic sobre el símbolo `+` (stage changes) que aparece al pasar el cursor sobre el nombre del archivo:

![Screenshot 21.png](../.img/instructivo-git/Screenshot%2021.png)

Luego de hacer esto, el archivo `script.py` se mueve del apartado *`Changes`* al apartado *`Staged Changes`*, con la letra `A` a la derecha. La misma representa que el archivo será "añadido" (added) al control de cambios.

Una vez que seleccionamos todos los cambios que queremos añadir al commit, es hora de elegir un mensaje para identificarlo. Aquí podríamos llamar a este commit, por ejemplo, `first commit`. Vamos a hacerlo escribiendo esto en el text box *`Message`*:

![Screenshot 22.png](../.img/instructivo-git/Screenshot%2022.png)

Finalmente, hacemos clic en el botón *`Commit`*.

![Screenshot 23.png](../.img/instructivo-git/Screenshot%2023.png)

Hemos realizado satisfactoriamente nuestro primer commit.

Supongamos ahora que nos toca como tarea traducir el mensaje "Hola mundo" al idioma inglés.

Lo que haríamos en este caso es volver al editor, modificar la línea correspondiente y guardar el archivo.

Al guardar el archivo, veremos que aparece `script.py` nuevamente dentro del apartado *`Changes`*, esta vez marcado con la letra `M` de modificado (modified).

![Screenshot 24.png](../.img/instructivo-git/Screenshot%2024.png)

Si hacemos clic sobre `script.py` podemos ver el cambio particular:

![Screenshot 25.png](../.img/instructivo-git/Screenshot%2025.png)

Vamos a commitear este cambio con el mensaje `traducción al inglés`:

![Screenshot 26.png](../.img/instructivo-git/Screenshot%2026.png)

Hacemos nuevamente clic en el botón *`Commit`*. Ya hicimos nuestros dos primeros commits, pero aún no están sincronizados con el repositorio remoto.

## 4. Crear un nuevo repositorio remoto

Si hacemos clic en el botón *`Publish branch`*, Visual Studio Code nos pedirá que nos identifiquemos en GitHub (por única vez):

![Screenshot 27.png](../.img/instructivo-git/Screenshot%2027.png)

Le damos clic al botón *`Allow`* y volvemos a ingresar nuestra información de login a GitHub:

![Screenshot 28.png](../.img/instructivo-git/Screenshot%2028.png)

Luego, autorizamos a Visual Studio Code para que haga cambios en GitHub a nuestro nombre:

![Screenshot 29.png](../.img/instructivo-git/Screenshot%2029.png)

Volvemos a Visual Studio Code haciendo clic en *`Abrir`*:

![Screenshot 30.png](../.img/instructivo-git/Screenshot%2030.png)

Le damos un nombre a nuestro nuevo repositorio (por defecto, el nombre de la carpeta sobre la que estamos trabajando) y elegimos entre:

- private repository: el contenido del repositorio solo será visible vía "invitación"
- public repository: el contenido del repositorio será visible para cualquiera que tenga el link

Ahora, es Git Credential Manager el que nos pide permisos. Hacemos clic sobre el botón *`Sign in with your browser`*:

![Screenshot 31.png](../.img/instructivo-git/Screenshot%2031.png)

Hacemos clic sobre el botón *`Authorize git-ecosystem`*:

![Screenshot 32.png](../.img/instructivo-git/Screenshot%2032.png)

Finalmente, volvemos a Visual Studio Code y encontramos la siguiente notificación, confirmando que el repositorio fue publicado a la nube:

![Screenshot 33.png](../.img/instructivo-git/Screenshot%2033.png)

En efecto, si hacemos clic en el botón *`Open on GitHub`* podremos ver que el mismo ya se encuentra en la nube:

![Screenshot 34.png](../.img/instructivo-git/Screenshot%2034.png)

## 5. Clonar un repositorio remoto existente

Veamos este último caso que se da cuando el repositorio ya se encuentra alojado en GitHub y lo queremos traer a nuestra computadora, es decir, *clonarlo*.

Para hacer esto, vamos a cerrar la carpeta abierta en Visual Studio Code haciendo clic en *`File`* > *`Close Folder`*:

![Screenshot 35.png](../.img/instructivo-git/Screenshot%2035.png)

Vamos a abrir el link al repositorio que queremos clonar, por ejemplo, este mismo repositorio: [link al repositorio](https://github.com/fabosso/edyp-s2-2025-c)

![Screenshot 36.png](../.img/instructivo-git/Screenshot%2036.png)

Hacemos clic en el botón *`<> Code`* y copiamos el link que aparece en la pestaña `HTTPS` (haciendo clic en el botón *`Copy url to clipboard`*):

![Screenshot 37.png](../.img/instructivo-git/Screenshot%2037.png)

Volvemos a Visual Studio Code y hacemos clic sobre el botón *`Clone Git Repository...`*:

![Screenshot 38.png](../.img/instructivo-git/Screenshot%2038.png)

Pegamos el link que habíamos copiado de GitHub en el recuadro que nos aparece, y apretamos `Enter`:

![Screenshot 39.png](../.img/instructivo-git/Screenshot%2039.png)

Elegimos una localización para la carpeta que se clonará, que **no** debe tener un repositorio de Git inicializado (yo por ejemplo, voy a elegir mi carpeta Documents):

![Screenshot 40.png](../.img/instructivo-git/Screenshot%2040.png)

Visual Studio Code nos pregunta si deseamos abrir el repositorio que acabamos de clonar, a lo que respondemos que sí, haciendo clic en el botón *`Open`*:

![Screenshot 41.png](../.img/instructivo-git/Screenshot%2041.png)

Hacemos clic sobre el botón *`Yes, I trust the authors`*.

![Screenshot 42.png](../.img/instructivo-git/Screenshot%2042.png)

Con estos pasos completados, hemos clonado exitosamente un repositorio remoto.

![Screenshot 43.png](../.img/instructivo-git/Screenshot%2043.png)
