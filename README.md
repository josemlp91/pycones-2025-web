<<<<<<< HEAD
# Web PyConEs 2025


![](https://github.com/PythonGranada/pycones-grx/actions/workflows/deploy.yml/badge.svg)

### Creador de contenidos o editor ✍️

Aquí no necesitas tener grandes conocimientos técnicos, solo necesitamos creatividad.
Todos los contenidos se escriben usando [Markdown](https://markdown.es/) y no tienes que pelearte con HTML ni CSS, solo darle rienda suelta a tu imaginación.

### Web developer 🕸

Si tienes conocimientos de maquetación web y un poco de gusto estético, puedes ayudar a mejorar aspectos de diseño o usabilidad de la web.
En principio estamos usando [Bulma Framework](https://bulma.io/), pero siempre se puede cambiar a algo más avanzado si merece la pena.


## Al cacharreo  🛠

La web es generada usando [Pelican](https://blog.getpelican.com/), que nos ahorra hacer trabajo aburrido, tener que usar copy/paste constantemente y otras muchas magias divertidas con Python que poco a poco irás descubriendo.


### Estructura del proyecto 📂

El proyecto queda estructurado en los siguientes directorios:
Divido los directorios en tres **categorías**.

1. **Infra**, su propósito es preparar el entorno, instalar las dependencias y otras magias.
2. **UI / UX**, contiene el código para darle forma y color a la web, generalmente HTML, CSS.
3. **Content**, contiene artículos y publicaciones en markdown.
4. **Code**, contiene scripts en python para hacer pequeñas magias con Pelican y Python.

Y tendríamos los siguientes directorios:

- **.github** (infra) Aquí se definen las cosas referentes a la integración continua, (mejor no tocarlo mucho xD)
- **compose** (infra) Aquí se definen los manifiestos Docker, que preparan todo lo necesario para que funcione en tu localhost.
- **content** (content) Aquí se alojan los artículos y publicaciones en formato Markdown.
- **plugins** (code) Plugins de Pelican.
- **themes** (ui/ux) Código HTML y CSS que pone bonita la web.
- **output** (auto generado) Aquí se guarda el código de la web compilado, se genera automáticamente, por lo tanto **no modifiques manualmente**.


### Localhost 👨🏼‍💻

Para arrancar este proyecto en local, independientemente del sistema operativo que uses, tienes dos alternativas


#### Docker 🐳

Para ello necesitas [Docker](https://www.docker.com/get-started) y [docker-compose](https://docs.docker.com/compose/install/).

```sh
docker-compose up --build
```

Accede con tu navegador a la url [localhost:8080](http://localhost:8080)

#### Python & Virtualenv 🐍

Debes tener instalado Python >= 3.6 y [virtualenv](https://virtualenv.pypa.io/en/latest/) y seguir los siguientes pasos:

1. Crear un virtualenv propio para este proyecto y activarlo

```bash
virtualenv venv
source ./venv/bin/activate
```

2. Instalar las dependencias Python necesarias

```bash
pip install -r requirements.txt
```

3. Iniciar el servidor web en local con el script o con make indicando de forma opcional el puerto deseado (por defecto 8000)

- Opción 1
```bash
./develop_server.sh start {PORT}
```

- Opción 2
```bash
 make devserver PORT={PORT}
```

## Flag del evento 🏁

Como sabemos cualquier evento o congreso pasa por diferentes etapas, donde la información a mostrar en la web debe ser diferente.
Para facilitar el trabajo contamos con el archivo **pelicanconf_flags.py** donde el organizador puede habilitar y deshabilitar elementos de la web.


| Variable                  | Descripción                                                  |
| ------------------------- | ------------------------------------------------------------ |
| LANDING_MODE              | Habilita el modo landing-page de la web, para poder tener una presentación reducida o completa de la web. |
| ENABLED_TICKETS           | Habilita links a la tienda de las entradas del evento.       |
| ENABLED_CALL_FOR_PAPERS   | Habilita bloque que hace la llamada a los ponentes.          |
| ENABLED_KEYNOTERS         | Habilita bloque que muestra los oradores plenarios del evento. |
| ENABLED_SPEAKERS          | Habilita pantalla de ponentes.                               |
| ENABLED_SPONSORSHIPS      | Habilita bloque con todos los patrocinadores.                |
| ENABLED_CALL_FOR_SPONSORS | Habilita bloque con llamamiento a patrocinadores             |
| ENABLED_TIMETABLE         | Habilita la vista del calendario del evento.                 |
| ENABLED_BLOG              | Habilita la funcionalidad de blog de contenidos de la web.   |
| ENABLED_SCHEDULE_INFO     | Habilita la vista del la información del programa en el sitio principal |

## Despliegue y puesta en producción de la web 🚀

La web cuenta con un sistema de despliegue continuo, de forma que cada cambio (commit) en la rama ``main`` la web se compila y se sube a ``github pages``, usando [GitHub Pages Pelican Build Action](https://github.com/marketplace/actions/github-pages-pelican-build-action).

## Guía para contribuir

1. Crea un fork de este repositorio en tu cuenta personal de GitHub.
2. Puedes visualizar tu clone de la web, si habilitas la opción ghpages en la rama ``gh-pages``.

![](https://github.com/PythonGranada/pycones-grx/blob/main/readme_images/ghpages.png?raw=true)

3. Para que se visualice correctamente debes crear un ``environment secret`` llamado ``SITEURL`` con la url completa de tu copia del sitio web.

![](https://github.com/PythonGranada/pycones-grx/blob/main/readme_images/environ.png?raw=true)

4. Realiza tus aportaciones, añade los cambios, siempre con un mensaje de commit descriptivo y a poder ser en Inglés.
5. Crea un ``Pull Request`` a este mismo repositorio, asegúrate primero de hacer ``Fetch upstream`` y no tener conflictos con el repositorio principal.
6. Cuando se acepte el PR se te notifica y ya podemos ver tus cambios en la web.

### Con la consola Github CLI

```bash
# Haces fork del repositorio y clone localmente.
gh repo fork git@github.com:PythonGranada/pycones-grx.git

# Actualizamos fork con cambios en repositorio principal.
git pull upstream main

# Actualizamos cambios en nuestro fork particular.
git commit -am "commit message"
git push

# Creamos pull request con nuestros cambios
gh pr create
```

### Herramientas para desarrollar

- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [GitHub CLI](https://cli.github.com/)
- [Python ^3.6](https://www.python.org/downloads/)
- [pre-commit](https://pre-commit.com/)
- [Docker y Docker-Compose](https://www.docker.com/)
- Editor de código o IDE, [Visual Studio Code](https://code.visualstudio.com/) o [WebStorm](https://www.jetbrains.com/es-es/webstorm/)
=======
# pycones-2025-web
>>>>>>> 4d75137195b0d2e2c8756fa763aaf68e6c71375f
