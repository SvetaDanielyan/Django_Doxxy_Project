# Django_Doxxy_Project
application with multiple domains routing.

Here is the application with which we can run application with multiple host serving

### how to use ? (how to run)

1. open terminal (in ubuntu press alt + t)
2. type this command
```commandline
git clone https://github.com/SvetaDanielyan/Django_Doxxy_Project
```
3. go to the folder with command
```commandline
cd doxxy
```
4. you need to install all requirements that project needed for this you need to use pyhton venv (or something like conda)
```commandline
# First create virtual envirement for you project 
python3 -m venv venv
```
if you  have problem with this you can check officale documentation https://docs.python.org/3/library/venv.htm
5. install all requirements
```commandline
pip install -r requirements.txt
```
6. make all migrations
```commandline
python3 manage.py makemigrations
python3 manage.py migrate
```
7. run the project 
```commandline
python3 manage.py runserver
```

If you want you can change allowed urls from settings.py line 29, for now it's looks like this
```commandline
ALLOWED_HOSTS = ['en.superproject.localhost', 'de.superproject.localhost', 'fr.superproject.localhost']
```
so you can see application with this urls...
