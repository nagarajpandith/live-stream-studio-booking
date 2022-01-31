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
Website to book Live Stream Studio and Manage bookings. 
1. Backend Framework: **Django**
2. Front-end Framework: **Bootstrap**

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#features">Features</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#development-notes">Development Notes</a></li>
    <li><a href="#screenshots">Screenshots</a></li>
    <li><a href="#project-maintainers">Project Maintainers</a></li>
    <li><a href="#license">License</a></li>
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
1. - Fork the [repo](https://github.com/nagarajpandith/live-stream-studio-booking)
   - Clone the repo to your local system
    ```git
    git clone https://github.com/nagarajpandith/live-stream-studio-booking.git
    cd live-stream-studio-booking 
    ```
2. Create a Virtual Environment for the Project
    - In Windows
    ```bash
    python -m venv env
    
    env\Scripts\activate
    ```

    - In Ubuntu/MacOS
    ```bash
    python -m virtualenv env
    
    source env/bin/activate
    ```
    If you are giving a different name then `env`, mention it in `.gitignore` first   

3. Install all the requirements
    ```bash
    pip install -r requirements.txt
    ```
4. Create .env file in the directory and enter the config parameters (without the quotes)
    ```python
   
   SK = 'Enter random character string'
   EADDRESS= 'Enter your email'
   EPASSWORD= 'Enter your email password'

    ```
    
5. Make migrations/ Create db.sqlite3

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
6. Create a super user.
    This is to access Admin panel and admin specific pages.
    ```djangotemplate
    python manage.py createsuperuser
    ```
    Enter your username, email and password.
    
7. Run server
    ```bash
    python manage.py runserver
    ```
    
### Development Notes
- If mailing causes SMTP Authentication errors, Enable [Less secure apps](https://www.google.com/settings/security/lesssecureapps) on your google account. If still facing the error, Enable [2FA](https://myaccount.google.com/signinoptions/two-step-verification/enroll-welcome?pli=1) and generate [App specific password](https://support.google.com/accounts/answer/185833?hl=en). Enter the 16 digit password generated in 'EPASSWORD' of .env file.

- To turn on Debugging, set
    ```python
    Debug = True 
    ```
    in project/settings.py.
    
- Disable Debugging to view custom error pages. 
    ```python
    Debug = False
    ALLOWED_HOSTS = ['your localhost url' or simply '*']
    ```
    in project/settings.py. 

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

- 404 page to users on Admin-specific pages
<img src="https://i.postimg.cc/sx1mRrbd/Screenshot-2022-01-31-at-8-57-49-AM.png" alt="404">

### Project Maintainers
| <img src = "https://avatars.githubusercontent.com/u/83623339?v=4" width="50px"> | <img src = "https://avatars.githubusercontent.com/u/75678927?v=4" width="50px"> | 
| :----------------------------------------------------------: | :----------------------------------------------------------: | 
| [Nagaraj Pandith](https://github.com/nagarajpandith/) |  [Kishor Balgi](https://github.com/KishorBalgi/)   |

### License
[Apache License 2.0](https://github.com/nagarajpandith/live-stream-studio-booking/blob/master/LICENSE)