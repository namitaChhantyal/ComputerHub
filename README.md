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


Some of Screenshots:
![home](https://user-images.githubusercontent.com/60824791/15![details](https://user-images.githubusercontent.com/60824791/156157878-587f75b0-1fc2-4b03-bce8-037abb99ff9b.jpg)
6157097-d16d2eaa-c96a-47c4-a7ee-ec369482e876.jpg)
![Order](https://user-images.githubusercontent.com/60824791/156158072-b640f69e-a35c-4b61-af93-a0b07f86e7f0.jpg)



admin side screenshots:
![admin](https://user-images.githubusercontent.com/60824791/156158004-c6df99fe-ae2c-44be-a8f4-2455969d958d.jpg)
![computerbrands](https://user-images.githubusercontent.com/60824791/156158021-d7487ce9-6331-42d7-9abf-34ac2856796d.jpg)![computerspecification](https://user-images.githubusercontent.com/60824791/156158034-fc93f629-4587-4e46-aedc-0226551f418a.jpg)
![Orders](https://user-images.githubusercontent.com/60824791/156158049-cf7e5792-11aa-4d12-aea8-78dc0836b996.jpg)



