# AditiFLIX Web Application

## Description

A Web application imitating Netflix that demonstrates use of Python's Flask framework. The application makes use of libraries such as the Jinja templating library and WTForms. Architectural design patterns and principles including Repository, Dependency Inversion and Single Responsibility have been used to design the application. The application uses Flask Blueprints to maintain a separation of concerns between application functions. Testing includes unit and end-to-end testing using the pytest tool. 

NOTE 1: The application will take up to 10 mins to start up at first due to the 1000 API calls being made to OMDB. After that everything should be smooth.

NOTE 2: A few bug fixes were committed after the due date but Martin has approved them and said they will not incur the 10% penalty. See email in the root folder :)
## Installation

**Installation via requirements.txt**

```shell
$ cd AFlix_A2
$ py -3 -m venv venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
```

When using PyCharm, set the virtual environment using 'File'->'Settings' and select 'Project:AFlix_A2' from the left menu. Select 'Project Interpreter', click on the gearwheel button and select 'Add'. Click the 'Existing environment' radio button to select the virtual environment. 

## Execution

**Running the application**

From the *AFlix_A2* directory, and within the activated virtual environment (see *venv\Scripts\activate* above):

````shell
$ flask run
```` 

The webapp can be accessed by going to http://localhost:5000/home

## Configuration

The *AFLix_A2/.env* file contains variable settings. They are set with appropriate values.

* `FLASK_APP`: Entry point of the application (should always be `wsgi.py`).
* `FLASK_ENV`: The environment in which to run the application (either `development` or `production`).
* `SECRET_KEY`: Secret key used to encrypt session data.
* `TESTING`: Set to False for running the application. Overridden and set to True automatically when testing the application.
* `WTF_CSRF_SECRET_KEY`: Secret key used by the WTForm library.
* `RECAPTCHA_PUBLIC_KEY` : Secret public key used by Recaptcha
* `RECAPTCHA_PRIVATE_KEY` : Secret private key used by Recaptcha

## Testing

Testing requires that file *AFLix_A2/tests/conftest.py* be edited to set the value of `TEST_DATA_PATH`. You should set this to the absolute path of the *AFLix_A2/tests/data* directory. 

E.g. 

`TEST_DATA_PATH = os.path.join('C:', os.sep, 'Users', 'aditi', 'Documents', 'Python dev', 'AFlix_A2', 'tests', 'data')`

assigns TEST_DATA_PATH with the following value (the use of os.path.join and os.sep ensures use of the correct platform path separator):

`C:\Users\aditi\Documents\python-dev\AFlix_A2\tests\data`

You can then run tests from within PyCharm.
