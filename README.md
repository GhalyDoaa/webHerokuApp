# webHerokuApp
basic simple python web app 

# Test Project is runnig locally
Make sure you cd into the correct folder (with all app files) before following the setup steps. Also, you need 
the latest version of Python 3 and postgres 
installed on your machine

run 
#### $expor FLASK_APP=app.y
then 
#### flask run --reload

# Test the end point with curl or postman and 

#Then create heroku Account and install heroku Cli
https://devcenter.heroku.com/categories/command-line

test installation using cli

#### $heroku login


# To deploy the app to heroku you need to config something

1)requirements.txt
For Python 3 use below

#### pip3 freeze > requirements.txt
but this saves all packages in the environment including those that you don't use in your current project.


You can use the following code to generate a requirements.txt file:

#### pip install pipreqs

#### pipreqs /path/to/project


2)setup.sh

here you put all the environment variables you use in project 
#### $export EXCITED="false"
#### $export DATABASE_URL="//the link you get from heroku //"



3)Config Vars on Heroku
put the same variable in 

4)Procfile

production file read about it from https://devcenter.heroku.com/articles/getting-started-with-python#define-a-procfile

write in it

web: gunicorn app:app





# Database Manage & Migrations on Heroku
take care that => heroku can apply you migrations
which means you do migration locally and upload files to heroku then run the migration upgrade command 

. localy 
install thos pack. 
#### pip3 install flask_script
#### pip3 install flask_migrate
#### pip3 install psycopg2-binary

### remember to include any new pack in requirements.txt

then run manage.py locally 

#### python manage.py db init
#### python manage.py db migrate
#### python manage.py db upgrade

and # DONE

in your folder you must have the same files that in this repo.

