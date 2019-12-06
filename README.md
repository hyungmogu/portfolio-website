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
