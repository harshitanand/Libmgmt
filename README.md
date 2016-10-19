# Libmgmt
A Library Management tool written in Django to perform basic tasks such as Issuing of Library books, Adding books, Assigning user passes etc can be managed.

![History Preview](https://raw.githubusercontent.com/harshitanand/Libmgmt/master/snapshots/issuehistory.png)

## Installation and Running

* Clone the repo
* Open librarymgmt/setting.py and create mysql database accordingly edit MySql configurations
* Download "registration" package using "pip install django-registration-redux"
* Run python manage.py migrate followed by python manage.py createsuperuser
* Run the server and head to admin page servername:port/admin
* login there with credentials and create 2 groups in there namely "students" and "teachers"
* Route to servername:port/lend login as admin 
	* Add books to the library
	* Add users to the library
	
	**ASK USERS TO REGISTER WITH OUR SITE**		
	  * Once registered they can lend books from library
	  * Mark it students can lend only 3 books from library and teachers can lend 6
			
## Features

* Change there password 
* Can reset it
* Password Stored into hashes
* Make a note that only admin can add books to stock

## License
>You can check out the full license [here](https://github.com/harshitanand/Libmgmt/blob/master/LICENSE)

This project is licensed under the terms of the **MIT** license.
