Los dos primeros: 

*python3 -m venv venv*

*source venv/bin/activate*

Son obligados primero porque son los que levantan el entorno virtual

Luego van los de instalar las dependencias en cualquier orden;

pip install django

pip install psycopg2-binary

python -m pip install Pillow

Y finalmente los comandos para levantar la página web, primero las migraciones para asegurarse, que juraría no es obligatorio

python3 manage.py migrate

python3 manage.py runserver 0.0.0.0:8080