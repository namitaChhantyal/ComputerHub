# ComputerHub
Computer Hub
Developed by: Namita Chhantyal

######This is computer hub website that displays the computer brands and its specifications.
Admin add the computer brands and its specification from admin panel

if user.is_superuser :


superuser can easily add the details of computer brand and it's specification from the admin page.
superuser can also delete the computers from the database.
if user.is not superuser:
user can buy computer

once order button is clicked it will update on admin panel which will let admin know about it.

Simply clone the project from Github and follow the procedure
Install all the packages used command from console

create Superadminr:


python manage.py createsuperuser //set username, email and password for superuser

Migrations:


pip install pillow
python manage.py migrate
python manage.py makemigrations

Run the server:


python manage.py runserver
