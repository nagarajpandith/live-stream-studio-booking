<p align="center"> 
 <img src="https://raw.githubusercontent.com/nagarajpandith/live-stream-studio-booking/main/static/img/Logo.png?token=GHSAT0AAAAAABQJ6S5JNVU4ZPCAWL3B4N7WYP76GIA" alt="LOGO" border="0" width=200 height=100/>&nbsp;</a></p>

<p align="center">
<a href="https://www.python.org/"><img src="https://forthebadge.com/images/badges/made-with-python.svg" border="0" title="Made with Python" />
</p>

<p align="center">
<a href="http://www.djangoproject.com/"><img src="https://www.djangoproject.com/m/img/badges/djangopowered126x54.gif" border="0" alt="Powered by Django." title="Powered by Django." /></a>  
</p>
  
<p align="center">
<a href="https://github.com/nagarajpandith/live-stream-studio-booking/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/nagarajpandith/live-stream-studio-booking?style=for-the-badge"></a>
</p>

<p align="center">
<a href="https://github.com/nagarajpandith/live-stream-studio-booking/"><img alt="GitHub stars" src="https://img.shields.io/github/last-commit/nagarajpandith/live-stream-studio-booking"></a>
<a href="https://github.com/nagarajpandith/live-stream-studio-booking/blob/main/LICENSE"><img alt="GitHub License" src="https://img.shields.io/github/license/nagarajpandith/live-stream-studio-booking"></a>
</p>

## [Live-Stream Studio Booking Website]()

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#features">Features</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#screenshots">Screenshots</a></li>
  </ol>
</details>

### Features
- Responsive Full-stack Booking system
- Automated mail notifications on form submissions & on accepting/rejecting bookings
- Filter bookings on a range (Year/Month/Week/Day)
- Export selected data as .csv
- Manage bookings by Accepting/Rejecting 
- Avoid duplicate booking with a gap of 30 minutes between each event

### Installation
- In Windows
    ```bash
python -m venv env

env\Scripts\activate

- In Ubuntu/MacOS

python -m virtualenv env

source env/bin/activate

- Install all the requirements
'''python
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
'''git
- Before pushing create .gitignore file and enter env, .env and db.sqlite3

### Screenshots
- [Figma Prototype](https://www.figma.com/file/WwhHu8pqO9LTpj8t4LoQjQ/Live-Stream-Studio-Website-Prototype)

- Home Page
<img src="https://i.postimg.cc/zBC0xbjw/Screenshot-2022-01-30-at-10-22-46-PM.png" alt="Home Page">

- Booking Form
<img src="https://i.postimg.cc/65gnG6VB/Screenshot-2022-01-30-at-10-24-44-PM.png" alt="Booking Form">

- Admin Panel
<img src="https://i.postimg.cc/Hnj8VFVJ/Screenshot-2022-01-30-at-10-29-57-PM.png" alt="Admin Panel">

- Manage Bookings Page
<img src="https://i.postimg.cc/pTLp63Q0/Screenshot-2022-01-30-at-10-31-31-PM.png" alt="Manage Bookings">

- Example of an Automated mail
<img src="https://i.postimg.cc/638GQD78/Screenshot-2022-01-30-at-10-36-31-PM.png" alt="Mail">