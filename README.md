# live-stream-studio-booking
[Prototype](https://www.figma.com/file/WwhHu8pqO9LTpj8t4LoQjQ/Live-Stream-Studio-Website-Prototype)
In Windows

python -m venv env

env\Scripts\activate
In Ubuntu/MacOS

python -m virtualenv env

source env/bin/activate

Install all the requirements
pip install -r requirements.txt

Enter env variables EADRESS and EPASSWORD with your gmail and password
Enable [Less secure apps](https://www.google.com/settings/security/lesssecureapps) if it causes SMTP authentication error

Make migrations/ Create db.sqlite3
python manage.py makemigrations
python manage.py migrate

Run server
python manage.py runserver

to authenticate urself
python manage.py createsuperuser
enter credentials

Login on admin(http://127.0.0.1:8000/admin/)

