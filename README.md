# Intranet del Ayuntamiento de Santa Úrsula

Aplicación web desarrollada con Django para centralizar la gestión interna de recursos y servicios municipales. El proyecto está en desarrollo y varias pantallas y funciones todavía necesitan completarse antes de poder utilizarlo como una intranet operativa.

## Funcionalidades y módulos

| Módulo | Contenido actual |
| --- | --- |
| `accounts` | Inicio de sesión, cierre de sesión y registro de usuarios. |
| `empleados` | Gestión de empleados y registros de vacaciones. |
| `areas` | Gestión de áreas y asignación de responsables y sedes. |
| `sedes` | Sedes, plantas y telecomunicaciones. |
| `extensiones` | Extensiones telefónicas fijas y móviles, y dispositivos móviles. |
| `equipos` | Proveedores, equipos, préstamos, pantallas, periféricos e impresoras. |
| `solicitudes` | Solicitudes vinculadas a llaves, vehículos, lugares y empleados. |
| `permisos` | Modelo y formulario de permisos; las vistas y rutas todavía no están implementadas. |
| `shared` | Modelos compartidos, actualmente incluye buzones de correo. |

Las rutas principales se configuran en `main/urls.py`. Las vistas de gestión están protegidas para usuarios autenticados, aunque aún falta definir permisos por rol.

### Rutas disponibles en el código

| Prefijo | Uso |
| --- | --- |
| `/admin/` | Administración integrada de Django. |
| `/accounts/` | Login, logout y registro. |
| `/empleados/` | Empleados y vacaciones. |
| `/areas/` | Áreas municipales. |
| `/sedes/` | Sedes; también `/sedes/plantas/` y `/sedes/telecomunicaciones/`. |
| `/extensiones/` | Extensiones fijas y móviles, y dispositivos. |
| `/equipos/` | Proveedores, equipos, préstamos, pantallas, periféricos e impresoras. |
| `/solicitudes/` | Solicitudes, llaves, vehículos y lugares. |

Estas rutas identifican las vistas declaradas, pero las páginas no estarán utilizables hasta que se creen las plantillas que faltan. La raíz `/` y el módulo `permisos` todavía no tienen páginas funcionales.

## Tecnologías

- Python 3.12 o superior (`.python-version` especifica 3.12).
- Django 6.0.2 o superior.
- PostgreSQL.
- [uv](https://docs.astral.sh/uv/) para sincronizar las dependencias declaradas en `pyproject.toml` y `uv.lock`.
- `just` es opcional y permite utilizar los comandos definidos en `justfile`.

## Preparación del entorno

1. Instala Python 3.12, PostgreSQL y `uv`.
2. Crea una base de datos y un usuario de PostgreSQL para el proyecto.
3. Clona el repositorio y entra en su directorio:

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd IntranetSantaUrsula
   ```

4. Sincroniza el entorno y las dependencias:

   ```bash
   uv sync
   ```

5. Copia `.env.example` a `.env`, genera una clave de Django nueva y completa las variables de PostgreSQL. La configuración carga estos valores desde el entorno; no guardes el archivo `.env` en Git.

   ```bash
   cp .env.example .env
   uv run python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
   ```

   Pega la clave generada en `DJANGO_SECRET_KEY` dentro de `.env`, completa `DB_USER` y `DB_PASSWORD`, y carga las variables en la terminal:

   ```bash
   set -a
   source .env
   set +a
   ```

6. Cuando los errores de modelos descritos en «Estado y limitaciones» estén corregidos, aplica las migraciones, crea una cuenta administrativa e inicia el servidor:

   ```bash
   uv run python manage.py migrate
   uv run python manage.py createsuperuser
   uv run python manage.py runserver
   ```

   El servidor de desarrollo estará disponible en `http://127.0.0.1:8000/`.

Para comprobar la configuración de Django se puede ejecutar:

```bash
uv run python manage.py check
```

El archivo `justfile` contiene equivalentes como `just check`, `just migrate` y `just dev`.

## Estado y limitaciones conocidas

- **El proyecto necesita correcciones antes de arrancar correctamente.** Hay varios `models.CharField` sin `max_length`, lo que provoca errores en las comprobaciones de Django y en la generación de migraciones.
- **Faltan las plantillas usadas por las vistas.** En las carpetas `templates` solo aparecen plantillas de ejemplo, mientras que las vistas solicitan nombres como `empleados/employee_list.html` y `equipos/equipo_list.html`. Al acceder a esas páginas Django devolverá `TemplateDoesNotExist`.
- **No hay página de inicio configurada.** La raíz `/` no tiene ruta, y el flujo de autenticación redirige al nombre de URL `index`, que no está definido.
- **El módulo `permisos` está incompleto.** `permisos/urls.py` referencia funciones que no existen en `permisos/views.py`, y sus rutas no están incluidas en `main/urls.py`.
- **La aplicación está restringida a personal (`is_staff`).** El registro de cuentas nuevas requiere una cuenta superusuario y crea una cuenta de personal. Las vistas de gestión requieren personal autenticado. El parámetro `next` del login solo permite redirecciones al mismo host.
- **La configuración requiere ajustes para producción.** `DEBUG` está desactivado de forma predeterminada y `ALLOWED_HOSTS` solo permite `localhost` y `127.0.0.1`. En producción define los hosts correctos, sirve el sitio por HTTPS, activa `DJANGO_SECURE_COOKIES` y configura `DJANGO_SECURE_SSL_REDIRECT` según el proxy TLS.
- **Hay tipos de datos que no representan bien los valores previstos.** Las direcciones IP están modeladas como enteros en `equipos`, y el PUK de telefonía como entero pequeño, insuficiente para un PUK habitual de ocho cifras.
- **La configuración de despliegue está incompleta.** `run.sh` espera un entorno `.venv` y Gunicorn, pero Gunicorn no figura entre las dependencias del proyecto.
- **Hay archivos locales y generados dentro del proyecto.** La copia contiene un entorno virtual (`intranet/`), `db.sqlite3` y bytecode de Python. `.gitignore` los excluye de nuevos commits, pero siguen en el disco local.

## Estructura del proyecto

```text
.
├── accounts/       # Autenticación y registro
├── areas/          # Áreas municipales
├── empleados/      # Empleados y vacaciones
├── equipos/        # Inventario y préstamos
├── extensiones/    # Telefonía y dispositivos
├── main/           # Configuración y rutas del proyecto Django
├── permisos/       # Modelo de permisos, pendiente de completar
├── sedes/          # Sedes, plantas y telecomunicaciones
├── shared/         # Modelos compartidos
└── solicitudes/    # Solicitudes de recursos
```

Las migraciones de cada aplicación están en su subcarpeta `migrations/`. Los modelos definen el esquema de datos y las vistas, formularios y rutas de cada aplicación se encuentran en sus archivos `views.py`, `forms.py` y `urls.py`.

## Comandos útiles

```bash
uv run python manage.py check       # Comprobaciones de Django
uv run python manage.py makemigrations
uv run python manage.py migrate
uv run python manage.py createsuperuser
uv run python manage.py runserver
```

## Seguridad de datos

No guardes contraseñas, claves secretas, datos personales reales ni bases de datos locales en el repositorio. Las credenciales que estaban en la copia de origen se han retirado de estos archivos de trabajo; si llegaron a un remoto, rota esas credenciales y la clave de Django. `.gitignore` evita nuevas inclusiones accidentales, pero no borra archivos de commits anteriores ni del repositorio de origen.
