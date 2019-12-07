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
**Note:** The following is based instructions provided in this [video](https://www.youtube.com/watch?v=ypnEf7W8db0)


### PART 1: Configure Your Django Application for Elastic Beanstalk

1. In project root folder, Create a new directory, called `.ebextensions`:

```
mkdir .ebextensions
```

2. In `.ebextensions` directory, create file named `django.config` with the following texts

```
option_settings:
  aws:elasticbeanstalk:container:python:
    WSGIPath: project/project/wsgi.py
```

**Note**
- WSGIPath, specifies the location of the WSGI script that Elastic Beanstalk uses to start your application.

- If WSGIPath not found, then it can be changed by clicking `modify` in `software` under `modification` under PROJECT ENV NAME (i.e. django-env)

<div style="text-align: center;">
    <img src="https://user-images.githubusercontent.com/6856382/70368110-ddc53180-185b-11ea-885f-04ff41f23529.png">
</div>

### PART 2: Installing AWS EB CLI

**Mac OS**
1. Update homebrew to latest version
```
brew update
```

2. Install aws eb cli
```
brew install awsebcli
```

3. Verify installation
```
eb --version
```

### PART 3: Setting up security credentials
1. Visit [this link](https://console.aws.amazon.com/iam/home?region=us-west-2#/security_credentials)

2. Select `Access keys`

<div style="text-align: center;">
    <img src="https://user-images.githubusercontent.com/6856382/70324494-78822980-17e4-11ea-862a-5a7ea37f892f.png">
</div>


3. Select `Create New Access Key`

4. Copy `Access Key ID` and `Secret Access Key`

<div style="text-align: center;">
    <img src="https://user-images.githubusercontent.com/6856382/70324622-d7e03980-17e4-11ea-889e-4ca0e5cb6b07.png">
</div>

### PART 2: Deploy Your Site With the EB CLI

1. Initialize your EB CLI repository with the eb init command:

```
eb init -p python-3.6 portfolio-site
```

2. Initialize your EB CLI repository `eb init`

```
eb init

Do you want to set up SSH for your instances?
(y/n): y
Select a keypair.
1) my-keypair
2) [ Create new KeyPair ]
```

- select `my-keypair` if there is one already
- select `Create new keypair` if none

2. Create an environment and deploy you application to it with `eb create`

```
eb create django-env
```

3. Find the domain name of your new environment by running eb status:

```
eb status

Environment details for: django-env
  Application name: portfolio-site
  ...
  CNAME: eb-django-app-dev.elasticbeanstalk.com
  ...
```

Your environment's domain name is the value of the CNAME property.

4. Edit the `settings.py` file in the ebdjango directory, locate the ALLOWED_HOSTS setting, and then add your application's domain name

`settings.py`
```
ALLOWED_HOSTS = ['eb-django-app-dev.elasticbeanstalk.com']
```

5. Deploy your application by running eb deploy

```
eb deploy
```

6. open your web site with eb open:
```
eb open
```
