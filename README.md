# siem dashboard

welcome to the siem dashboard project! this simple dashboard is designed to help you monitor and visualize security events easily. whether you're a beginner or an experienced developer, this readme will guide you through the process of setting up and using the siem dashboard.

## overview

siem dashboard is a basic security information and event management dashboard built with flask, sqlalchemy, and flask-login. it provides a user-friendly framework for tracking security events in your system.

## features

- **user authentication:** securely log in to access the dashboard.
- **event logging:** easily log and display security events.
- **sqlite database:** store events and user information efficiently.

## getting started

### prerequisites

- **python 3.x**
- **virtual environment (optional but recommended)**


## navigate to the project directory:

```bash
cd siem-dashboard
```

## (optional) create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # on linux/mac
venv\scripts\activate     # on windows
```

## install dependencies:

```bash
pip install -r requirements.txt
```

## initialize the database:

```bash
python
from app import db
db.create_all()
exit()
```

## usage:

### run the application:

```bash
python run.py
```

### access the dashboard:

open your web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to access the siem dashboard.

### user authentication:

visit [http://127.0.0.1:5000/login](http://127.0.0.1:5000/login) to log in with the default user credentials:
- username: admin
- password: admin_password
```
