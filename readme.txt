https://openclassrooms.com/fr/courses/4425076-decouvrez-le-framework-django
cd disquaire
python -m venv venv
venv\Scripts\activate
pip install django
python -m django --version

pip install psycopg2
pip install django-debug-toolbar
pip install black
pip install pyinstaller ++++++ a revoire 
pip install PyMySQL

pip freeze > requirements.txt
pip install -r requirements.txt

django-admin
django-admin startproject disquaire_project
cd disquaire_project
django-admin startapp store



disquaire_project\manage.py
disquaire_project\manage.py help
disquaire_project\manage.py makemigrations ++ apres avoir regler la configuration du model corespondant
disquaire_project\manage.py migrate
disquaire_project\manage.py sqlmigrate store 0001


disquaire_project\manage.py shell
disquaire_project\manage.py dbshell #added the directory D:\sqlite3  to the environment variable PATH

disquaire_project\manage.py createsuperuser
disquaire_project\manage.py collectstatic

disquaire_project\manage.py runserver 8080
venv\Scripts\deactivate

