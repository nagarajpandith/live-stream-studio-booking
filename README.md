# live-stream-studio-booking
[Prototype](https://www.figma.com/file/WwhHu8pqO9LTpj8t4LoQjQ/Live-Stream-Studio-Website-Prototype)

- In Windows

python -m venv env

env\Scripts\activate

- In Ubuntu/MacOS

python -m virtualenv env

source env/bin/activate

- Install all the requirements
pip install -r requirements.txt

- Create .env file and enter SK=django-insecure-*&t17oo6wt7uyml@jbg=zj91y!_j!#)z)430(@749x6*q#j_#l
- Enter env variables EADRESS=your gmail and EPASSWORD=password
- Enable [Less secure apps](https://www.google.com/settings/security/lesssecureapps) if it causes SMTP authentication error

- Make migrations/Create db.sqlite3
python manage.py makemigrations
python manage.py migrate

- Run server
python manage.py runserver

- To authenticate urself as admin
python manage.py createsuperuser
Enter credentials

- Login on admin(http://127.0.0.1:8000/admin/)

- Before pushing create .gitignore file and enter env, .env and db.sqlite3
