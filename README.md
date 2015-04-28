# Libmgmt
Install Instructions:
			1. Clone the repo
			2. Open librarymgmt/setting.py and create mysql database accordingly. Edit MySql configurations there
			3. Download "registration" package using "pip install django-registration-redux"
			4. Run python manage.py migrate followed by python manage.py createsuperuser
		
		Run the server and head to admin page servername:port/admin
		login there with credentials and create 2 groups in there namely "students" and "teachers"
		
		Route to servername:port/lend login as admin 
			1. Add books to the library
			2. Add users to the library
						
						ASK USERS TO REGISTER WITH OUR SITE
			
			1. Once registered they can lend books from library
			2. Mark it students can lend only 3 books from library and teachers can lend 6
			
		Features Added for Users Accounts
			1. Change there password 
			2. Can reset it
			3. Password Stored into hashes
			4. Make a note that only admin can add books to stock
