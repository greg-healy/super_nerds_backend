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

# Super Nerd Wallet

## Features Overview

Our client wanted a digital payment system similar to Paypal/Venmo. We’ve created a web app that lets you create an account to access a personalized dashboard in which you can link a hypothetical bank account, withdraw money from said bank account, and send those funds to other registered users on the platform. You can also deposit funds back into your bank account, view your historical transactions, and request / deny other users’ requests for money. 


### Create Your Account and Log In

The registration page stores your email and password for future authentication. Once registered, a user can use the Log In page to log into their dashboard.

### Withdraw and Deposit Money from Your Bank/

From the dashboard the Bank widget allows you to link your hypothetical bank account and withdraw money. You can also deposit money back into the bank.

### Send and Request Money from Your Friends

The Send Money widget allows you to send funds instantly to other users. You can also request money from other users, but they have the choice to either approve or deny your request when they log into their dashboard. 

### View Your Transaction History

The Transactions widget allows you to see all historical transactions between other users.

## Installation - Frontend 

Navigate to your project directory on your local machine and run:

### `git clone https://github.com/gregoryphealy/super_nerds_frontend.git`

Clones all of the files located in this repository's master branch into your project directory.

### `npm install`

Runs the npm installer and installs all necessary packages listed in the `package.json` file into a `node_modules` folder.

### `npm start`

Runs the app in the development mode.<br />
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

## Quality Attributes

### Reliability

We want users’ money transfers to occur quickly and without error. 

### Integrity

We want the software to be intuitive for new users so that they can easily navigate to the features they want to use and make transactions. 

### Usability

We want our software to catch and manage all errors appropriately, malicious or otherwise. 

## Software Architecture and Design

### High Level Architecture

![High Level Architecture](https://github.com/gregoryphealy/super_nerds_frontend/blob/master/diagrams/high_level_architecture.png?raw=true)

### Communication Diagram

![Communication Diagram](https://github.com/gregoryphealy/super_nerds_frontend/blob/master/diagrams/client_server_communication.png?raw=true)

### React Component Diagram

![React Component Diagram](https://github.com/gregoryphealy/super_nerds_frontend/blob/master/diagrams/react_component_diagram.png?raw=true)

### Database Entity Relationship Diagram

![Database Entity Relationship Diagram](https://github.com/gregoryphealy/super_nerds_frontend/blob/master/diagrams/database_erd.png?raw=true)

## Design Patterns, Modules, and Components

Command - Individual clients will receive a unique token to represent them upon logging in. When a client wishes to make a request for additional information from the database, they will send this token to the API server, and this will be decoded to determine who the client is. This information will then be used to retrieve information for the client that (1) is relevant to their request and (2) they have permission to access

## Final State of the Software

### Overview of know bugs/issues 

- Activity tab isn’t implemented
- The ‘See more transactions’ link isn’t implemented
- If you refresh the page, you’re logged out

### What is left in the Product Backlog

- Finish the Activity Tab
- Update the ‘See more transactions’ link so that it views additional transaction history
- Simulate Banks more realistically so that we’re making requests to accounts with finite amounts of money. 

## General File Structure

### Frontend


Most of the files for the React frontend are contained within the src directory. Within here the entry point of our application is the `index.js` file and we also have a `history.js` file for keeping track of the current path in the user’s address bar. We have two folders which are used to manage the state of variables in a user's particular session using the Redux Store. These are the `actions` folder and the “reducers” folder. The `api` folder contains a little bit of setup we used in other files for making requests to our backend. The largest folder of them all is the `components` folder, and in here we have the different components used to build the application. The `Activity`, `RequestNotifications`, `SendRequest`, and `Wallet` folder contain all of the subcomponents pertinent to using those aspects of the summary page. The remainder of the files in this directory pertain to the navbar, footer, registration, logging in, and the summary and home pages. 

### Backend

`wsgi.py`, `__init__.py`, `extensions.py`, `settings.py`, and `commands.py` set up the basic framework for the backend server. `models.py` is where the table models are created using the ORM software - SqlAlchemy. The `routes` directory contains files for handling routes to the backend. Most are labeled intuitively: `auth.py`, `bank.py`, `requests.py`, and `transactions.py` all deal with the authorization, banking, requesting, and transaction routes respectively. `debugging.py` is used for debugging only and `main.py` deals with the homepage and more general routes. 

## How to contribute to the project

All members will continue to further make modification of the projects. Since this project can be used as a portfolio,individual members can also make their own individual modifications as they see fit. 

