# travello-Django-Website

# Set Up Steps:

1) Create a virutal environment and install Django in environment. 

pip install virtualenvwrapper-win
mkvirtualenv testdjango

pip install django

To switch into virtual envirnment we use below command:
workon testdjango

2) We create the apps in django project a single app or website can use multiple django apps.

django-admin startproject djangoWebProject

djangoWebProject is the project name

3) We create the apps using below command 

python manage.py startapp accounts

4) after creating the apps we mention the redirection in urls.py in project and as well django app.

we mention redirection in urlpatterns :
    path('travello/',include('travello.urls'))
	
Here travello is our app name	

5)	Inside the app we redirect to view method define for redirection

    path('', views.index , name ='index'),
	
6) So we are now in the method index inside views.py where we either get parameter's from GET or POST method.
 request.POST['first_name']
 
7) In travello app we create a ORM model for destination class where the destination places are fetched from DB and update in frontend.

8) We stored all the images in static folder which will be easy for access for templates.

we load static by {% load static %}

we access the images with the command similar to 

 <link rel="stylesheet" type="text/css" href="{% static 'styles/responsive.css' %}">


# Creation of a Model to create/fetch table

1) We define our classes in the apps model.py here the model is Destination which extends the class models.Model
which will converted to table and stored in postgre DB.

class Destination(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to = 'pics')
    desc = models.TextField(max_length=250)
    price = models.IntegerField(default =0)
	
	// here we are declaring the data types for the class which will be our columns of table
	
2) In admin.py of travello app we need to register our model as below :

admin.site.register(Destination) 

3) After the creation of model we migrate it to DB using the following command
python manage.py makemigrations  

	a)We need to configure the database in settings.py from djangoproject.
	b) 
	
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'djangoDB',
        'USER' :'postgres',
        'PASSWORD' :'root',
        'HOST' : 'localhost'
    }
}

4) for migration 
	a) python manage.py makemigrations   # which converts the model into sql query.
	b) python manage.py sqlmigrate travello 0001 # to check the sql query.
	c) python manage.py migrate # to execute the SQL query.

5)After migrating for first time we upload some django models like auth_user ,auth_group which are useful in creating a login functionality.

We need to create superuser by running  
python manage.py createsuperuser and login into http://localhost:8000/admin/

from the admin page we can create the data to store in the DB.

# Creation of Registration page

1) For this we have created the accounts app & register.html page were we send through the post method .

2) We are using the post method  for allowing the user to register.
We use 
 
                user = User.objects.create_user(username=user_name,
                                                first_name=first_name,
                                                last_name=last_name,
                                                email=email,
                                                password=password1                                         
                                                )
                user.save()
				
				to save data in DB

3) We use 
from django.contrib.auth.models import User,auth

django inbuilt methods User.objects.filter(username = user_name).exists() to check username exists
and User.objects.filter(email = email).exists() if email is already taken

# login and logout of page

1) for login we used login page where we login the user using auth module

            auth.login(request,user)
2) for logout we use below method

    auth.logout(request)


# {% csrf_token %} usage 

The CSRF middleware and template tag provides easy-to-use protection against Cross Site Request Forgeries. This type of attack occurs when a malicious website contains a link, a form button or some JavaScript that is intended to perform some action on your website, using the credentials of a logged-in user who visits the malicious site in their browser. A related type of attack, ‘login CSRF’, where an attacking site tricks a user’s browser into logging into a site with someone else’s credentials, is also covered.


 