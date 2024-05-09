# python -m venv venv

# venv\Scripts\activate

# pip install django

# ------------------------------------------------------------------------------

# django-admin startproject app .

# python manage.py runserver

# ------------------------------------------------------------------------------

### Criar apps

# python manage.py startapp cars-por-exemplo

# ------------------------------------------------------------------------------

### Pegam os models e jogam para o banco de dados

# python manage.py makemigrations

# python manage.py migrate

# ------------------------------------------------------------------------------

### Para criar o super usuario que tem acesso ao admin do Django

# python manage.py createsuperuser

### Para manipular imagens

# python -m pip install Pillow

# ------------------------------------------------------------------------------

### para criar um arquivo listando as libs, para boas praticas

# pip freeze > requirements.txt

# pip install -r ./requirements.txt
