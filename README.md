# Instructions for CS361
Clone the repo

Create the virtual environment and install dependencies by running `pipenv install`. Note that if you don't have `pipenv` installed you may need to run `pip install pipenv`. Check out this article for more on pipenv: https://thoughtbot.com/blog/how-to-manage-your-python-projects-with-pipenv

If you install any additional dependencies, be sure to push your update Pipfile as well. 

To run the app, enter the virtual environment with `pipenv shell`. To leave the shell type `exit`.

Type `flask run`. It should begin running on localhost:5000. 

## Setting up the database in Heroku
1. Push to the `development` branch  
2. Go to Heroku and reset the database (overview page of the dashboard, click on the database, and go to the settings tab). 
3. Make sure the environment variables (`DATABASE_URL` and `SECRET_KEY`) are still set properly on the Settings tab of the dashboard.
4. Open the Heroku CLI (click the 'More' button in the top right) and run  the `flask create_tables` command.

NOTE: We'll need to follow these steps every time we make a material change to the database (changes to `models.py`) in order for those changes to take effect, and so we don't get any errors. These situations should be obvious because we'll have to do the same deleting and creation of our database locally as well. A potential work around for the future might be to have instructions to destroy any old tables when instantiating new ones...



## File Explanations

`.flaskenv` 

Sets what context flask is running in. If `FLASK_ENV` set to development, debug mode will be on. `FLASK_APP` is used to specify how to load the app. 

`.env`

Sets the database URI and the SECRET_KEY
