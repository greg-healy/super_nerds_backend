import os  # needed to get the env variables

# When use flask run, get the settings from the .env folder and get the URI
# Note: the .env file should not be in the Development branch b/c Heroku.
# On Heroku, the environment variables have been manually entered

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

# get the Secret Key
SECRET_KEY = os.environ.get('SECRET_KEY')

# According to PrettyPrinted, it's annoying
SQLALCHEMY_TRACK_MODIFICATIONS = False
