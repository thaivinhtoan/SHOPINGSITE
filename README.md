# ECOMMERCE WEBSITE

## Running this project

To get this project up and running you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install `virtualenv` with

```
pip install virtualenv
```

Clone or download this repository and open it in your editor of choice. In a `windows terminal`, run the following command in the base directory of this project

```
py -m venv venv
```

That will created a new folder `venv` in your project directory. Next activate it with this command on `WINDOWS`:

```
.\venv\Scripts\activate
```

Then install the project dependencies with

```
pip install -r requirements.txt
```

Now you can run the project with this command

```
python manage.py runserver
```

**Note** if you want payments to work you will need to enter your own Stripe API keys into the `.env` file in the settings files.

## TESTS

You need install library `coverage` first

```
coverage run --omit='*/venv/*' manage.py test
coverage report
```

If you run

```
coverage html
```

Folder `html` will be created, copy `path` and check this on browser file `.html`

# Session

```
from django.contrib.sessions.models import Session
s = Session.objects.get(pk='rfxige4v583rsb1nudrp4n64n6w07gwa')
s.get_decoded()
```

# CREATE REQUIREMENTS

```
pip freeze > requirements.txt
```

# STRIPE

Auth: 4000 0025 0000 3155

1. Download the latest windows tar.gz file from https://github.com/stripe/stripe-cli/releases/latest
2. Unzip the stripe_X.X.X_windows_x86_64.zip file
3. Run the unzipped .exe file

```
.\stripe.exe login

.\stripe.exe listen
```
