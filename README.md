# Portfolio Website

## Steps to Running/Exiting the Program
1. Install pipenv by typing `pip install pipenv` or `pip3 install pipenv` for python3 users
2. In `project` folder, install dependencies by typing `pipenv install`
3. In `project` folder, enter virtual environment by typing `pipenv shell`
4. In `project` folder, run app by typing `python manage.py runserver`
5. View the project by opening a browser like Chrome and entering the provided url (i.e. `http://127.0.0.1:8000/`)
6. When done, exit by pressing `Ctrl`+`C` and virtual environment by typing `exit`

## Accessing Admin Panel
1. In `project` folder, run `python manage.py createsuperuser` if admin user not setup
2. Access admin panel by entering the extension `/admin` to main url (i.e. `http://127.0.0.1:8000/admin`)


## Deploying Django App to Amazon AWS, Elastic Beanstalk
**Note:** The instruction is based on this [video](https://www.youtube.com/watch?v=ypnEf7W8db0)

### PART 1: Configure Your Django Application for Elastic Beanstalk

1. Create a new directory, called .ebextensions:

(eb-virt) ~/ebdjango$ mkdir .ebextensions
Within the .ebextensions directory, add a configuration file named django.config with the following text:

Example ~/ebdjango/.ebextensions/django.config

option_settings:
  aws:elasticbeanstalk:container:python:
    WSGIPath: ebdjango/wsgi.py
This setting, WSGIPath, specifies the location of the WSGI script that Elastic Beanstalk uses to start your application.

Deactivate your virtual environment by with the deactivate command:

(eb-virt) ~/ebdjango$ deactivate
Reactivate your virtual environment whenever you need to add additional packages to your application or run your application locally.



### PART 2: Deploy Your Site With the EB CLI

Next, you'll create your application environment and deploy your configured application with Elastic Beanstalk.

Immediately after deployment, you'll edit Django's configuration to add the domain name that Elastic Beanstalk assigned to your application to Django's ALLOWED_HOSTS, and then you'll redeploy your application. This is a Django security requirement, designed to prevent HTTP Host header attacks. For details, see Host header validation.



To create an environment and deploy your Django application

Initialize your EB CLI repository with the eb init command:

~/ebdjango$ eb init -p python-3.6 django-tutorial

Application django-tutorial has been created.
This command creates a new application named django-tutorial and configures your local repository to create environments with the latest Python 3.6 platform version.

~/ebdjango$ eb init
Do you want to set up SSH for your instances?
(y/n): y
Select a keypair.
1) my-keypair
2) [ Create new KeyPair ]
Select a key pair if you have one already, or follow the prompts to create a new one. If you don't see the prompt or need to change your settings later, run eb init -i.

Create an environment and deploy you application to it with eb create:

~/ebdjango$ eb create django-env

This command creates a load balanced Elastic Beanstalk environment named django-env. Creating an environment takes about 5 minutes. As Elastic Beanstalk creates the resources necessary to run your application, it outputs informational messages that the EB CLI relays to your terminal.

When the environment creation process completes, find the domain name of your new environment by running eb status:

~/ebdjango$ eb status
Environment details for: django-env
  Application name: django-tutorial
  ...
  CNAME: eb-django-app-dev.elasticbeanstalk.com
  ...
Your environment's domain name is the value of the CNAME property.

Edit the settings.py file in the ebdjango directory, locate the ALLOWED_HOSTS setting, and then add your application's domain name that you found in the previous step to the setting's value. If you can't find this setting in the file, add it to a new line.

...
ALLOWED_HOSTS = ['eb-django-app-dev.elasticbeanstalk.com']
Save the file, and then deploy your application by running eb deploy. When you run eb deploy, the EB CLI bundles up the contents of your project directory and deploys it to your environment.

~/ebdjango$ eb deploy
Note

If you are using Git with your project, see Using the EB CLI with Git.

When the environment update process completes, open your web site with eb open:

~/ebdjango$ eb open
This will open a browser window using the domain name created for your application. You should see the same Django website that you created and tested locally.