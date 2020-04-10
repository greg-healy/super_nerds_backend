## Instructions for CS361
Clone the repo

Create a virtual environment by running `python3 -m venv venv`. This will create virtual environment configuration files in a `venv` folder. This `venv` folder is ignored in the .gitignore file. Note: This works on Linux/Mac. Go here for additional directions on setting up and using virtual environments: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/ .

Enter the virtual environment with `source venv/bin/activate`.

Install the required dependencies from `requirements.txt` by running `pip install -r requirements.txt`.

If you install any additional dependencies, be sure to update the `requirements.txt` file by running the bash command `pip freeze > requirements.txt`.

Start the `api.py` application by running `flask run`. Note that the .flaskenv file is already configured with the location of the flask app and knows to run it in debug mode so that when `flask` is called, it knows what to do.
