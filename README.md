# API

#Setup virtual environment using: 
python3 -m venv (name_of_virtual_environment)

#activate it using
source (name_of_virtual_environment)/bin/activate

run pip -r install requirements.txt

run python manage.py migrate
run python manage.py makemigrations
run python manage.py runserver

Following are the API endpoints and their method with parameter:

     API Endpoint               Method                     Parameters
1)    /login                     POST                         email
                                                              password
                                                              
2)   /create                     POST                         password
                                                              email
                                                              first_name
                                                              last_name

3)   /reset                      POST                         email
                                                              password


