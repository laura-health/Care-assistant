# Web service for integration of entities with #laurabot

To get started, we'll help you set up a development environment, deploy the server, add a database and create a new view.


## Prerequisites

You'll need the following:
* [Python](https://www.python.org/downloads/)
* [Database URI] The uri of the database connection



## 1. Run the app locally

Install the dependencies listed in the [requirements.txt](https://pip.readthedocs.io/en/stable/user_guide/#requirements-files) file to be able to run the app locally.

You can optionally use a [virtual environment](https://packaging.python.org/installing/#creating-and-using-virtual-environments) to avoid having these dependencies clash with those of other Python projects or your operating system.
  ```
pip install -r requirements.txt
  ```

Run the app.
  ```
python server.py
  ```

 View your app at: http://localhost:8080



## 2. Configuring the settings files

You should configure the files with the right values.
The only required settings are:
  - CORS_ORIGINS - Define the origin allowed to make requests.
  - SQLALCHEMY_DATABASE_URI - Define the database URI. See: [uri_help_link](https://flask-sqlalchemy.pocoo.org/2.2/config/#connection-uri-format)
  - USERNAME - Define the only username allowed to make requests.
  - PASSWORD - Define the password for the only user allowed to make requests.



## 3. Setting up the environment

There are three types of settings, each one is for a specific environment.
  - default.py is the file for default settings that you can override by the others environment settings.
  - development.py is the file for settings that are used only when running locally.
  - testing.py is the file for settings that are used when running in the test environment.
  - production.py is the file for settings that are used when running in production.

To set up the setting file you must set an environment variable 'APP_CONFIG_FILE'.
To do this, for example on production environment:
  ```
cd web-service-flask
export APP_CONFIG_FILE=config/production.py
  ```



## 4. Creating a systemd service (optional)

```
cp web-service-flask.service /etc/systemd/system/
systemctl daemon-reload
systemctl start web-service-flask
```



## 5. Creating a new view

The only file you need to edit is 'views_config.json'. This file contains everything necessary to create a new view, with an url, checking the parameters and executing the query on the database.

A view has the following structure:

"<view name>": {
    "parameters": ["<param 0>", "<param 1>", "<param 2>", ...],
    "query": "SELECT * FROM table WHERE <column field> >= {parameters[0]}"
}

What the fields mean:
  - View name: This is will define the view url (/<view name>). Each view must have a unique name (url).
  - Parameters: This is an array, with the name of each parameter for this request. The parameters will alway be a date and the should be used in the query string.
  - Query: This is the query string that will be executed in the database. To use each parameter inside the string, the sintax must be '{parameters[i]}', where 'i' is the index of the parameter in the parameters array. The index starts with 0.  
